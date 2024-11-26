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
cm_type = "diverging"

# RGB-values of this colormap
cm_data = [
    [0.59357707, 0.98983624, 0.10298105],
    [0.58543490, 0.98586376, 0.10747761],
    [0.57729897, 0.98189469, 0.11181264],
    [0.56916921, 0.97792875, 0.11600264],
    [0.56104561, 0.97396567, 0.12006166],
    [0.55292825, 0.97000517, 0.12400180],
    [0.54481726, 0.96604696, 0.12783355],
    [0.53671258, 0.96209078, 0.13156672],
    [0.52861493, 0.95813624, 0.13520830],
    [0.52052475, 0.95418301, 0.13876532],
    [0.51244252, 0.95023076, 0.14224406],
    [0.50436874, 0.94627914, 0.14565037],
    [0.49630389, 0.94232783, 0.14898971],
    [0.48824904, 0.93837643, 0.15226599],
    [0.48020519, 0.93442455, 0.15548315],
    [0.47217347, 0.93047178, 0.15864467],
    [0.46415519, 0.92651773, 0.16175370],
    [0.45615107, 0.92256205, 0.16481446],
    [0.44816294, 0.91860430, 0.16782905],
    [0.44019310, 0.91464397, 0.17079872],
    [0.43224265, 0.91068072, 0.17372726],
    [0.42431417, 0.90671406, 0.17661570],
    [0.41641017, 0.90274351, 0.17946547],
    [0.40853278, 0.89876866, 0.18227902],
    [0.40068544, 0.89478897, 0.18505658],
    [0.39287107, 0.89080400, 0.18779975],
    [0.38509301, 0.88681328, 0.19050973],
    [0.37735564, 0.88281626, 0.19318616],
    [0.36966256, 0.87881249, 0.19583070],
    [0.36201838, 0.87480149, 0.19844353],
    [0.35442831, 0.87078274, 0.20102431],
    [0.34689758, 0.86675575, 0.20357323],
    [0.33943185, 0.86272004, 0.20609025],
    [0.33203722, 0.85867516, 0.20857518],
    [0.32472025, 0.85462063, 0.21102760],
    [0.31748795, 0.85055602, 0.21344693],
    [0.31034775, 0.84648090, 0.21583243],
    [0.30330751, 0.84239486, 0.21818320],
    [0.29637553, 0.83829753, 0.22049822],
    [0.28956046, 0.83418857, 0.22277634],
    [0.28287131, 0.83006765, 0.22501628],
    [0.27631742, 0.82593451, 0.22721671],
    [0.26990833, 0.82178892, 0.22937628],
    [0.26365374, 0.81763069, 0.23149389],
    [0.25756372, 0.81345968, 0.23356748],
    [0.25164822, 0.80927581, 0.23559549],
    [0.24591708, 0.80507904, 0.23757683],
    [0.24038016, 0.80086939, 0.23950942],
    [0.23504696, 0.79664694, 0.24139178],
    [0.22992658, 0.79241182, 0.24322256],
    [0.22502766, 0.78816421, 0.24499995],
    [0.22035816, 0.78390435, 0.24672285],
    [0.21592528, 0.77963255, 0.24838964],
    [0.21173529, 0.77534914, 0.24999924],
    [0.20779347, 0.77105451, 0.25155039],
    [0.20410395, 0.76674911, 0.25304214],
    [0.20066962, 0.76243339, 0.25447357],
    [0.19749207, 0.75810789, 0.25584391],
    [0.19457156, 0.75377313, 0.25715255],
    [0.19190693, 0.74942970, 0.25839900],
    [0.18949565, 0.74507816, 0.25958292],
    [0.18733385, 0.74071915, 0.26070413],
    [0.18541627, 0.73635326, 0.26176250],
    [0.18373660, 0.73198114, 0.26275823],
    [0.18228709, 0.72760342, 0.26369128],
    [0.18105939, 0.72322073, 0.26456221],
    [0.18004387, 0.71883370, 0.26537122],
    [0.17923045, 0.71444295, 0.26611895],
    [0.17860845, 0.71004908, 0.26680607],
    [0.17816638, 0.70565274, 0.26743301],
    [0.17789306, 0.70125447, 0.26800081],
    [0.17777682, 0.69685486, 0.26851024],
    [0.17780567, 0.69245449, 0.26896199],
    [0.17796837, 0.68805386, 0.26935721],
    [0.17825354, 0.68365350, 0.26969688],
    [0.17864991, 0.67925392, 0.26998191],
    [0.17914666, 0.67485561, 0.27021328],
    [0.17973362, 0.67045901, 0.27039219],
    [0.18040090, 0.66606455, 0.27051968],
    [0.18113908, 0.66167266, 0.27059683],
    [0.18193923, 0.65728373, 0.27062473],
    [0.18279292, 0.65289815, 0.27060442],
    [0.18369221, 0.64851629, 0.27053695],
    [0.18462988, 0.64413847, 0.27042348],
    [0.18559909, 0.63976501, 0.27026507],
    [0.18659349, 0.63539622, 0.27006278],
    [0.18760720, 0.63103238, 0.26981765],
    [0.18863480, 0.62667375, 0.26953070],
    [0.18967131, 0.62232060, 0.26920296],
    [0.19071216, 0.61797316, 0.26883542],
    [0.19175317, 0.61363164, 0.26842906],
    [0.19279039, 0.60929627, 0.26798477],
    [0.19382040, 0.60496724, 0.26750351],
    [0.19484008, 0.60064473, 0.26698623],
    [0.19584656, 0.59632889, 0.26643382],
    [0.19683725, 0.59201988, 0.26584716],
    [0.19780982, 0.58771785, 0.26522710],
    [0.19876208, 0.58342294, 0.26457444],
    [0.19969193, 0.57913530, 0.26388989],
    [0.20059794, 0.57485500, 0.26317436],
    [0.20147859, 0.57058214, 0.26242862],
    [0.20233248, 0.56631684, 0.26165339],
    [0.20315812, 0.56205922, 0.26084926],
    [0.20395477, 0.55780930, 0.26001707],
    [0.20472152, 0.55356716, 0.25915753],
    [0.20545721, 0.54933290, 0.25827113],
    [0.20616137, 0.54510656, 0.25735864],
    [0.20683348, 0.54088816, 0.25642071],
    [0.20747262, 0.53667781, 0.25545777],
    [0.20807868, 0.53247549, 0.25447057],
    [0.20865122, 0.52828126, 0.25345965],
    [0.20918971, 0.52409515, 0.25242546],
    [0.20969425, 0.51991715, 0.25136868],
    [0.21016426, 0.51574734, 0.25028967],
    [0.21059989, 0.51158567, 0.24918907],
    [0.21100088, 0.50743218, 0.24806729],
    [0.21136719, 0.50328687, 0.24692481],
    [0.21169885, 0.49914973, 0.24576212],
    [0.21199575, 0.49502077, 0.24457961],
    [0.21225808, 0.49089997, 0.24337778],
    [0.21248571, 0.48678734, 0.24215696],
    [0.21267891, 0.48268283, 0.24091764],
    [0.21283762, 0.47858647, 0.23966014],
    [0.21296211, 0.47449819, 0.23838490],
    [0.21305240, 0.47041800, 0.23709224],
    [0.21310872, 0.46634585, 0.23578254],
    [0.21313121, 0.46228173, 0.23445615],
    [0.21312003, 0.45822559, 0.23311339],
    [0.21307544, 0.45417741, 0.23175461],
    [0.21299752, 0.45013715, 0.23038007],
    [0.21288663, 0.44610475, 0.22899016],
    [0.21274279, 0.44208020, 0.22758508],
    [0.21256639, 0.43806343, 0.22616519],
    [0.21235755, 0.43405441, 0.22473074],
    [0.21211652, 0.43005308, 0.22328199],
    [0.21184357, 0.42605938, 0.22181924],
    [0.21153882, 0.42207329, 0.22034267],
    [0.21120261, 0.41809472, 0.21885260],
    [0.21083510, 0.41412363, 0.21734923],
    [0.21043655, 0.41015996, 0.21583278],
    [0.21000720, 0.40620364, 0.21430350],
    [0.20954722, 0.40225463, 0.21276157],
    [0.20905690, 0.39831284, 0.21120724],
    [0.20853642, 0.39437821, 0.20964067],
    [0.20798603, 0.39045069, 0.20806208],
    [0.20740594, 0.38653018, 0.20647165],
    [0.20679635, 0.38261664, 0.20486955],
    [0.20615750, 0.37870997, 0.20325598],
    [0.20548959, 0.37481011, 0.20163108],
    [0.20479282, 0.37091699, 0.19999504],
    [0.20406740, 0.36703051, 0.19834800],
    [0.20331352, 0.36315061, 0.19669012],
    [0.20253138, 0.35927720, 0.19502154],
    [0.20172116, 0.35541020, 0.19334241],
    [0.20088307, 0.35154952, 0.19165286],
    [0.20001726, 0.34769508, 0.18995302],
    [0.19912392, 0.34384679, 0.18824301],
    [0.19820323, 0.34000455, 0.18652297],
    [0.19725533, 0.33616828, 0.18479298],
    [0.19628040, 0.33233788, 0.18305319],
    [0.19527859, 0.32851326, 0.18130368],
    [0.19425003, 0.32469433, 0.17954455],
    [0.19319491, 0.32088096, 0.17777593],
    [0.19211332, 0.31707308, 0.17599786],
    [0.19100541, 0.31327058, 0.17421046],
    [0.18987132, 0.30947334, 0.17241382],
    [0.18871111, 0.30568128, 0.17060798],
    [0.18752499, 0.30189426, 0.16879306],
    [0.18631298, 0.29811219, 0.16696909],
    [0.18507521, 0.29433495, 0.16513615],
    [0.18381180, 0.29056242, 0.16329431],
    [0.18252277, 0.28679449, 0.16144360],
    [0.18120829, 0.28303103, 0.15958412],
    [0.17986834, 0.27927193, 0.15771585],
    [0.17850307, 0.27551705, 0.15583890],
    [0.17711247, 0.27176627, 0.15395325],
    [0.17569663, 0.26801945, 0.15205898],
    [0.17425557, 0.26427647, 0.15015608],
    [0.17278935, 0.26053718, 0.14824461],
    [0.17129797, 0.25680145, 0.14632457],
    [0.16978147, 0.25306913, 0.14439598],
    [0.16823984, 0.24934008, 0.14245885],
    [0.16667310, 0.24561414, 0.14051320],
    [0.16508122, 0.24189116, 0.13855900],
    [0.16346421, 0.23817098, 0.13659629],
    [0.16182200, 0.23445346, 0.13462501],
    [0.16015463, 0.23073840, 0.13264522],
    [0.15846194, 0.22702567, 0.13065680],
    [0.15674402, 0.22331504, 0.12865984],
    [0.15500067, 0.21960639, 0.12665422],
    [0.15323187, 0.21589950, 0.12463995],
    [0.15143754, 0.21219419, 0.12261699],
    [0.14961751, 0.20849029, 0.12058525],
    [0.14777176, 0.20478755, 0.11854474],
    [0.14590010, 0.20108579, 0.11649537],
    [0.14400236, 0.19738482, 0.11443703],
    [0.14207847, 0.19368438, 0.11236973],
    [0.14012821, 0.18998427, 0.11029335],
    [0.13815136, 0.18628425, 0.10820778],
    [0.13614773, 0.18258409, 0.10611291],
    [0.13411718, 0.17888350, 0.10400873],
    [0.13205940, 0.17518226, 0.10189504],
    [0.12997412, 0.17148010, 0.09977172],
    [0.12786107, 0.16777674, 0.09763865],
    [0.12571996, 0.16407188, 0.09549567],
    [0.12355049, 0.16036523, 0.09334265],
    [0.12135232, 0.15665646, 0.09117943],
    [0.11912504, 0.15294527, 0.08900579],
    [0.11686828, 0.14923132, 0.08682155],
    [0.11458160, 0.14551424, 0.08462648],
    [0.11226456, 0.14179369, 0.08242036],
    [0.10991666, 0.13806926, 0.08020294],
    [0.10753739, 0.13434057, 0.07797395],
    [0.10512619, 0.13060718, 0.07573309],
    [0.10268247, 0.12686865, 0.07348006],
    [0.10020561, 0.12312452, 0.07121454],
    [0.09769494, 0.11937428, 0.06893616],
    [0.09514971, 0.11561744, 0.06664450],
    [0.09256912, 0.11185344, 0.06433911],
    [0.08995234, 0.10808172, 0.06201951],
    [0.08729854, 0.10430163, 0.05968528],
    [0.08460672, 0.10051254, 0.05733578],
    [0.08187581, 0.09671377, 0.05497037],
    [0.07910481, 0.09290454, 0.05258851],
    [0.07629244, 0.08908410, 0.05018930],
    [0.07343748, 0.08525157, 0.04777207],
    [0.07053851, 0.08140606, 0.04533580],
    [0.06759412, 0.07754654, 0.04287963],
    [0.06460262, 0.07367200, 0.04040157],
    [0.06156235, 0.06978122, 0.03790755],
    [0.05847142, 0.06587296, 0.03548345],
    [0.05532777, 0.06194584, 0.03312947],
    [0.05212920, 0.05799834, 0.03084584],
    [0.04887329, 0.05402876, 0.02863281],
    [0.04555743, 0.05003522, 0.02649069],
    [0.04217872, 0.04601566, 0.02441974],
    [0.03872659, 0.04196773, 0.02242030],
    [0.03533289, 0.03789383, 0.02049279],
    [0.03205406, 0.03399100, 0.01863764],
    [0.02889486, 0.03030111, 0.01685540],
    [0.02586033, 0.02682294, 0.01514673],
    [0.02295578, 0.02355537, 0.01351242],
    [0.02018686, 0.02049736, 0.01195353],
    [0.01755949, 0.01764806, 0.01047122],
    [0.01508002, 0.01500676, 0.00906704],
    [0.01275517, 0.01257298, 0.00774287],
    [0.01059209, 0.01034650, 0.00650110],
    [0.00859844, 0.00832749, 0.00534470],
    [0.00678244, 0.00651659, 0.00427743],
    [0.00515301, 0.00491508, 0.00330407],
    [0.00371991, 0.00352518, 0.00243075],
    [0.00249411, 0.00235040, 0.00166547],
    [0.00148836, 0.00139629, 0.00101895],
    [0.00071850, 0.00067188, 0.00050625],
    [0.00020697, 0.00019319, 0.00015064],
    [0.00000000, 0.00000000, 0.00000000],
    [0.00023800, 0.00017868, 0.00017286],
    [0.00084374, 0.00061372, 0.00059183],
    [0.00178352, 0.00126017, 0.00121164],
    [0.00304723, 0.00209698, 0.00201086],
    [0.00463082, 0.00311039, 0.00297550],
    [0.00653328, 0.00429023, 0.00409511],
    [0.00875486, 0.00562860, 0.00536167],
    [0.01129704, 0.00711895, 0.00676851],
    [0.01416189, 0.00875579, 0.00831006],
    [0.01735178, 0.01053444, 0.00998163],
    [0.02086992, 0.01245066, 0.01177893],
    [0.02471901, 0.01450091, 0.01369849],
    [0.02890298, 0.01668170, 0.01573683],
    [0.03342483, 0.01899023, 0.01789126],
    [0.03828875, 0.02142358, 0.02015893],
    [0.04338362, 0.02397938, 0.02253761],
    [0.04843960, 0.02665518, 0.02502496],
    [0.05346256, 0.02944888, 0.02761907],
    [0.05845609, 0.03235840, 0.03031801],
    [0.06342306, 0.03538187, 0.03312013],
    [0.06836626, 0.03851744, 0.03602377],
    [0.07328787, 0.04172937, 0.03902756],
    [0.07819027, 0.04489411, 0.04208216],
    [0.08307501, 0.04801929, 0.04508916],
    [0.08794429, 0.05110668, 0.04805962],
    [0.09279903, 0.05415845, 0.05099586],
    [0.09764151, 0.05717583, 0.05389914],
    [0.10247216, 0.06016079, 0.05677161],
    [0.10729289, 0.06311436, 0.05961434],
    [0.11210435, 0.06603808, 0.06242901],
    [0.11690768, 0.06893308, 0.06521683],
    [0.12170407, 0.07180033, 0.06797886],
    [0.12649389, 0.07464115, 0.07071655],
    [0.13127865, 0.07745608, 0.07343050],
    [0.13605859, 0.08024633, 0.07612206],
    [0.14083442, 0.08301272, 0.07879214],
    [0.14560739, 0.08575571, 0.08144127],
    [0.15037747, 0.08847639, 0.08407069],
    [0.15514549, 0.09117531, 0.08668104],
    [0.15991236, 0.09385292, 0.08927285],
    [0.16467809, 0.09651012, 0.09184714],
    [0.16944330, 0.09914740, 0.09440453],
    [0.17420898, 0.10176500, 0.09694534],
    [0.17897501, 0.10436377, 0.09947053],
    [0.18374186, 0.10694415, 0.10198068],
    [0.18851032, 0.10950638, 0.10447612],
    [0.19328066, 0.11205096, 0.10695746],
    [0.19805304, 0.11457841, 0.10942536],
    [0.20282784, 0.11708911, 0.11188030],
    [0.20760568, 0.11958326, 0.11432260],
    [0.21238691, 0.12206118, 0.11675273],
    [0.21717159, 0.12452337, 0.11917127],
    [0.22196006, 0.12697011, 0.12157867],
    [0.22675264, 0.12940169, 0.12397533],
    [0.23154967, 0.13181835, 0.12636162],
    [0.23635169, 0.13422019, 0.12873779],
    [0.24115866, 0.13660766, 0.13110443],
    [0.24597085, 0.13898099, 0.13346189],
    [0.25078852, 0.14134040, 0.13581055],
    [0.25561194, 0.14368610, 0.13815077],
    [0.26044133, 0.14601829, 0.14048290],
    [0.26527695, 0.14833718, 0.14280729],
    [0.27011902, 0.15064293, 0.14512427],
    [0.27496776, 0.15293573, 0.14743419],
    [0.27982338, 0.15521573, 0.14973739],
    [0.28468611, 0.15748312, 0.15203418],
    [0.28955612, 0.15973802, 0.15432491],
    [0.29443362, 0.16198060, 0.15660989],
    [0.29931880, 0.16421099, 0.15888946],
    [0.30421183, 0.16642934, 0.16116393],
    [0.30911289, 0.16863576, 0.16343364],
    [0.31402214, 0.17083039, 0.16569890],
    [0.31893974, 0.17301336, 0.16796005],
    [0.32386585, 0.17518477, 0.17021741],
    [0.32880061, 0.17734474, 0.17247131],
    [0.33374416, 0.17949339, 0.17472208],
    [0.33869688, 0.18163066, 0.17696993],
    [0.34365890, 0.18375664, 0.17921518],
    [0.34863013, 0.18587157, 0.18145829],
    [0.35361070, 0.18797558, 0.18369962],
    [0.35860075, 0.19006871, 0.18593949],
    [0.36360097, 0.19215064, 0.18817793],
    [0.36861088, 0.19422189, 0.19041564],
    [0.37363054, 0.19628257, 0.19265299],
    [0.37866073, 0.19833226, 0.19488998],
    [0.38370103, 0.20037141, 0.19712728],
    [0.38875150, 0.20240014, 0.19936529],
    [0.39381290, 0.20441799, 0.20160403],
    [0.39888446, 0.20642569, 0.20384437],
    [0.40396721, 0.20842258, 0.20608622],
    [0.40906038, 0.21040937, 0.20833044],
    [0.41416490, 0.21238546, 0.21057702],
    [0.41927998, 0.21435158, 0.21282685],
    [0.42440678, 0.21630693, 0.21507983],
    [0.42954445, 0.21825226, 0.21733690],
    [0.43469347, 0.22018732, 0.21959834],
    [0.43985414, 0.22211195, 0.22186452],
    [0.44502609, 0.22402653, 0.22413618],
    [0.45020946, 0.22593104, 0.22641381],
    [0.45540484, 0.22782507, 0.22869772],
    [0.46061186, 0.22970898, 0.23098868],
    [0.46583058, 0.23158282, 0.23328730],
    [0.47106109, 0.23344656, 0.23559419],
    [0.47630346, 0.23530020, 0.23790998],
    [0.48155773, 0.23714376, 0.24023537],
    [0.48682395, 0.23897724, 0.24257107],
    [0.49210212, 0.24080067, 0.24491785],
    [0.49739222, 0.24261411, 0.24727653],
    [0.50269421, 0.24441763, 0.24964797],
    [0.50800800, 0.24621130, 0.25203310],
    [0.51333405, 0.24799476, 0.25443268],
    [0.51867183, 0.24976844, 0.25684792],
    [0.52402108, 0.25153260, 0.25927997],
    [0.52938250, 0.25328658, 0.26172969],
    [0.53475505, 0.25503130, 0.26419866],
    [0.54013945, 0.25676607, 0.26668789],
    [0.54553478, 0.25849166, 0.26919906],
    [0.55094122, 0.26020788, 0.27173358],
    [0.55635867, 0.26191473, 0.27429305],
    [0.56178653, 0.26361267, 0.27687935],
    [0.56722452, 0.26530186, 0.27949441],
    [0.57267225, 0.26698255, 0.28214032],
    [0.57812919, 0.26865509, 0.28481940],
    [0.58359479, 0.27031983, 0.28753414],
    [0.58906873, 0.27197689, 0.29028723],
    [0.59454953, 0.27362746, 0.29308184],
    [0.60003697, 0.27527150, 0.29592117],
    [0.60552938, 0.27691035, 0.29880900],
    [0.61102567, 0.27854474, 0.30174937],
    [0.61652439, 0.28017571, 0.30474683],
    [0.62202368, 0.28180467, 0.30780643],
    [0.62752118, 0.28343348, 0.31093380],
    [0.63301430, 0.28506416, 0.31413523],
    [0.63849988, 0.28669926, 0.31741773],
    [0.64397428, 0.28834174, 0.32078919],
    [0.64943269, 0.28999568, 0.32425826],
    [0.65486982, 0.29166555, 0.32783471],
    [0.66027858, 0.29335766, 0.33152897],
    [0.66565119, 0.29507892, 0.33535259],
    [0.67097809, 0.29683808, 0.33931770],
    [0.67624771, 0.29864601, 0.34343651],
    [0.68144701, 0.30051520, 0.34772093],
    [0.68656112, 0.30246028, 0.35218124],
    [0.69157408, 0.30449739, 0.35682492],
    [0.69646972, 0.30664336, 0.36165516],
    [0.70123281, 0.30891470, 0.36666901],
    [0.70585094, 0.31132560, 0.37185705],
    [0.71031581, 0.31388648, 0.37720343],
    [0.71462422, 0.31660274, 0.38268732],
    [0.71877805, 0.31947452, 0.38828516],
    [0.72278353, 0.32249720, 0.39397311],
    [0.72664996, 0.32566256, 0.39972887],
    [0.73038834, 0.32896017, 0.40553317],
    [0.73401027, 0.33237858, 0.41136994],
    [0.73752706, 0.33590626, 0.41722654],
    [0.74094929, 0.33953219, 0.42309315],
    [0.74428662, 0.34324619, 0.42896216],
    [0.74754752, 0.34703913, 0.43482831],
    [0.75073960, 0.35090280, 0.44068725],
    [0.75386934, 0.35483006, 0.44653633],
    [0.75694247, 0.35881465, 0.45237351],
    [0.75996410, 0.36285095, 0.45819705],
    [0.76293837, 0.36693431, 0.46400651],
    [0.76586930, 0.37106038, 0.46980083],
    [0.76876007, 0.37522559, 0.47557999],
    [0.77161366, 0.37942670, 0.48134375],
    [0.77443271, 0.38366085, 0.48709203],
    [0.77721952, 0.38792555, 0.49282494],
    [0.77997612, 0.39221863, 0.49854268],
    [0.78270437, 0.39653814, 0.50424542],
    [0.78540608, 0.40088226, 0.50993318],
    [0.78808251, 0.40524962, 0.51560658],
    [0.79073534, 0.40963865, 0.52126544],
    [0.79336559, 0.41404829, 0.52691033],
    [0.79597444, 0.41847741, 0.53254148],
    [0.79856309, 0.42292497, 0.53815897],
    [0.80113247, 0.42739010, 0.54376310],
    [0.80368345, 0.43187204, 0.54935418],
    [0.80621690, 0.43637007, 0.55493241],
    [0.80873363, 0.44088353, 0.56049800],
    [0.81123438, 0.44541186, 0.56605118],
    [0.81371987, 0.44995451, 0.57159213],
    [0.81619085, 0.45451095, 0.57712094],
    [0.81864786, 0.45908082, 0.58263792],
    [0.82109148, 0.46366373, 0.58814326],
    [0.82352232, 0.46825931, 0.59363707],
    [0.82594104, 0.47286716, 0.59911941],
    [0.82834799, 0.47748711, 0.60459061],
    [0.83074384, 0.48211879, 0.61005065],
    [0.83312898, 0.48676202, 0.61549975],
    [0.83550393, 0.49141655, 0.62093799],
    [0.83786914, 0.49608219, 0.62636551],
    [0.84022509, 0.50075874, 0.63178238],
    [0.84257213, 0.50544608, 0.63718879],
    [0.84491085, 0.51014398, 0.64258469],
    [0.84724148, 0.51485239, 0.64797032],
    [0.84956454, 0.51957115, 0.65334568],
    [0.85188043, 0.52430013, 0.65871085],
    [0.85418946, 0.52903928, 0.66406597],
    [0.85649206, 0.53378849, 0.66941107],
    [0.85878868, 0.53854764, 0.67474616],
    [0.86107960, 0.54331671, 0.68007139],
    [0.86336519, 0.54809564, 0.68538681],
    [0.86564582, 0.55288438, 0.69069246],
    [0.86792194, 0.55768282, 0.69598833],
    [0.87019382, 0.56249097, 0.70127454],
    [0.87246181, 0.56730880, 0.70655113],
    [0.87472627, 0.57213627, 0.71181813],
    [0.87698756, 0.57697337, 0.71707558],
    [0.87924600, 0.58182006, 0.72232352],
    [0.88150199, 0.58667633, 0.72756195],
    [0.88375583, 0.59154217, 0.73279092],
    [0.88600786, 0.59641759, 0.73801047],
    [0.88825842, 0.60130257, 0.74322062],
    [0.89050785, 0.60619714, 0.74842137],
    [0.89275649, 0.61110128, 0.75361277],
    [0.89500466, 0.61601501, 0.75879481],
    [0.89725272, 0.62093834, 0.76396752],
    [0.89950099, 0.62587128, 0.76913089],
    [0.90174981, 0.63081386, 0.77428495],
    [0.90399951, 0.63576610, 0.77942969],
    [0.90625044, 0.64072801, 0.78456512],
    [0.90850293, 0.64569962, 0.78969124],
    [0.91075731, 0.65068097, 0.79480803],
    [0.91301392, 0.65567207, 0.79991551],
    [0.91527310, 0.66067297, 0.80501365],
    [0.91753519, 0.66568370, 0.81010244],
    [0.91980053, 0.67070429, 0.81518188],
    [0.92206946, 0.67573479, 0.82025194],
    [0.92434232, 0.68077522, 0.82531259],
    [0.92661945, 0.68582564, 0.83036382],
    [0.92890121, 0.69088609, 0.83540560],
    [0.93118794, 0.69595660, 0.84043788],
    [0.93347999, 0.70103723, 0.84546064],
    [0.93577771, 0.70612803, 0.85047383],
    [0.93808145, 0.71122903, 0.85547742],
    [0.94039158, 0.71634030, 0.86047134],
    [0.94270844, 0.72146188, 0.86545555],
    [0.94503241, 0.72659383, 0.87042998],
    [0.94736385, 0.73173619, 0.87539457],
    [0.94970311, 0.73688902, 0.88034926],
    [0.95205059, 0.74205239, 0.88529397],
    [0.95440664, 0.74722633, 0.89022861],
    [0.95677164, 0.75241092, 0.89515310],
    [0.95914597, 0.75760622, 0.90006735],
    [0.96153002, 0.76281227, 0.90497125],
    [0.96392418, 0.76802914, 0.90986471],
    [0.96632887, 0.77325687, 0.91474759],
    [0.96874447, 0.77849554, 0.91961978],
    [0.97117140, 0.78374520, 0.92448115],
    [0.97361006, 0.78900592, 0.92933156],
    [0.97606083, 0.79427777, 0.93417087],
    [0.97852419, 0.79956078, 0.93899891],
    [0.98100057, 0.80485502, 0.94381552],
    [0.98349043, 0.81016054, 0.94862050],
]

# Create ListedColormap object for this colormap
assert len(cm_data) == 511
cmap = ListedColormap(cm_data, name="cmr.watermelon")
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)
