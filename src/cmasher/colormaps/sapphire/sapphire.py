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
    [0.00019243, 0.00019125, 0.00022348],
    [0.00066397, 0.00066318, 0.00079297],
    [0.00136919, 0.00137385, 0.00167808],
    [0.00228749, 0.00230493, 0.00287090],
    [0.00340565, 0.00344497, 0.00436952],
    [0.00471417, 0.00478595, 0.00617483],
    [0.00620572, 0.00632185, 0.00828931],
    [0.00787441, 0.00804794, 0.01071648],
    [0.00971537, 0.00996043, 0.01346058],
    [0.01172450, 0.01205619, 0.01652639],
    [0.01389826, 0.01433263, 0.01991913],
    [0.01623357, 0.01678753, 0.02364436],
    [0.01872772, 0.01941904, 0.02770797],
    [0.02137831, 0.02222556, 0.03211609],
    [0.02418317, 0.02520571, 0.03687508],
    [0.02714037, 0.02835830, 0.04194909],
    [0.03024815, 0.03168231, 0.04703353],
    [0.03350490, 0.03517686, 0.05209720],
    [0.03690916, 0.03884119, 0.05714355],
    [0.04045939, 0.04260315, 0.06217557],
    [0.04399981, 0.04631752, 0.06719596],
    [0.04749933, 0.04999517, 0.07220711],
    [0.05096041, 0.05363845, 0.07721118],
    [0.05438525, 0.05724946, 0.08221017],
    [0.05777584, 0.06083014, 0.08720581],
    [0.06113399, 0.06438223, 0.09219974],
    [0.06446137, 0.06790731, 0.09719346],
    [0.06775946, 0.07140685, 0.10218837],
    [0.07102967, 0.07488218, 0.10718574],
    [0.07427327, 0.07833453, 0.11218675],
    [0.07749143, 0.08176505, 0.11719249],
    [0.08068524, 0.08517479, 0.12220405],
    [0.08385570, 0.08856473, 0.12722239],
    [0.08700375, 0.09193578, 0.13224841],
    [0.09013026, 0.09528880, 0.13728295],
    [0.09323603, 0.09862457, 0.14232693],
    [0.09632181, 0.10194386, 0.14738106],
    [0.09938832, 0.10524735, 0.15244607],
    [0.10243620, 0.10853570, 0.15752271],
    [0.10546608, 0.11180953, 0.16261168],
    [0.10847853, 0.11506943, 0.16771355],
    [0.11147408, 0.11831594, 0.17282901],
    [0.11445325, 0.12154959, 0.17795868],
    [0.11741652, 0.12477088, 0.18310305],
    [0.12036431, 0.12798026, 0.18826278],
    [0.12329706, 0.13117819, 0.19343838],
    [0.12621518, 0.13436509, 0.19863030],
    [0.12911899, 0.13754136, 0.20383921],
    [0.13200888, 0.14070738, 0.20906547],
    [0.13488516, 0.14386353, 0.21430961],
    [0.13774812, 0.14701015, 0.21957213],
    [0.14059808, 0.15014758, 0.22485339],
    [0.14343526, 0.15327613, 0.23015402],
    [0.14625996, 0.15639613, 0.23547423],
    [0.14907235, 0.15950784, 0.24081472],
    [0.15187272, 0.16261159, 0.24617563],
    [0.15466119, 0.16570762, 0.25155765],
    [0.15743802, 0.16879621, 0.25696090],
    [0.16020331, 0.17187759, 0.26238611],
    [0.16295728, 0.17495205, 0.26783336],
    [0.16570001, 0.17801978, 0.27330330],
    [0.16843168, 0.18108104, 0.27879612],
    [0.17115237, 0.18413605, 0.28431229],
    [0.17386217, 0.18718501, 0.28985223],
    [0.17656122, 0.19022815, 0.29541615],
    [0.17924952, 0.19326566, 0.30100463],
    [0.18192718, 0.19629776, 0.30661790],
    [0.18459425, 0.19932463, 0.31225626],
    [0.18725072, 0.20234647, 0.31792022],
    [0.18989663, 0.20536346, 0.32361010],
    [0.19253200, 0.20837580, 0.32932614],
    [0.19515682, 0.21138366, 0.33506870],
    [0.19777104, 0.21438722, 0.34083822],
    [0.20037462, 0.21738667, 0.34663506],
    [0.20296752, 0.22038217, 0.35245946],
    [0.20554969, 0.22337392, 0.35831175],
    [0.20812102, 0.22636207, 0.36419227],
    [0.21068141, 0.22934682, 0.37010135],
    [0.21323074, 0.23232833, 0.37603932],
    [0.21576888, 0.23530679, 0.38200651],
    [0.21829565, 0.23828237, 0.38800322],
    [0.22081089, 0.24125525, 0.39402976],
    [0.22331438, 0.24422562, 0.40008644],
    [0.22580592, 0.24719367, 0.40617353],
    [0.22828525, 0.25015959, 0.41229131],
    [0.23075210, 0.25312358, 0.41844003],
    [0.23320613, 0.25608583, 0.42462020],
    [0.23564702, 0.25904657, 0.43083196],
    [0.23807445, 0.26200601, 0.43707541],
    [0.24048799, 0.26496438, 0.44335093],
    [0.24288715, 0.26792191, 0.44965896],
    [0.24527158, 0.27087888, 0.45599923],
    [0.24764056, 0.27383549, 0.46237267],
    [0.24999372, 0.27679210, 0.46877871],
    [0.25233026, 0.27974893, 0.47521824],
    [0.25464960, 0.28270636, 0.48169095],
    [0.25695100, 0.28566470, 0.48819697],
    [0.25923354, 0.28862430, 0.49473675],
    [0.26149637, 0.29158557, 0.50131022],
    [0.26373850, 0.29454893, 0.50791733],
    [0.26595885, 0.29751484, 0.51455810],
    [0.26815622, 0.30048381, 0.52123246],
    [0.27032929, 0.30345640, 0.52794026],
    [0.27247650, 0.30643318, 0.53468164],
    [0.27459630, 0.30941485, 0.54145604],
    [0.27668698, 0.31240218, 0.54826279],
    [0.27874626, 0.31539594, 0.55510220],
    [0.28077214, 0.31839712, 0.56197285],
    [0.28276202, 0.32140676, 0.56887409],
    [0.28471300, 0.32442604, 0.57580502],
    [0.28662183, 0.32745632, 0.58276436],
    [0.28848487, 0.33049916, 0.58975031],
    [0.29029806, 0.33355639, 0.59676043],
    [0.29205645, 0.33663008, 0.60379245],
    [0.29375466, 0.33972271, 0.61084250],
    [0.29538623, 0.34283716, 0.61790644],
    [0.29694378, 0.34597689, 0.62497846],
    [0.29841873, 0.34914607, 0.63205098],
    [0.29980091, 0.35234971, 0.63911438],
    [0.30107837, 0.35559396, 0.64615585],
    [0.30223771, 0.35888642, 0.65315716],
    [0.30326269, 0.36223644, 0.66009509],
    [0.30413586, 0.36565560, 0.66693620],
    [0.30483898, 0.36915807, 0.67363428],
    [0.30535529, 0.37276056, 0.68012621],
    [0.30567606, 0.37648139, 0.68632646],
    [0.30580909, 0.38033759, 0.69212832],
    [0.30579143, 0.38433904, 0.69741440],
    [0.30569412, 0.38848165, 0.70208607],
    [0.30561025, 0.39274449, 0.70609911],
    [0.30562815, 0.39709519, 0.70947957],
    [0.30580850, 0.40150021, 0.71230615],
    [0.30618086, 0.40593198, 0.71467768],
    [0.30675101, 0.41037122, 0.71668827],
    [0.30751245, 0.41480523, 0.71841742],
    [0.30845221, 0.41922652, 0.71992777],
    [0.30955578, 0.42363076, 0.72126766],
    [0.31080918, 0.42801553, 0.72247450],
    [0.31219950, 0.43237971, 0.72357716],
    [0.31371495, 0.43672306, 0.72459788],
    [0.31534534, 0.44104571, 0.72555443],
    [0.31708149, 0.44534817, 0.72646071],
    [0.31891556, 0.44963099, 0.72732833],
    [0.32084052, 0.45389488, 0.72816665],
    [0.32284974, 0.45814084, 0.72898261],
    [0.32493773, 0.46236963, 0.72978273],
    [0.32709934, 0.46658213, 0.73057201],
    [0.32933014, 0.47077912, 0.73135513],
    [0.33162598, 0.47496141, 0.73213579],
    [0.33398301, 0.47912987, 0.73291694],
    [0.33639765, 0.48328538, 0.73370088],
    [0.33886718, 0.48742837, 0.73449122],
    [0.34138819, 0.49155995, 0.73528845],
    [0.34395827, 0.49568062, 0.73609521],
    [0.34657491, 0.49979108, 0.73691295],
    [0.34923568, 0.50389205, 0.73774268],
    [0.35193845, 0.50798418, 0.73858561],
    [0.35468119, 0.51206806, 0.73944274],
    [0.35746199, 0.51614432, 0.74031489],
    [0.36027917, 0.52021345, 0.74120326],
    [0.36313103, 0.52427602, 0.74210840],
    [0.36601584, 0.52833272, 0.74303030],
    [0.36893232, 0.53238388, 0.74397037],
    [0.37187890, 0.53643015, 0.74492840],
    [0.37485437, 0.54047191, 0.74590536],
    [0.37785730, 0.54450981, 0.74690075],
    [0.38088676, 0.54854402, 0.74791636],
    [0.38394139, 0.55257524, 0.74895125],
    [0.38702011, 0.55660388, 0.75000583],
    [0.39012193, 0.56063032, 0.75108045],
    [0.39324595, 0.56465488, 0.75217590],
    [0.39639113, 0.56867808, 0.75329175],
    [0.39955656, 0.57270030, 0.75442820],
    [0.40274138, 0.57672193, 0.75558540],
    [0.40594477, 0.58074333, 0.75676347],
    [0.40916593, 0.58476488, 0.75796251],
    [0.41240408, 0.58878695, 0.75918255],
    [0.41565853, 0.59280984, 0.76042396],
    [0.41892855, 0.59683390, 0.76168675],
    [0.42221342, 0.60085953, 0.76297067],
    [0.42551248, 0.60488706, 0.76427569],
    [0.42882506, 0.60891685, 0.76560175],
    [0.43215068, 0.61294904, 0.76694988],
    [0.43548861, 0.61698414, 0.76831898],
    [0.43883824, 0.62102247, 0.76970895],
    [0.44219917, 0.62506414, 0.77112108],
    [0.44557068, 0.62910968, 0.77255390],
    [0.44895233, 0.63315925, 0.77400819],
    [0.45234356, 0.63721322, 0.77548365],
    [0.45574388, 0.64127186, 0.77698022],
    [0.45915280, 0.64533545, 0.77849799],
    [0.46256983, 0.64940429, 0.78003681],
    [0.46599448, 0.65347869, 0.78159647],
    [0.46942635, 0.65755885, 0.78317740],
    [0.47286489, 0.66164520, 0.78477860],
    [0.47630979, 0.66573782, 0.78640124],
    [0.47976052, 0.66983714, 0.78804423],
    [0.48321662, 0.67394345, 0.78970740],
    [0.48667784, 0.67805683, 0.79139178],
    [0.49014363, 0.68217774, 0.79309619],
    [0.49361360, 0.68630642, 0.79482056],
    [0.49708740, 0.69044308, 0.79656519],
    [0.50056468, 0.69458797, 0.79833005],
    [0.50404498, 0.69874143, 0.80011454],
    [0.50752794, 0.70290370, 0.80191855],
    [0.51101320, 0.70707506, 0.80374196],
    [0.51450045, 0.71125569, 0.80558495],
    [0.51798932, 0.71544589, 0.80744725],
    [0.52147944, 0.71964593, 0.80932844],
    [0.52497047, 0.72385608, 0.81122836],
    [0.52846207, 0.72807659, 0.81314683],
    [0.53195393, 0.73230771, 0.81508366],
    [0.53544572, 0.73654969, 0.81703865],
    [0.53893713, 0.74080279, 0.81901157],
    [0.54242785, 0.74506725, 0.82100220],
    [0.54591759, 0.74934332, 0.82301031],
    [0.54940606, 0.75363125, 0.82503564],
    [0.55289296, 0.75793128, 0.82707794],
    [0.55637803, 0.76224368, 0.82913693],
    [0.55986099, 0.76656866, 0.83121233],
    [0.56334158, 0.77090649, 0.83330385],
    [0.56681954, 0.77525740, 0.83541118],
    [0.57029463, 0.77962164, 0.83753402],
    [0.57376660, 0.78399944, 0.83967204],
    [0.57723524, 0.78839104, 0.84182490],
    [0.58070031, 0.79279667, 0.84399226],
    [0.58416161, 0.79721657, 0.84617377],
    [0.58761893, 0.80165098, 0.84836907],
    [0.59107208, 0.80610012, 0.85057778],
    [0.59452102, 0.81056413, 0.85279998],
    [0.59796546, 0.81504331, 0.85503489],
    [0.60140523, 0.81953789, 0.85728208],
    [0.60484018, 0.82404809, 0.85954115],
    [0.60827017, 0.82857413, 0.86181167],
    [0.61169511, 0.83311619, 0.86409337],
    [0.61511505, 0.83767441, 0.86638624],
    [0.61852970, 0.84224910, 0.86868933],
    [0.62193896, 0.84684047, 0.87100218],
    [0.62534275, 0.85144871, 0.87332436],
    [0.62874125, 0.85607390, 0.87565605],
    [0.63213426, 0.86071633, 0.87799637],
    [0.63552164, 0.86537621, 0.88034468],
    [0.63890337, 0.87005376, 0.88270051],
    [0.64227985, 0.87474894, 0.88506435],
    [0.64565066, 0.87946214, 0.88743481],
    [0.64901583, 0.88419354, 0.88981141],
    [0.65237567, 0.88894318, 0.89219435],
    [0.65573011, 0.89371127, 0.89458291],
    [0.65907900, 0.89849809, 0.89697620],
    [0.66242273, 0.90330365, 0.89937441],
    [0.66576131, 0.90812813, 0.90177696],
    [0.66909457, 0.91297182, 0.90418285],
    [0.67242305, 0.91783468, 0.90659250],
    [0.67574664, 0.92271695, 0.90900496],
    [0.67906523, 0.92761889, 0.91141938],
]

# Create ListedColormap object for this colormap
assert len(cm_data) == 256
cmap = ListedColormap(cm_data, name="cmr.sapphire")
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
mpl.colormaps.register(cmap=cmap)
mpl.colormaps.register(cmap=cmap_r)
