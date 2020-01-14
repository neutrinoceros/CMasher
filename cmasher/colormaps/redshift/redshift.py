from matplotlib.colors import ListedColormap

cm_type = "diverging"

cm_data = [[5.78692840e-01, 9.47004534e-01, 9.53835089e-01],
           [5.73300958e-01, 9.42448134e-01, 9.52185844e-01],
           [5.67904138e-01, 9.37906186e-01, 9.50550251e-01],
           [5.62501828e-01, 9.33378441e-01, 9.48929504e-01],
           [5.57094001e-01, 9.28864700e-01, 9.47323254e-01],
           [5.51680262e-01, 9.24364725e-01, 9.45732234e-01],
           [5.46260408e-01, 9.19878293e-01, 9.44156633e-01],
           [5.40834283e-01, 9.15405185e-01, 9.42596495e-01],
           [5.35401418e-01, 9.10945148e-01, 9.41052774e-01],
           [5.29961833e-01, 9.06497972e-01, 9.39525036e-01],
           [5.24515168e-01, 9.02063412e-01, 9.38013919e-01],
           [5.19061153e-01, 8.97641224e-01, 9.36519804e-01],
           [5.13599714e-01, 8.93231185e-01, 9.35042546e-01],
           [5.08130514e-01, 8.88833041e-01, 9.33582712e-01],
           [5.02653292e-01, 8.84446544e-01, 9.32140656e-01],
           [4.97167970e-01, 8.80071461e-01, 9.30716251e-01],
           [4.91674325e-01, 8.75707544e-01, 9.29309753e-01],
           [4.86171948e-01, 8.71354522e-01, 9.27921902e-01],
           [4.80660799e-01, 8.67012158e-01, 9.26552467e-01],
           [4.75140686e-01, 8.62680199e-01, 9.25201622e-01],
           [4.69611394e-01, 8.58358385e-01, 9.23869585e-01],
           [4.64072657e-01, 8.54046451e-01, 9.22556718e-01],
           [4.58524236e-01, 8.49744130e-01, 9.21263293e-01],
           [4.52966030e-01, 8.45451166e-01, 9.19989242e-01],
           [4.47397837e-01, 8.41167290e-01, 9.18734745e-01],
           [4.41819459e-01, 8.36892232e-01, 9.17499973e-01],
           [4.36230702e-01, 8.32625718e-01, 9.16285085e-01],
           [4.30631373e-01, 8.28367471e-01, 9.15090231e-01],
           [4.25021288e-01, 8.24117213e-01, 9.13915551e-01],
           [4.19400262e-01, 8.19874661e-01, 9.12761172e-01],
           [4.13768119e-01, 8.15639529e-01, 9.11627211e-01],
           [4.08124687e-01, 8.11411529e-01, 9.10513772e-01],
           [4.02469802e-01, 8.07190370e-01, 9.09420950e-01],
           [3.96803304e-01, 8.02975757e-01, 9.08348825e-01],
           [3.91125045e-01, 7.98767391e-01, 9.07297464e-01],
           [3.85434884e-01, 7.94564972e-01, 9.06266924e-01],
           [3.79732689e-01, 7.90368192e-01, 9.05257244e-01],
           [3.74018344e-01, 7.86176744e-01, 9.04268451e-01],
           [3.68291742e-01, 7.81990315e-01, 9.03300558e-01],
           [3.62552792e-01, 7.77808588e-01, 9.02353560e-01],
           [3.56801422e-01, 7.73631242e-01, 9.01427436e-01],
           [3.51037448e-01, 7.69457933e-01, 9.00522481e-01],
           [3.45260887e-01, 7.65288338e-01, 8.99638516e-01],
           [3.39471788e-01, 7.61122132e-01, 8.98775317e-01],
           [3.33670169e-01, 7.56958978e-01, 8.97932792e-01],
           [3.27855879e-01, 7.52798495e-01, 8.97111369e-01],
           [3.22029122e-01, 7.48640355e-01, 8.96310603e-01],
           [3.16190082e-01, 7.44484220e-01, 8.95530166e-01],
           [3.10338662e-01, 7.40329674e-01, 8.94770632e-01],
           [3.04475280e-01, 7.36176394e-01, 8.94031249e-01],
           [2.98600109e-01, 7.32023987e-01, 8.93312085e-01],
           [2.92713429e-01, 7.27872062e-01, 8.92613085e-01],
           [2.86815720e-01, 7.23720253e-01, 8.91933779e-01],
           [2.80907351e-01, 7.19568136e-01, 8.91274268e-01],
           [2.74988962e-01, 7.15415329e-01, 8.90634084e-01],
           [2.69061237e-01, 7.11261425e-01, 8.90012916e-01],
           [2.63124858e-01, 7.07105970e-01, 8.89410864e-01],
           [2.57180924e-01, 7.02948593e-01, 8.88827028e-01],
           [2.51230430e-01, 6.98788826e-01, 8.88261402e-01],
           [2.45274625e-01, 6.94626213e-01, 8.87713728e-01],
           [2.39315083e-01, 6.90460341e-01, 8.87183219e-01],
           [2.33353507e-01, 6.86290746e-01, 8.86669459e-01],
           [2.27391881e-01, 6.82116958e-01, 8.86171983e-01],
           [2.21432481e-01, 6.77938476e-01, 8.85690423e-01],
           [2.15477996e-01, 6.73754829e-01, 8.85224061e-01],
           [2.09531518e-01, 6.69565533e-01, 8.84772141e-01],
           [2.03596591e-01, 6.65370084e-01, 8.84333945e-01],
           [1.97677299e-01, 6.61167973e-01, 8.83908683e-01],
           [1.91778351e-01, 6.56958680e-01, 8.83495480e-01],
           [1.85905169e-01, 6.52741636e-01, 8.83093687e-01],
           [1.80064006e-01, 6.48516336e-01, 8.82702059e-01],
           [1.74262029e-01, 6.44282242e-01, 8.82319418e-01],
           [1.68507468e-01, 6.40038815e-01, 8.81944496e-01],
           [1.62809859e-01, 6.35785434e-01, 8.81576365e-01],
           [1.57180072e-01, 6.31521552e-01, 8.81213460e-01],
           [1.51630475e-01, 6.27246648e-01, 8.80853939e-01],
           [1.46175578e-01, 6.22960017e-01, 8.80496851e-01],
           [1.40831375e-01, 6.18661207e-01, 8.80139636e-01],
           [1.35616639e-01, 6.14349529e-01, 8.79780903e-01],
           [1.30552271e-01, 6.10024426e-01, 8.79418327e-01],
           [1.25661794e-01, 6.05685341e-01, 8.79049446e-01],
           [1.20971707e-01, 6.01331668e-01, 8.78671861e-01],
           [1.16511563e-01, 5.96962778e-01, 8.78283072e-01],
           [1.12313402e-01, 5.92578135e-01, 8.77879944e-01],
           [1.08411955e-01, 5.88177194e-01, 8.77459198e-01],
           [1.04844299e-01, 5.83759401e-01, 8.77017401e-01],
           [1.01649143e-01, 5.79324204e-01, 8.76550875e-01],
           [9.88650977e-02, 5.74871174e-01, 8.76055248e-01],
           [9.65299433e-02, 5.70399900e-01, 8.75525883e-01],
           [9.46800608e-02, 5.65909873e-01, 8.74958273e-01],
           [9.33458797e-02, 5.61400868e-01, 8.74346664e-01],
           [9.25534686e-02, 5.56872508e-01, 8.73685607e-01],
           [9.23193790e-02, 5.52324723e-01, 8.72968423e-01],
           [9.26524359e-02, 5.47757391e-01, 8.72188384e-01],
           [9.35518714e-02, 5.43170516e-01, 8.71338162e-01],
           [9.50066950e-02, 5.38564305e-01, 8.70409626e-01],
           [9.69974085e-02, 5.33939078e-01, 8.69394153e-01],
           [9.94960176e-02, 5.29295411e-01, 8.68282281e-01],
           [1.02468098e-01, 5.24634109e-01, 8.67063874e-01],
           [1.05875414e-01, 5.19956133e-01, 8.65728330e-01],
           [1.09675761e-01, 5.15262814e-01, 8.64264188e-01],
           [1.13825799e-01, 5.10555737e-01, 8.62659495e-01],
           [1.18280497e-01, 5.05836943e-01, 8.60901548e-01],
           [1.22995807e-01, 5.01108771e-01, 8.58977360e-01],
           [1.27928180e-01, 4.96373991e-01, 8.56873612e-01],
           [1.33034952e-01, 4.91635812e-01, 8.54576873e-01],
           [1.38274606e-01, 4.86897881e-01, 8.52073885e-01],
           [1.43607170e-01, 4.82164234e-01, 8.49351901e-01],
           [1.48994245e-01, 4.77439269e-01, 8.46399020e-01],
           [1.54397994e-01, 4.72727808e-01, 8.43204529e-01],
           [1.59783445e-01, 4.68034774e-01, 8.39759425e-01],
           [1.65116349e-01, 4.63365350e-01, 8.36056706e-01],
           [1.70365215e-01, 4.58724648e-01, 8.32091774e-01],
           [1.75500824e-01, 4.54117670e-01, 8.27862671e-01],
           [1.80496667e-01, 4.49549147e-01, 8.23370253e-01],
           [1.85329435e-01, 4.45023391e-01, 8.18618195e-01],
           [1.89978991e-01, 4.40544209e-01, 8.13612915e-01],
           [1.94429078e-01, 4.36114753e-01, 8.08363251e-01],
           [1.98666394e-01, 4.31737576e-01, 8.02880303e-01],
           [2.02681886e-01, 4.27414456e-01, 7.97176723e-01],
           [2.06468728e-01, 4.23146613e-01, 7.91266744e-01],
           [2.10024161e-01, 4.18934517e-01, 7.85165130e-01],
           [2.13347437e-01, 4.14778131e-01, 7.78887270e-01],
           [2.16440070e-01, 4.10676919e-01, 7.72448643e-01],
           [2.19305491e-01, 4.06629916e-01, 7.65864489e-01],
           [2.21948709e-01, 4.02635810e-01, 7.59149540e-01],
           [2.24375980e-01, 3.98693013e-01, 7.52317815e-01],
           [2.26593924e-01, 3.94799781e-01, 7.45382836e-01],
           [2.28610197e-01, 3.90954195e-01, 7.38357023e-01],
           [2.30432432e-01, 3.87154276e-01, 7.31252161e-01],
           [2.32068926e-01, 3.83397966e-01, 7.24078812e-01],
           [2.33527523e-01, 3.79683233e-01, 7.16847009e-01],
           [2.34816084e-01, 3.76008051e-01, 7.09565901e-01],
           [2.35942398e-01, 3.72370426e-01, 7.02243776e-01],
           [2.36914105e-01, 3.68768412e-01, 6.94888104e-01],
           [2.37738643e-01, 3.65200126e-01, 6.87505580e-01],
           [2.38422282e-01, 3.61663789e-01, 6.80103136e-01],
           [2.38972594e-01, 3.58157636e-01, 6.72685501e-01],
           [2.39395009e-01, 3.54680041e-01, 6.65258749e-01],
           [2.39696225e-01, 3.51229407e-01, 6.57826776e-01],
           [2.39881773e-01, 3.47804242e-01, 6.50393943e-01],
           [2.39956943e-01, 3.44403123e-01, 6.42964150e-01],
           [2.39926779e-01, 3.41024699e-01, 6.35540879e-01],
           [2.39796090e-01, 3.37667689e-01, 6.28127227e-01],
           [2.39569444e-01, 3.34330882e-01, 6.20725937e-01],
           [2.39251183e-01, 3.31013128e-01, 6.13339431e-01],
           [2.38845424e-01, 3.27713344e-01, 6.05969844e-01],
           [2.38355808e-01, 3.24430499e-01, 5.98619437e-01],
           [2.37785799e-01, 3.21163615e-01, 5.91290231e-01],
           [2.37139189e-01, 3.17911780e-01, 5.83983238e-01],
           [2.36418594e-01, 3.14674104e-01, 5.76700831e-01],
           [2.35627508e-01, 3.11449771e-01, 5.69443559e-01],
           [2.34768626e-01, 3.08237993e-01, 5.62212823e-01],
           [2.33844361e-01, 3.05038009e-01, 5.55010144e-01],
           [2.32857559e-01, 3.01849126e-01, 5.47835919e-01],
           [2.31810546e-01, 2.98670665e-01, 5.40691084e-01],
           [2.30705538e-01, 2.95501982e-01, 5.33576454e-01],
           [2.29544644e-01, 2.92342466e-01, 5.26492728e-01],
           [2.28329868e-01, 2.89191531e-01, 5.19440505e-01],
           [2.27063120e-01, 2.86048621e-01, 5.12420289e-01],
           [2.25746215e-01, 2.82913203e-01, 5.05432497e-01],
           [2.24380878e-01, 2.79784770e-01, 4.98477470e-01],
           [2.22968752e-01, 2.76662836e-01, 4.91555475e-01],
           [2.21511396e-01, 2.73546937e-01, 4.84666715e-01],
           [2.20010239e-01, 2.70436621e-01, 4.77811461e-01],
           [2.18466444e-01, 2.67331436e-01, 4.70990359e-01],
           [2.16881625e-01, 2.64230995e-01, 4.64202867e-01],
           [2.15256985e-01, 2.61134895e-01, 4.57449146e-01],
           [2.13593418e-01, 2.58042718e-01, 4.50729909e-01],
           [2.11892450e-01, 2.54954135e-01, 4.44044228e-01],
           [2.10154732e-01, 2.51868737e-01, 4.37393064e-01],
           [2.08381656e-01, 2.48786217e-01, 4.30775450e-01],
           [2.06573793e-01, 2.45706187e-01, 4.24192274e-01],
           [2.04732430e-01, 2.42628362e-01, 4.17642496e-01],
           [2.02858067e-01, 2.39552372e-01, 4.11126922e-01],
           [2.00951756e-01, 2.36477929e-01, 4.04644823e-01],
           [1.99014302e-01, 2.33404731e-01, 3.98195962e-01],
           [1.97046147e-01, 2.30332431e-01, 3.91780945e-01],
           [1.95048234e-01, 2.27260766e-01, 3.85398932e-01],
           [1.93021210e-01, 2.24189441e-01, 3.79049751e-01],
           [1.90965676e-01, 2.21118165e-01, 3.72733244e-01],
           [1.88882068e-01, 2.18046628e-01, 3.66449615e-01],
           [1.86771070e-01, 2.14974566e-01, 3.60198266e-01],
           [1.84633214e-01, 2.11901701e-01, 3.53978926e-01],
           [1.82468982e-01, 2.08827751e-01, 3.47791363e-01],
           [1.80278832e-01, 2.05752438e-01, 3.41635323e-01],
           [1.78063194e-01, 2.02675486e-01, 3.35510539e-01],
           [1.75822472e-01, 1.99596616e-01, 3.29416728e-01],
           [1.73557047e-01, 1.96515552e-01, 3.23353592e-01],
           [1.71267273e-01, 1.93432015e-01, 3.17320821e-01],
           [1.68953481e-01, 1.90345728e-01, 3.11318090e-01],
           [1.66615979e-01, 1.87256408e-01, 3.05345062e-01],
           [1.64255048e-01, 1.84163774e-01, 2.99401390e-01],
           [1.61870950e-01, 1.81067539e-01, 2.93486714e-01],
           [1.59463922e-01, 1.77967413e-01, 2.87600662e-01],
           [1.57034176e-01, 1.74863103e-01, 2.81742854e-01],
           [1.54581876e-01, 1.71754305e-01, 2.75912999e-01],
           [1.52107134e-01, 1.68640705e-01, 2.70110883e-01],
           [1.49610173e-01, 1.65522006e-01, 2.64335837e-01],
           [1.47091119e-01, 1.62397894e-01, 2.58587437e-01],
           [1.44550070e-01, 1.59268044e-01, 2.52865249e-01],
           [1.41987011e-01, 1.56132104e-01, 2.47169165e-01],
           [1.39402031e-01, 1.52989740e-01, 2.41498612e-01],
           [1.36795217e-01, 1.49840614e-01, 2.35852930e-01],
           [1.34166545e-01, 1.46684356e-01, 2.30231753e-01],
           [1.31515885e-01, 1.43520568e-01, 2.24635009e-01],
           [1.28843336e-01, 1.40348896e-01, 2.19061687e-01],
           [1.26148778e-01, 1.37168927e-01, 2.13511466e-01],
           [1.23432032e-01, 1.33980228e-01, 2.07984146e-01],
           [1.20693111e-01, 1.30782396e-01, 2.02478680e-01],
           [1.17931726e-01, 1.27574952e-01, 1.96995048e-01],
           [1.15147777e-01, 1.24357446e-01, 1.91532377e-01],
           [1.12341037e-01, 1.21129384e-01, 1.86090147e-01],
           [1.09511209e-01, 1.17890242e-01, 1.80667973e-01],
           [1.06658103e-01, 1.14639504e-01, 1.75264889e-01],
           [1.03781280e-01, 1.11376578e-01, 1.69880751e-01],
           [1.00880520e-01, 1.08100903e-01, 1.64514367e-01],
           [9.79552928e-02, 1.04811822e-01, 1.59165616e-01],
           [9.50052857e-02, 1.01508706e-01, 1.53833276e-01],
           [9.20299100e-02, 9.81908332e-02, 1.48517042e-01],
           [8.90287064e-02, 9.48574837e-02, 1.43215838e-01],
           [8.60010553e-02, 9.15078661e-02, 1.37928993e-01],
           [8.29462963e-02, 8.81411436e-02, 1.32655723e-01],
           [7.98637948e-02, 8.47564453e-02, 1.27394821e-01],
           [7.67526386e-02, 8.13527897e-02, 1.22145928e-01],
           [7.36121083e-02, 7.79291923e-02, 1.16907471e-01],
           [7.04412107e-02, 7.44845475e-02, 1.11678639e-01],
           [6.72388963e-02, 7.10176749e-02, 1.06458404e-01],
           [6.40041036e-02, 6.75273224e-02, 1.01245258e-01],
           [6.07355301e-02, 6.40121018e-02, 9.60381728e-02],
           [5.74318124e-02, 6.04705226e-02, 9.08357274e-02],
           [5.40914827e-02, 5.69009698e-02, 8.56362070e-02],
           [5.07128356e-02, 5.33016572e-02, 8.04381104e-02],
           [4.72939791e-02, 4.96706236e-02, 7.52397997e-02],
           [4.38328995e-02, 4.60057289e-02, 7.00390473e-02],
           [4.03253250e-02, 4.23045858e-02, 6.48337039e-02],
           [3.68119799e-02, 3.85588031e-02, 5.96215760e-02],
           [3.34383800e-02, 3.49234868e-02, 5.43999018e-02],
           [3.02065532e-02, 3.14566306e-02, 4.91655596e-02],
           [2.71185916e-02, 2.81589142e-02, 4.39151506e-02],
           [2.41766866e-02, 2.50311454e-02, 3.86382927e-02],
           [2.13831525e-02, 2.20742794e-02, 3.36012698e-02],
           [1.87405026e-02, 1.92894533e-02, 2.89448430e-02],
           [1.62514037e-02, 1.66779945e-02, 2.46610222e-02],
           [1.39187470e-02, 1.42414639e-02, 2.07420804e-02],
           [1.17456978e-02, 1.19817007e-02, 1.71805773e-02],
           [9.73575395e-03, 9.90087988e-03, 1.39694399e-02],
           [7.89285303e-03, 8.00159702e-03, 1.11018863e-02],
           [6.22148215e-03, 6.28697637e-03, 8.57157164e-03],
           [4.72684477e-03, 4.76082980e-03, 6.37274354e-03],
           [3.41513042e-03, 3.42790180e-03, 4.50037440e-03],
           [2.29393772e-03, 2.29426270e-03, 2.95045739e-03],
           [1.37301685e-03, 1.36800262e-03, 1.72055651e-03],
           [6.65756539e-04, 6.60629159e-04, 8.10977578e-04],
           [1.92918273e-04, 1.90603023e-04, 2.27925431e-04],
           [0.00000000e+00, 0.00000000e+00, 0.00000000e+00],
           [2.50405921e-04, 1.75018632e-04, 1.61710024e-04],
           [8.92517404e-04, 5.99317811e-04, 5.48450163e-04],
           [1.89567776e-03, 1.22699630e-03, 1.11291812e-03],
           [3.25253820e-03, 2.03614515e-03, 1.83192211e-03],
           [4.96160635e-03, 3.01221751e-03, 2.68991955e-03],
           [7.02399861e-03, 4.14436312e-03, 3.67528175e-03],
           [9.44225669e-03, 5.42394949e-03, 4.77876441e-03],
           [1.22197998e-02, 6.84381586e-03, 5.99272741e-03],
           [1.53606337e-02, 8.39784466e-03, 7.31068274e-03],
           [1.88691811e-02, 1.00806931e-02, 8.72700914e-03],
           [2.27501768e-02, 1.18876142e-02, 1.02367606e-02],
           [2.70085984e-02, 1.38143315e-02, 1.18355320e-02],
           [3.16496202e-02, 1.58569485e-02, 1.35193608e-02],
           [3.66785804e-02, 1.80118805e-02, 1.52846533e-02],
           [4.20542897e-02, 2.02758026e-02, 1.71281286e-02],
           [4.74355350e-02, 2.26456088e-02, 1.90467735e-02],
           [5.27839353e-02, 2.51183799e-02, 2.10378075e-02],
           [5.81033308e-02, 2.76913565e-02, 2.30986538e-02],
           [6.33970688e-02, 3.03619180e-02, 2.52269163e-02],
           [6.86680902e-02, 3.31275645e-02, 2.74203591e-02],
           [7.39189970e-02, 3.59859018e-02, 2.96768911e-02],
           [7.91521062e-02, 3.89346285e-02, 3.19945518e-02],
           [8.43694929e-02, 4.19298541e-02, 3.43714996e-02],
           [8.95730253e-02, 4.48721388e-02, 3.68060017e-02],
           [9.47643935e-02, 4.77722699e-02, 3.92964257e-02],
           [9.99451333e-02, 5.06320448e-02, 4.18043645e-02],
           [1.05116646e-01, 5.34530985e-02, 4.42646752e-02],
           [1.10280214e-01, 5.62369230e-02, 4.66888506e-02],
           [1.15437094e-01, 5.89848377e-02, 4.90784317e-02],
           [1.20588439e-01, 6.16980544e-02, 5.14348543e-02],
           [1.25735130e-01, 6.43777979e-02, 5.37596057e-02],
           [1.30878100e-01, 6.70251295e-02, 5.60539823e-02],
           [1.36018216e-01, 6.96410291e-02, 5.83191994e-02],
           [1.41156286e-01, 7.22264036e-02, 6.05563995e-02],
           [1.46293290e-01, 7.47819523e-02, 6.27664774e-02],
           [1.51429817e-01, 7.73085251e-02, 6.49505447e-02],
           [1.56566443e-01, 7.98069012e-02, 6.71096359e-02],
           [1.61703793e-01, 8.22777548e-02, 6.92446667e-02],
           [1.66842650e-01, 8.47215852e-02, 7.13563472e-02],
           [1.71983587e-01, 8.71389633e-02, 7.34454941e-02],
           [1.77126932e-01, 8.95305615e-02, 7.55130609e-02],
           [1.82273188e-01, 9.18968842e-02, 7.75598017e-02],
           [1.87423286e-01, 9.42380986e-02, 7.95860741e-02],
           [1.92577220e-01, 9.65549486e-02, 8.15929480e-02],
           [1.97735422e-01, 9.88478473e-02, 8.35810970e-02],
           [2.02898825e-01, 1.01116817e-01, 8.55507439e-02],
           [2.08067292e-01, 1.03362578e-01, 8.75029495e-02],
           [2.13241393e-01, 1.05585328e-01, 8.94381633e-02],
           [2.18421683e-01, 1.07785240e-01, 9.13568183e-02],
           [2.23608097e-01, 1.09962891e-01, 9.32598227e-02],
           [2.28801578e-01, 1.12118112e-01, 9.51472407e-02],
           [2.34001873e-01, 1.14251561e-01, 9.70200821e-02],
           [2.39209734e-01, 1.16363147e-01, 9.88785222e-02],
           [2.44425160e-01, 1.18453298e-01, 1.00723325e-01],
           [2.49648704e-01, 1.20522014e-01, 1.02554790e-01],
           [2.54880412e-01, 1.22569646e-01, 1.04373606e-01],
           [2.60120851e-01, 1.24596132e-01, 1.06180032e-01],
           [2.65369901e-01, 1.26601911e-01, 1.07974864e-01],
           [2.70628370e-01, 1.28586694e-01, 1.09758139e-01],
           [2.75895932e-01, 1.30551041e-01, 1.11530796e-01],
           [2.81173297e-01, 1.32494696e-01, 1.13292933e-01],
           [2.86460480e-01, 1.34417924e-01, 1.15045196e-01],
           [2.91757557e-01, 1.36320927e-01, 1.16788172e-01],
           [2.97065280e-01, 1.38203356e-01, 1.18521910e-01],
           [3.02383423e-01, 1.40065620e-01, 1.20247227e-01],
           [3.07712194e-01, 1.41907774e-01, 1.21964590e-01],
           [3.13052080e-01, 1.43729626e-01, 1.23674247e-01],
           [3.18403221e-01, 1.45531253e-01, 1.25376717e-01],
           [3.23765661e-01, 1.47312795e-01, 1.27072590e-01],
           [3.29139621e-01, 1.49074238e-01, 1.28762320e-01],
           [3.34525317e-01, 1.50815557e-01, 1.30446364e-01],
           [3.39923145e-01, 1.52536558e-01, 1.32125045e-01],
           [3.45333133e-01, 1.54237347e-01, 1.33798973e-01],
           [3.50755421e-01, 1.55917923e-01, 1.35468671e-01],
           [3.56190197e-01, 1.57578234e-01, 1.37134635e-01],
           [3.61637641e-01, 1.59218220e-01, 1.38797370e-01],
           [3.67097926e-01, 1.60837816e-01, 1.40457395e-01],
           [3.72571216e-01, 1.62436952e-01, 1.42115242e-01],
           [3.78057669e-01, 1.64015553e-01, 1.43771459e-01],
           [3.83557434e-01, 1.65573540e-01, 1.45426609e-01],
           [3.89070650e-01, 1.67110832e-01, 1.47081276e-01],
           [3.94597449e-01, 1.68627342e-01, 1.48736058e-01],
           [4.00138057e-01, 1.70122884e-01, 1.50391502e-01],
           [4.05692703e-01, 1.71597256e-01, 1.52048170e-01],
           [4.11261318e-01, 1.73050524e-01, 1.53706852e-01],
           [4.16843991e-01, 1.74482598e-01, 1.55368242e-01],
           [4.22440890e-01, 1.75893300e-01, 1.57032997e-01],
           [4.28052465e-01, 1.77282163e-01, 1.58701605e-01],
           [4.33678349e-01, 1.78649505e-01, 1.60375140e-01],
           [4.39318877e-01, 1.79994946e-01, 1.62054215e-01],
           [4.44974232e-01, 1.81318239e-01, 1.63739582e-01],
           [4.50644228e-01, 1.82619498e-01, 1.65432264e-01],
           [4.56329331e-01, 1.83898166e-01, 1.67132886e-01],
           [4.62029291e-01, 1.85154398e-01, 1.68842578e-01],
           [4.67744278e-01, 1.86387911e-01, 1.70562231e-01],
           [4.73474563e-01, 1.87598299e-01, 1.72292720e-01],
           [4.79219860e-01, 1.88785724e-01, 1.74035309e-01],
           [4.84980279e-01, 1.89949924e-01, 1.75791060e-01],
           [4.90756134e-01, 1.91090398e-01, 1.77560971e-01],
           [4.96547245e-01, 1.92207159e-01, 1.79346391e-01],
           [5.02353573e-01, 1.93300057e-01, 1.81148646e-01],
           [5.08175118e-01, 1.94368884e-01, 1.82969101e-01],
           [5.14011846e-01, 1.95413453e-01, 1.84809217e-01],
           [5.19863683e-01, 1.96433608e-01, 1.86670552e-01],
           [5.25730581e-01, 1.97429142e-01, 1.88554739e-01],
           [5.31612649e-01, 1.98399652e-01, 1.90463429e-01],
           [5.37509421e-01, 1.99345375e-01, 1.92398666e-01],
           [5.43420655e-01, 2.00266281e-01, 1.94362486e-01],
           [5.49346690e-01, 2.01161630e-01, 1.96356788e-01],
           [5.55286577e-01, 2.02032189e-01, 1.98384196e-01],
           [5.61240610e-01, 2.02877220e-01, 2.00446937e-01],
           [5.67208085e-01, 2.03697166e-01, 2.02547837e-01],
           [5.73188571e-01, 2.04492120e-01, 2.04689789e-01],
           [5.79181634e-01, 2.05262158e-01, 2.06875900e-01],
           [5.85186703e-01, 2.06007502e-01, 2.09109565e-01],
           [5.91203043e-01, 2.06728553e-01, 2.11394499e-01],
           [5.97229738e-01, 2.07425930e-01, 2.13734761e-01],
           [6.03265762e-01, 2.08100368e-01, 2.16134765e-01],
           [6.09310296e-01, 2.08752305e-01, 2.18599267e-01],
           [6.15361552e-01, 2.09383437e-01, 2.21133653e-01],
           [6.21418030e-01, 2.09995061e-01, 2.23743711e-01],
           [6.27477956e-01, 2.10588826e-01, 2.26435831e-01],
           [6.33539095e-01, 2.11166979e-01, 2.29217080e-01],
           [6.39598686e-01, 2.11732496e-01, 2.32095254e-01],
           [6.45653345e-01, 2.12289230e-01, 2.35078919e-01],
           [6.51699717e-01, 2.12840977e-01, 2.38177557e-01],
           [6.57732983e-01, 2.13393659e-01, 2.41401524e-01],
           [6.63747877e-01, 2.13953885e-01, 2.44762185e-01],
           [6.69737953e-01, 2.14530055e-01, 2.48271845e-01],
           [6.75695954e-01, 2.15131836e-01, 2.51943881e-01],
           [6.81612637e-01, 2.15772046e-01, 2.55792179e-01],
           [6.87477664e-01, 2.16465341e-01, 2.59831245e-01],
           [6.93278886e-01, 2.17229438e-01, 2.64075428e-01],
           [6.99002681e-01, 2.18084671e-01, 2.68538402e-01],
           [7.04633700e-01, 2.19054575e-01, 2.73231715e-01],
           [7.10155726e-01, 2.20164618e-01, 2.78163892e-01],
           [7.15552162e-01, 2.21441535e-01, 2.83338751e-01],
           [7.20807191e-01, 2.22911508e-01, 2.88754239e-01],
           [7.25906987e-01, 2.24598156e-01, 2.94401565e-01],
           [7.30840940e-01, 2.26520375e-01, 3.00265174e-01],
           [7.35602598e-01, 2.28690528e-01, 3.06323794e-01],
           [7.40190012e-01, 2.31113574e-01, 3.12552090e-01],
           [7.44605521e-01, 2.33787117e-01, 3.18922961e-01],
           [7.48855005e-01, 2.36702450e-01, 3.25409542e-01],
           [7.52946908e-01, 2.39846102e-01, 3.31986705e-01],
           [7.56891213e-01, 2.43201511e-01, 3.38632260e-01],
           [7.60698529e-01, 2.46750603e-01, 3.45327544e-01],
           [7.64379583e-01, 2.50474937e-01, 3.52056393e-01],
           [7.67944520e-01, 2.54356673e-01, 3.58806560e-01],
           [7.71402848e-01, 2.58379021e-01, 3.65567959e-01],
           [7.74763357e-01, 2.62526473e-01, 3.72332346e-01],
           [7.78033766e-01, 2.66785165e-01, 3.79094075e-01],
           [7.81221287e-01, 2.71142442e-01, 3.85847823e-01],
           [7.84332066e-01, 2.75587302e-01, 3.92590390e-01],
           [7.87371724e-01, 2.80109885e-01, 3.99318896e-01],
           [7.90345331e-01, 2.84701440e-01, 4.06031013e-01],
           [7.93257067e-01, 2.89354569e-01, 4.12725807e-01],
           [7.96111189e-01, 2.94062289e-01, 4.19401378e-01],
           [7.98911043e-01, 2.98818882e-01, 4.26057354e-01],
           [8.01659812e-01, 3.03619159e-01, 4.32693112e-01],
           [8.04360350e-01, 3.08458564e-01, 4.39308253e-01],
           [8.07015187e-01, 3.13333128e-01, 4.45902617e-01],
           [8.09626959e-01, 3.18239045e-01, 4.52475490e-01],
           [8.12197392e-01, 3.23173558e-01, 4.59027603e-01],
           [8.14728746e-01, 3.28133626e-01, 4.65558380e-01],
           [8.17222531e-01, 3.33117054e-01, 4.72068381e-01],
           [8.19680611e-01, 3.38121484e-01, 4.78557318e-01],
           [8.22104510e-01, 3.43144996e-01, 4.85025328e-01],
           [8.24495534e-01, 3.48185978e-01, 4.91472731e-01],
           [8.26855017e-01, 3.53242899e-01, 4.97899662e-01],
           [8.29184177e-01, 3.58314417e-01, 5.04306306e-01],
           [8.31484242e-01, 3.63399267e-01, 5.10692731e-01],
           [8.33756388e-01, 3.68496303e-01, 5.17058998e-01],
           [8.36001418e-01, 3.73604753e-01, 5.23405617e-01],
           [8.38220319e-01, 3.78723748e-01, 5.29732744e-01],
           [8.40414334e-01, 3.83852261e-01, 5.36040132e-01],
           [8.42583873e-01, 3.88989990e-01, 5.42328600e-01],
           [8.44730280e-01, 3.94135918e-01, 5.48597672e-01],
           [8.46853989e-01, 3.99289794e-01, 5.54848014e-01],
           [8.48955780e-01, 4.04451122e-01, 5.61079794e-01],
           [8.51036810e-01, 4.09619140e-01, 5.67292684e-01],
           [8.53097435e-01, 4.14793740e-01, 5.73487314e-01],
           [8.55138400e-01, 4.19974530e-01, 5.79663796e-01],
           [8.57160420e-01, 4.25161166e-01, 5.85822255e-01],
           [8.59164180e-01, 4.30353342e-01, 5.91962831e-01],
           [8.61150338e-01, 4.35550793e-01, 5.98085673e-01],
           [8.63119528e-01, 4.40753286e-01, 6.04190941e-01],
           [8.65072364e-01, 4.45960618e-01, 6.10278800e-01],
           [8.67009434e-01, 4.51172614e-01, 6.16349424e-01],
           [8.68931314e-01, 4.56389124e-01, 6.22402990e-01],
           [8.70838557e-01, 4.61610018e-01, 6.28439682e-01],
           [8.72731706e-01, 4.66835188e-01, 6.34459685e-01],
           [8.74611646e-01, 4.72064291e-01, 6.40462844e-01],
           [8.76478648e-01, 4.77297426e-01, 6.46449598e-01],
           [8.78333157e-01, 4.82534573e-01, 6.52420200e-01],
           [8.80175998e-01, 4.87775458e-01, 6.58374544e-01],
           [8.82007630e-01, 4.93020065e-01, 6.64312867e-01],
           [8.83828303e-01, 4.98268524e-01, 6.70235579e-01],
           [8.85639170e-01, 5.03520364e-01, 6.76142293e-01],
           [8.87440021e-01, 5.08776027e-01, 6.82033811e-01],
           [8.89232095e-01, 5.14035000e-01, 6.87909685e-01],
           [8.91015191e-01, 5.19297722e-01, 6.93770686e-01],
           [8.92790602e-01, 5.24563661e-01, 6.99616342e-01],
           [8.94558167e-01, 5.29833230e-01, 7.05447374e-01],
           [8.96318786e-01, 5.35106162e-01, 7.11263644e-01],
           [8.98072928e-01, 5.40382471e-01, 7.17065364e-01],
           [8.99820856e-01, 5.45662301e-01, 7.22852902e-01],
           [9.01563450e-01, 5.50945411e-01, 7.28626157e-01],
           [9.03301088e-01, 5.56231883e-01, 7.34385416e-01],
           [9.05034121e-01, 5.61521810e-01, 7.40130983e-01],
           [9.06763092e-01, 5.66815172e-01, 7.45863021e-01],
           [9.08488837e-01, 5.72111773e-01, 7.51581496e-01],
           [9.10211624e-01, 5.77411766e-01, 7.57286781e-01],
           [9.11931920e-01, 5.82715183e-01, 7.62979108e-01],
           [9.13650254e-01, 5.88022020e-01, 7.68658672e-01],
           [9.15367157e-01, 5.93332277e-01, 7.74325672e-01],
           [9.17083153e-01, 5.98645956e-01, 7.79980318e-01],
           [9.18798768e-01, 6.03963064e-01, 7.85622826e-01],
           [9.20514633e-01, 6.09283546e-01, 7.91253353e-01],
           [9.22231134e-01, 6.14607493e-01, 7.96872214e-01],
           [9.23948784e-01, 6.19934921e-01, 8.02479652e-01],
           [9.25668101e-01, 6.25265847e-01, 8.08075913e-01],
           [9.27389602e-01, 6.30600289e-01, 8.13661250e-01],
           [9.29113802e-01, 6.35938267e-01, 8.19235926e-01],
           [9.30841215e-01, 6.41279803e-01, 8.24800211e-01],
           [9.32572353e-01, 6.46624922e-01, 8.30354383e-01],
           [9.34307831e-01, 6.51973593e-01, 8.35898672e-01],
           [9.36048111e-01, 6.57325872e-01, 8.41433402e-01],
           [9.37793672e-01, 6.62681804e-01, 8.46958895e-01],
           [9.39545018e-01, 6.68041422e-01, 8.52475465e-01],
           [9.41302651e-01, 6.73404760e-01, 8.57983438e-01],
           [9.43067073e-01, 6.78771854e-01, 8.63483146e-01],
           [9.44838780e-01, 6.84142743e-01, 8.68974933e-01],
           [9.46618335e-01, 6.89517432e-01, 8.74459121e-01],
           [9.48406446e-01, 6.94895851e-01, 8.79935972e-01],
           [9.50203343e-01, 7.00278181e-01, 8.85405987e-01],
           [9.52009511e-01, 7.05664467e-01, 8.90869552e-01],
           [9.53825431e-01, 7.11054758e-01, 8.96327065e-01],
           [9.55651891e-01, 7.16448947e-01, 9.01778791e-01],
           [9.57489204e-01, 7.21847170e-01, 9.07225227e-01],
           [9.59337703e-01, 7.27249552e-01, 9.12666864e-01],
           [9.61197903e-01, 7.32656122e-01, 9.18104122e-01],
           [9.63070679e-01, 7.38066736e-01, 9.23537276e-01],
           [9.64956022e-01, 7.43481686e-01, 9.28966994e-01],
           [9.66854371e-01, 7.48901041e-01, 9.34393756e-01],
           [9.68766742e-01, 7.54324587e-01, 9.39817814e-01],
           [9.70692994e-01, 7.59752676e-01, 9.45239910e-01],
           [9.72633664e-01, 7.65185329e-01, 9.50660512e-01],
           [9.74589543e-01, 7.70622443e-01, 9.56080000e-01],
           [9.76560523e-01, 7.76064347e-01, 9.61499119e-01],
           [9.78547422e-01, 7.81510927e-01, 9.66918257e-01],
           [9.80550430e-01, 7.86962366e-01, 9.72338056e-01],
           [9.82569839e-01, 7.92418797e-01, 9.77759126e-01],
           [9.84606361e-01, 7.97880156e-01, 9.83181927e-01],
           [9.86659787e-01, 8.03346807e-01, 9.88607269e-01]]

test_cm = ListedColormap(cm_data, name="redshift")
