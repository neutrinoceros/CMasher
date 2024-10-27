# %% IMPORTS
# Package imports
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
    [0.24309136, 0.01863338, 0.08934888],
    [0.24804834, 0.01832749, 0.09056240],
    [0.25300942, 0.01797397, 0.09171907],
    [0.25797417, 0.01757320, 0.09281736],
    [0.26294307, 0.01712403, 0.09385472],
    [0.26791452, 0.01662911, 0.09483032],
    [0.27288913, 0.01608733, 0.09574117],
    [0.27786538, 0.01550157, 0.09658607],
    [0.28284278, 0.01487304, 0.09736270],
    [0.28782102, 0.01420276, 0.09806832],
    [0.29279871, 0.01349403, 0.09870107],
    [0.29777491, 0.01274961, 0.09925847],
    [0.30274847, 0.01197287, 0.09973799],
    [0.30771804, 0.01116788, 0.10013708],
    [0.31268232, 0.01033900, 0.10045291],
    [0.31763972, 0.00949150, 0.10068267],
    [0.32258800, 0.00863243, 0.10082417],
    [0.32752565, 0.00776775, 0.10087393],
    [0.33244986, 0.00690668, 0.10083001],
    [0.33735854, 0.00605740, 0.10068909],
    [0.34224871, 0.00523060, 0.10044894],
    [0.34711725, 0.00443797, 0.10010734],
    [0.35196078, 0.00369238, 0.09966226],
    [0.35677561, 0.00300812, 0.09911207],
    [0.36155796, 0.00240036, 0.09845512],
    [0.36630323, 0.00188703, 0.09769155],
    [0.37100710, 0.00148604, 0.09682094],
    [0.37566464, 0.00121756, 0.09584471],
    [0.38027106, 0.00110208, 0.09476441],
    [0.38482137, 0.00116127, 0.09358301],
    [0.38931057, 0.00141734, 0.09230471],
    [0.39373387, 0.00189244, 0.09093464],
    [0.39808681, 0.00260823, 0.08947884],
    [0.40236528, 0.00358566, 0.08794465],
    [0.40656573, 0.00484424, 0.08634009],
    [0.41068530, 0.00640163, 0.08467365],
    [0.41472185, 0.00827339, 0.08295418],
    [0.41867398, 0.01047271, 0.08119070],
    [0.42254107, 0.01301029, 0.07939194],
    [0.42632324, 0.01589441, 0.07756620],
    [0.43002124, 0.01913101, 0.07572116],
    [0.43363642, 0.02272395, 0.07386387],
    [0.43717059, 0.02667527, 0.07200027],
    [0.44062592, 0.03098552, 0.07013558],
    [0.44400487, 0.03565401, 0.06827425],
    [0.44731003, 0.04067491, 0.06641981],
    [0.45054413, 0.04575655, 0.06457493],
    [0.45370990, 0.05080261, 0.06274171],
    [0.45681004, 0.05581132, 0.06092161],
    [0.45984719, 0.06078162, 0.05911559],
    [0.46282395, 0.06571290, 0.05732446],
    [0.46574272, 0.07060526, 0.05554812],
    [0.46860579, 0.07545910, 0.05378637],
    [0.47141540, 0.08027487, 0.05203924],
    [0.47417354, 0.08505361, 0.05030583],
    [0.47688217, 0.08979616, 0.04858581],
    [0.47954300, 0.09450386, 0.04687801],
    [0.48215778, 0.09917766, 0.04518209],
    [0.48472800, 0.10381898, 0.04349685],
    [0.48725506, 0.10842912, 0.04182137],
    [0.48974031, 0.11300935, 0.04015040],
    [0.49218496, 0.11756094, 0.03849120],
    [0.49459017, 0.12208515, 0.03687955],
    [0.49695696, 0.12658323, 0.03531382],
    [0.49928632, 0.13105642, 0.03379248],
    [0.50157913, 0.13550589, 0.03231415],
    [0.50383622, 0.13993281, 0.03087752],
    [0.50605833, 0.14433831, 0.02948142],
    [0.50824623, 0.14872334, 0.02812502],
    [0.51040058, 0.15308895, 0.02680734],
    [0.51252190, 0.15743625, 0.02552737],
    [0.51461087, 0.16176600, 0.02428472],
    [0.51666794, 0.16607921, 0.02307861],
    [0.51869360, 0.17037673, 0.02190855],
    [0.52068834, 0.17465933, 0.02077423],
    [0.52265254, 0.17892785, 0.01967526],
    [0.52458658, 0.18318304, 0.01861140],
    [0.52649089, 0.18742553, 0.01758266],
    [0.52836568, 0.19165615, 0.01658871],
    [0.53021138, 0.19587543, 0.01562982],
    [0.53202823, 0.20008401, 0.01470600],
    [0.53381645, 0.20428257, 0.01381731],
    [0.53557629, 0.20847165, 0.01296398],
    [0.53730808, 0.21265170, 0.01214649],
    [0.53901195, 0.21682331, 0.01136507],
    [0.54068808, 0.22098699, 0.01062010],
    [0.54233666, 0.22514321, 0.00991205],
    [0.54395785, 0.22929243, 0.00924148],
    [0.54555181, 0.23343506, 0.00860897],
    [0.54711869, 0.23757152, 0.00801515],
    [0.54865860, 0.24170220, 0.00746073],
    [0.55017168, 0.24582748, 0.00694643],
    [0.55165803, 0.24994772, 0.00647303],
    [0.55311774, 0.25406326, 0.00604137],
    [0.55455091, 0.25817444, 0.00565232],
    [0.55595761, 0.26228158, 0.00530679],
    [0.55733792, 0.26638496, 0.00500573],
    [0.55869191, 0.27048490, 0.00475014],
    [0.56001963, 0.27458166, 0.00454106],
    [0.56132113, 0.27867551, 0.00437954],
    [0.56259646, 0.28276670, 0.00426670],
    [0.56384570, 0.28685546, 0.00420370],
    [0.56506891, 0.29094196, 0.00419178],
    [0.56626609, 0.29502650, 0.00423205],
    [0.56743724, 0.29910929, 0.00432573],
    [0.56858240, 0.30319052, 0.00447410],
    [0.56970165, 0.30727034, 0.00467849],
    [0.57079503, 0.31134892, 0.00494022],
    [0.57186247, 0.31542650, 0.00526054],
    [0.57290400, 0.31950324, 0.00564079],
    [0.57391977, 0.32357919, 0.00608247],
    [0.57490968, 0.32765460, 0.00658685],
    [0.57587371, 0.33172962, 0.00715529],
    [0.57681201, 0.33580430, 0.00778930],
    [0.57772452, 0.33987882, 0.00849022],
    [0.57861118, 0.34395334, 0.00925941],
    [0.57947219, 0.34802786, 0.01009843],
    [0.58030739, 0.35210260, 0.01100855],
    [0.58111684, 0.35617763, 0.01199120],
    [0.58190064, 0.36025301, 0.01304785],
    [0.58265865, 0.36432891, 0.01417975],
    [0.58339105, 0.36840533, 0.01538841],
    [0.58409771, 0.37248243, 0.01667507],
    [0.58477872, 0.37656025, 0.01804109],
    [0.58543408, 0.38063888, 0.01948778],
    [0.58606378, 0.38471841, 0.02101636],
    [0.58666789, 0.38879886, 0.02262811],
    [0.58724632, 0.39288038, 0.02432417],
    [0.58779921, 0.39696294, 0.02610575],
    [0.58832644, 0.40104670, 0.02797386],
    [0.58882816, 0.40513162, 0.02992964],
    [0.58930423, 0.40921787, 0.03197399],
    [0.58975480, 0.41330542, 0.03410791],
    [0.59017975, 0.41739439, 0.03633221],
    [0.59057918, 0.42148479, 0.03864772],
    [0.59095302, 0.42557671, 0.04104236],
    [0.59130131, 0.42967020, 0.04343720],
    [0.59162403, 0.43376530, 0.04583796],
    [0.59192114, 0.43786212, 0.04824370],
    [0.59219270, 0.44196064, 0.05065361],
    [0.59243858, 0.44606101, 0.05306680],
    [0.59265890, 0.45016320, 0.05548251],
    [0.59285348, 0.45426735, 0.05789990],
    [0.59302237, 0.45837349, 0.06031823],
    [0.59316550, 0.46248168, 0.06273671],
    [0.59328277, 0.46659204, 0.06515459],
    [0.59337424, 0.47070457, 0.06757114],
    [0.59343970, 0.47481940, 0.06998560],
    [0.59347912, 0.47893660, 0.07239723],
    [0.59349244, 0.48305623, 0.07480532],
    [0.59347948, 0.48717842, 0.07720911],
    [0.59344019, 0.49130321, 0.07960789],
    [0.59337441, 0.49543072, 0.08200092],
    [0.59328194, 0.49956106, 0.08438746],
    [0.59316273, 0.50369428, 0.08676680],
    [0.59301651, 0.50783055, 0.08913818],
    [0.59284309, 0.51196996, 0.09150088],
    [0.59264235, 0.51611258, 0.09385417],
    [0.59241396, 0.52025858, 0.09619730],
    [0.59215766, 0.52440808, 0.09852953],
    [0.59187331, 0.52856117, 0.10085013],
    [0.59156051, 0.53271802, 0.10315834],
    [0.59121894, 0.53687876, 0.10545341],
    [0.59084837, 0.54104351, 0.10773460],
    [0.59044837, 0.54521243, 0.11000116],
    [0.59001854, 0.54938568, 0.11225233],
    [0.58955855, 0.55356340, 0.11448735],
    [0.58906795, 0.55774574, 0.11670547],
    [0.58854625, 0.56193288, 0.11890591],
    [0.58799298, 0.56612498, 0.12108792],
    [0.58740771, 0.57032220, 0.12325073],
    [0.58678981, 0.57452473, 0.12539356],
    [0.58613873, 0.57873275, 0.12751563],
    [0.58545394, 0.58294641, 0.12961618],
    [0.58473477, 0.58716592, 0.13169441],
    [0.58398056, 0.59139147, 0.13374953],
    [0.58319061, 0.59562324, 0.13578074],
    [0.58236429, 0.59986142, 0.13778727],
    [0.58150075, 0.60410621, 0.13976829],
    [0.58059922, 0.60835783, 0.14172299],
    [0.57965890, 0.61261645, 0.14365056],
    [0.57867895, 0.61688228, 0.14555018],
    [0.57765843, 0.62115554, 0.14742099],
    [0.57659641, 0.62543642, 0.14926217],
    [0.57549192, 0.62972515, 0.15107287],
    [0.57434398, 0.63402190, 0.15285221],
    [0.57315149, 0.63832693, 0.15459932],
    [0.57191335, 0.64264042, 0.15631332],
    [0.57062842, 0.64696260, 0.15799330],
    [0.56929555, 0.65129366, 0.15963836],
    [0.56791345, 0.65563383, 0.16124755],
    [0.56648083, 0.65998334, 0.16281993],
    [0.56499636, 0.66434239, 0.16435454],
    [0.56345871, 0.66871117, 0.16585040],
    [0.56186636, 0.67308993, 0.16730650],
    [0.56021781, 0.67747887, 0.16872181],
    [0.55851151, 0.68187821, 0.17009527],
    [0.55674586, 0.68628814, 0.17142584],
    [0.55491916, 0.69070889, 0.17271239],
    [0.55302964, 0.69514067, 0.17395381],
    [0.55107547, 0.69958369, 0.17514891],
    [0.54905473, 0.70403815, 0.17629652],
    [0.54696553, 0.70850424, 0.17739543],
    [0.54480574, 0.71298219, 0.17844435],
    [0.54257321, 0.71747220, 0.17944198],
    [0.54026570, 0.72197446, 0.18038698],
    [0.53788088, 0.72648916, 0.18127797],
    [0.53541640, 0.73101650, 0.18211352],
    [0.53286962, 0.73555668, 0.18289215],
    [0.53023791, 0.74010988, 0.18361229],
    [0.52751846, 0.74467629, 0.18427237],
    [0.52470839, 0.74925610, 0.18487072],
    [0.52180471, 0.75384947, 0.18540566],
    [0.51880417, 0.75845659, 0.18587537],
    [0.51570339, 0.76307763, 0.18627798],
    [0.51249886, 0.76771277, 0.18661155],
    [0.50918685, 0.77236217, 0.18687405],
    [0.50576348, 0.77702598, 0.18706336],
    [0.50222468, 0.78170436, 0.18717730],
    [0.49856601, 0.78639746, 0.18721350],
    [0.49478284, 0.79110545, 0.18716951],
    [0.49087030, 0.79582847, 0.18704278],
    [0.48682317, 0.80056665, 0.18683059],
    [0.48263593, 0.80532013, 0.18653010],
    [0.47830282, 0.81008902, 0.18613835],
    [0.47381743, 0.81487347, 0.18565211],
    [0.46917302, 0.81967359, 0.18506800],
    [0.46436236, 0.82448952, 0.18438241],
    [0.45937767, 0.82932135, 0.18359154],
    [0.45421058, 0.83416919, 0.18269130],
    [0.44885201, 0.83903314, 0.18167733],
    [0.44329221, 0.84391329, 0.18054498],
    [0.43752050, 0.84880972, 0.17928924],
    [0.43152512, 0.85372253, 0.17790462],
    [0.42529326, 0.85865180, 0.17638526],
    [0.41881084, 0.86359760, 0.17472476],
    [0.41206230, 0.86856000, 0.17291617],
    [0.40503036, 0.87353906, 0.17095189],
    [0.39769574, 0.87853483, 0.16882354],
    [0.39003682, 0.88354737, 0.16652189],
    [0.38202920, 0.88857672, 0.16403670],
    [0.37364516, 0.89362293, 0.16135653],
    [0.36485299, 0.89868601, 0.15846859],
    [0.35561615, 0.90376599, 0.15535841],
    [0.34589207, 0.90886290, 0.15200954],
    [0.33563060, 0.91397675, 0.14840307],
    [0.32477213, 0.91910757, 0.14451714],
    [0.31324486, 0.92425534, 0.14032627],
    [0.30096083, 0.92942009, 0.13580031],
    [0.28781045, 0.93460179, 0.13090324],
    [0.27365414, 0.93980045, 0.12559132],
    [0.25830942, 0.94501603, 0.11981050],
    [0.24152998, 0.95024853, 0.11349274],
    [0.22296933, 0.95549793, 0.10655012],
    [0.20211288, 0.96076418, 0.09886573],
    [0.17813682, 0.96604726, 0.09027807],
]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.pepper", N=256)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)