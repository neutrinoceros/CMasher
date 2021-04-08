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
cm_type = 'diverging'

# RGB-values of this colormap
cm_data = [[0.57869284, 0.94700453, 0.95383509],
           [0.57330096, 0.94244813, 0.95218584],
           [0.56790414, 0.93790619, 0.95055025],
           [0.56250183, 0.93337844, 0.94892950],
           [0.55709400, 0.92886470, 0.94732325],
           [0.55168026, 0.92436472, 0.94573223],
           [0.54626041, 0.91987829, 0.94415663],
           [0.54083428, 0.91540519, 0.94259649],
           [0.53540142, 0.91094515, 0.94105277],
           [0.52996183, 0.90649797, 0.93952504],
           [0.52451517, 0.90206341, 0.93801392],
           [0.51906115, 0.89764122, 0.93651980],
           [0.51359971, 0.89323118, 0.93504255],
           [0.50813051, 0.88883304, 0.93358271],
           [0.50265329, 0.88444654, 0.93214066],
           [0.49716797, 0.88007146, 0.93071625],
           [0.49167433, 0.87570754, 0.92930975],
           [0.48617195, 0.87135452, 0.92792190],
           [0.48066080, 0.86701216, 0.92655247],
           [0.47514069, 0.86268020, 0.92520162],
           [0.46961139, 0.85835838, 0.92386959],
           [0.46407266, 0.85404645, 0.92255672],
           [0.45852424, 0.84974413, 0.92126329],
           [0.45296603, 0.84545117, 0.91998924],
           [0.44739784, 0.84116729, 0.91873474],
           [0.44181946, 0.83689223, 0.91749997],
           [0.43623070, 0.83262572, 0.91628509],
           [0.43063137, 0.82836747, 0.91509023],
           [0.42502129, 0.82411721, 0.91391555],
           [0.41940026, 0.81987466, 0.91276117],
           [0.41376812, 0.81563953, 0.91162721],
           [0.40812469, 0.81141153, 0.91051377],
           [0.40246980, 0.80719037, 0.90942095],
           [0.39680330, 0.80297576, 0.90834883],
           [0.39112505, 0.79876739, 0.90729746],
           [0.38543488, 0.79456497, 0.90626692],
           [0.37973269, 0.79036819, 0.90525724],
           [0.37401834, 0.78617674, 0.90426845],
           [0.36829174, 0.78199032, 0.90330056],
           [0.36255279, 0.77780859, 0.90235356],
           [0.35680142, 0.77363124, 0.90142744],
           [0.35103745, 0.76945793, 0.90052248],
           [0.34526089, 0.76528834, 0.89963852],
           [0.33947179, 0.76112213, 0.89877532],
           [0.33367017, 0.75695898, 0.89793279],
           [0.32785588, 0.75279849, 0.89711137],
           [0.32202912, 0.74864036, 0.89631060],
           [0.31619008, 0.74448422, 0.89553017],
           [0.31033866, 0.74032967, 0.89477063],
           [0.30447528, 0.73617639, 0.89403125],
           [0.29860011, 0.73202399, 0.89331209],
           [0.29271343, 0.72787206, 0.89261309],
           [0.28681572, 0.72372025, 0.89193378],
           [0.28090735, 0.71956814, 0.89127427],
           [0.27498896, 0.71541533, 0.89063408],
           [0.26906124, 0.71126143, 0.89001292],
           [0.26312486, 0.70710597, 0.88941086],
           [0.25718092, 0.70294859, 0.88882703],
           [0.25123043, 0.69878883, 0.88826140],
           [0.24527462, 0.69462621, 0.88771373],
           [0.23931508, 0.69046034, 0.88718322],
           [0.23335351, 0.68629075, 0.88666946],
           [0.22739188, 0.68211696, 0.88617198],
           [0.22143248, 0.67793848, 0.88569042],
           [0.21547800, 0.67375483, 0.88522406],
           [0.20953152, 0.66956553, 0.88477214],
           [0.20359659, 0.66537008, 0.88433394],
           [0.19767730, 0.66116797, 0.88390868],
           [0.19177835, 0.65695868, 0.88349548],
           [0.18590517, 0.65274164, 0.88309369],
           [0.18006401, 0.64851634, 0.88270206],
           [0.17426203, 0.64428224, 0.88231942],
           [0.16850747, 0.64003882, 0.88194450],
           [0.16280986, 0.63578543, 0.88157637],
           [0.15718007, 0.63152155, 0.88121346],
           [0.15163047, 0.62724665, 0.88085394],
           [0.14617558, 0.62296002, 0.88049685],
           [0.14083138, 0.61866121, 0.88013964],
           [0.13561664, 0.61434953, 0.87978090],
           [0.13055227, 0.61002443, 0.87941833],
           [0.12566179, 0.60568534, 0.87904945],
           [0.12097171, 0.60133167, 0.87867186],
           [0.11651156, 0.59696278, 0.87828307],
           [0.11231340, 0.59257814, 0.87787994],
           [0.10841196, 0.58817719, 0.87745920],
           [0.10484430, 0.58375940, 0.87701740],
           [0.10164914, 0.57932420, 0.87655087],
           [0.09886510, 0.57487117, 0.87605525],
           [0.09652994, 0.57039990, 0.87552588],
           [0.09468006, 0.56590987, 0.87495827],
           [0.09334588, 0.56140087, 0.87434666],
           [0.09255347, 0.55687251, 0.87368561],
           [0.09231938, 0.55232472, 0.87296842],
           [0.09265244, 0.54775739, 0.87218838],
           [0.09355187, 0.54317052, 0.87133816],
           [0.09500670, 0.53856430, 0.87040963],
           [0.09699741, 0.53393908, 0.86939415],
           [0.09949602, 0.52929541, 0.86828228],
           [0.10246810, 0.52463411, 0.86706387],
           [0.10587541, 0.51995613, 0.86572833],
           [0.10967576, 0.51526281, 0.86426419],
           [0.11382580, 0.51055574, 0.86265950],
           [0.11828050, 0.50583694, 0.86090155],
           [0.12299581, 0.50110877, 0.85897736],
           [0.12792818, 0.49637399, 0.85687361],
           [0.13303495, 0.49163581, 0.85457687],
           [0.13827461, 0.48689788, 0.85207389],
           [0.14360717, 0.48216423, 0.84935190],
           [0.14899424, 0.47743927, 0.84639902],
           [0.15439799, 0.47272781, 0.84320453],
           [0.15978344, 0.46803477, 0.83975943],
           [0.16511635, 0.46336535, 0.83605671],
           [0.17036521, 0.45872465, 0.83209177],
           [0.17550082, 0.45411767, 0.82786267],
           [0.18049667, 0.44954915, 0.82337025],
           [0.18532943, 0.44502339, 0.81861819],
           [0.18997899, 0.44054421, 0.81361291],
           [0.19442908, 0.43611475, 0.80836325],
           [0.19866639, 0.43173758, 0.80288030],
           [0.20268189, 0.42741446, 0.79717672],
           [0.20646873, 0.42314661, 0.79126674],
           [0.21002416, 0.41893452, 0.78516513],
           [0.21334744, 0.41477813, 0.77888727],
           [0.21644007, 0.41067692, 0.77244864],
           [0.21930549, 0.40662992, 0.76586449],
           [0.22194871, 0.40263581, 0.75914954],
           [0.22437598, 0.39869301, 0.75231781],
           [0.22659392, 0.39479978, 0.74538284],
           [0.22861020, 0.39095420, 0.73835702],
           [0.23043243, 0.38715428, 0.73125216],
           [0.23206893, 0.38339797, 0.72407881],
           [0.23352752, 0.37968323, 0.71684701],
           [0.23481608, 0.37600805, 0.70956590],
           [0.23594240, 0.37237043, 0.70224378],
           [0.23691411, 0.36876841, 0.69488810],
           [0.23773864, 0.36520013, 0.68750558],
           [0.23842228, 0.36166379, 0.68010314],
           [0.23897259, 0.35815764, 0.67268550],
           [0.23939501, 0.35468004, 0.66525875],
           [0.23969623, 0.35122941, 0.65782678],
           [0.23988177, 0.34780424, 0.65039394],
           [0.23995694, 0.34440312, 0.64296415],
           [0.23992678, 0.34102470, 0.63554088],
           [0.23979609, 0.33766769, 0.62812723],
           [0.23956944, 0.33433088, 0.62072594],
           [0.23925118, 0.33101313, 0.61333943],
           [0.23884542, 0.32771334, 0.60596984],
           [0.23835581, 0.32443050, 0.59861944],
           [0.23778580, 0.32116362, 0.59129023],
           [0.23713919, 0.31791178, 0.58398324],
           [0.23641859, 0.31467410, 0.57670083],
           [0.23562751, 0.31144977, 0.56944356],
           [0.23476863, 0.30823799, 0.56221282],
           [0.23384436, 0.30503801, 0.55501014],
           [0.23285756, 0.30184913, 0.54783592],
           [0.23181055, 0.29867067, 0.54069108],
           [0.23070554, 0.29550198, 0.53357645],
           [0.22954464, 0.29234247, 0.52649273],
           [0.22832987, 0.28919153, 0.51944051],
           [0.22706312, 0.28604862, 0.51242029],
           [0.22574622, 0.28291320, 0.50543250],
           [0.22438088, 0.27978477, 0.49847747],
           [0.22296875, 0.27666284, 0.49155548],
           [0.22151140, 0.27354694, 0.48466672],
           [0.22001024, 0.27043662, 0.47781146],
           [0.21846644, 0.26733144, 0.47099036],
           [0.21688162, 0.26423100, 0.46420287],
           [0.21525699, 0.26113489, 0.45744915],
           [0.21359342, 0.25804272, 0.45072991],
           [0.21189245, 0.25495414, 0.44404423],
           [0.21015473, 0.25186874, 0.43739306],
           [0.20838166, 0.24878622, 0.43077545],
           [0.20657379, 0.24570619, 0.42419227],
           [0.20473243, 0.24262836, 0.41764250],
           [0.20285807, 0.23955237, 0.41112692],
           [0.20095176, 0.23647793, 0.40464482],
           [0.19901430, 0.23340473, 0.39819596],
           [0.19704615, 0.23033243, 0.39178094],
           [0.19504823, 0.22726077, 0.38539893],
           [0.19302121, 0.22418944, 0.37904975],
           [0.19096568, 0.22111817, 0.37273324],
           [0.18888207, 0.21804663, 0.36644962],
           [0.18677107, 0.21497457, 0.36019827],
           [0.18463321, 0.21190170, 0.35397893],
           [0.18246898, 0.20882775, 0.34779136],
           [0.18027883, 0.20575244, 0.34163532],
           [0.17806319, 0.20267549, 0.33551054],
           [0.17582247, 0.19959662, 0.32941673],
           [0.17355705, 0.19651555, 0.32335359],
           [0.17126727, 0.19343202, 0.31732082],
           [0.16895348, 0.19034573, 0.31131809],
           [0.16661598, 0.18725641, 0.30534506],
           [0.16425505, 0.18416377, 0.29940139],
           [0.16187095, 0.18106754, 0.29348671],
           [0.15946392, 0.17796741, 0.28760066],
           [0.15703418, 0.17486310, 0.28174285],
           [0.15458188, 0.17175430, 0.27591300],
           [0.15210713, 0.16864071, 0.27011088],
           [0.14961017, 0.16552201, 0.26433584],
           [0.14709112, 0.16239789, 0.25858744],
           [0.14455007, 0.15926804, 0.25286525],
           [0.14198701, 0.15613210, 0.24716916],
           [0.13940203, 0.15298974, 0.24149861],
           [0.13679522, 0.14984061, 0.23585293],
           [0.13416654, 0.14668436, 0.23023175],
           [0.13151588, 0.14352057, 0.22463501],
           [0.12884334, 0.14034890, 0.21906169],
           [0.12614878, 0.13716893, 0.21351147],
           [0.12343203, 0.13398023, 0.20798415],
           [0.12069311, 0.13078240, 0.20247868],
           [0.11793173, 0.12757495, 0.19699505],
           [0.11514778, 0.12435745, 0.19153238],
           [0.11234104, 0.12112938, 0.18609015],
           [0.10951121, 0.11789024, 0.18066797],
           [0.10665810, 0.11463950, 0.17526489],
           [0.10378128, 0.11137658, 0.16988075],
           [0.10088052, 0.10810090, 0.16451437],
           [0.09795529, 0.10481182, 0.15916562],
           [0.09500529, 0.10150871, 0.15383328],
           [0.09202991, 0.09819083, 0.14851704],
           [0.08902871, 0.09485748, 0.14321584],
           [0.08600106, 0.09150787, 0.13792899],
           [0.08294630, 0.08814114, 0.13265572],
           [0.07986379, 0.08475645, 0.12739482],
           [0.07675264, 0.08135279, 0.12214593],
           [0.07361211, 0.07792919, 0.11690747],
           [0.07044121, 0.07448455, 0.11167864],
           [0.06723890, 0.07101767, 0.10645840],
           [0.06400410, 0.06752732, 0.10124526],
           [0.06073553, 0.06401210, 0.09603817],
           [0.05743181, 0.06047052, 0.09083573],
           [0.05409148, 0.05690097, 0.08563621],
           [0.05071284, 0.05330166, 0.08043811],
           [0.04729398, 0.04967062, 0.07523980],
           [0.04383290, 0.04600573, 0.07003905],
           [0.04032533, 0.04230459, 0.06483370],
           [0.03681198, 0.03855880, 0.05962158],
           [0.03343838, 0.03492349, 0.05439990],
           [0.03020655, 0.03145663, 0.04916556],
           [0.02711859, 0.02815891, 0.04391515],
           [0.02417669, 0.02503115, 0.03863829],
           [0.02138315, 0.02207428, 0.03360127],
           [0.01874050, 0.01928945, 0.02894484],
           [0.01625140, 0.01667799, 0.02466102],
           [0.01391875, 0.01424146, 0.02074208],
           [0.01174570, 0.01198170, 0.01718058],
           [0.00973575, 0.00990088, 0.01396944],
           [0.00789285, 0.00800160, 0.01110189],
           [0.00622148, 0.00628698, 0.00857157],
           [0.00472684, 0.00476083, 0.00637274],
           [0.00341513, 0.00342790, 0.00450037],
           [0.00229394, 0.00229426, 0.00295046],
           [0.00137302, 0.00136800, 0.00172056],
           [0.00066576, 0.00066063, 0.00081098],
           [0.00019292, 0.00019060, 0.00022793],
           [0.00000000, 0.00000000, 0.00000000],
           [0.00024615, 0.00017402, 0.00018678],
           [0.00087651, 0.00059522, 0.00064582],
           [0.00186026, 0.00121727, 0.00133402],
           [0.00319002, 0.00201789, 0.00223163],
           [0.00486438, 0.00298218, 0.00332572],
           [0.00688465, 0.00409900, 0.00460664],
           [0.00925360, 0.00535941, 0.00606670],
           [0.01197496, 0.00675600, 0.00769941],
           [0.01505310, 0.00828238, 0.00949915],
           [0.01849283, 0.00993297, 0.01146086],
           [0.02229932, 0.01170280, 0.01357993],
           [0.02647801, 0.01358738, 0.01585207],
           [0.03103458, 0.01558259, 0.01827322],
           [0.03597484, 0.01768468, 0.02083953],
           [0.04128527, 0.01989015, 0.02354726],
           [0.04663688, 0.02219574, 0.02639278],
           [0.05195829, 0.02459837, 0.02937254],
           [0.05725332, 0.02709516, 0.03248304],
           [0.06252528, 0.02968336, 0.03572079],
           [0.06777709, 0.03236039, 0.03908234],
           [0.07301135, 0.03512373, 0.04249786],
           [0.07823033, 0.03797101, 0.04585147],
           [0.08343602, 0.04089098, 0.04915452],
           [0.08863026, 0.04376921, 0.05240871],
           [0.09381466, 0.04660434, 0.05561550],
           [0.09899070, 0.04939825, 0.05877621],
           [0.10415972, 0.05215268, 0.06189196],
           [0.10932303, 0.05486915, 0.06496371],
           [0.11448168, 0.05754915, 0.06799237],
           [0.11963664, 0.06019409, 0.07097870],
           [0.12478882, 0.06280523, 0.07392337],
           [0.12993921, 0.06538365, 0.07682690],
           [0.13508850, 0.06793051, 0.07968980],
           [0.14023734, 0.07044690, 0.08251252],
           [0.14538653, 0.07293368, 0.08529534],
           [0.15053661, 0.07539182, 0.08803858],
           [0.15568804, 0.07782225, 0.09074250],
           [0.16084158, 0.08022562, 0.09340714],
           [0.16599741, 0.08260293, 0.09603279],
           [0.17115623, 0.08495474, 0.09861938],
           [0.17631820, 0.08728194, 0.10116707],
           [0.18148390, 0.08958506, 0.10367575],
           [0.18665343, 0.09186493, 0.10614548],
           [0.19182735, 0.09412200, 0.10857605],
           [0.19700567, 0.09635711, 0.11096751],
           [0.20218885, 0.09857069, 0.11331960],
           [0.20737699, 0.10076343, 0.11563220],
           [0.21257022, 0.10293594, 0.11790518],
           [0.21776892, 0.10508866, 0.12013818],
           [0.22297307, 0.10722225, 0.12233107],
           [0.22818278, 0.10933729, 0.12448359],
           [0.23339817, 0.11143429, 0.12659544],
           [0.23861945, 0.11351372, 0.12866624],
           [0.24384653, 0.11557623, 0.13069576],
           [0.24907946, 0.11762233, 0.13268366],
           [0.25431826, 0.11965258, 0.13462958],
           [0.25956293, 0.12166750, 0.13653315],
           [0.26481344, 0.12366766, 0.13839399],
           [0.27006976, 0.12565358, 0.14021170],
           [0.27533180, 0.12762583, 0.14198589],
           [0.28059949, 0.12958498, 0.14371614],
           [0.28587272, 0.13153160, 0.14540202],
           [0.29115134, 0.13346626, 0.14704313],
           [0.29643521, 0.13538958, 0.14863902],
           [0.30172414, 0.13730214, 0.15018927],
           [0.30701794, 0.13920457, 0.15169344],
           [0.31231639, 0.14109751, 0.15315110],
           [0.31761928, 0.14298158, 0.15456179],
           [0.32292642, 0.14485737, 0.15592496],
           [0.32823742, 0.14672565, 0.15724032],
           [0.33355199, 0.14858712, 0.15850743],
           [0.33886990, 0.15044238, 0.15972574],
           [0.34419076, 0.15229223, 0.16089488],
           [0.34951411, 0.15413745, 0.16201454],
           [0.35483980, 0.15597865, 0.16308405],
           [0.36016717, 0.15781679, 0.16410329],
           [0.36549598, 0.15965253, 0.16507166],
           [0.37082563, 0.16148682, 0.16598898],
           [0.37615579, 0.16332036, 0.16685469],
           [0.38148580, 0.16515417, 0.16766869],
           [0.38681532, 0.16698898, 0.16843040],
           [0.39214367, 0.16882582, 0.16913973],
           [0.39747030, 0.17066560, 0.16979641],
           [0.40279473, 0.17250917, 0.17040000],
           [0.40811625, 0.17435762, 0.17095048],
           [0.41343422, 0.17621191, 0.17144765],
           [0.41874803, 0.17807305, 0.17189132],
           [0.42405705, 0.17994202, 0.17228129],
           [0.42936053, 0.18181993, 0.17261758],
           [0.43465775, 0.18370783, 0.17290016],
           [0.43994800, 0.18560681, 0.17312900],
           [0.44523052, 0.18751796, 0.17330414],
           [0.45050455, 0.18944239, 0.17342567],
           [0.45576931, 0.19138122, 0.17349371],
           [0.46102401, 0.19333559, 0.17350844],
           [0.46626782, 0.19530663, 0.17347009],
           [0.47149993, 0.19729549, 0.17337894],
           [0.47671950, 0.19930331, 0.17323530],
           [0.48192569, 0.20133125, 0.17303958],
           [0.48711764, 0.20338044, 0.17279218],
           [0.49229449, 0.20545203, 0.17249361],
           [0.49745539, 0.20754714, 0.17214440],
           [0.50259949, 0.20966688, 0.17174506],
           [0.50772591, 0.21181236, 0.17129632],
           [0.51283378, 0.21398469, 0.17079886],
           [0.51792224, 0.21618491, 0.17025344],
           [0.52299045, 0.21841406, 0.16966083],
           [0.52803758, 0.22067316, 0.16902184],
           [0.53306277, 0.22296319, 0.16833743],
           [0.53806522, 0.22528511, 0.16760853],
           [0.54304412, 0.22763981, 0.16683608],
           [0.54799868, 0.23002817, 0.16602113],
           [0.55292813, 0.23245103, 0.16516477],
           [0.55783173, 0.23490917, 0.16426807],
           [0.56270875, 0.23740332, 0.16333217],
           [0.56755850, 0.23993418, 0.16235825],
           [0.57238029, 0.24250238, 0.16134750],
           [0.57717348, 0.24510851, 0.16030114],
           [0.58193746, 0.24775310, 0.15922042],
           [0.58667165, 0.25043664, 0.15810659],
           [0.59137548, 0.25315955, 0.15696096],
           [0.59604843, 0.25592219, 0.15578480],
           [0.60069003, 0.25872487, 0.15457938],
           [0.60529979, 0.26156787, 0.15334610],
           [0.60987733, 0.26445137, 0.15208620],
           [0.61442224, 0.26737554, 0.15080101],
           [0.61893416, 0.27034047, 0.14949185],
           [0.62341279, 0.27334621, 0.14816010],
           [0.62785784, 0.27639275, 0.14680699],
           [0.63226905, 0.27948004, 0.14543385],
           [0.63664621, 0.28260800, 0.14404197],
           [0.64098913, 0.28577648, 0.14263274],
           [0.64529766, 0.28898529, 0.14120738],
           [0.64957166, 0.29223423, 0.13976716],
           [0.65381105, 0.29552304, 0.13831336],
           [0.65801576, 0.29885142, 0.13684725],
           [0.66218574, 0.30221905, 0.13537010],
           [0.66632098, 0.30562559, 0.13388318],
           [0.67042148, 0.30907066, 0.13238773],
           [0.67448729, 0.31255384, 0.13088503],
           [0.67851846, 0.31607473, 0.12937632],
           [0.68251505, 0.31963288, 0.12786285],
           [0.68647718, 0.32322782, 0.12634591],
           [0.69040493, 0.32685910, 0.12482673],
           [0.69429846, 0.33052621, 0.12330661],
           [0.69815790, 0.33422868, 0.12178683],
           [0.70198340, 0.33796599, 0.12026868],
           [0.70577514, 0.34173764, 0.11875347],
           [0.70953331, 0.34554309, 0.11724277],
           [0.71325810, 0.34938183, 0.11573784],
           [0.71694971, 0.35325337, 0.11423999],
           [0.72060834, 0.35715718, 0.11275072],
           [0.72423425, 0.36109269, 0.11127184],
           [0.72782762, 0.36505946, 0.10980449],
           [0.73138870, 0.36905693, 0.10835048],
           [0.73491775, 0.37308460, 0.10691154],
           [0.73841496, 0.37714200, 0.10548912],
           [0.74188065, 0.38122856, 0.10408544],
           [0.74531498, 0.38534389, 0.10270186],
           [0.74871828, 0.38948741, 0.10134077],
           [0.75209074, 0.39365872, 0.10000384],
           [0.75543264, 0.39785734, 0.09869323],
           [0.75874426, 0.40208277, 0.09741133],
           [0.76202578, 0.40633464, 0.09615999],
           [0.76527751, 0.41061247, 0.09494179],
           [0.76849973, 0.41491579, 0.09375926],
           [0.77169263, 0.41924427, 0.09261462],
           [0.77485646, 0.42359748, 0.09151047],
           [0.77799148, 0.42797503, 0.09044948],
           [0.78109800, 0.43237646, 0.08943468],
           [0.78417621, 0.43680146, 0.08846857],
           [0.78722634, 0.44124968, 0.08755401],
           [0.79024865, 0.44572074, 0.08669390],
           [0.79324337, 0.45021432, 0.08589118],
           [0.79621073, 0.45473007, 0.08514882],
           [0.79915097, 0.45926767, 0.08446980],
           [0.80206433, 0.46382681, 0.08385706],
           [0.80495101, 0.46840720, 0.08331354],
           [0.80781125, 0.47300854, 0.08284214],
           [0.81064525, 0.47763056, 0.08244567],
           [0.81345329, 0.48227294, 0.08212705],
           [0.81623558, 0.48693542, 0.08188894],
           [0.81899227, 0.49161779, 0.08173368],
           [0.82172356, 0.49631982, 0.08166363],
           [0.82442963, 0.50104128, 0.08168096],
           [0.82711088, 0.50578179, 0.08178822],
           [0.82976733, 0.51054129, 0.08198674],
           [0.83239912, 0.51531958, 0.08227805],
           [0.83500666, 0.52011631, 0.08266403],
           [0.83758998, 0.52493140, 0.08314546],
           [0.84014922, 0.52976470, 0.08372309],
           [0.84268481, 0.53461583, 0.08439814],
           [0.84519660, 0.53948489, 0.08517024],
           [0.84768513, 0.54437144, 0.08604030],
           [0.85015020, 0.54927557, 0.08700745],
           [0.85259236, 0.55419689, 0.08807206],
           [0.85501137, 0.55913552, 0.08923280],
           [0.85740788, 0.56409100, 0.09048973],
           [0.85978161, 0.56906349, 0.09184109],
           [0.86213299, 0.57405268, 0.09328617],
           [0.86446212, 0.57905850, 0.09482352],
           [0.86676901, 0.58408094, 0.09645145],
           [0.86905411, 0.58911967, 0.09816879],
           [0.87131737, 0.59417472, 0.09997355],
           [0.87355889, 0.59924605, 0.10186383],
           [0.87577894, 0.60433346, 0.10383795],
           [0.87797777, 0.60943682, 0.10589408],
           [0.88015531, 0.61455616, 0.10803004],
           [0.88231174, 0.61969139, 0.11024385],
           [0.88444721, 0.62484242, 0.11253354],
           [0.88656198, 0.63000910, 0.11489725],
           [0.88865616, 0.63519140, 0.11733295],
           [0.89072981, 0.64038930, 0.11983860],
           [0.89278305, 0.64560273, 0.12241226],
           [0.89481603, 0.65083165, 0.12505206],
           [0.89682888, 0.65607599, 0.12775614],
           [0.89882174, 0.66133572, 0.13052269],
           [0.90079473, 0.66661079, 0.13334997],
           [0.90274797, 0.67190115, 0.13623626],
           [0.90468160, 0.67720678, 0.13917993],
           [0.90659573, 0.68252766, 0.14217936],
           [0.90849047, 0.68786374, 0.14523303],
           [0.91036594, 0.69321503, 0.14833946],
           [0.91222224, 0.69858150, 0.15149722],
           [0.91405947, 0.70396314, 0.15470495],
           [0.91587775, 0.70935994, 0.15796133],
           [0.91767716, 0.71477191, 0.16126513],
           [0.91945779, 0.72019905, 0.16461513],
           [0.92121989, 0.72564129, 0.16801025],
           [0.92296355, 0.73109863, 0.17144936],
           [0.92468872, 0.73657116, 0.17493140],
           [0.92639549, 0.74205889, 0.17845535],
           [0.92808393, 0.74756185, 0.18202028],
           [0.92975424, 0.75308000, 0.18562529],
           [0.93140669, 0.75861327, 0.18926956],
           [0.93304103, 0.76416185, 0.19295219],
           [0.93465733, 0.76972578, 0.19667241],
           [0.93625590, 0.77530497, 0.20042949],
           [0.93783688, 0.78089942, 0.20422272],
           [0.93939998, 0.78650935, 0.20805139],
           [0.94094543, 0.79213474, 0.21191486],
           [0.94247364, 0.79777544, 0.21581253],
           [0.94398413, 0.80343178, 0.21974379],
           [0.94547723, 0.80910368, 0.22370807],
           [0.94695317, 0.81479110, 0.22770486],
           [0.94841148, 0.82049435, 0.23173362],
           [0.94985293, 0.82621317, 0.23579388],
           [0.95127696, 0.83194788, 0.23988517],
           [0.95268386, 0.83769845, 0.24400704],
           [0.95407377, 0.84346490, 0.24815906],
           [0.95544635, 0.84924747, 0.25234084],
           [0.95680225, 0.85504596, 0.25655197],
           [0.95814072, 0.86086080, 0.26079212],
           [0.95946267, 0.86669168, 0.26506089],
           [0.96076719, 0.87253909, 0.26935799]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.iceburn', N=511)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
