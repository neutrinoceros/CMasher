# %% IMPORTS
# Package imports
from matplotlib.cm import register_cmap
from matplotlib.colors import ListedColormap

# All declaration
__all__ = ['cmap']

# Author declaration
__author__ = "Ellert van der Velden (@1313e)"

# Package declaration
__package__ = 'cmasher'


# %% GLOBALS AND DEFINITIONS
# Type of this colormap
cm_type = 'sequential'

# RGB-values of this colormap
cm_data = [[0.00000000, 0.00000000, 0.00000000],
           [0.00023657, 0.00020216, 0.00023587],
           [0.00082976, 0.00069660, 0.00083235],
           [0.00173735, 0.00143463, 0.00175217],
           [0.00294381, 0.00239376, 0.00298288],
           [0.00444119, 0.00355931, 0.00451882],
           [0.00622519, 0.00492054, 0.00635739],
           [0.00829364, 0.00646898, 0.00849771],
           [0.01064584, 0.00819768, 0.01094003],
           [0.01328211, 0.01010073, 0.01368534],
           [0.01620354, 0.01217300, 0.01673516],
           [0.01941187, 0.01440995, 0.02009135],
           [0.02290933, 0.01680747, 0.02375605],
           [0.02669858, 0.01936185, 0.02773162],
           [0.03078267, 0.02206964, 0.03202052],
           [0.03516501, 0.02492766, 0.03662535],
           [0.03984928, 0.02793291, 0.04152182],
           [0.04463647, 0.03108254, 0.04642300],
           [0.04938451, 0.03437388, 0.05128763],
           [0.05410495, 0.03780433, 0.05611890],
           [0.05880139, 0.04134998, 0.06091957],
           [0.06347706, 0.04485215, 0.06569200],
           [0.06813499, 0.04830641, 0.07043838],
           [0.07277800, 0.05171502, 0.07516070],
           [0.07740825, 0.05508030, 0.07986012],
           [0.08202794, 0.05840418, 0.08453794],
           [0.08663948, 0.06168813, 0.08919570],
           [0.09124460, 0.06493384, 0.09383410],
           [0.09584485, 0.06814288, 0.09845368],
           [0.10044262, 0.07131605, 0.10305586],
           [0.10503867, 0.07445506, 0.10764026],
           [0.10963524, 0.07756047, 0.11220806],
           [0.11423300, 0.08063375, 0.11675876],
           [0.11883417, 0.08367520, 0.12129337],
           [0.12343931, 0.08668613, 0.12581121],
           [0.12804988, 0.08966714, 0.13031244],
           [0.13266736, 0.09261870, 0.13479718],
           [0.13729250, 0.09554172, 0.13926476],
           [0.14192645, 0.09843675, 0.14371487],
           [0.14657030, 0.10130432, 0.14814705],
           [0.15122511, 0.10414492, 0.15256072],
           [0.15589188, 0.10695901, 0.15695522],
           [0.16057149, 0.10974710, 0.16132964],
           [0.16526488, 0.11250961, 0.16568310],
           [0.16997287, 0.11524700, 0.17001447],
           [0.17469620, 0.11795975, 0.17432253],
           [0.17943558, 0.12064833, 0.17860592],
           [0.18419162, 0.12331325, 0.18286313],
           [0.18896557, 0.12595456, 0.18709293],
           [0.19375733, 0.12857321, 0.19129317],
           [0.19856788, 0.13116941, 0.19546224],
           [0.20339733, 0.13374392, 0.19959793],
           [0.20824655, 0.13629700, 0.20369834],
           [0.21311536, 0.13882959, 0.20776094],
           [0.21800407, 0.14134230, 0.21178335],
           [0.22291285, 0.14383585, 0.21576305],
           [0.22784174, 0.14631101, 0.21969735],
           [0.23279039, 0.14876883, 0.22358340],
           [0.23775864, 0.15121024, 0.22741833],
           [0.24274588, 0.15363644, 0.23119913],
           [0.24775139, 0.15604876, 0.23492276],
           [0.25277421, 0.15844861, 0.23858617],
           [0.25781375, 0.16083722, 0.24218638],
           [0.26286824, 0.16321657, 0.24572039],
           [0.26793670, 0.16558809, 0.24918535],
           [0.27301716, 0.16795391, 0.25257857],
           [0.27810793, 0.17031588, 0.25589755],
           [0.28320718, 0.17267600, 0.25914005],
           [0.28831262, 0.17503647, 0.26230416],
           [0.29342205, 0.17739946, 0.26538829],
           [0.29853316, 0.17976713, 0.26839127],
           [0.30364356, 0.18214166, 0.27131231],
           [0.30875087, 0.18452519, 0.27415106],
           [0.31385271, 0.18691977, 0.27690761],
           [0.31894682, 0.18932735, 0.27958246],
           [0.32403096, 0.19174978, 0.28217650],
           [0.32910302, 0.19418880, 0.28469104],
           [0.33416104, 0.19664595, 0.28712770],
           [0.33920326, 0.19912263, 0.28948839],
           [0.34422806, 0.20162006, 0.29177526],
           [0.34923398, 0.20413934, 0.29399068],
           [0.35421977, 0.20668136, 0.29613718],
           [0.35918434, 0.20924688, 0.29821737],
           [0.36412675, 0.21183655, 0.30023395],
           [0.36904625, 0.21445084, 0.30218965],
           [0.37394218, 0.21709014, 0.30408717],
           [0.37881402, 0.21975474, 0.30592927],
           [0.38366138, 0.22244484, 0.30771858],
           [0.38848395, 0.22516056, 0.30945769],
           [0.39328149, 0.22790196, 0.31114914],
           [0.39805383, 0.23066908, 0.31279541],
           [0.40280085, 0.23346187, 0.31439884],
           [0.40752250, 0.23628030, 0.31596172],
           [0.41221874, 0.23912427, 0.31748623],
           [0.41688954, 0.24199372, 0.31897448],
           [0.42153492, 0.24488853, 0.32042849],
           [0.42615488, 0.24780861, 0.32185022],
           [0.43074943, 0.25075386, 0.32324154],
           [0.43531859, 0.25372417, 0.32460425],
           [0.43986236, 0.25671945, 0.32594006],
           [0.44438074, 0.25973962, 0.32725066],
           [0.44887373, 0.26278460, 0.32853768],
           [0.45334128, 0.26585432, 0.32980267],
           [0.45778335, 0.26894873, 0.33104716],
           [0.46219990, 0.27206779, 0.33227266],
           [0.46659083, 0.27521145, 0.33348061],
           [0.47095606, 0.27837971, 0.33467244],
           [0.47529548, 0.28157254, 0.33584955],
           [0.47960894, 0.28478996, 0.33701333],
           [0.48389631, 0.28803196, 0.33816514],
           [0.48815742, 0.29129858, 0.33930634],
           [0.49239208, 0.29458983, 0.34043826],
           [0.49660011, 0.29790575, 0.34156224],
           [0.50078129, 0.30124637, 0.34267961],
           [0.50493540, 0.30461175, 0.34379170],
           [0.50906220, 0.30800193, 0.34489982],
           [0.51316146, 0.31141696, 0.34600531],
           [0.51723290, 0.31485689, 0.34710949],
           [0.52127628, 0.31832177, 0.34821370],
           [0.52529132, 0.32181166, 0.34931928],
           [0.52927777, 0.32532659, 0.35042758],
           [0.53323533, 0.32886662, 0.35153993],
           [0.53716374, 0.33243178, 0.35265768],
           [0.54106274, 0.33602211, 0.35378218],
           [0.54493205, 0.33963762, 0.35491479],
           [0.54877142, 0.34327834, 0.35605687],
           [0.55258058, 0.34694427, 0.35720979],
           [0.55635931, 0.35063540, 0.35837490],
           [0.56010736, 0.35435173, 0.35955355],
           [0.56382452, 0.35809322, 0.36074709],
           [0.56751058, 0.36185984, 0.36195686],
           [0.57116536, 0.36565152, 0.36318421],
           [0.57478870, 0.36946820, 0.36443046],
           [0.57838044, 0.37330981, 0.36569690],
           [0.58194045, 0.37717623, 0.36698482],
           [0.58546864, 0.38106737, 0.36829550],
           [0.58896493, 0.38498308, 0.36963021],
           [0.59242926, 0.38892323, 0.37099012],
           [0.59586159, 0.39288766, 0.37237643],
           [0.59926194, 0.39687619, 0.37379035],
           [0.60263031, 0.40088865, 0.37523297],
           [0.60596675, 0.40492483, 0.37670535],
           [0.60927136, 0.40898452, 0.37820861],
           [0.61254422, 0.41306749, 0.37974371],
           [0.61578545, 0.41717352, 0.38131161],
           [0.61899525, 0.42130233, 0.38291329],
           [0.62217375, 0.42545370, 0.38454957],
           [0.62532118, 0.42962735, 0.38622129],
           [0.62843777, 0.43382299, 0.38792928],
           [0.63152373, 0.43804038, 0.38967418],
           [0.63457941, 0.44227918, 0.39145680],
           [0.63760502, 0.44653916, 0.39327765],
           [0.64060094, 0.45081997, 0.39513743],
           [0.64356743, 0.45512138, 0.39703657],
           [0.64650491, 0.45944302, 0.39897568],
           [0.64941366, 0.46378466, 0.40095509],
           [0.65229414, 0.46814594, 0.40297531],
           [0.65514666, 0.47252662, 0.40503660],
           [0.65797166, 0.47692637, 0.40713932],
           [0.66076955, 0.48134491, 0.40928377],
           [0.66354070, 0.48578198, 0.41147010],
           [0.66628560, 0.49023725, 0.41369860],
           [0.66900465, 0.49471046, 0.41596939],
           [0.67169825, 0.49920137, 0.41828257],
           [0.67436689, 0.50370967, 0.42063826],
           [0.67701103, 0.50823509, 0.42303656],
           [0.67963108, 0.51277740, 0.42547745],
           [0.68222749, 0.51733636, 0.42796095],
           [0.68480071, 0.52191171, 0.43048705],
           [0.68735124, 0.52650320, 0.43305574],
           [0.68987955, 0.53111059, 0.43566695],
           [0.69238605, 0.53573369, 0.43832059],
           [0.69487121, 0.54037226, 0.44101655],
           [0.69733551, 0.54502609, 0.44375474],
           [0.69977941, 0.54969497, 0.44653501],
           [0.70220339, 0.55437870, 0.44935723],
           [0.70460793, 0.55907708, 0.45222122],
           [0.70699349, 0.56378992, 0.45512682],
           [0.70936057, 0.56851702, 0.45807384],
           [0.71170965, 0.57325820, 0.46106207],
           [0.71404122, 0.57801329, 0.46409130],
           [0.71635578, 0.58278211, 0.46716129],
           [0.71865383, 0.58756449, 0.47027181],
           [0.72093587, 0.59236026, 0.47342259],
           [0.72320243, 0.59716925, 0.47661336],
           [0.72545402, 0.60199130, 0.47984383],
           [0.72769126, 0.60682622, 0.48311372],
           [0.72991463, 0.61167388, 0.48642268],
           [0.73212466, 0.61653413, 0.48977038],
           [0.73432193, 0.62140682, 0.49315646],
           [0.73650698, 0.62629181, 0.49658053],
           [0.73868052, 0.63118889, 0.50004221],
           [0.74084307, 0.63609797, 0.50354107],
           [0.74299519, 0.64101892, 0.50707665],
           [0.74513749, 0.64595160, 0.51064849],
           [0.74727076, 0.65089581, 0.51425609],
           [0.74939547, 0.65585149, 0.51789893],
           [0.75151226, 0.66081852, 0.52157643],
           [0.75362190, 0.66579672, 0.52528803],
           [0.75572496, 0.67078603, 0.52903311],
           [0.75782205, 0.67578636, 0.53281102],
           [0.75991399, 0.68079754, 0.53662109],
           [0.76200130, 0.68581953, 0.54046262],
           [0.76408467, 0.69085226, 0.54433486],
           [0.76616486, 0.69589560, 0.54823705],
           [0.76824237, 0.70094956, 0.55216840],
           [0.77031799, 0.70601403, 0.55612807],
           [0.77239227, 0.71108900, 0.56011521],
           [0.77446586, 0.71617444, 0.56412894],
           [0.77653941, 0.72127031, 0.56816834],
           [0.77861344, 0.72637666, 0.57223249],
           [0.78068866, 0.73149345, 0.57632043],
           [0.78276546, 0.73662077, 0.58043118],
           [0.78484456, 0.74175859, 0.58456374],
           [0.78692631, 0.74690703, 0.58871711],
           [0.78901132, 0.75206613, 0.59289024],
           [0.79109994, 0.75723602, 0.59708212],
           [0.79319269, 0.76241676, 0.60129168],
           [0.79528988, 0.76760852, 0.60551787],
           [0.79739196, 0.77281141, 0.60975963],
           [0.79949915, 0.77802561, 0.61401590],
           [0.80161186, 0.78325127, 0.61828560],
           [0.80373023, 0.78848861, 0.62256767],
           [0.80585459, 0.79373780, 0.62686106],
           [0.80798504, 0.79899908, 0.63116470],
           [0.81012180, 0.80427268, 0.63547754],
           [0.81226492, 0.80955884, 0.63979856],
           [0.81441453, 0.81485783, 0.64412669],
           [0.81657065, 0.82016992, 0.64846094],
           [0.81873331, 0.82549539, 0.65280027],
           [0.82090249, 0.83083453, 0.65714369],
           [0.82307814, 0.83618765, 0.66149020],
           [0.82526020, 0.84155506, 0.66583882],
           [0.82744857, 0.84693709, 0.67018859],
           [0.82964311, 0.85233406, 0.67453853],
           [0.83184370, 0.85774630, 0.67888770],
           [0.83405014, 0.86317417, 0.68323515],
           [0.83626228, 0.86861799, 0.68757995],
           [0.83847989, 0.87407814, 0.69192117],
           [0.84070279, 0.87955495, 0.69625787],
           [0.84293072, 0.88504878, 0.70058914],
           [0.84516348, 0.89055999, 0.70491405],
           [0.84740081, 0.89608895, 0.70923168],
           [0.84964248, 0.90163599, 0.71354110],
           [0.85188824, 0.90720148, 0.71784138],
           [0.85413786, 0.91278578, 0.72213158],
           [0.85639108, 0.91838925, 0.72641076],
           [0.85864771, 0.92401221, 0.73067795],
           [0.86090750, 0.92965504, 0.73493219],
           [0.86317026, 0.93531806, 0.73917248],
           [0.86543578, 0.94100163, 0.74339781],
           [0.86770394, 0.94670604, 0.74760716],
           [0.86997452, 0.95243166, 0.75179949],
           [0.87224749, 0.95817877, 0.75597371],
           [0.87452265, 0.96394771, 0.76012872],
           [0.87680007, 0.96973874, 0.76426341]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.sepia', N=len(cm_data))
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)