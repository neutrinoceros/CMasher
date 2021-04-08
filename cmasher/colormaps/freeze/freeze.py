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
           [0.00025090, 0.00022180, 0.00028925],
           [0.00087549, 0.00076428, 0.00103974],
           [0.00182388, 0.00157413, 0.00222593],
           [0.00307531, 0.00262693, 0.00384875],
           [0.00461724, 0.00390688, 0.00591605],
           [0.00644107, 0.00540250, 0.00843895],
           [0.00854045, 0.00710488, 0.01143060],
           [0.01091047, 0.00900677, 0.01490552],
           [0.01354717, 0.01110213, 0.01887938],
           [0.01644728, 0.01338580, 0.02336873],
           [0.01960804, 0.01585328, 0.02839099],
           [0.02302706, 0.01850063, 0.03396434],
           [0.02670223, 0.02132431, 0.04010768],
           [0.03063167, 0.02432113, 0.04646570],
           [0.03481365, 0.02748820, 0.05281301],
           [0.03924657, 0.03082286, 0.05916034],
           [0.04378837, 0.03432267, 0.06551273],
           [0.04826530, 0.03798534, 0.07187471],
           [0.05269083, 0.04177303, 0.07825031],
           [0.05706819, 0.04551195, 0.08464294],
           [0.06140021, 0.04920217, 0.09105579],
           [0.06568940, 0.05284659, 0.09749177],
           [0.06993794, 0.05644777, 0.10395354],
           [0.07414780, 0.06000805, 0.11044356],
           [0.07832072, 0.06352946, 0.11696443],
           [0.08245823, 0.06701392, 0.12351815],
           [0.08656168, 0.07046319, 0.13010659],
           [0.09063230, 0.07387885, 0.13673166],
           [0.09467117, 0.07726234, 0.14339511],
           [0.09867929, 0.08061489, 0.15009922],
           [0.10265747, 0.08393780, 0.15684521],
           [0.10660647, 0.08723223, 0.16363453],
           [0.11052696, 0.09049921, 0.17046865],
           [0.11441954, 0.09373956, 0.17734982],
           [0.11828468, 0.09695432, 0.18427876],
           [0.12212282, 0.10014435, 0.19125672],
           [0.12593432, 0.10331032, 0.19828561],
           [0.12971948, 0.10645298, 0.20536659],
           [0.13347851, 0.10957313, 0.21250039],
           [0.13721161, 0.11267126, 0.21968909],
           [0.14091888, 0.11574805, 0.22693347],
           [0.14460038, 0.11880417, 0.23423425],
           [0.14825613, 0.12183991, 0.24159398],
           [0.15188608, 0.12485608, 0.24901224],
           [0.15549013, 0.12785296, 0.25649132],
           [0.15906812, 0.13083117, 0.26403158],
           [0.16261986, 0.13379110, 0.27163450],
           [0.16614509, 0.13673323, 0.27930098],
           [0.16964351, 0.13965796, 0.28703215],
           [0.17311475, 0.14256578, 0.29482882],
           [0.17655839, 0.14545700, 0.30269245],
           [0.17997399, 0.14833225, 0.31062302],
           [0.18336096, 0.15119161, 0.31862312],
           [0.18671878, 0.15403587, 0.32669189],
           [0.19004675, 0.15686522, 0.33483129],
           [0.19334416, 0.15968012, 0.34304214],
           [0.19661026, 0.16248118, 0.35132441],
           [0.19984417, 0.16526873, 0.35967957],
           [0.20304493, 0.16804315, 0.36810880],
           [0.20621158, 0.17080514, 0.37661184],
           [0.20934304, 0.17355524, 0.38518939],
           [0.21243811, 0.17629397, 0.39384213],
           [0.21549547, 0.17902179, 0.40257132],
           [0.21851379, 0.18173945, 0.41137689],
           [0.22149160, 0.18444770, 0.42025899],
           [0.22442730, 0.18714726, 0.42921793],
           [0.22731918, 0.18983894, 0.43825391],
           [0.23016540, 0.19252363, 0.44736698],
           [0.23296397, 0.19520229, 0.45655706],
           [0.23571277, 0.19787598, 0.46582388],
           [0.23840952, 0.20054584, 0.47516700],
           [0.24105165, 0.20321298, 0.48458666],
           [0.24363654, 0.20587884, 0.49408181],
           [0.24616141, 0.20854502, 0.50365089],
           [0.24862323, 0.21121323, 0.51329246],
           [0.25101845, 0.21388495, 0.52300671],
           [0.25334368, 0.21656240, 0.53279066],
           [0.25559513, 0.21924783, 0.54264188],
           [0.25776839, 0.22194330, 0.55255957],
           [0.25985932, 0.22465179, 0.56253898],
           [0.26186289, 0.22737595, 0.57257800],
           [0.26377390, 0.23011893, 0.58267277],
           [0.26558696, 0.23288439, 0.59281783],
           [0.26729599, 0.23567604, 0.60300847],
           [0.26889427, 0.23849783, 0.61323986],
           [0.27037497, 0.24135445, 0.62350459],
           [0.27173064, 0.24425084, 0.63379488],
           [0.27295327, 0.24719240, 0.64410211],
           [0.27403391, 0.25018480, 0.65441750],
           [0.27496352, 0.25323444, 0.66472940],
           [0.27573251, 0.25634820, 0.67502483],
           [0.27633020, 0.25953324, 0.68529063],
           [0.27674544, 0.26279727, 0.69551159],
           [0.27696685, 0.26614854, 0.70566997],
           [0.27698258, 0.26959564, 0.71574631],
           [0.27677941, 0.27314731, 0.72572114],
           [0.27634519, 0.27681274, 0.73557034],
           [0.27566713, 0.28060105, 0.74526910],
           [0.27473265, 0.28452119, 0.75479072],
           [0.27352966, 0.28858173, 0.76410686],
           [0.27204633, 0.29279060, 0.77318850],
           [0.27027341, 0.29715471, 0.78200417],
           [0.26820235, 0.30167962, 0.79052335],
           [0.26582668, 0.30636924, 0.79871595],
           [0.26314304, 0.31122542, 0.80655274],
           [0.26015086, 0.31624773, 0.81400690],
           [0.25685210, 0.32143337, 0.82105518],
           [0.25325310, 0.32677687, 0.82767775],
           [0.24936298, 0.33227037, 0.83385990],
           [0.24519404, 0.33790378, 0.83959211],
           [0.24076142, 0.34366505, 0.84487037],
           [0.23608281, 0.34954062, 0.84969607],
           [0.23117775, 0.35551592, 0.85407576],
           [0.22606710, 0.36157585, 0.85802062],
           [0.22077265, 0.36770526, 0.86154574],
           [0.21531691, 0.37388928, 0.86466937],
           [0.20972262, 0.38011371, 0.86741218],
           [0.20401169, 0.38636546, 0.86979634],
           [0.19820716, 0.39263224, 0.87184514],
           [0.19233052, 0.39890328, 0.87358201],
           [0.18640436, 0.40516872, 0.87503047],
           [0.18044969, 0.41142032, 0.87621317],
           [0.17449003, 0.41765045, 0.87715258],
           [0.16854689, 0.42385314, 0.87786951],
           [0.16264352, 0.43002317, 0.87838395],
           [0.15680424, 0.43615623, 0.87871467],
           [0.15105467, 0.44224882, 0.87887926],
           [0.14542201, 0.44829818, 0.87889403],
           [0.13993537, 0.45430220, 0.87877411],
           [0.13462605, 0.46025931, 0.87853341],
           [0.12952780, 0.46616843, 0.87818476],
           [0.12467691, 0.47202887, 0.87773994],
           [0.12011220, 0.47784031, 0.87720971],
           [0.11587493, 0.48360267, 0.87660400],
           [0.11200905, 0.48931600, 0.87593229],
           [0.10855740, 0.49498086, 0.87520238],
           [0.10556400, 0.50059777, 0.87442194],
           [0.10307166, 0.50616728, 0.87359826],
           [0.10111766, 0.51169039, 0.87273708],
           [0.09973624, 0.51716776, 0.87184481],
           [0.09895171, 0.52260053, 0.87092607],
           [0.09878172, 0.52798951, 0.86998626],
           [0.09923172, 0.53333589, 0.86902915],
           [0.10029868, 0.53864057, 0.86805927],
           [0.10196801, 0.54390472, 0.86707983],
           [0.10421719, 0.54912936, 0.86609426],
           [0.10701631, 0.55431553, 0.86510567],
           [0.11032983, 0.55946432, 0.86411656],
           [0.11411937, 0.56457672, 0.86312957],
           [0.11834484, 0.56965375, 0.86214696],
           [0.12296614, 0.57469642, 0.86117064],
           [0.12794465, 0.57970567, 0.86020254],
           [0.13324382, 0.58468242, 0.85924441],
           [0.13882971, 0.58962759, 0.85829767],
           [0.14467143, 0.59454205, 0.85736371],
           [0.15074117, 0.59942660, 0.85644385],
           [0.15701408, 0.60428205, 0.85553918],
           [0.16346824, 0.60910915, 0.85465073],
           [0.17008437, 0.61390862, 0.85377945],
           [0.17684564, 0.61868114, 0.85292617],
           [0.18373744, 0.62342735, 0.85209166],
           [0.19074714, 0.62814784, 0.85127664],
           [0.19786384, 0.63284317, 0.85048178],
           [0.20507824, 0.63751387, 0.84970756],
           [0.21238235, 0.64216041, 0.84895462],
           [0.21976940, 0.64678321, 0.84822350],
           [0.22723371, 0.65138268, 0.84751460],
           [0.23477048, 0.65595917, 0.84682835],
           [0.24237570, 0.66051298, 0.84616533],
           [0.25004610, 0.66504439, 0.84552589],
           [0.25777909, 0.66955362, 0.84491036],
           [0.26557243, 0.67404086, 0.84431940],
           [0.27342457, 0.67850624, 0.84375329],
           [0.28133426, 0.68294987, 0.84321250],
           [0.28930049, 0.68737179, 0.84269776],
           [0.29732295, 0.69177205, 0.84220916],
           [0.30540104, 0.69615059, 0.84174776],
           [0.31353492, 0.70050738, 0.84131382],
           [0.32172449, 0.70484229, 0.84090833],
           [0.32997021, 0.70915520, 0.84053179],
           [0.33827222, 0.71344593, 0.84018534],
           [0.34663130, 0.71771426, 0.83986954],
           [0.35504765, 0.72195996, 0.83958586],
           [0.36352212, 0.72618277, 0.83933505],
           [0.37205510, 0.73038239, 0.83911863],
           [0.38064704, 0.73455851, 0.83893806],
           [0.38929869, 0.73871080, 0.83879454],
           [0.39801020, 0.74283894, 0.83869004],
           [0.40678177, 0.74694259, 0.83862643],
           [0.41561350, 0.75102143, 0.83860568],
           [0.42450548, 0.75507513, 0.83862976],
           [0.43345718, 0.75910343, 0.83870123],
           [0.44246798, 0.76310607, 0.83882259],
           [0.45153700, 0.76708287, 0.83899653],
           [0.46066304, 0.77103367, 0.83922588],
           [0.46984454, 0.77495843, 0.83951363],
           [0.47907957, 0.77885716, 0.83986290],
           [0.48836584, 0.78272998, 0.84027691],
           [0.49770064, 0.78657714, 0.84075898],
           [0.50708091, 0.79039899, 0.84131248],
           [0.51650318, 0.79419602, 0.84194076],
           [0.52596364, 0.79796886, 0.84264717],
           [0.53545814, 0.80171828, 0.84343499],
           [0.54498225, 0.80544521, 0.84430734],
           [0.55453129, 0.80915071, 0.84526721],
           [0.56410039, 0.81283597, 0.84631738],
           [0.57368456, 0.81650235, 0.84746034],
           [0.58327872, 0.82015129, 0.84869834],
           [0.59287781, 0.82378438, 0.85003326],
           [0.60247685, 0.82740326, 0.85146665],
           [0.61207096, 0.83100967, 0.85299972],
           [0.62165538, 0.83460544, 0.85463332],
           [0.63122562, 0.83819240, 0.85636792],
           [0.64077759, 0.84177240, 0.85820356],
           [0.65030746, 0.84534729, 0.86013994],
           [0.65981175, 0.84891893, 0.86217646],
           [0.66928693, 0.85248921, 0.86431238],
           [0.67873032, 0.85605990, 0.86654644],
           [0.68813976, 0.85963268, 0.86887706],
           [0.69751237, 0.86320941, 0.87130298],
           [0.70684710, 0.86679155, 0.87382199],
           [0.71614179, 0.87038083, 0.87643245],
           [0.72539598, 0.87397857, 0.87913191],
           [0.73460771, 0.87758647, 0.88191867],
           [0.74377717, 0.88120567, 0.88479007],
           [0.75290380, 0.88483749, 0.88774385],
           [0.76198665, 0.88848336, 0.89077799],
           [0.77102620, 0.89214431, 0.89388990],
           [0.78002246, 0.89582144, 0.89707729],
           [0.78897560, 0.89951584, 0.90033785],
           [0.79788586, 0.90322852, 0.90366935],
           [0.80675363, 0.90696045, 0.90706954],
           [0.81557937, 0.91071256, 0.91053626],
           [0.82436362, 0.91448570, 0.91406738],
           [0.83310697, 0.91828073, 0.91766081],
           [0.84181004, 0.92209843, 0.92131454],
           [0.85047348, 0.92593960, 0.92502662],
           [0.85909758, 0.92980508, 0.92879528],
           [0.86768305, 0.93369561, 0.93261867],
           [0.87623077, 0.93761181, 0.93649497],
           [0.88474116, 0.94155446, 0.94042253],
           [0.89321422, 0.94552444, 0.94439991],
           [0.90165110, 0.94952226, 0.94842532],
           [0.91005156, 0.95354885, 0.95249749],
           [0.91841619, 0.95760487, 0.95661487],
           [0.92674495, 0.96169117, 0.96077616],
           [0.93503794, 0.96580855, 0.96498002],
           [0.94329477, 0.96995798, 0.96922525],
           [0.95151541, 0.97414029, 0.97351050],
           [0.95969854, 0.97835678, 0.97783479],
           [0.96784374, 0.98260842, 0.98219677],
           [0.97594916, 0.98689671, 0.98659540],
           [0.98401251, 0.99122336, 0.99102959],
           [0.99203098, 0.99559025, 0.99549813],
           [1.00000000, 1.00000000, 1.00000000]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.freeze', N=256)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
