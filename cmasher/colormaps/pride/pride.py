# %% IMPORTS
# Package imports
from matplotlib.cm import register_cmap
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
    [0.08752792, 0.05445008, 0.15633391],
    [0.09204695, 0.05639320, 0.16203897],
    [0.09650895, 0.05829607, 0.16786880],
    [0.10090870, 0.06016328, 0.17382488],
    [0.10524039, 0.06200004, 0.17990780],
    [0.10949779, 0.06381198, 0.18611729],
    [0.11367403, 0.06560565, 0.19245137],
    [0.11776199, 0.06738816, 0.19890668],
    [0.12175433, 0.06916725, 0.20547828],
    [0.12564365, 0.07095122, 0.21215945],
    [0.12942267, 0.07274885, 0.21894186],
    [0.13308433, 0.07456920, 0.22581549],
    [0.13662198, 0.07642163, 0.23276864],
    [0.14002950, 0.07831532, 0.23978863],
    [0.14330141, 0.08025937, 0.24686136],
    [0.14643291, 0.08226244, 0.25397225],
    [0.14941998, 0.08433262, 0.26110614],
    [0.15225934, 0.08647727, 0.26824775],
    [0.15494847, 0.08870295, 0.27538192],
    [0.15748551, 0.09101525, 0.28249390],
    [0.15986928, 0.09341878, 0.28956951],
    [0.16209917, 0.09591718, 0.29659525],
    [0.16417504, 0.09851308, 0.30355858],
    [0.16609723, 0.10120815, 0.31044773],
    [0.16786643, 0.10400316, 0.31725196],
    [0.16948361, 0.10689806, 0.32396152],
    [0.17095007, 0.10989202, 0.33056744],
    [0.17226726, 0.11298355, 0.33706178],
    [0.17343684, 0.11617055, 0.34343746],
    [0.17446061, 0.11945041, 0.34968818],
    [0.17534051, 0.12282010, 0.35580842],
    [0.17607859, 0.12627622, 0.36179338],
    [0.17667704, 0.12981506, 0.36763888],
    [0.17713811, 0.13343270, 0.37334141],
    [0.17746410, 0.13712505, 0.37889811],
    [0.17765753, 0.14088788, 0.38430647],
    [0.17772085, 0.14471691, 0.38956469],
    [0.17765681, 0.14860777, 0.39467122],
    [0.17746800, 0.15255614, 0.39962515],
    [0.17715730, 0.15655769, 0.40442584],
    [0.17672775, 0.16060812, 0.40907299],
    [0.17618229, 0.16470324, 0.41356679],
    [0.17552411, 0.16883893, 0.41790767],
    [0.17475650, 0.17301117, 0.42209636],
    [0.17388287, 0.17721606, 0.42613389],
    [0.17290686, 0.18144976, 0.43002153],
    [0.17183216, 0.18570864, 0.43376083],
    [0.17066251, 0.18998919, 0.43735357],
    [0.16940200, 0.19428801, 0.44080170],
    [0.16805489, 0.19860183, 0.44410739],
    [0.16662536, 0.20292760, 0.44727300],
    [0.16511815, 0.20726230, 0.45030103],
    [0.16353786, 0.21160317, 0.45319416],
    [0.16188934, 0.21594754, 0.45595518],
    [0.16017794, 0.22029285, 0.45858702],
    [0.15840893, 0.22463672, 0.46109273],
    [0.15658782, 0.22897695, 0.46347542],
    [0.15472045, 0.23331142, 0.46573832],
    [0.15281289, 0.23763816, 0.46788473],
    [0.15087146, 0.24195534, 0.46991799],
    [0.14890271, 0.24626125, 0.47184151],
    [0.14691347, 0.25055433, 0.47365872],
    [0.14491106, 0.25483305, 0.47537315],
    [0.14290279, 0.25909612, 0.47698827],
    [0.14089618, 0.26334235, 0.47850753],
    [0.13889947, 0.26757056, 0.47993450],
    [0.13692086, 0.27177976, 0.48127266],
    [0.13496883, 0.27596907, 0.48252547],
    [0.13305232, 0.28013764, 0.48369643],
    [0.13118042, 0.28428476, 0.48478897],
    [0.12936216, 0.28840987, 0.48580637],
    [0.12760751, 0.29251232, 0.48675218],
    [0.12592585, 0.29659172, 0.48762958],
    [0.12432688, 0.30064769, 0.48844181],
    [0.12282043, 0.30467992, 0.48919206],
    [0.12141630, 0.30868816, 0.48988346],
    [0.12012416, 0.31267225, 0.49051910],
    [0.11895347, 0.31663207, 0.49110196],
    [0.11791336, 0.32056757, 0.49163494],
    [0.11701255, 0.32447876, 0.49212087],
    [0.11625924, 0.32836571, 0.49256249],
    [0.11566099, 0.33222853, 0.49296243],
    [0.11522492, 0.33606732, 0.49332344],
    [0.11495702, 0.33988228, 0.49364800],
    [0.11486213, 0.34367370, 0.49393834],
    [0.11494478, 0.34744177, 0.49419705],
    [0.11520786, 0.35118683, 0.49442624],
    [0.11565340, 0.35490919, 0.49462809],
    [0.11628239, 0.35860921, 0.49480473],
    [0.11709469, 0.36228726, 0.49495819],
    [0.11808882, 0.36594380, 0.49509011],
    [0.11926311, 0.36957912, 0.49520286],
    [0.12061397, 0.37319378, 0.49529773],
    [0.12213744, 0.37678822, 0.49537642],
    [0.12382885, 0.38036291, 0.49544055],
    [0.12568303, 0.38391827, 0.49549190],
    [0.12769383, 0.38745486, 0.49553160],
    [0.12985495, 0.39097318, 0.49556102],
    [0.13215972, 0.39447374, 0.49558142],
    [0.13460127, 0.39795707, 0.49559400],
    [0.13717257, 0.40142368, 0.49559986],
    [0.13986655, 0.40487412, 0.49560002],
    [0.14267615, 0.40830893, 0.49559543],
    [0.14559445, 0.41172862, 0.49558704],
    [0.14861463, 0.41513371, 0.49557582],
    [0.15172999, 0.41852479, 0.49556227],
    [0.15493410, 0.42190240, 0.49554701],
    [0.15822077, 0.42526707, 0.49553070],
    [0.16158414, 0.42861927, 0.49551431],
    [0.16501848, 0.43195963, 0.49549772],
    [0.16851844, 0.43528863, 0.49548162],
    [0.17207896, 0.43860678, 0.49546650],
    [0.17569522, 0.44191466, 0.49545222],
    [0.17936270, 0.44521270, 0.49543967],
    [0.18307720, 0.44850150, 0.49542829],
    [0.18683470, 0.45178148, 0.49541885],
    [0.19063154, 0.45505319, 0.49541097],
    [0.19446429, 0.45831712, 0.49540465],
    [0.19832966, 0.46157369, 0.49540031],
    [0.20222478, 0.46482343, 0.49539724],
    [0.20614689, 0.46806681, 0.49539538],
    [0.21009336, 0.47130421, 0.49539508],
    [0.21406195, 0.47453613, 0.49539550],
    [0.21805055, 0.47776300, 0.49539633],
    [0.22205719, 0.48098524, 0.49539725],
    [0.22608011, 0.48420325, 0.49539786],
    [0.23011762, 0.48741741, 0.49539800],
    [0.23416837, 0.49062812, 0.49539682],
    [0.23823107, 0.49383575, 0.49539374],
    [0.24230459, 0.49704067, 0.49538818],
    [0.24638792, 0.50024322, 0.49537945],
    [0.25048021, 0.50344372, 0.49536687],
    [0.25458073, 0.50664248, 0.49534967],
    [0.25868887, 0.50983982, 0.49532705],
    [0.26280416, 0.51303600, 0.49529816],
    [0.26692622, 0.51623130, 0.49526213],
    [0.27105469, 0.51942595, 0.49521840],
    [0.27518951, 0.52262020, 0.49516568],
    [0.27933064, 0.52581426, 0.49510297],
    [0.28347814, 0.52900834, 0.49502922],
    [0.28763217, 0.53220259, 0.49494334],
    [0.29179280, 0.53539718, 0.49484473],
    [0.29596043, 0.53859225, 0.49473212],
    [0.30013555, 0.54178792, 0.49460405],
    [0.30431866, 0.54498430, 0.49445941],
    [0.30851002, 0.54818143, 0.49429795],
    [0.31271059, 0.55137942, 0.49411748],
    [0.31692102, 0.55457829, 0.49391701],
    [0.32114182, 0.55777805, 0.49369614],
    [0.32537418, 0.56097873, 0.49345256],
    [0.32961865, 0.56418028, 0.49318613],
    [0.33387640, 0.56738267, 0.49289495],
    [0.33814830, 0.57058585, 0.49257816],
    [0.34243538, 0.57378975, 0.49223461],
    [0.34673877, 0.57699426, 0.49186297],
    [0.35105947, 0.58019927, 0.49146232],
    [0.35539867, 0.58340466, 0.49103141],
    [0.35975757, 0.58661028, 0.49056899],
    [0.36413716, 0.58981597, 0.49007450],
    [0.36853902, 0.59302156, 0.48954576],
    [0.37296371, 0.59622684, 0.48898352],
    [0.37741303, 0.59943162, 0.48838510],
    [0.38188799, 0.60263568, 0.48775010],
    [0.38638958, 0.60583879, 0.48707812],
    [0.39091937, 0.60904071, 0.48636723],
    [0.39547834, 0.61224120, 0.48561706],
    [0.40006746, 0.61544001, 0.48482731],
    [0.40468823, 0.61863685, 0.48399620],
    [0.40934175, 0.62183146, 0.48312299],
    [0.41402871, 0.62502358, 0.48220800],
    [0.41875042, 0.62821291, 0.48124980],
    [0.42350802, 0.63139917, 0.48024749],
    [0.42830248, 0.63458208, 0.47920045],
    [0.43313462, 0.63776134, 0.47810840],
    [0.43800511, 0.64093668, 0.47697128],
    [0.44291513, 0.64410781, 0.47578781],
    [0.44786547, 0.64727443, 0.47455752],
    [0.45285688, 0.65043626, 0.47327996],
    [0.45789008, 0.65359301, 0.47195472],
    [0.46296570, 0.65674441, 0.47058142],
    [0.46808433, 0.65989019, 0.46915974],
    [0.47324633, 0.66303010, 0.46768979],
    [0.47845245, 0.66616385, 0.46617069],
    [0.48370315, 0.66929119, 0.46460213],
    [0.48899883, 0.67241186, 0.46298382],
    [0.49433987, 0.67552562, 0.46131548],
    [0.49972657, 0.67863224, 0.45959684],
    [0.50515923, 0.68173147, 0.45782765],
    [0.51063806, 0.68482310, 0.45600765],
    [0.51616327, 0.68790691, 0.45413659],
    [0.52173499, 0.69098269, 0.45221420],
    [0.52735335, 0.69405024, 0.45024025],
    [0.53301842, 0.69710936, 0.44821445],
    [0.53873026, 0.70015988, 0.44613656],
    [0.54448886, 0.70320160, 0.44400627],
    [0.55029423, 0.70623437, 0.44182330],
    [0.55614598, 0.70925806, 0.43958801],
    [0.56204429, 0.71227248, 0.43729959],
    [0.56798909, 0.71527748, 0.43495760],
    [0.57398027, 0.71827292, 0.43256168],
    [0.58001770, 0.72125865, 0.43011141],
    [0.58610124, 0.72423455, 0.42760637],
    [0.59223071, 0.72720048, 0.42504609],
    [0.59840589, 0.73015634, 0.42243016],
    [0.60462588, 0.73310215, 0.41975946],
    [0.61089116, 0.73603767, 0.41703201],
    [0.61720154, 0.73896279, 0.41424719],
    [0.62355679, 0.74187742, 0.41140432],
    [0.62995669, 0.74478146, 0.40850267],
    [0.63640004, 0.74767501, 0.40554339],
    [0.64288738, 0.75055785, 0.40252410],
    [0.64941862, 0.75342984, 0.39944362],
    [0.65599353, 0.75629090, 0.39630098],
    [0.66261097, 0.75914117, 0.39309691],
    [0.66927108, 0.76198049, 0.38982957],
    [0.67597411, 0.76480867, 0.38649681],
    [0.68271984, 0.76762564, 0.38309731],
    [0.68950640, 0.77043173, 0.37963294],
    [0.69633514, 0.77322649, 0.37609915],
    [0.70320587, 0.77600985, 0.37249427],
    [0.71011710, 0.77878207, 0.36881911],
    [0.71706926, 0.78154293, 0.36507064],
    [0.72406277, 0.78429221, 0.36124564],
    [0.73109609, 0.78703020, 0.35734467],
    [0.73816957, 0.78975670, 0.35336444],
    [0.74528382, 0.79247145, 0.34930088],
    [0.75243681, 0.79517489, 0.34515515],
    [0.75962972, 0.79786659, 0.34092168],
    [0.76686259, 0.80054644, 0.33659700],
    [0.77413333, 0.80321494, 0.33218183],
    [0.78144402, 0.80587139, 0.32766798],
    [0.78879297, 0.80851618, 0.32305486],
    [0.79618046, 0.81114915, 0.31833738],
    [0.80360708, 0.81377001, 0.31350943],
    [0.81107072, 0.81637931, 0.30857037],
    [0.81857375, 0.81897625, 0.30350935],
    [0.82611350, 0.82156155, 0.29832601],
    [0.83369193, 0.82413452, 0.29300924],
    [0.84130759, 0.82669553, 0.28755484],
    [0.84896098, 0.82924432, 0.28195349],
    [0.85665198, 0.83178087, 0.27619635],
    [0.86437995, 0.83430528, 0.27027480],
    [0.87214576, 0.83681719, 0.26417549],
    [0.87994802, 0.83931699, 0.25788906],
    [0.88778819, 0.84180409, 0.25139755],
    [0.89566452, 0.84427902, 0.24468901],
    [0.90357867, 0.84674113, 0.23774045],
    [0.91152892, 0.84919093, 0.23053474],
    [0.91951673, 0.85162784, 0.22304277],
    [0.92754082, 0.85405223, 0.21523836],
    [0.93560204, 0.85646372, 0.20708390],
    [0.94369997, 0.85886238, 0.19853799],
    [0.95183441, 0.86124822, 0.18954940],
    [0.96000625, 0.86362083, 0.18005051],
    [0.96821377, 0.86598077, 0.16996509],
    [0.97645964, 0.86832697, 0.15917699],
    [0.97677870, 0.86238645, 0.15511138],
    [0.97705968, 0.85645921, 0.15107024],
    [0.97730297, 0.85054514, 0.14705473],
    [0.97750893, 0.84464413, 0.14306613],
    [0.97767793, 0.83875607, 0.13910578],
    [0.97781030, 0.83288087, 0.13517518],
    [0.97790635, 0.82701843, 0.13127592],
    [0.97796637, 0.82116867, 0.12740975],
    [0.97799065, 0.81533150, 0.12357856],
    [0.97797944, 0.80950686, 0.11978440],
    [0.97793300, 0.80369466, 0.11602949],
    [0.97785155, 0.79789486, 0.11231628],
    [0.97773531, 0.79210738, 0.10864740],
    [0.97758449, 0.78633217, 0.10502572],
    [0.97739927, 0.78056919, 0.10145437],
    [0.97717983, 0.77481839, 0.09793676],
    [0.97692633, 0.76907975, 0.09447657],
    [0.97663892, 0.76335321, 0.09107784],
    [0.97631776, 0.75763876, 0.08774490],
    [0.97596297, 0.75193638, 0.08448249],
    [0.97557467, 0.74624605, 0.08129571],
    [0.97515298, 0.74056775, 0.07819007],
    [0.97469800, 0.73490149, 0.07517148],
    [0.97421021, 0.72924703, 0.07224664],
    [0.97368951, 0.72360447, 0.06942221],
    [0.97313583, 0.71797393, 0.06670519],
    [0.97254922, 0.71235541, 0.06410312],
    [0.97192977, 0.70674892, 0.06162387],
    [0.97127752, 0.70115449, 0.05927557],
    [0.97059296, 0.69557187, 0.05706716],
    [0.96987609, 0.69000113, 0.05500703],
    [0.96912659, 0.68444251, 0.05310302],
    [0.96834452, 0.67889604, 0.05136321],
    [0.96753005, 0.67336167, 0.04979551],
    [0.96668384, 0.66783904, 0.04840818],
    [0.96580516, 0.66232866, 0.04720612],
    [0.96489405, 0.65683060, 0.04619447],
    [0.96395109, 0.65134452, 0.04537835],
    [0.96297618, 0.64587055, 0.04476016],
    [0.96196892, 0.64040903, 0.04433994],
    [0.96092979, 0.63495970, 0.04411823],
    [0.95985892, 0.62952254, 0.04409312],
    [0.95875575, 0.62409801, 0.04425943],
    [0.95762104, 0.61868564, 0.04461378],
    [0.95645441, 0.61328578, 0.04514863],
    [0.95525570, 0.60789861, 0.04585576],
    [0.95402572, 0.60252363, 0.04672868],
    [0.95276350, 0.59716162, 0.04775541],
    [0.95147004, 0.59181192, 0.04892886],
    [0.95014456, 0.58647519, 0.05023678],
    [0.94878769, 0.58115104, 0.05167074],
    [0.94739902, 0.57583985, 0.05321958],
    [0.94597896, 0.57054142, 0.05487459],
    [0.94452718, 0.56525606, 0.05662539],
    [0.94304413, 0.55998352, 0.05846422],
    [0.94152930, 0.55472430, 0.06038105],
    [0.93998345, 0.54947786, 0.06237007],
    [0.93840582, 0.54424492, 0.06442156],
    [0.93679717, 0.53902496, 0.06653078],
    [0.93515705, 0.53381842, 0.06869001],
    [0.93348553, 0.52862536, 0.07089355],
    [0.93178309, 0.52344548, 0.07313736],
    [0.93004922, 0.51827929, 0.07541504],
    [0.92828420, 0.51312666, 0.07772287],
    [0.92648828, 0.50798748, 0.08005753],
    [0.92466114, 0.50286212, 0.08241431],
    [0.92280285, 0.49775063, 0.08479007],
    [0.92091391, 0.49265267, 0.08718318],
    [0.91899396, 0.48756867, 0.08958983],
    [0.91704306, 0.48249869, 0.09200767],
    [0.91506128, 0.47744277, 0.09443465],
    [0.91304890, 0.47240075, 0.09686954],
    [0.91100584, 0.46737282, 0.09931027],
    [0.90893209, 0.46235912, 0.10175508],
    [0.90682772, 0.45735968, 0.10420269],
    [0.90469280, 0.45237454, 0.10665194],
    [0.90252741, 0.44740376, 0.10910180],
    [0.90033161, 0.44244738, 0.11155136],
    [0.89810556, 0.43750535, 0.11400006],
    [0.89584925, 0.43257782, 0.11644693],
    [0.89356273, 0.42766483, 0.11889128],
    [0.89124607, 0.42276645, 0.12133257],
    [0.88889935, 0.41788270, 0.12377033],
    [0.88652265, 0.41301363, 0.12620414],
    [0.88411603, 0.40815928, 0.12863364],
    [0.88167959, 0.40331967, 0.13105853],
    [0.87921338, 0.39849486, 0.13347855],
    [0.87671751, 0.39368487, 0.13589347],
    [0.87419208, 0.38888967, 0.13830329],
    [0.87163719, 0.38410930, 0.14070781],
    [0.86905287, 0.37934382, 0.14310682],
    [0.86643921, 0.37459325, 0.14550020],
    [0.86379630, 0.36985763, 0.14788787],
    [0.86112421, 0.36513695, 0.15026978],
    [0.85842305, 0.36043124, 0.15264587],
    [0.85569303, 0.35574032, 0.15501666],
    [0.85293413, 0.35106435, 0.15738168],
    [0.85014642, 0.34640335, 0.15974085],
    [0.84733000, 0.34175732, 0.16209419],
    [0.84448512, 0.33712603, 0.16444234],
    [0.84161173, 0.33250963, 0.16678479],
    [0.83870993, 0.32790816, 0.16912146],
    [0.83577992, 0.32332138, 0.17145295],
    [0.83282175, 0.31874937, 0.17377900],
    [0.82983545, 0.31419218, 0.17609933],
    [0.82682132, 0.30964946, 0.17841492],
    [0.82377927, 0.30512146, 0.18072487],
    [0.82070951, 0.30060793, 0.18302979],
    [0.81761212, 0.29610887, 0.18532952],
    [0.81448721, 0.29162419, 0.18762411],
    [0.81133489, 0.28715376, 0.18991373],
    [0.80815526, 0.28269753, 0.19219826],
    [0.80494843, 0.27825537, 0.19447783],
    [0.80171453, 0.27382715, 0.19675251],
    [0.79845361, 0.26941284, 0.19902204],
    [0.79516586, 0.26501213, 0.20128700],
    [0.79185130, 0.26062508, 0.20354673],
    [0.78851009, 0.25625139, 0.20580169],
    [0.78514233, 0.25189095, 0.20805178],
    [0.78174807, 0.24754365, 0.21029670],
    [0.77832746, 0.24320922, 0.21253675],
    [0.77488060, 0.23888748, 0.21477189],
    [0.77140755, 0.23457829, 0.21700180],
    [0.76790841, 0.23028144, 0.21922646],
    [0.76438329, 0.22599663, 0.22144601],
    [0.76083227, 0.22172363, 0.22366036],
    [0.75725543, 0.21746226, 0.22586922],
    [0.75365284, 0.21321223, 0.22807250],
    [0.75002458, 0.20897328, 0.23027008],
    [0.74637073, 0.20474512, 0.23246184],
    [0.74269134, 0.20052745, 0.23464762],
    [0.73898649, 0.19631995, 0.23682727],
    [0.73525623, 0.19212231, 0.23900059],
    [0.73150060, 0.18793417, 0.24116738],
    [0.72771966, 0.18375520, 0.24332741],
    [0.72391343, 0.17958503, 0.24548042],
    [0.72008196, 0.17542328, 0.24762616],
    [0.71622525, 0.17126956, 0.24976431],
    [0.71234333, 0.16712346, 0.25189456],
    [0.70843620, 0.16298456, 0.25401657],
    [0.70450387, 0.15885242, 0.25612995],
    [0.70054631, 0.15472658, 0.25823434],
    [0.69656352, 0.15060653, 0.26032965],
    [0.69255545, 0.14649183, 0.26241508],
    [0.68852207, 0.14238199, 0.26449015],
    [0.68446333, 0.13827647, 0.26655453],
    [0.68037914, 0.13417471, 0.26860782],
    [0.67626946, 0.13007624, 0.27064908],
    [0.67213418, 0.12598043, 0.27267811],
    [0.66797319, 0.12188673, 0.27469408],
    [0.66378640, 0.11779458, 0.27669629],
    [0.65957364, 0.11370335, 0.27868422],
    [0.65533480, 0.10961246, 0.28065688],
    [0.65106969, 0.10552128, 0.28261364],
    [0.64677815, 0.10142921, 0.28455363],
    [0.64245999, 0.09733565, 0.28647567],
    [0.63811495, 0.09323995, 0.28837938],
    [0.63374286, 0.08914155, 0.29026323],
    [0.62934346, 0.08503984, 0.29212617],
    [0.62491645, 0.08093428, 0.29396724],
    [0.62046156, 0.07682433, 0.29578524],
    [0.61597849, 0.07270954, 0.29757868],
    [0.61146692, 0.06858949, 0.29934622],
    [0.60692650, 0.06446386, 0.30108639],
    [0.60235686, 0.06033246, 0.30279764],
    [0.59775761, 0.05619524, 0.30447830],
    [0.59312836, 0.05205234, 0.30612660],
    [0.58846868, 0.04790419, 0.30774064],
    [0.58377813, 0.04375150, 0.30931842],
    [0.57905626, 0.03958633, 0.31085779],
    [0.57430258, 0.03553832, 0.31235659],
    [0.56951656, 0.03174353, 0.31381251],
    [0.56469777, 0.02819987, 0.31522280],
    [0.55984570, 0.02490543, 0.31658479],
    [0.55495972, 0.02185857, 0.31789598],
    [0.55003944, 0.01905721, 0.31915292],
    [0.54508421, 0.01649988, 0.32035290],
    [0.54009364, 0.01418450, 0.32149216],
    [0.53506707, 0.01210967, 0.32256769],
    [0.53000414, 0.01027322, 0.32357540],
    [0.52490435, 0.00867329, 0.32451159],
    [0.51976718, 0.00730801, 0.32537242],
    [0.51459232, 0.00617496, 0.32615352],
    [0.50937942, 0.00527169, 0.32685057],
    [0.50412820, 0.00459550, 0.32745912],
    [0.49883845, 0.00414334, 0.32797456],
    [0.49351007, 0.00391176, 0.32839217],
    [0.48814305, 0.00389685, 0.32870713],
    [0.48273750, 0.00409419, 0.32891454],
    [0.47729369, 0.00449875, 0.32900950],
    [0.47181202, 0.00510487, 0.32898709],
    [0.46629306, 0.00590618, 0.32884247],
    [0.46073754, 0.00689559, 0.32857092],
    [0.45514636, 0.00806527, 0.32816791],
    [0.44952072, 0.00940630, 0.32762900],
    [0.44386196, 0.01090904, 0.32695012],
    [0.43817160, 0.01256314, 0.32612757],
    [0.43245143, 0.01435711, 0.32515798],
    [0.42670346, 0.01627877, 0.32403846],
    [0.42092984, 0.01831523, 0.32276667],
    [0.41513297, 0.02045279, 0.32134077],
    [0.40931540, 0.02267720, 0.31975957],
    [0.40347984, 0.02497369, 0.31802247],
    [0.39762912, 0.02732722, 0.31612956],
    [0.39176619, 0.02972241, 0.31408155],
    [0.38589406, 0.03214387, 0.31187980],
    [0.38001576, 0.03457641, 0.30952634],
    [0.37413435, 0.03700496, 0.30702377],
    [0.36825293, 0.03941467, 0.30437522],
    [0.36237443, 0.04175651, 0.30158440],
    [0.35650177, 0.04396933, 0.29865545],
    [0.35063775, 0.04606145, 0.29559288],
    [0.34478506, 0.04803206, 0.29240158],
    [0.33894627, 0.04988081, 0.28908670],
    [0.33312376, 0.05160777, 0.28565358],
    [0.32731976, 0.05321341, 0.28210775],
    [0.32153630, 0.05469857, 0.27845479],
    [0.31577523, 0.05606435, 0.27470034],
    [0.31003845, 0.05731174, 0.27085009],
    [0.30432731, 0.05844262, 0.26690960],
    [0.29864314, 0.05945880, 0.26288435],
    [0.29298736, 0.06036170, 0.25877985],
    [0.28736075, 0.06115387, 0.25460122],
    [0.28176439, 0.06183698, 0.25035367],
    [0.27619895, 0.06241336, 0.24604208],
    [0.27066497, 0.06288536, 0.24167115],
    [0.26516295, 0.06325514, 0.23724543],
    [0.25969341, 0.06352471, 0.23276936],
    [0.25425646, 0.06369656, 0.22824696],
    [0.24885223, 0.06377292, 0.22368215],
    [0.24348079, 0.06375601, 0.21907864],
    [0.23814208, 0.06364801, 0.21443993],
    [0.23283608, 0.06345087, 0.20976941],
    [0.22756254, 0.06316678, 0.20507013],
    [0.22232111, 0.06279787, 0.20034494],
    [0.21711142, 0.06234614, 0.19559652],
    [0.21193335, 0.06181308, 0.19082768],
    [0.20678617, 0.06120095, 0.18604051],
    [0.20166950, 0.06051127, 0.18123735],
    [0.19658276, 0.05974580, 0.17642018],
    [0.19152541, 0.05890604, 0.17159096],
    [0.18649662, 0.05799375, 0.16675122],
    [0.18149606, 0.05700991, 0.16190292],
    [0.17652272, 0.05595626, 0.15704718],
    [0.17157588, 0.05483404, 0.15218535],
    [0.16665478, 0.05364437, 0.14731867],
    [0.16175869, 0.05238821, 0.14244829],
    [0.15688661, 0.05106677, 0.13757500],
    [0.15203766, 0.04968094, 0.13269961],
    [0.14721089, 0.04823157, 0.12782280],
    [0.14240530, 0.04671941, 0.12294513],
    [0.13761989, 0.04514511, 0.11806704],
    [0.13285355, 0.04350924, 0.11318884],
    [0.12810517, 0.04181228, 0.10831071],
    [0.12337357, 0.04004903, 0.10343270],
]

# Create ListedColormap object for this colormap
cmap = ListedColormap(cm_data, name="cmr.pride", N=511)
cmap_r = cmap.reversed()

# Register (reversed) cmap in MPL
register_cmap(cmap=cmap)
register_cmap(cmap=cmap_r)
