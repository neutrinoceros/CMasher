"""
Utils
=====
Utility functions for registering and manipulating colormaps in various ways.

"""

from __future__ import annotations

from collections import defaultdict
from importlib.util import find_spec
from itertools import chain
from pathlib import Path
from textwrap import dedent
from typing import TYPE_CHECKING, NewType, overload

import matplotlib as mpl
import numpy as np
from colorspacious import cspace_converter
from matplotlib.colors import (
    Colormap,
    LinearSegmentedColormap,
    ListedColormap as LC,
    to_hex,
    to_rgb,
)

from cmasher import cm as cmrcm

from ._known_cmap_types import _CMASHER_BUILTIN_MAP_TYPES

if TYPE_CHECKING:
    import os
    import sys
    from collections.abc import Callable, Iterator
    from typing import Literal, Protocol, TypeAlias, TypeVar

    from matplotlib.artist import Artist
    from numpy.typing import NDArray

    if sys.version_info >= (3, 12):
        from typing import Self
    else:
        from typing_extensions import Self

    T = TypeVar("T", int, float)
    RGB: TypeAlias = tuple[T, T, T]

    class SupportsDunderLT(Protocol):
        def __lt__(self, other: Self, /) -> bool: ...

    class SupportsDunderGT(Protocol):
        def __gt__(self, other: Self, /) -> bool: ...

    SupportsOrdering: TypeAlias = SupportsDunderLT | SupportsDunderGT


_HAS_VISCM = find_spec("viscm") is not None

# All declaration
__all__ = [
    "combine_cmaps",
    "create_cmap_mod",
    "create_cmap_overview",
    "get_bibtex",
    "get_cmap_list",
    "get_cmap_type",
    "get_sub_cmap",
    "import_cmaps",
    "register_cmap",
    "set_cmap_legend_entry",
    "take_cmap_colors",
    "view_cmap",
]


# %% GLOBALS
# Obtain the colorspace converter for showing cmaps in gray-scale
cspace_convert = cspace_converter("sRGB1", "CAM02-UCS")

# New types
Category = NewType("Category", str)
Name = NewType("Name", str)


# %% HELPER FUNCTIONS
# Define function for obtaining the sorting order for lightness ranking
def _get_cmap_lightness_rank(
    cmap: Colormap,
) -> tuple[int, int, float, float, float, str]:
    """
    Returns a tuple of objects used for sorting the provided `cmap` based
    on its lightness profile.

    Parameters
    ----------
    cmap : :obj:`~matplotlib.colors.Colormap` object
        The registered name of the colormap in :mod:`matplotlib.cm` or its
        corresponding :obj:`~matplotlib.colors.Colormap` object.

    Returns
    -------
    L_slope : int
        The slope type of lightness profile of `cmap`.
    L_type : int
        The range type of lightness profile of `cmap`.
        This is only used for sequential colormaps.
    L_start : float
        The starting lightness value of `cmap`.
        For diverging/cyclic colormaps, this is the central lightness value.
    L_rng : float
        The lightness range of `cmap`.
    L_rmse : float
        The RMSE of the lightness profile of `cmap`.
        For diverging/cyclic colormaps, this is the max RMSE of either half.
    name : str
        The name of `cmap`.
        For qualitative and miscellaneous colormaps, this is the only value
        that is used.

    """
    # Obtain the colormap
    cm_type = get_cmap_type(cmap)

    # Determine lightness profile stats for sequential/diverging/cyclic
    if cm_type in ("sequential", "diverging", "cyclic"):
        # Get RGB values for colormap
        rgb = cmap(np.arange(cmap.N))[:, :3]

        # Get lightness values of colormap
        lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
        lightness = lab[:, 0]

        # If cyclic colormap, add first lightness at the end
        if cm_type == "cyclic":
            lightness = np.r_[lightness, [lightness[0]]]

        # Determine number of values that will be in deltas
        N_deltas = len(lightness) - 1

        # Determine the deltas of the lightness profile
        deltas = np.diff(lightness)
        derivs = N_deltas * deltas

        # Set lightness profile type to 0
        L_type = 0

        # Determine the RMSE of the lightness profile of a sequential colormap
        if cm_type == "sequential":
            # Take RMSE of entire lightness profile
            L_rmse = np.around(np.std(derivs), 0)

            # Calculate starting lightness value
            L_start = np.around(lightness[0], 0)

            # Determine type of lightness profile
            L_type += (not np.allclose(rgb[0], [0, 0, 0])) * 2
            L_type += np.allclose(rgb[0], [0, 0, 0]) == np.allclose(rgb[-1], [1, 1, 1])

        # Diverging/cyclic colormaps
        else:
            # Determine the center of the colormap
            central_i = [int(np.ceil(N_deltas / 2)), int(np.floor(N_deltas / 2))]

            # Calculate RMSE of both halves
            L_rmse = np.max(
                [
                    np.around(np.std(derivs[: central_i[0]]), 0),
                    np.around(np.std(derivs[central_i[1] :]), 0),
                ]
            )

            # Calculate central lightness value
            L_start = np.around(np.average(lightness[central_i]), 0)

        # Determine lightness range
        L_rng = np.around(np.max(lightness) - np.min(lightness), 0)

        # Determine if cmap goes from dark to light or the opposite
        L_slope = (L_start > lightness[-1]) * 2 - 1

    # For qualitative/misc colormaps, set all lightness values to zero
    else:
        L_slope = L_type = L_start = L_rng = L_rmse = 0

    # Return lightness contributions to the rank
    return (L_slope, L_type, L_start, L_rng, L_rmse, cmap.name)


# Define function for obtaining the sorting order for perceptual ranking
def _get_cmap_perceptual_rank(
    cmap: Colormap,
) -> tuple[int, int, float, float, float, float, str]:
    """
    In addition to returning the lightness rank as given by
    :func:`~_get_cmap_lightness_rank`, also returns the length of the
    perceptual profile, also known as the perceptual range, of the provided
    `cmap`.

    Parameters
    ----------
    cmap : :obj:`~matplotlib.colors.Colormap` object
        The registered name of the colormap in :mod:`matplotlib.cm` or its
        corresponding :obj:`~matplotlib.colors.Colormap` object.

    Returns
    -------
    *L_rank : objects
        The values returned by :func:`~_get_cmap_lightness_rank`, except for
        the name of the colormap.
    P_rng : float
        The perceptual range of `cmap`.
    name : str
        The name of `cmap`.
        For qualitative and miscellaneous colormaps, this is the only value
        that is used.

    """
    # Obtain the colormap
    cm_type = get_cmap_type(cmap)

    # Determine perceptual range for sequential/diverging/cyclic
    if cm_type in ("sequential", "diverging", "cyclic"):
        # Get RGB values for colormap
        rgb = cmap(np.arange(cmap.N))[:, :3]

        # Get lab values of colormap
        lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)

        # If cyclic colormap, add first lab at the end
        if cm_type == "cyclic":
            lab = np.r_[lab, [lab[0]]]

        # Determine the deltas of the lightness profile
        deltas = np.sqrt(np.sum(np.diff(lab, axis=0) ** 2, axis=-1))

        # Determine perceptual range
        P_rng = np.around(np.sum(deltas), 0)

    # For qualitative/misc colormaps, set all values to zero
    else:
        P_rng = 0

    # Return perceptual contributions to the rank
    return (*_get_cmap_lightness_rank(cmap)[:-1], P_rng, cmap.name)


# %% FUNCTIONS
# This function combines multiple colormaps at given nodes
def combine_cmaps(
    *cmaps: Colormap | str,
    nodes: list[float] | NDArray[np.floating] | None = None,
    n_rgb_levels: int = 256,
    combined_cmap_name: str = "combined_cmap",
) -> LinearSegmentedColormap:
    """Create a composite matplotlib colormap by combining multiple colormaps.

    Parameters
    ----------
    *cmaps: Colormap or colormap name (str) to be combined.
    nodes: list or numpy array of nodes (float). Defaults: equal divisions.
        The blending points between colormaps, in the range [0, 1].
    n_rgb_levels: int. Defaults: 256.
        Number of RGB levels for each colormap segment.
    combined_cmap_name: str. Defaults: "combined_cmap".
        name of the combined Colormap.

    Returns
    -------
    Colormap: The composite colormap.

    Raises
    ------
    TypeError: If the list contains mixed datatypes or invalid
        colormap names.
    ValueError: If the cmaps contain only one single colormap,
        or if the number of nodes is not one less than the number
        of colormaps, or if the nodes do not contain incrementing values
        between 0.0 and 1.0.

    Note
    ----
    The colormaps are combined from low value to high value end.

    References
    ----------
    - https://stackoverflow.com/questions/31051488/combining-two-matplotlib-colormaps/31052741#31052741

    Examples
    --------
    Using predefined colormap names::
        >>> custom_cmap_1 = combine_cmaps(
            ["ocean", "prism", "coolwarm"], nodes=[0.2, 0.75]
        )

    Using Colormap objects::
        >>> cmap_0 = plt.get_cmap("Blues")
        >>> cmap_1 = plt.get_cmap("Oranges")
        >>> cmap_2 = plt.get_cmap("Greens")
        >>> custom_cmap_2 = combine_cmaps([cmap_0, cmap_1, cmap_2])

    """
    # Check colormap datatype and convert to list[Colormap]
    if len(cmaps) <= 1:
        raise ValueError("Expected at least two colormaps to combine.")
    for cm in cmaps:
        if not isinstance(cm, Colormap | str):
            raise TypeError(f"Unsupported colormap type: {type(cm)}.")
    _cmaps: list[Colormap] = [
        cm if isinstance(cm, Colormap) else mpl.colormaps[cm] for cm in cmaps
    ]

    # Generate default nodes for equal separation
    if nodes is None:
        nodes_arr = np.linspace(0, 1, len(_cmaps) + 1)
    elif isinstance(nodes, list | np.ndarray):
        nodes_arr = np.concatenate([[0.0], nodes, [1.0]])
    else:
        raise TypeError(f"Unsupported nodes type: {type(nodes)}, expect list of float.")

    # Check nodes length
    if len(nodes_arr) != len(_cmaps) + 1:
        raise ValueError(
            "Number of nodes should be one less than the number of colormaps."
        )

    # Check node values
    if any((nodes_arr < 0) | (nodes_arr > 1)) or any(np.diff(nodes_arr) <= 0):
        raise ValueError(
            "Nodes should only contain increasing values between 0.0 and 1.0."
        )

    # Generate composite colormap
    combined_cmap_segments = []

    for i, cmap in enumerate(_cmaps):
        start_position = nodes_arr[i]
        end_position = nodes_arr[i + 1]

        # Calculate the length of the segment
        segment_length = int(n_rgb_levels * (end_position - start_position))

        # Append the segment to the combined colormap segments
        combined_cmap_segments.append(cmap(np.linspace(0, 1, segment_length)))

    # Combine the segments (from bottom to top)
    return LinearSegmentedColormap.from_list(
        combined_cmap_name, np.vstack(combined_cmap_segments)
    )


# This function creates a standalone module of a CMasher colormap
def create_cmap_mod(
    cmap: Name,
    *,
    save_dir: str | os.PathLike[str] = ".",
    _copy_name: str | None = None,
) -> str:
    """
    Creates a standalone Python module of the provided *CMasher* `cmap` and
    saves it in the given `save_dir` as '<`cmap`>.py'.

    A standalone colormap module can be used to quickly share a colormap with
    someone without adding the *CMasher* dependency.
    Importing the created module allows the colormap to be used in the same way
    as usual through *MPL* (including the 'cmr.' prefix).

    Parameters
    ----------
    cmap : str
        The name of the *CMasher* colormap a standalone Python module must be
        made for. An added 'cmr.' prefix will be ignored.

    Optional
    --------
    save_dir: str or os.PathLike[str] Default: '.'
        The path to the directory where the module must be saved.
        By default, the current directory is used.

    Returns
    -------
    cmap_path : str
        The path to the Python file containing the colormap module.

    Example
    -------
    Creating a standalone Python module of the 'rainforest' colormap::

        >>> create_cmap_mod('rainforest')

    One can now import the 'rainforest' colormap in any script by moving the
    created 'rainforest.py' file to the proper working directory and importing
    it with ``import rainforest``.

    Note
    ----
    Unlike other *CMasher* utility functions, `cmap` solely accepts names of
    colormaps that are registered in *CMasher* (:mod:`cmasher.cm`).

    """
    # Get absolute value to provided save_dir
    save_dir = Path(save_dir).resolve()

    # Remove any 'cmr.' prefix from provided cmap
    name = cmap.removeprefix("cmr.")

    # Obtain the CMasher colormap associated with the provided cmap
    if (_cmap := cmrcm.cmap_d.get(name, None)) is None:
        raise ValueError(f"{name!r} is not a valid cmasher colormap name")

    cm_type = get_cmap_type(cmap)

    # Obtain the RGB tuples of provided cmap
    rgb = np.array(_cmap.colors)

    # Convert RGB values to string
    array_str = np.array2string(
        rgb,
        max_line_width=79,
        prefix="cm_data = ",
        separator=", ",
        threshold=rgb.size,
        formatter={"float": lambda x: f"{x:.8f}"},
    )

    # Create Python module template and add obtained RGB data to it
    cm_py_file = dedent(
        """
        import matplotlib as mpl
        from matplotlib.colors import ListedColormap

        # All declaration
        __all__ = ["cmap"]

        # Author declaration
        __author__ = "Ellert van der Velden (@1313e)"

        # Package declaration
        __package__ = "cmasher"


        # %% GLOBALS AND DEFINITIONS
        # Type of this colormap
        cm_type = '{0}'

        # RGB-values of this colormap
        cm_data = {1}

        # Create ListedColormap object for this colormap
        assert len(cm_data) == {3}
        cmap = ListedColormap(cm_data, name='cmr.{2}')
        cmap_r = cmap.reversed()

        # Register (reversed) cmap in MPL
        mpl.colormaps.register(cmap=cmap)
        mpl.colormaps.register(cmap=cmap_r)
        """
    )

    # If this colormap is cyclic, add code to register shifted version as well
    if cm_type == "cyclic":
        cm_py_file += dedent(
            """
            # Shift the entire colormap by half of its length
            cm_data_s = list(cm_data[{4}:])
            cm_data_s.extend(cm_data[:{4}])

            # Create ListedColormap object for this shifted version
            cmap_s = ListedColormap(cm_data_s, name='cmr.{2}_s', N={3})
            cmap_s_r = cmap_s.reversed()

            # Register shifted versions in MPL as well
            mpl.colormaps.register(cmap=cmap_s)
            mpl.colormaps.register(cmap=cmap_s_r)
            """
        )

    # Format py-file string
    cm_py_file = cm_py_file.format(
        cm_type, array_str, _copy_name or name, len(rgb), len(rgb) // 2
    )

    # Obtain the path to the module
    cmap_path = save_dir / f"{_copy_name or name}.py"

    # Create Python module
    with open(cmap_path, "w") as f:
        f.write(cm_py_file[1:])

    # Return cmap_path
    return str(cmap_path.resolve())


# This function creates an overview plot of all colormaps specified
def create_cmap_overview(
    cmaps: list[Colormap | Name] | dict[Category, list[Colormap | Name]] | None = None,
    *,
    savefig: str | os.PathLike[str] | None = None,
    use_types: bool = True,
    sort: Literal["alphabetical", "name", "lightness", "perceptual", None]
    | Callable[[Colormap], SupportsOrdering] = "alphabetical",
    show_grayscale: bool = True,
    show_info: bool = False,
    plot_profile: bool | float = False,
    dark_mode: bool = False,
    title: str | None = "Colormap Overview",
    wscale: float = 1,
    hscale: float = 1,
) -> None:
    """
    Creates an overview plot containing all colormaps defined in the provided
    `cmaps`.

    Optional
    --------
    cmaps : list of {str; :obj:`~matplotlib.colors.Colormap` objects}, dict \
        of lists or None. Default: None
        A list of all colormaps that must be included in the overview plot.
        If dict of lists, the keys define categories for the colormaps.
        If *None*, all colormaps defined in *CMasher* are used instead.
    savefig : str, os.PathLike or None. Default: None
        If not *None*, the path where the overview plot must be saved to.
        Else, the plot will simply be shown.
    use_types : bool. Default: True
        Whether all colormaps in `cmaps` should be categorized into their
        colormap types (sequential; diverging; cyclic; qualitative; misc).
        If `cmaps` is a dict, this value is ignored.
    sort : {'alphabetical'/'name'; 'lightness'; 'perceptual'}, function or \
        None. Default: 'alphabetical'
        String or function indicating how the colormaps should be sorted in the
        overview.
        If 'alphabetical', the colormaps are sorted alphabetically on their
        name.
        If 'lightness', the colormaps are sorted based on their lightness
        profile, which is given by :func:`~_get_cmap_lightness_rank`.
        If 'perceptual', the colormaps sorted based on their perceptual range
        in  addition to their lightness profile, which is given by
        :func:`~_get_cmap_perceptual_rank`. Note that this is only meaningful
        if all `cmaps` are perceptually uniform sequential.
        If function, a function definition that takes a
        :obj:`~matplotlib.colors.Colormap` object and returns the sorted
        position of that colormap.
        If *None*, the colormaps retain the order they were given in.
    show_grayscale : bool. Default: True
        Whether to show the grayscale versions of the given `cmaps` in the
        overview.
    show_info : bool. Default: False
        Whether the statistics information of all sequential, diverging and
        cyclic colormaps should be shown under their names. This is a series of
        numbers representing, in order, the starting (sequential) or central
        (diverging/cyclic) lightness value; the final/outer lightness value;
        and the perceptual range of the colormap.
    plot_profile : bool or float. Default: False
        Whether the lightness profiles of all non-qualitative colormaps should
        be plotted. If not *False*, the lightness profile of a colormap is
        plotted on top of its gray-scale version and `plot_profile` is used for
        setting the alpha (opacity) value.
        If `plot_profile` is *True*, it will be set to `0.25`.
        If `show_grayscale` is *False*, this value is ignored.
    dark_mode : bool. Default: False
        Whether the colormap overview should be created using mostly dark
        colors.
    title : str or None. Default: "Colormap Overview"
        String to be used as the title of the colormap overview.
        If empty or *None*, no title will be used.
    wscale, hscale : float. Default: (1, 1)
        Floats that determine with what factor the colormap subplot dimensions
        in the overview should be scaled with.
        The default values uses the default dimensions for the subplots (which
        are determined by other input arguments).

    Notes
    -----
    The colormaps in `cmaps` can either be provided as their registered name in
    :mod:`matplotlib.cm`, or their corresponding
    :obj:`~matplotlib.colors.Colormap` object.
    Any provided reversed colormaps (colormaps that end their name with '_r')
    are ignored if their normal versions were provided as well.

    When `sort` is 'lightness' or 'perceptual', qualitative and miscellaneous
    colormaps are solely sorted on their names, as the lightness/perceptual
    profile of these colormaps is meaningless.

    If `plot_profile` is not set to *False*, the lightness profiles are plotted
    on top of the gray-scale colormap versions, where the y-axis ranges from 0%
    lightness to 100% lightness.
    The lightness profile transitions between black and white at 50% lightness.

    """
    import matplotlib.pyplot as plt
    from matplotlib.axes import Axes

    # If cmaps is None, use cmap_d.values
    if cmaps is None:
        cmaps = list(cmrcm.cmap_d.values())

    # If sort is a string, obtain proper function
    sort_key: Callable[[Colormap], SupportsOrdering] | None
    if isinstance(sort, str):
        # Check what string was provided and obtain sorting function
        if sort in ("alphabetical", "name"):

            def get_name(x: Colormap) -> str:
                return x.name

            sort_key = get_name
        elif sort == "lightness":
            sort_key = _get_cmap_lightness_rank
        elif sort == "perceptual":
            sort_key = _get_cmap_perceptual_rank
        else:
            raise ValueError(
                f"Input argument 'sort' has invalid string value {sort!r}!"
            )
    elif callable(sort):
        sort_key = sort
    else:
        sort_key = None

    # Streamline cmaps to a homogeneous container type
    cmaps_iter: Iterator[Colormap | Name]
    if isinstance(cmaps, dict):
        use_types = True
        cmaps_iter = chain.from_iterable(cmaps.values())
    else:
        cmaps_iter = iter(cmaps)

    cmaps_by_categories: defaultdict[str, list[Colormap]] = defaultdict(list)
    for cm_candidate in cmaps_iter:
        cat = get_cmap_type(cm_candidate) if use_types else "all"
        if isinstance(cm_candidate, str):
            cm = mpl.colormaps[cm_candidate]
        else:
            cm = cm_candidate
        cmaps_by_categories[cat].append(cm)

    # Remove all reversed colormaps that also have their original
    for cat, cmap_group in cmaps_by_categories.items():
        names = [cm.name for cm in cmap_group]
        cmaps_by_categories[cat] = [
            cm
            for cm in cmap_group
            if not (cm.name.endswith("_r") and cm.name[:-2] in names)
        ]

    # Sort the colormaps if requested
    if sort_key is not None:
        for cat in cmaps_by_categories:
            cmaps_by_categories[cat] = sorted(cmaps_by_categories[cat], key=sort_key)

    # Check value of show_grayscale
    if show_grayscale:
        # If True, the overview will have two columns
        ncols = 2
    else:
        # If False, the overview will have one column
        ncols = 1
        wscale *= 0.5

    # Determine text/element positions
    wscale = 0.2 + 0.8 * wscale
    left_pos = 0.2 / wscale
    spacing = 0.01 / wscale
    title_pos = left_pos + (1 - spacing - left_pos) / 2

    # If plot_profile is True, set it to its default value
    if plot_profile is True:
        plot_profile = 0.25

    # Check if dark mode is requested
    if dark_mode:
        # If so, use dark gray for the background and light gray for the text
        edge_color = "#24292E"
        face_color = "#24292E"
        text_color = "#9DA5B4"
    else:
        # If not, use white for the background and black for the text
        edge_color = "#FFFFFF"
        face_color = "#FFFFFF"
        text_color = "#000000"

    # Create figure instance
    nplotables = (
        (1 if title else 0)
        + (len(cmaps_by_categories) if use_types else 0)
        + sum(len(_) for _ in cmaps_by_categories.values())
    )
    height = (0.4 * nplotables + 0.1) * hscale

    fig, axs = plt.subplots(
        figsize=(6.4 * wscale, height),
        nrows=nplotables,
        ncols=ncols,
        edgecolor=edge_color,
        facecolor=face_color,
    )

    # Adjust subplot positioning
    fig.subplots_adjust(
        top=(1 - 0.05 / height),
        bottom=0.05 / height,
        left=left_pos,
        right=1.0 - spacing,
        wspace=0.05,
    )

    # Narrow axs' type
    if nplotables == 1 or isinstance(axs, Axes):
        axs = np.array([axs])

    ### NEW LOGIC
    for ax in axs:
        if ncols == 1:
            ax.set_axis_off()
        else:
            for axx in ax:
                axx.set_axis_off()

    # Add title to cmaps_list if requested
    if title:
        ax0 = next(axs.flat)

        # Obtain position bbox of ax0
        pos0 = ax0.get_position()

        # Write the title as text in the correct position
        fig.text(
            title_pos,
            pos0.y0 + pos0.height / 2,
            title,
            va="center",
            ha="center",
            fontsize=18,
            c=text_color,
        )
        axs_offset = 1
    else:
        axs_offset = 0

    next_axs_offset = axs_offset
    for cat, cmap_group in cmaps_by_categories.items():
        if use_types:
            # Write the cm_type as text in the correct position
            if ncols == 1:
                ax0 = axs[next_axs_offset]
            else:
                ax0 = axs[next_axs_offset, 0]
            fig.text(
                title_pos,
                ax0.get_position().y0,
                cat,
                va="bottom",
                ha="center",
                fontsize=14,
                c=text_color,
            )
            axs_offset += 1

        next_axs_offset = axs_offset + len(cmap_group)
        for ax, cm in zip(axs[axs_offset:next_axs_offset], cmap_group, strict=True):
            if ncols == 1:
                ax0 = ax
            else:
                ax0 = ax[0]
            pos0 = ax0.get_position()

            # Obtain the colormap type
            cm_type = get_cmap_type(cm)

            # Get array of all values for which a colormap value is requested
            x = np.arange(cm.N)

            # Get RGB values for colormap
            rgb = cm(x)[:, :3]

            # Add colormap subplot
            ax0.imshow(rgb[np.newaxis, ...], aspect="auto")

            # Add gray-scale colormap subplot if requested
            if show_grayscale:
                # Get lightness values of colormap
                lab = cspace_convert(rgb)
                lightness = lab[:, 0]

                # Normalize lightness values
                lightness /= 99.99871678

                # Get RGB values for lightness values using neutral
                rgb_L = cmrcm.neutral(lightness)[:, :3]

                # Add gray-scale colormap subplot
                ax[1].imshow(rgb_L[np.newaxis, ...], aspect="auto")

                # Check if the lightness profile was requested
                if plot_profile and (cm_type != "qualitative"):
                    # Determine the points that need to be plotted
                    plot_L = -(lightness - 0.5)
                    points = np.stack([x, plot_L], axis=1)

                    # Determine the colors that each point must have
                    # Use black for lightness >= 0.5 and white for lightness <= 0.5.
                    colors = np.zeros_like(plot_L, dtype=int)
                    colors[plot_L >= 0] = 1

                    # Split points up into segments with the same color
                    s_idx = np.nonzero(np.diff(colors))[0] + 1
                    segments = np.split(points, s_idx)

                    # Loop over all pairs of adjacent segments
                    for i, (seg1, seg2) in enumerate(
                        zip(segments[:-1], segments[1:], strict=True)
                    ):
                        # Determine the point in the center of these segments
                        central_point = (seg1[-1] + seg2[0]) / 2

                        # Add this point to the ends of these segments
                        # This ensures that color changes in between segments
                        segments[i] = np.r_[segments[i], [central_point]]
                        segments[i + 1] = np.r_[[central_point], segments[i + 1]]

                    from matplotlib.collections import LineCollection

                    # Create an MPL LineCollection object with these segments
                    lc = LineCollection(
                        segments,
                        cmap=cmrcm.neutral,
                        alpha=plot_profile,
                    )
                    lc.set_linewidth(1)

                    # Determine the colors of each segment
                    s_colors = [colors[0]]
                    s_colors.extend(colors[s_idx])

                    # Set the values of the line-collection to be these colors
                    lc.set_array(np.array(s_colors))

                    # Add line-collection to this subplot
                    ax[1].add_collection(lc)

            # Determine positions of colormap name
            x_text = pos0.x0 - spacing
            y_text = pos0.y0 + pos0.height / 2

            # Check if lightness information was requested for valid cm_type
            if show_info and cm_type in ("sequential", "diverging", "cyclic"):
                # If so, obtain lightness/perceptual profile information
                rank = _get_cmap_perceptual_rank(cm)[0:6]

                # Write name of colormap in the correct position
                fig.text(
                    x_text,
                    y_text,
                    cm.name,
                    va="bottom",
                    ha="right",
                    fontsize=10,
                    c=text_color,
                )

                # Write lightness profile information in the correct position
                fig.text(
                    x_text,
                    y_text,
                    f"({rank[2]:.3g}, {rank[2] - rank[0] * rank[3]:.3g}, {rank[5]:.3g})",
                    va="top",
                    ha="right",
                    fontsize=10,
                    c=text_color,
                )
            else:
                # If not, just write the name of the colormap
                fig.text(
                    x_text,
                    y_text,
                    cm.name,
                    va="center",
                    ha="right",
                    fontsize=10,
                    c=text_color,
                )
        axs_offset = next_axs_offset

    # If savefig is not None, save the figure
    if savefig is not None:
        savefig = Path(savefig)
        dpi = 100 if (savefig.suffix == ".svg") else 250
        fig.savefig(
            savefig,
            dpi=dpi,
            facecolor=face_color,
            edgecolor=edge_color,
        )
        plt.close(fig)

    # Else, simply show it
    else:
        plt.show()


# Define function that prints a string with the BibTeX entry to CMasher's paper
def get_bibtex() -> None:
    """
    Prints a string that gives the BibTeX entry for citing the *CMasher* paper
    (Van der Velden 2020, JOSS, 5, 2004).

    """
    # Create string with BibTeX entry
    bibtex = dedent(
        r"""
        @ARTICLE{2020JOSS....5.2004V,
            author = {{van der Velden}, Ellert},
            title = "{CMasher: Scientific colormaps for making accessible,
                informative and 'cmashing' plots}",
            journal = {The Journal of Open Source Software},
            keywords = {Python, science, colormaps, data visualization,
                plotting, Electrical Engineering and Systems Science - Image
                and Video Processing, Physics - Data Analysis, Statistics and
                Probability},
            year = 2020,
            month = feb,
            volume = {5},
            number = {46},
            eid = {2004},
            pages = {2004},
            doi = {10.21105/joss.02004},
            archivePrefix = {arXiv},
            eprint = {2003.01069},
            primaryClass = {eess.IV},
            adsurl = {https://ui.adsabs.harvard.edu/abs/2020JOSS....5.2004V},
            adsnote = {Provided by the SAO/NASA Astrophysics Data System}
        }
        """
    )

    # Print the string
    print(bibtex.strip())


# This function returns a list of all colormaps available in CMasher
def get_cmap_list(
    cmap_type: Literal[
        "a",
        "all",
        "s",
        "seq",
        "sequential",
        "d",
        "div",
        "diverging",
        "c",
        "cyc",
        "cyclic",
    ] = "all",
) -> list[str]:
    """
    Returns a list with the names of all colormaps available in *CMasher* of
    the given `cmap_type`.

    Note that *CMasher* colormaps registered in *MPL* have an added 'cmr.'
    prefix.

    Optional
    --------
    cmap_type : {'a'/'all'; 's'/'seq'/'sequential'; 'd'/'div'/'diverging'; \
        'c'/'cyc'/'cyclic'}. Default: 'all'
        The colormap type that should be in the returned list.

    Returns
    -------
    cmap_list : list of str
        List containing the names of all colormaps available in *CMasher*.

    """
    # Obtain proper list
    if cmap_type in ("a", "all"):
        cmaps = list(cmrcm.cmap_d)
    elif cmap_type in ("s", "seq", "sequential"):
        cmaps = list(cmrcm.cmap_cd["sequential"])
    elif cmap_type in ("d", "div", "diverging"):
        cmaps = list(cmrcm.cmap_cd["diverging"])
    elif cmap_type in ("c", "cyc", "cyclic"):
        cmaps = list(cmrcm.cmap_cd["cyclic"])
    else:
        raise ValueError(cmap_type)

    # Return cmaps
    return cmaps


# This function determines the colormap type of a given colormap
def get_cmap_type(cmap: Colormap | Name) -> str:
    """
    Checks what the colormap type (sequential; diverging; cyclic; qualitative;
    misc) of the provided `cmap` is and returns it.

    Parameters
    ----------
    cmap : str or :obj:`~matplotlib.colors.Colormap` object
        The registered name of the colormap in :mod:`matplotlib.cm` or its
        corresponding :obj:`~matplotlib.colors.Colormap` object.

    Returns
    -------
    cm_type : {'sequential'; 'diverging'; 'cyclic'; 'qualitative'; 'misc'}
        A string stating which of the defined colormap types the provided
        `cmap` has.

    """
    # Obtain the colormap
    if isinstance(cmap, str):
        if cmap in _CMASHER_BUILTIN_MAP_TYPES:
            # fast track for known results
            return _CMASHER_BUILTIN_MAP_TYPES[cmap]

        cmap = mpl.colormaps[cmap]

    # Get RGB values for colormap
    rgb = cmap(np.arange(cmap.N))[:, :3]

    # Get lightness values of colormap
    lab = cspace_converter("sRGB1", "CAM02-UCS")(rgb)
    lightness = lab[:, 0]
    diff_L = np.diff(lightness)

    # Obtain central values of lightness
    N = cmap.N - 1
    central_i = [int(np.floor(N / 2)), int(np.ceil(N / 2))]
    diff_L0 = np.diff(lightness[: central_i[0] + 1])
    diff_L1 = np.diff(lightness[central_i[1] :])

    # Obtain perceptual differences of last two and first two values
    lab_red = lab[[-2, -1, 0, 1]]
    deltas = np.sqrt(np.sum(np.diff(lab_red, axis=0) ** 2, axis=-1))

    # Check the statistics of cmap and determine the colormap type
    # QUALITATIVE
    # If the colormap has less than 40 values, assume it is qualitative
    if cmap.N < 40:
        return "qualitative"

    # MISC 1
    # If the colormap has only a single lightness, it is misc
    elif np.allclose(diff_L, 0):  # pragma: no cover
        return "misc"

    # SEQUENTIAL
    # If the lightness values always increase or decrease, it is sequential
    elif np.isclose(np.abs(np.sum(diff_L)), np.sum(np.abs(diff_L))):
        return "sequential"

    # DIVERGING
    # If the lightness values have a central extreme and sequential sides
    # Then it is diverging
    elif np.isclose(np.abs(np.sum(diff_L0)), np.sum(np.abs(diff_L0))) and np.isclose(
        np.abs(np.sum(diff_L1)), np.sum(np.abs(diff_L1))
    ):
        # If the perceptual difference between the last and first value is
        # comparable to the other perceptual differences, it is cyclic
        if np.all(np.abs(np.diff(deltas)) < deltas[::2]) and np.diff(deltas[::2]):
            return "cyclic"

        # Otherwise, it is a normal diverging colormap
        else:
            return "diverging"

    # MISC 2
    # If none of the criteria above apply, it is misc
    else:
        return "misc"


# Function create a colormap using a subset of the colors in an existing one
def get_sub_cmap(
    cmap: Colormap | Name, start: float, stop: float, *, N: int | None = None
) -> LC:
    """
    Creates a :obj:`~matplotlib.cm.ListedColormap` object using the colors in
    the range `[start, stop]` of the provided `cmap` and returns it.

    This function can be used to create a colormap that only uses a portion of
    an existing colormap.
    If `N` is not set to *None*, this function creates a qualitative colormap
    from `cmap` instead.

    Parameters
    ----------
    cmap : str or :obj:`~matplotlib.colors.Colormap` object
        The registered name of the colormap in :mod:`matplotlib.cm` or its
        corresponding :obj:`~matplotlib.colors.Colormap` object.
    start, stop : float
        The normalized range of the colors in `cmap` that must be in the
        sub-colormap.

    Optional
    --------
    N : int or None. Default: None
        The number of color segments to take from the provided `cmap` within
        the range given by the provided `start` and `stop`.
        If *None*, take all colors in `cmap` within this range.

    Returns
    -------
    sub_cmap : :obj:`~matplotlib.colors.ListedColormap`
        The created colormap that uses a subset of the colors in `cmap`.
        If `N` is not *None*, this will be a qualitative colormap.

    Example
    -------
    Creating a colormap using the first 80% of the 'rainforest' colormap::

        >>> get_sub_cmap('cmr.rainforest', 0, 0.8)

    Creating a qualitative colormap containing five colors from the middle 60%
    of the 'lilac' colormap:

        >>> get_sub_cmap('cmr.lilac', 0.2, 0.8, N=5)

    Notes
    -----
    As it can create artifacts, this function does not interpolate between the
    colors in `cmap` to fill up the space. Therefore, using values for `start`
    and `stop` that are too close to each other, may result in a colormap that
    contains too few different colors to be smooth.
    It is recommended to use at least 128 different colors in a colormap for
    optimal results (*CMasher* colormaps have 256 or 511/510 different colors,
    for sequential or diverging/cyclic colormaps respectively).
    One can check the number of colors in a colormap with
    :attr:`matplotlib.colors.Colormap.N`.

    Any colormaps created using this function are not registered in either
    *CMasher* or *MPL*.

    """
    if isinstance(cmap, str):
        # Obtain the colormap
        cmap = mpl.colormaps[cmap]

    # Check value of N to determine suffix for the name
    suffix = "_sub" if N is None else "_qual"

    # Obtain colors
    colors = take_cmap_colors(cmap, N, cmap_range=(start, stop))

    # Create new colormap
    sub_cmap = LC(colors, cmap.name + suffix, N=len(colors))

    # Return sub_cmap
    return sub_cmap


# Function to import all custom colormaps in a file or directory
def import_cmaps(
    cmap_path: str | os.PathLike[str],
    *,
    _skip_registration: bool = False,
) -> None:
    """
    Reads in custom colormaps from a provided file or directory `cmap_path`;
    transforms them into :obj:`~matplotlib.colors.ListedColormap` objects; and
    makes them available in the :mod:`cmasher.cm` module, in addition to
    registering them in the :mod:`matplotlib.cm` module.
    Both the imported colormap and its reversed version will be registered.

    If a provided colormap is a 'cyclic' colormap, its shifted version will
    also be registered with the `_s` suffix.

    Parameters
    ----------
    cmap_path : str or os.PathLike[str]
        Relative or absolute path to a custom colormap file; or directory that
        contains custom colormap files. A colormap file can be a *NumPy* binary
        file ('.npy'); a *viscm* source file ('.jscm'); or any text file.
        If the file is not a JSCM-file, it must contain the normalized; 8-bit;
        or hexadecimal string RGB values that define the colormap.

    Notes
    -----
    All colormap files must have names starting with the 'cm\\_' prefix. The
    resulting colormaps will have the name of their file without the prefix and
    extension.

    In *MPL*, the colormaps will have the added 'cmr.' prefix to avoid name
    clashes.

    Example
    -------
    Importing a colormap named 'test' can be done by saving its normalized RGB
    values in a file called 'cm_test.txt' and executing

        >>> import_cmaps('/path/to/dir/cm_test.txt')

    The 'test' colormap is now available in *CMasher* and *MPL* using

        >>> cmr.cm.test                 # CMasher
        >>> plt.get_cmap('cmr.test')    # MPL

    """
    # Obtain path to file or directory with colormaps
    cmap_path_input = cmap_path
    cmap_path = Path(cmap_path).resolve()

    # Check if provided file or directory exists
    if not cmap_path.exists():
        raise FileNotFoundError(
            f"Input argument 'cmap_path' is a non-existing path ({cmap_path_input!r})!"
        )

    cm_files: list[Path]

    # Check if cmap_path is a file or directory and act accordingly
    if cmap_path.is_file():
        # If file, split cmap_path up into dir and file components
        cmap_dir = cmap_path.parent
        cmap_file = cmap_path

        # Check if its name starts with 'cm_' and raise error if not
        if not cmap_file.stem.startswith("cm_"):
            raise OSError(
                "Input argument 'cmap_path' does not lead to a file "
                f"with the 'cm_' prefix ({cmap_path_input!r})!"
            )

        # Set cm_files to be the sole read-in file
        cm_files = [cmap_file]
    else:
        # If directory, obtain the names of all colormap files in cmap_path
        cmap_dir = cmap_path
        cm_files = sorted(cmap_dir.glob("cm_*"))

        def sort_key(name):
            # prioritize binary files over text files because binary loads faster
            if (ext := name.suffix) == ".npy":
                return 0
            if ext == ".txt":
                return 1
            return 10

        cm_files.sort(key=sort_key)
        del sort_key

    if any(file.suffix == ".jscm" for file in cm_files) and not _HAS_VISCM:
        raise ValueError("The 'viscm' package is required to read '.jscm' files!")

    # Read in all the defined colormaps, transform and register them
    seen: set[str] = set()
    for cm_file in cm_files:
        # Split basename and extension
        base_str = cm_file.stem
        ext_str = cm_file.suffix
        if base_str in seen:
            continue
        else:
            seen.add(base_str)

        cm_name = Name(base_str.removeprefix("cm_"))

        # Process colormap files
        try:
            # If file is a NumPy binary file
            if ext_str == ".npy":
                rgb = np.load(cm_file)

            # If file is viscm source file
            elif ext_str == ".jscm":
                import viscm

                # Load colormap
                cmap = viscm.gui.Colormap(None, None, None)
                cmap.load(cm_file)

                # Create editor and obtain RGB values
                v = viscm.viscm_editor(
                    uniform_space=cmap.uniform_space,
                    cmtype=cmap.cmtype,
                    method=cmap.method,
                    **cmap.params,
                )
                rgb, _ = v.cmap_model.get_sRGB()

            # If file is anything else
            else:
                rgb = np.genfromtxt(cm_file, dtype=None, comments="//", encoding=None)  # type: ignore [call-overload]

            if not _skip_registration:
                # Register colormap
                register_cmap(cm_name, rgb)

            # Check if provided cmap is a cyclic colormap
            # If so, obtain its shifted (reversed) versions as well
            if get_cmap_type(Name("cmr." + cm_name)) == "cyclic":
                # Determine the central value index of the colormap
                idx = len(rgb) // 2

                # Shift the entire colormap by this index
                rgb_s = np.r_[rgb[idx:], rgb[:idx]]

                if not _skip_registration:
                    # Register this colormap as well
                    register_cmap(cm_name + "_s", rgb_s)

        # If any error is raised, reraise it
        except Exception as error:
            raise ValueError(f"Failed to import colormap {cm_name!r}") from error


# Function to register a custom colormap in MPL and CMasher
def register_cmap(name: str, data: RGB) -> None:
    """
    Creates a :obj:`~matplotlib.colors.ListedColormap` object using the
    provided `name` and `data`, and registers the colormap in the
    :mod:`cmasher.cm` and :mod:`matplotlib.cm` modules.
    A reversed version of the colormap will be registered as well.

    Parameters
    ----------
    name : str
        The name that this colormap must have.
    data : 2D array_like of {float; int} with shape `(N, 3)` or 1D array_like \
        of str with shape `(N, )`
        An array containing the RGB values of all segments in the colormap.
        If float, the array contains normalized RGB values.
        If int, the array contains 8-bit RGB values.
        If str, the array contains hexadecimal string RGB values.

    Note
    ----
    In *MPL*, the colormap will have the added 'cmr.' prefix to avoid name
    clashes.

    """
    # Convert provided data to a NumPy array
    cm_data_arr = np.array(data)

    # Check the type of the data
    if issubclass(cm_data_arr.dtype.type, str):
        # If the values are strings, make sure they start with a '#'
        if cm_data_arr.ndim == 0:
            cm_data = [cm_data_arr.item()]
        else:
            cm_data = [f"#{x.removeprefix('#')}" for x in cm_data_arr]

        try:
            # Convert all values to floats
            colorlist = [to_rgb(_) for _ in cm_data]
        except ValueError:
            raise ValueError(
                f"Input data isn't valid hexadecimal RGB values: {data=}"
            ) from None
    else:
        # Make sure that cm_data is 2D
        cm_data_arr = np.atleast_2d(cm_data_arr)

        # If the values are integers, divide them by 255
        if issubclass(cm_data_arr.dtype.type, np.integer):
            cm_data_arr = cm_data_arr / 255

        # Convert cm_data to a list
        # see https://github.com/numpy/numpy/issues/27944
        colorlist = cm_data_arr.tolist()

    # Transform colorlist into a Colormap
    cmap_N = len(colorlist)
    cmap_mpl = LC(colorlist, "cmr." + name, N=cmap_N)
    cmap_cmr = LC(colorlist, name, N=cmap_N)
    cmap_mpl_r = cmap_mpl.reversed()
    cmap_cmr_r = cmap_cmr.reversed()

    # Determine the cm_type of the colormap
    if name in _CMASHER_BUILTIN_MAP_TYPES:
        cm_type = _CMASHER_BUILTIN_MAP_TYPES[name]
    else:
        cm_type = get_cmap_type(cmap_mpl)
        # Test that the colormaps can be called
        cmap_mpl(1)
        cmap_mpl_r(1)

    # Add cmap to matplotlib's cmap list
    mpl.colormaps.register(cmap=cmap_mpl)
    setattr(cmrcm, cmap_cmr.name, cmap_cmr)
    cmrcm.__all__.append(cmap_cmr.name)
    cmrcm.cmap_d[cmap_cmr.name] = cmap_cmr
    cmrcm.cmap_cd[cm_type][cmap_cmr.name] = cmap_cmr

    # Add reversed cmap to matplotlib's cmap list
    mpl.colormaps.register(cmap=cmap_mpl_r)
    setattr(cmrcm, cmap_cmr_r.name, cmap_cmr_r)
    cmrcm.__all__.append(cmap_cmr_r.name)
    cmrcm.cmap_d[cmap_cmr_r.name] = cmap_cmr_r
    cmrcm.cmap_cd[cm_type][cmap_cmr_r.name] = cmap_cmr_r


# Function to set the legend label of an artist that uses a colormap
def set_cmap_legend_entry(artist: Artist, label: str) -> None:
    """
    Sets the label of the provided `artist` to `label`, and creates a legend
    entry using a miniature version of the colormap of `artist` as the legend
    icon.

    This function can be used to add legend entries for *MPL* artists that use
    a colormap, like those made with :func:`~matplotlib.pyplot.hexbin`;
    :func:`~matplotlib.pyplot.hist2d`; :func:`~matplotlib.pyplot.scatter`; or
    any :mod:`~matplotlib.pyplot` function that takes `cmap` as an input
    argument.
    Keep in mind that using this function will override any legend entry that
    already exists for `artist`.

    Parameters
    ----------
    artist : :obj:`~matplotlib.artist.Artist` object
        Any artist object that has the `cmap` attribute, for which a legend
        entry must be made using its colormap as the icon.
    label : str
        The string that must be set as the label of `artist`.

    """
    from matplotlib.legend import Legend

    # Obtain the colormap of the provided artist
    cmap = getattr(artist, "cmap", None)

    # If cmap is None, raise error
    if cmap is None:
        raise ValueError("Input argument 'artist' does not have attribute 'cmap'!")

    # Set the label of this artist
    artist.set_label(label)

    # Add the HandlerColorPolyCollection to the default handler map for artist
    from ._handlercolorpolycollection import _HandlerColorPolyCollection

    Legend.get_default_handler_map()[artist] = _HandlerColorPolyCollection()  # type: ignore [index]


# Function to take N equally spaced colors from a colormap
@overload
def take_cmap_colors(
    cmap: Colormap | Name,
    N: int | None,
    *,
    cmap_range: tuple[float, float] = (0, 1),
    return_fmt: Literal["float", "norm"] = "float",
) -> RGB[float]: ...


@overload
def take_cmap_colors(
    cmap: Colormap | Name,
    N: int | None,
    *,
    cmap_range: tuple[float, float] = (0, 1),
    return_fmt: Literal["int", "8bit"],
) -> RGB[int]: ...


@overload
def take_cmap_colors(
    cmap: Colormap | Name,
    N: int | None,
    *,
    cmap_range: tuple[float, float] = (0, 1),
    return_fmt: Literal["str", "hex"],
) -> list[str]: ...


def take_cmap_colors(
    cmap: Colormap | Name,
    N: int | None,
    *,
    cmap_range: tuple[float, float] = (0, 1),
    return_fmt: Literal["float", "norm", "int", "8bit", "str", "hex"] = "float",
) -> RGB[float] | RGB[int] | list[str]:
    """
    Takes `N` equally spaced colors from the provided colormap `cmap` and
    returns them.

    Parameters
    ----------
    cmap : str or :obj:`~matplotlib.colors.Colormap` object
        The registered name of the colormap in :mod:`matplotlib.cm` or its
        corresponding :obj:`~matplotlib.colors.Colormap` object.
    N : int or None
        The number of colors to take from the provided `cmap` within the given
        `cmap_range`.
        If *None*, take all colors in `cmap` within this range.

    Optional
    --------
    cmap_range : tuple of float. Default: (0, 1)
        The normalized value range in the colormap from which colors should be
        taken.
        By default, colors are taken from the entire colormap.
    return_fmt : {'float'/'norm'; 'int'/'8bit'; 'str'/'hex'}. Default: 'float'
        The format of the requested colors.
        If 'float'/'norm', the colors are returned as normalized RGB tuples.
        If 'int'/'8bit', the colors are returned as 8-bit RGB tuples.
        If 'str'/'hex', the colors are returned using their hexadecimal string
        representations.

    Returns
    -------
    colors : list of {tuple; str}
        The colors that were taken from the provided `cmap`.

    Examples
    --------
    Taking five equally spaced colors from the 'rainforest' colormap::

        >>> take_cmap_colors('cmr.rainforest', 5)
        [(0.0, 0.0, 0.0),
         (0.226123592, 0.124584033, 0.562997277),
         (0.0548210513, 0.515835251, 0.45667819),
         (0.709615979, 0.722863985, 0.0834727592),
         (1.0, 1.0, 1.0)]

    Requesting their 8-bit RGB values instead::

        >>> take_cmap_colors('cmr.rainforest', 5, return_fmt='int')
        [(0, 0, 0),
         (58, 32, 144),
         (14, 132, 116),
         (181, 184, 21),
         (255, 255, 255)]

    Requesting HEX-code values instead::

        >>> take_cmap_colors('cmr.rainforest', 5, return_fmt='hex')
        ['#000000', '#3A2090', '#0E8474', '#B5B815', '#FFFFFF']

    Requesting colors in a specific range::

        >>> take_cmap_colors('cmr.rainforest', 5, cmap_range=(0.2, 0.8),
                             return_fmt='hex')
        ['#3E0374', '#10528A', '#0E8474', '#5CAD3C', '#D6BF4A']

    Note
    ----
    Using this function on a perceptually uniform sequential colormap, like
    those in *CMasher*, allows one to pick a number of line colors that are
    different but still sequential. This is useful when plotting a set of lines
    that describe the same property, but have a different initial state.

    """
    # Obtain the colormap
    if isinstance(cmap, str):
        cmap = mpl.colormaps[cmap]

    # Check if provided cmap_range is valid
    if not ((0 <= cmap_range[0] <= 1) and (0 <= cmap_range[1] <= 1)):
        raise ValueError(
            "Input argument 'cmap_range' does not contain normalized values!"
        )

    # Extract and convert start and stop to their integer indices (inclusive)
    start = int(np.floor(cmap_range[0] * cmap.N))
    stop = int(np.ceil(cmap_range[1] * cmap.N)) - 1

    # Pick colors
    index: NDArray[np.int64]
    if N is None:
        index = np.arange(start, stop + 1, dtype="int64")
    else:
        index = np.array(np.rint(np.linspace(start, stop, num=N)), dtype="int64")
    colors = cmap(index)

    # Convert colors to proper format
    if return_fmt in ("float", "norm", "int", "8bit"):
        colors = np.apply_along_axis(to_rgb, 1, colors)  # type: ignore [call-overload]
        if return_fmt in ("int", "8bit"):
            colors = np.array(np.rint(colors * 255), dtype=int)
            return [(int(c[0]), int(c[1]), int(c[2])) for c in colors]  # type: ignore [misc]
        else:
            return [(float(c[0]), float(c[1]), float(c[2])) for c in colors]  # type: ignore [misc]
    elif return_fmt in ("str", "hex"):
        return [to_hex(x).upper() for x in colors]
    else:
        raise ValueError(return_fmt)


# Function to view what a colormap looks like
def view_cmap(
    cmap: Colormap | Name,
    *,
    savefig: str | None = None,
    show_test: bool = False,
    show_grayscale: bool = False,
) -> None:
    """
    Shows a simple plot of the provided `cmap`.

    Parameters
    ----------
    cmap : str or :obj:`~matplotlib.colors.Colormap` object
        The registered name of the colormap in :mod:`matplotlib.cm` or its
        corresponding :obj:`~matplotlib.colors.Colormap` object.

    Optional
    --------
    savefig : str or None. Default: None
        If not *None*, the path where the plot must be saved to.
        Else, the plot will simply be shown.
    show_test : bool. Default: False
        If *True*, show a colormap test in the plot instead.
    show_grayscale : bool. Default: False
        If *True*, also show the grayscale version of `cmap`.

    """
    import matplotlib.pyplot as plt
    from matplotlib.axes import Axes

    if isinstance(cmap, str):
        # Obtain cmap
        cmap = mpl.colormaps[cmap]

    # Check if show_grayscale is True
    if show_grayscale:
        # If so, create a colormap of cmap in grayscale
        rgb = cmap(np.arange(cmap.N))[:, :3]
        lightness = cspace_convert(rgb)[:, 0]
        lightness /= 99.99871678
        rgb_L = cmrcm.neutral(lightness)[:, :3]
        cmap_L = LC(rgb_L)

        # Set that there are two plots to create
        nplots = 2
    else:
        # Else, there is only one plot
        nplots = 1

    # Create figure
    fig, ax = plt.subplots(ncols=nplots, figsize=(12.8 * nplots, 3.2))

    # Check if show_test is True
    if show_test:
        # If so, use a colormap test data file
        data = np.load(Path(__file__).parent / "data" / "colormaptest.npy")
    else:
        # If not, just plot the colormap
        data = [np.linspace(0, 1, cmap.N)]

    # If show_grayscale is True, show both plots instead of just one
    if show_grayscale:
        if isinstance(ax, Axes):  # pragma: no cover
            raise RuntimeError
        ax[0].imshow(data, cmap=cmap, aspect="auto")
        ax[0].set_axis_off()
        ax[1].imshow(data, cmap=cmap_L, aspect="auto")
        ax[1].set_axis_off()
    else:
        if not isinstance(ax, Axes):  # pragma: no cover
            raise RuntimeError
        ax.imshow(data, cmap=cmap, aspect="auto")
        ax.set_axis_off()

    # Use tight layout
    fig.tight_layout(pad=0, h_pad=0, w_pad=0)

    # If savefig is not None, save the figure
    if savefig is not None:
        fig.savefig(savefig, dpi=100, bbox_inches="tight", pad_inches=0)
        plt.close(fig)

    # Else, simply show it
    else:
        plt.show()


# %% IMPORT SCRIPT
# Import all colormaps defined in './colormaps'
import_cmaps(Path(__file__).parent / "colormaps")
