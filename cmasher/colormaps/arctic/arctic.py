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
           [0.00023317, 0.00023028, 0.00027453],
           [0.00080462, 0.00079836, 0.00097870],
           [0.00165943, 0.00165369, 0.00207937],
           [0.00277259, 0.00277421, 0.00357020],
           [0.00412797, 0.00414626, 0.00545173],
           [0.00571385, 0.00576031, 0.00772779],
           [0.00752107, 0.00760925, 0.01040421],
           [0.00954215, 0.00968758, 0.01348806],
           [0.01177083, 0.01199092, 0.01698708],
           [0.01420170, 0.01451574, 0.02090980],
           [0.01682996, 0.01725912, 0.02526553],
           [0.01965133, 0.02021868, 0.03006390],
           [0.02266196, 0.02339243, 0.03531473],
           [0.02585832, 0.02677874, 0.04101630],
           [0.02923711, 0.03037623, 0.04680336],
           [0.03279517, 0.03418377, 0.05256750],
           [0.03652963, 0.03820048, 0.05831331],
           [0.04043774, 0.04236545, 0.06404492],
           [0.04433712, 0.04648195, 0.06976602],
           [0.04818165, 0.05055441, 0.07547990],
           [0.05197463, 0.05458604, 0.08118947],
           [0.05571879, 0.05857973, 0.08689746],
           [0.05941653, 0.06253805, 0.09260633],
           [0.06307009, 0.06646337, 0.09831801],
           [0.06668142, 0.07035781, 0.10403447],
           [0.07025225, 0.07422330, 0.10975749],
           [0.07378415, 0.07806161, 0.11548875],
           [0.07727855, 0.08187438, 0.12122978],
           [0.08073670, 0.08566311, 0.12698202],
           [0.08415976, 0.08942918, 0.13274679],
           [0.08754875, 0.09317389, 0.13852534],
           [0.09090463, 0.09689843, 0.14431884],
           [0.09422821, 0.10060392, 0.15012841],
           [0.09752027, 0.10429141, 0.15595507],
           [0.10078149, 0.10796188, 0.16179981],
           [0.10401247, 0.11161626, 0.16766357],
           [0.10721376, 0.11525541, 0.17354722],
           [0.11038584, 0.11888017, 0.17945162],
           [0.11352914, 0.12249131, 0.18537756],
           [0.11664405, 0.12608957, 0.19132582],
           [0.11973075, 0.12967564, 0.19729754],
           [0.12278963, 0.13325021, 0.20329312],
           [0.12582092, 0.13681391, 0.20931317],
           [0.12882482, 0.14036737, 0.21535833],
           [0.13180148, 0.14391117, 0.22142921],
           [0.13475095, 0.14744588, 0.22752663],
           [0.13767317, 0.15097202, 0.23365158],
           [0.14056835, 0.15449014, 0.23980401],
           [0.14343650, 0.15800077, 0.24598443],
           [0.14627744, 0.16150436, 0.25219383],
           [0.14909104, 0.16500140, 0.25843288],
           [0.15187739, 0.16849239, 0.26470139],
           [0.15463619, 0.17197775, 0.27100034],
           [0.15736717, 0.17545792, 0.27733049],
           [0.16007039, 0.17893339, 0.28369136],
           [0.16274519, 0.18240452, 0.29008469],
           [0.16539162, 0.18587178, 0.29650983],
           [0.16800916, 0.18933556, 0.30296778],
           [0.17059751, 0.19279629, 0.30945877],
           [0.17315623, 0.19625436, 0.31598321],
           [0.17568492, 0.19971020, 0.32254145],
           [0.17818299, 0.20316418, 0.32913409],
           [0.18065017, 0.20661674, 0.33576076],
           [0.18308543, 0.21006823, 0.34242314],
           [0.18548865, 0.21351911, 0.34912010],
           [0.18785897, 0.21696976, 0.35585259],
           [0.19019551, 0.22042058, 0.36262130],
           [0.19249785, 0.22387200, 0.36942564],
           [0.19476516, 0.22732445, 0.37626595],
           [0.19699630, 0.23077831, 0.38314312],
           [0.19919049, 0.23423404, 0.39005705],
           [0.20134687, 0.23769208, 0.39700759],
           [0.20346440, 0.24115288, 0.40399493],
           [0.20554197, 0.24461690, 0.41101921],
           [0.20757840, 0.24808461, 0.41808051],
           [0.20957247, 0.25155650, 0.42517886],
           [0.21152287, 0.25503307, 0.43231423],
           [0.21342823, 0.25851484, 0.43948652],
           [0.21528710, 0.26200234, 0.44669555],
           [0.21709795, 0.26549615, 0.45394105],
           [0.21885920, 0.26899683, 0.46122269],
           [0.22056856, 0.27250496, 0.46854123],
           [0.22222469, 0.27602122, 0.47589516],
           [0.22382576, 0.27954625, 0.48328375],
           [0.22536896, 0.28308073, 0.49070781],
           [0.22685272, 0.28662541, 0.49816540],
           [0.22827420, 0.29018103, 0.50565656],
           [0.22963128, 0.29374843, 0.51317967],
           [0.23092057, 0.29732842, 0.52073491],
           [0.23213990, 0.30092192, 0.52831985],
           [0.23328601, 0.30452990, 0.53593347],
           [0.23435505, 0.30815334, 0.54357517],
           [0.23534395, 0.31179334, 0.55124246],
           [0.23624897, 0.31545103, 0.55893339],
           [0.23706609, 0.31912763, 0.56664575],
           [0.23779107, 0.32282445, 0.57437693],
           [0.23841869, 0.32654289, 0.58212496],
           [0.23894471, 0.33028441, 0.58988569],
           [0.23936426, 0.33405062, 0.59765495],
           [0.23967036, 0.33784324, 0.60543039],
           [0.23985856, 0.34166406, 0.61320537],
           [0.23992182, 0.34551506, 0.62097538],
           [0.23985322, 0.34939836, 0.62873454],
           [0.23964615, 0.35331618, 0.63647532],
           [0.23929319, 0.35727092, 0.64418979],
           [0.23878605, 0.36126518, 0.65186941],
           [0.23811713, 0.36530167, 0.65950346],
           [0.23727862, 0.36938322, 0.66707989],
           [0.23626216, 0.37351288, 0.67458555],
           [0.23505958, 0.37769382, 0.68200540],
           [0.23366438, 0.38192919, 0.68932165],
           [0.23206980, 0.38622226, 0.69651517],
           [0.23027216, 0.39057610, 0.70356355],
           [0.22826953, 0.39499363, 0.71044243],
           [0.22606398, 0.39947733, 0.71712482],
           [0.22366202, 0.40402912, 0.72358176],
           [0.22107696, 0.40864995, 0.72978242],
           [0.21832968, 0.41333960, 0.73569535],
           [0.21544988, 0.41809642, 0.74128972],
           [0.21247761, 0.42291694, 0.74653688],
           [0.20946307, 0.42779582, 0.75141235],
           [0.20646549, 0.43272585, 0.75589785],
           [0.20355123, 0.43769824, 0.75998287],
           [0.20079063, 0.44270297, 0.76366565],
           [0.19825429, 0.44772938, 0.76695329],
           [0.19600914, 0.45276682, 0.76986099],
           [0.19411495, 0.45780520, 0.77241053],
           [0.19262197, 0.46283542, 0.77462841],
           [0.19156935, 0.46784963, 0.77654391],
           [0.19098524, 0.47284129, 0.77818757],
           [0.19088570, 0.47780537, 0.77958923],
           [0.19127741, 0.48273790, 0.78077786],
           [0.19215751, 0.48763616, 0.78178014],
           [0.19351606, 0.49249821, 0.78262084],
           [0.19533693, 0.49732293, 0.78332228],
           [0.19759934, 0.50210982, 0.78390439],
           [0.20027919, 0.50685888, 0.78438479],
           [0.20335048, 0.51157040, 0.78477933],
           [0.20678595, 0.51624499, 0.78510186],
           [0.21055813, 0.52088345, 0.78536478],
           [0.21463978, 0.52548677, 0.78557863],
           [0.21900458, 0.53005601, 0.78575302],
           [0.22362738, 0.53459230, 0.78589635],
           [0.22848445, 0.53909681, 0.78601595],
           [0.23355363, 0.54357075, 0.78611828],
           [0.23881437, 0.54801530, 0.78620933],
           [0.24424778, 0.55243167, 0.78629411],
           [0.24983662, 0.55682106, 0.78637693],
           [0.25556507, 0.56118460, 0.78646219],
           [0.26141893, 0.56552344, 0.78655322],
           [0.26738534, 0.56983870, 0.78665310],
           [0.27345257, 0.57413143, 0.78676497],
           [0.27961017, 0.57840266, 0.78689133],
           [0.28584880, 0.58265342, 0.78703432],
           [0.29216004, 0.58688468, 0.78719602],
           [0.29853635, 0.59109738, 0.78737827],
           [0.30497098, 0.59529242, 0.78758272],
           [0.31145792, 0.59947068, 0.78781085],
           [0.31799178, 0.60363300, 0.78806406],
           [0.32456766, 0.60778019, 0.78834372],
           [0.33118143, 0.61191303, 0.78865069],
           [0.33782932, 0.61603230, 0.78898592],
           [0.34450779, 0.62013870, 0.78935056],
           [0.35121386, 0.62423294, 0.78974540],
           [0.35794502, 0.62831570, 0.79017091],
           [0.36469854, 0.63238763, 0.79062834],
           [0.37147270, 0.63644936, 0.79111774],
           [0.37826529, 0.64050149, 0.79164021],
           [0.38507499, 0.64454462, 0.79219580],
           [0.39189995, 0.64857932, 0.79278557],
           [0.39873922, 0.65260612, 0.79340949],
           [0.40559148, 0.65662556, 0.79406830],
           [0.41245575, 0.66063816, 0.79476235],
           [0.41933127, 0.66464439, 0.79549189],
           [0.42621714, 0.66864476, 0.79625747],
           [0.43311270, 0.67263971, 0.79705942],
           [0.44001747, 0.67662971, 0.79789795],
           [0.44693096, 0.68061519, 0.79877340],
           [0.45385264, 0.68459657, 0.79968616],
           [0.46078217, 0.68857428, 0.80063655],
           [0.46771930, 0.69254870, 0.80162476],
           [0.47466379, 0.69652023, 0.80265107],
           [0.48161542, 0.70048924, 0.80371576],
           [0.48857403, 0.70445612, 0.80481911],
           [0.49553947, 0.70842121, 0.80596139],
           [0.50251165, 0.71238488, 0.80714286],
           [0.50949047, 0.71634746, 0.80836382],
           [0.51647592, 0.72030930, 0.80962448],
           [0.52346799, 0.72427072, 0.81092511],
           [0.53046668, 0.72823205, 0.81226596],
           [0.53747200, 0.73219359, 0.81364728],
           [0.54448397, 0.73615566, 0.81506936],
           [0.55150265, 0.74011857, 0.81653244],
           [0.55852809, 0.74408262, 0.81803679],
           [0.56556035, 0.74804809, 0.81958270],
           [0.57259949, 0.75201529, 0.82117042],
           [0.57964557, 0.75598450, 0.82280027],
           [0.58669869, 0.75995601, 0.82447251],
           [0.59375893, 0.76393009, 0.82618741],
           [0.60082638, 0.76790703, 0.82794527],
           [0.60790113, 0.77188710, 0.82974637],
           [0.61498325, 0.77587057, 0.83159103],
           [0.62207283, 0.77985772, 0.83347954],
           [0.62916996, 0.78384883, 0.83541221],
           [0.63627470, 0.78784415, 0.83738935],
           [0.64338707, 0.79184398, 0.83941135],
           [0.65050719, 0.79584857, 0.84147847],
           [0.65763514, 0.79985820, 0.84359103],
           [0.66477096, 0.80387314, 0.84574936],
           [0.67191472, 0.80789365, 0.84795379],
           [0.67906640, 0.81192004, 0.85020472],
           [0.68622604, 0.81595257, 0.85250247],
           [0.69339371, 0.81999150, 0.85484735],
           [0.70056942, 0.82403713, 0.85723972],
           [0.70775318, 0.82808975, 0.85967992],
           [0.71494489, 0.83214965, 0.86216838],
           [0.72214463, 0.83621711, 0.86470538],
           [0.72935239, 0.84029242, 0.86729125],
           [0.73656808, 0.84437589, 0.86992639],
           [0.74379161, 0.84846784, 0.87261119],
           [0.75102301, 0.85256856, 0.87534593],
           [0.75826220, 0.85667836, 0.87813094],
           [0.76550897, 0.86079759, 0.88096669],
           [0.77276334, 0.86492656, 0.88385341],
           [0.78002521, 0.86906558, 0.88679144],
           [0.78729432, 0.87321505, 0.88978119],
           [0.79457064, 0.87737527, 0.89282293],
           [0.80185404, 0.88154660, 0.89591693],
           [0.80914417, 0.88572944, 0.89906364],
           [0.81644105, 0.88992412, 0.90226322],
           [0.82374437, 0.89413104, 0.90551602],
           [0.83105389, 0.89835059, 0.90882234],
           [0.83836951, 0.90258315, 0.91218235],
           [0.84569073, 0.90682918, 0.91559647],
           [0.85301755, 0.91108904, 0.91906475],
           [0.86034944, 0.91536322, 0.92258758],
           [0.86768629, 0.91965211, 0.92616502],
           [0.87502760, 0.92395622, 0.92979737],
           [0.88237314, 0.92827598, 0.93348471],
           [0.88972239, 0.93261192, 0.93722727],
           [0.89707509, 0.93696449, 0.94102508],
           [0.90443060, 0.94133428, 0.94487836],
           [0.91178868, 0.94572174, 0.94878703],
           [0.91914846, 0.95012756, 0.95275133],
           [0.92650970, 0.95455223, 0.95677110],
           [0.93387153, 0.95899642, 0.96084644],
           [0.94123333, 0.96346078, 0.96497727],
           [0.94859441, 0.96794597, 0.96916344],
           [0.95595357, 0.97245284, 0.97340496],
           [0.96331004, 0.97698211, 0.97770154],
           [0.97066265, 0.98153466, 0.98205293],
           [0.97800972, 0.98611156, 0.98645894],
           [0.98534976, 0.99071387, 0.99091911],
           [0.99268073, 0.99534284, 0.99543298],
           [1.00000000, 1.00000000, 1.00000000]]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name='cmr.arctic', N=256)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
