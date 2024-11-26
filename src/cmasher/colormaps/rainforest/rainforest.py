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
cm_type = "sequential"

# RGB-values of this colormap
cm_data = [
    [0.00000000, 0.00000000, 0.00000000],
    [0.00035348, 0.00018213, 0.00028529],
    [0.00128648, 0.00060495, 0.00102842],
    [0.00278017, 0.00120245, 0.00221135],
    [0.00484080, 0.00193870, 0.00384561],
    [0.00747951, 0.00278742, 0.00595280],
    [0.01070945, 0.00372704, 0.00856159],
    [0.01454267, 0.00473959, 0.01170513],
    [0.01899260, 0.00580832, 0.01542306],
    [0.02407094, 0.00691841, 0.01975933],
    [0.02978955, 0.00805560, 0.02476426],
    [0.03615793, 0.00920708, 0.03049255],
    [0.04309015, 0.01035914, 0.03700839],
    [0.05002764, 0.01150036, 0.04420850],
    [0.05690889, 0.01261875, 0.05155580],
    [0.06373722, 0.01370261, 0.05903594],
    [0.07051465, 0.01474054, 0.06666383],
    [0.07724209, 0.01572147, 0.07445354],
    [0.08391944, 0.01663467, 0.08241831],
    [0.09054575, 0.01746977, 0.09057060],
    [0.09711928, 0.01821687, 0.09892205],
    [0.10363755, 0.01886656, 0.10748338],
    [0.11009796, 0.01940935, 0.11626554],
    [0.11649730, 0.01983620, 0.12527872],
    [0.12283067, 0.02014042, 0.13452913],
    [0.12909439, 0.02031350, 0.14402636],
    [0.13528273, 0.02035041, 0.15377434],
    [0.14139011, 0.02024637, 0.16377707],
    [0.14741086, 0.01999714, 0.17403814],
    [0.15333851, 0.01960089, 0.18455794],
    [0.15916608, 0.01905793, 0.19533444],
    [0.16488647, 0.01837026, 0.20636417],
    [0.17049218, 0.01754237, 0.21764133],
    [0.17597550, 0.01658120, 0.22915829],
    [0.18132834, 0.01549679, 0.24090499],
    [0.18654212, 0.01430350, 0.25286782],
    [0.19160807, 0.01301909, 0.26503145],
    [0.19651733, 0.01166410, 0.27738033],
    [0.20126018, 0.01026643, 0.28989271],
    [0.20582690, 0.00885675, 0.30254797],
    [0.21020707, 0.00747322, 0.31532054],
    [0.21438997, 0.00615793, 0.32818551],
    [0.21836420, 0.00496178, 0.34111258],
    [0.22211790, 0.00394128, 0.35407100],
    [0.22563857, 0.00315967, 0.36702864],
    [0.22891311, 0.00268921, 0.37994912],
    [0.23192784, 0.00260911, 0.39279509],
    [0.23466851, 0.00300633, 0.40552711],
    [0.23712033, 0.00397543, 0.41810379],
    [0.23926810, 0.00561814, 0.43048200],
    [0.24109636, 0.00804265, 0.44261706],
    [0.24258951, 0.01136251, 0.45446314],
    [0.24373208, 0.01569526, 0.46597364],
    [0.24450903, 0.02116053, 0.47710173],
    [0.24490602, 0.02787786, 0.48780105],
    [0.24490975, 0.03596403, 0.49802654],
    [0.24450851, 0.04527317, 0.50773491],
    [0.24369255, 0.05485464, 0.51688580],
    [0.24245442, 0.06459689, 0.52544292],
    [0.24078934, 0.07446643, 0.53337486],
    [0.23869576, 0.08443034, 0.54065588],
    [0.23617539, 0.09445600, 0.54726684],
    [0.23323344, 0.10451116, 0.55319577],
    [0.22987882, 0.11456402, 0.55843817],
    [0.22612359, 0.12458403, 0.56299728],
    [0.22198312, 0.13454210, 0.56688374],
    [0.21747564, 0.14441114, 0.57011523],
    [0.21262202, 0.15416630, 0.57271576],
    [0.20744476, 0.16378577, 0.57471484],
    [0.20196762, 0.17325075, 0.57614642],
    [0.19621532, 0.18254549, 0.57704782],
    [0.19021288, 0.19165743, 0.57745873],
    [0.18398508, 0.20057702, 0.57742012],
    [0.17755678, 0.20929734, 0.57697362],
    [0.17095138, 0.21781440, 0.57616024],
    [0.16419068, 0.22612677, 0.57501971],
    [0.15729560, 0.23423486, 0.57359029],
    [0.15028788, 0.24214004, 0.57190944],
    [0.14318305, 0.24984699, 0.57000995],
    [0.13600121, 0.25735938, 0.56792527],
    [0.12875507, 0.26468395, 0.56568325],
    [0.12146089, 0.27182656, 0.56331179],
    [0.11413150, 0.27879434, 0.56083519],
    [0.10677811, 0.28559492, 0.55827508],
    [0.09941208, 0.29223583, 0.55565145],
    [0.09204385, 0.29872479, 0.55298213],
    [0.08468313, 0.30506954, 0.55028291],
    [0.07733906, 0.31127781, 0.54756770],
    [0.07002039, 0.31735725, 0.54484867],
    [0.06273575, 0.32331535, 0.54213637],
    [0.05549391, 0.32915943, 0.53943989],
    [0.04830422, 0.33489659, 0.53676697],
    [0.04117711, 0.34053373, 0.53412415],
    [0.03431301, 0.34607743, 0.53151696],
    [0.02823151, 0.35153380, 0.52895090],
    [0.02291138, 0.35690931, 0.52642828],
    [0.01831692, 0.36220981, 0.52395192],
    [0.01441361, 0.36744062, 0.52152493],
    [0.01116009, 0.37260755, 0.51914697],
    [0.00852043, 0.37771542, 0.51681985],
    [0.00645349, 0.38276942, 0.51454247],
    [0.00492165, 0.38777406, 0.51231495],
    [0.00388401, 0.39273403, 0.51013518],
    [0.00330343, 0.39765337, 0.50800245],
    [0.00313922, 0.40253639, 0.50591329],
    [0.00335534, 0.40738675, 0.50386607],
    [0.00391350, 0.41220824, 0.50185688],
    [0.00477763, 0.41700434, 0.49988199],
    [0.00591469, 0.42177814, 0.49793828],
    [0.00729035, 0.42653287, 0.49602046],
    [0.00887382, 0.43127137, 0.49412384],
    [0.01063728, 0.43599622, 0.49224386],
    [0.01255386, 0.44070995, 0.49037469],
    [0.01459998, 0.44541483, 0.48851050],
    [0.01675538, 0.45011291, 0.48664535],
    [0.01900372, 0.45480600, 0.48477336],
    [0.02133114, 0.45949578, 0.48288771],
    [0.02372824, 0.46418372, 0.48098173],
    [0.02618991, 0.46887103, 0.47904864],
    [0.02871551, 0.47355874, 0.47708154],
    [0.03130917, 0.47824765, 0.47507350],
    [0.03397939, 0.48293840, 0.47301725],
    [0.03673999, 0.48763141, 0.47090565],
    [0.03960997, 0.49232687, 0.46873158],
    [0.04254495, 0.49702482, 0.46648794],
    [0.04550242, 0.50172506, 0.46416771],
    [0.04851696, 0.50642727, 0.46176388],
    [0.05161452, 0.51113090, 0.45926961],
    [0.05482105, 0.51583525, 0.45667819],
    [0.05816200, 0.52053947, 0.45398309],
    [0.06166185, 0.52524253, 0.45117794],
    [0.06534357, 0.52994330, 0.44825642],
    [0.06922865, 0.53464049, 0.44521263],
    [0.07333640, 0.53933267, 0.44204082],
    [0.07768384, 0.54401831, 0.43873546],
    [0.08228551, 0.54869579, 0.43529123],
    [0.08715324, 0.55336341, 0.43170265],
    [0.09229669, 0.55801931, 0.42796498],
    [0.09772305, 0.56266160, 0.42407362],
    [0.10343720, 0.56728829, 0.42002408],
    [0.10944196, 0.57189736, 0.41581155],
    [0.11573850, 0.57648671, 0.41143183],
    [0.12232648, 0.58105412, 0.40688128],
    [0.12920424, 0.58559738, 0.40215589],
    [0.13636922, 0.59011427, 0.39725069],
    [0.14381797, 0.59460238, 0.39216313],
    [0.15154652, 0.59905933, 0.38688917],
    [0.15955083, 0.60348273, 0.38142398],
    [0.16782596, 0.60787002, 0.37576548],
    [0.17636792, 0.61221870, 0.36990793],
    [0.18517164, 0.61652610, 0.36384903],
    [0.19423323, 0.62078959, 0.35758343],
    [0.20354805, 0.62500639, 0.35110816],
    [0.21311291, 0.62917367, 0.34441716],
    [0.22292319, 0.63328853, 0.33750808],
    [0.23297712, 0.63734796, 0.33037299],
    [0.24327075, 0.64134885, 0.32300881],
    [0.25380149, 0.64528801, 0.31541000],
    [0.26456806, 0.64916207, 0.30756892],
    [0.27556862, 0.65296757, 0.29947914],
    [0.28680131, 0.65670094, 0.29113422],
    [0.29826515, 0.66035841, 0.28252611],
    [0.30995941, 0.66393610, 0.27364605],
    [0.32188354, 0.66742992, 0.26448458],
    [0.33403704, 0.67083566, 0.25503144],
    [0.34641936, 0.67414894, 0.24527563],
    [0.35903067, 0.67736514, 0.23520375],
    [0.37187089, 0.68047947, 0.22480135],
    [0.38493698, 0.68348739, 0.21405665],
    [0.39822972, 0.68638367, 0.20294960],
    [0.41174390, 0.68916381, 0.19146660],
    [0.42547894, 0.69182246, 0.17958321],
    [0.43942652, 0.69435547, 0.16728307],
    [0.45357915, 0.69675858, 0.15454345],
    [0.46792606, 0.69902821, 0.14134113],
    [0.48245238, 0.70116178, 0.12765286],
    [0.49713840, 0.70315810, 0.11345636],
    [0.51195889, 0.70501777, 0.09873170],
    [0.52688474, 0.70674308, 0.08346012],
    [0.54187673, 0.70833987, 0.06764129],
    [0.55689246, 0.70981624, 0.05129587],
    [0.57188177, 0.71118407, 0.03467604],
    [0.58679239, 0.71245786, 0.02096499],
    [0.60156811, 0.71365546, 0.01144501],
    [0.61615466, 0.71479652, 0.00628442],
    [0.63050079, 0.71590203, 0.00561290],
    [0.64456172, 0.71699300, 0.00951989],
    [0.65830117, 0.71808941, 0.01805924],
    [0.67169008, 0.71921013, 0.03125583],
    [0.68471159, 0.72037067, 0.04849044],
    [0.69735437, 0.72158502, 0.06611147],
    [0.70961598, 0.72286398, 0.08347276],
    [0.72149995, 0.72421591, 0.10054993],
    [0.73301372, 0.72564719, 0.11735160],
    [0.74416804, 0.72716234, 0.13389929],
    [0.75497589, 0.72876431, 0.15021920],
    [0.76545070, 0.73045515, 0.16633694],
    [0.77560665, 0.73223593, 0.18227761],
    [0.78545927, 0.73410637, 0.19806771],
    [0.79502059, 0.73606716, 0.21372532],
    [0.80430524, 0.73811714, 0.22927357],
    [0.81332540, 0.74025571, 0.24473025],
    [0.82209182, 0.74248244, 0.26010980],
    [0.83061539, 0.74479634, 0.27542763],
    [0.83890582, 0.74719653, 0.29069728],
    [0.84697167, 0.74968230, 0.30593027],
    [0.85482062, 0.75225302, 0.32113698],
    [0.86245947, 0.75490816, 0.33632669],
    [0.86989396, 0.75764747, 0.35150687],
    [0.87712923, 0.76047070, 0.36668485],
    [0.88416978, 0.76337768, 0.38186782],
    [0.89101913, 0.76636851, 0.39706152],
    [0.89767991, 0.76944365, 0.41226982],
    [0.90415420, 0.77260358, 0.42749685],
    [0.91044358, 0.77584886, 0.44274736],
    [0.91654853, 0.77918057, 0.45802267],
    [0.92246923, 0.78259973, 0.47332599],
    [0.92820506, 0.78610768, 0.48865891],
    [0.93375472, 0.78970603, 0.50402183],
    [0.93911639, 0.79339650, 0.51941608],
    [0.94428753, 0.79718118, 0.53484032],
    [0.94926502, 0.80106227, 0.55029462],
    [0.95404514, 0.80504233, 0.56577636],
    [0.95862355, 0.80912404, 0.58128369],
    [0.96299535, 0.81331040, 0.59681267],
    [0.96715510, 0.81760462, 0.61235912],
    [0.97109682, 0.82201013, 0.62791738],
    [0.97481410, 0.82653054, 0.64348056],
    [0.97830011, 0.83116968, 0.65904062],
    [0.98154779, 0.83593148, 0.67458753],
    [0.98454982, 0.84081997, 0.69011015],
    [0.98729905, 0.84583920, 0.70559469],
    [0.98978835, 0.85099316, 0.72102612],
    [0.99201133, 0.85628564, 0.73638624],
    [0.99396216, 0.86172014, 0.75165543],
    [0.99563650, 0.86729965, 0.76681061],
    [0.99703146, 0.87302652, 0.78182704],
    [0.99814653, 0.87890219, 0.79667691],
    [0.99898398, 0.88492695, 0.81133029],
    [0.99954928, 0.89109977, 0.82575569],
    [0.99985230, 0.89741786, 0.83991936],
    [0.99990681, 0.90387677, 0.85378806],
    [0.99973262, 0.91046972, 0.86732686],
    [0.99935332, 0.91718818, 0.88050438],
    [0.99880092, 0.92402056, 0.89328714],
    [0.99810973, 0.93095404, 0.90564927],
    [0.99732359, 0.93797243, 0.91756364],
    [0.99649290, 0.94505713, 0.92900703],
    [0.99567604, 0.95218676, 0.93995905],
    [0.99494896, 0.95933417, 0.95039442],
    [0.99442226, 0.96646091, 0.96027218],
    [0.99432420, 0.97349028, 0.96947845],
    [0.99602609, 0.97996738, 0.97716299],
    [0.99775551, 0.98647064, 0.98470323],
    [0.99904735, 0.99315948, 0.99234139],
    [1.00000000, 1.00000000, 1.00000000],
]

# Create ListedColormap object for this colormap
assert len(cm_data) == 256
cmap = ListedColormap(cm_data, name="cmr.rainforest")
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)
