import numpy as np

lumos = [[12.337607601941746, 12.075241609902044, 14.801469522621884, 12.015247841832803, 9.851322193204561, 8.340004448359837, 8.759903833068215, 9.699534210863876, 8.301465976891055, 7.967202104174967, 8.942621479249055, 8.378365766544153, 9.76667413190982, 9.846564868654157, 7.824144201516125, 7.34340432506385, 7.664119167734064, 8.177921493900703, 7.693692775277957, 7.480970087594753, 7.478821592934058, 7.822731661855627, 7.809808068634458, 7.97922322576639, 8.032366945685126, 8.178093514534925], [12.372301811420492, 13.7658025962131, 15.345725211798873, 14.049430089954136, 12.424406134879405, 10.110298928275993, 10.523721179392416, 12.272071857451907, 12.247071941611278, 10.249421713150362, 10.571276437666626, 10.262797525584276, 11.536972951118596, 11.57192224625575, 9.327644931670186, 8.656344925714018, 8.715962559346229, 9.10599314702398, 8.384811660316716, 8.446509882779432, 8.85338253446979, 8.309833853697278, 8.153444797011279, 8.213510383738681, 8.458436597012273, 8.743169985548427]],[[12.58525988058541, 11.757233891997823, 12.240663349849997, 11.294341143511632, 9.398120368137054, 8.292669400519626, 8.068843035751332, 8.47054931105874, 9.069646985961326, 8.675590159819977, 7.652720946568408, 8.216142205827065, 6.842007704577361, 7.236637485041456, 6.861379040862411, 6.354406010635334, 6.572773895298398, 7.016813632829492, 7.788103374399581, 8.156996220654365, 8.184028875106787, 8.215561401245969, 8.149878407812182, 8.614880609339714, 8.631927882340397, 8.766613316773594], [12.535251243116699, 12.874774359280682, 13.3938569049915, 12.02464524044876, 10.492988154375801, 8.34236130030974, 8.010712992671008, 7.757632067280106, 9.16460732619958, 9.301636843972068, 9.395910319467893, 9.391384800074176, 7.858410061088394, 7.007431196063233, 7.116416484757866, 7.30539307541382, 6.597451387766733, 7.239877852256775, 7.774429183841331, 8.050431452220318, 7.992032620836076, 8.247077669568439, 8.299086610087613, 8.48437120759259, 8.67444481756662, 8.368142698020405]],[[9.03412023940386, 13.518649506834993, 14.526959912883157, 12.658918979031771, 11.08997866731043, 9.322751320405125, 9.30069296080538, 9.346784818407677, 8.235021843403887, 8.017241824267357, 7.6446969801239435, 7.366395490552213, 7.376606095401184, 7.304007078283381, 6.949932152993813, 7.275013028484493, 7.0111301234851755, 7.107324440713878, 7.57251322050686, 7.692617425820756, 7.414061012450898, 7.260479642684805, 7.596232924740475, 7.836979027645355, 8.162039803832654, 8.065353003470227], [12.769548203702595, 11.112384817239098, 14.899001050437231, 14.613630381135376, 12.400650369523603, 11.076534774345644, 10.726486289959237, 11.625077950613168, 9.661138575562555, 9.69495389491283, 9.90682932581494, 10.090195154952596, 9.434147817529366, 9.183767793497223, 8.715685692296647, 8.633913967695674, 8.641719507622382, 8.582780864430038, 8.133724254186474, 8.542322473792353, 8.210223442147091, 8.376258727590265, 8.139682980523979, 8.28406895474366, 8.235925020375195, 8.362166715682028]],[[9.03412023940386, 13.518649506834993, 14.526959912883157, 12.658918979031771, 11.08997866731043, 9.322751320405125, 9.30069296080538, 9.346784818407677, 8.235021843403887, 8.017241824267357, 7.6446969801239435, 7.366395490552213, 7.376606095401184, 7.304007078283381, 6.949932152993813, 7.275013028484493, 7.0111301234851755, 7.107324440713878, 7.57251322050686, 7.692617425820756, 7.414061012450898, 7.260479642684805, 7.596232924740475, 7.836979027645355, 8.162039803832654, 8.065353003470227], [12.769548203702595, 11.112384817239098, 14.899001050437231, 14.613630381135376, 12.400650369523603, 11.076534774345644, 10.726486289959237, 11.625077950613168, 9.661138575562555, 9.69495389491283, 9.90682932581494, 10.090195154952596, 9.434147817529366, 9.183767793497223, 8.715685692296647, 8.633913967695674, 8.641719507622382, 8.582780864430038, 8.133724254186474, 8.542322473792353, 8.210223442147091, 8.376258727590265, 8.139682980523979, 8.28406895474366, 8.235925020375195, 8.362166715682028]],[[9.03412023940386, 13.518649506834993, 14.526959912883157, 12.658918979031771, 11.08997866731043, 9.322751320405125, 9.30069296080538, 9.346784818407677, 8.235021843403887, 8.017241824267357, 7.6446969801239435, 7.366395490552213, 7.376606095401184, 7.304007078283381, 6.949932152993813, 7.275013028484493, 7.0111301234851755, 7.107324440713878, 7.57251322050686, 7.692617425820756, 7.414061012450898, 7.260479642684805, 7.596232924740475, 7.836979027645355, 8.162039803832654, 8.065353003470227], [12.769548203702595, 11.112384817239098, 14.899001050437231, 14.613630381135376, 12.400650369523603, 11.076534774345644, 10.726486289959237, 11.625077950613168, 9.661138575562555, 9.69495389491283, 9.90682932581494, 10.090195154952596, 9.434147817529366, 9.183767793497223, 8.715685692296647, 8.633913967695674, 8.641719507622382, 8.582780864430038, 8.133724254186474, 8.542322473792353, 8.210223442147091, 8.376258727590265, 8.139682980523979, 8.28406895474366, 8.235925020375195, 8.362166715682028]],[[12.092557194136205, 14.120236974572668, 14.827835711533737, 12.901786943861925, 11.196501611160311, 9.309206814777136, 10.152257287208203, 10.863331155757978, 9.045246659420172, 8.377257545795512, 8.223953944665725, 7.470840473511589, 7.801813983291069, 8.268822383889974, 6.9371788314387866, 7.250172634231747, 7.818224958131472, 8.086292717698097, 8.12381919355901, 8.333280001514822, 8.215025414843412, 8.733040631062524, 9.058328956991843, 9.49444193191849, 9.655598791096503, 9.881259430658591], [13.15498976709768, 13.906304411347557, 14.550605018377798, 14.354705611825109, 12.387034795936133, 11.607729060422061, 11.950941794085695, 12.071974927758184, 10.87741707543021, 10.39318696335819, 10.589443437580744, 9.966035294114192, 9.848936943320295, 10.009377120680968, 9.475084294252078, 8.961675140665767, 8.834466063151792, 9.806903083441389, 9.382930405728988, 9.3351692284343, 9.488396513952715, 9.400092811761212, 9.66979398617856, 9.797914333068071, 9.75766373493154, 9.8573367927573]],[[11.339924881627892, 11.91050350873885, 14.044047797989052, 10.18996299279974, 8.898458717567296, 7.1374527311176115, 8.290010537684145, 7.995964332993853, 9.250053060310906, 8.614669200135918, 8.336050954582245, 6.803523347128424, 6.576140182922471, 6.416057159035225, 6.744937184201118, 6.997177341735917, 7.760988755131393, 8.601666057404518, 8.016039911424581, 8.096856961044274, 8.167907048765388, 8.448273828519834, 8.638733360835454, 9.009551200630272, 8.959870573373975, 9.020326803747137], [11.41519130787772, 11.251708819057093, 14.781071327682843, 11.553869160456781, 10.680835958854669, 9.352033118206053, 9.601506018236558, 9.090750075896716, 8.97351580403465, 8.988647525200554, 8.830885430641231, 8.506360551991959, 8.515490843286178, 8.240679008003232, 7.858719402156842, 7.6502387956603926, 9.060670029288966, 9.944674828744606, 8.27514981693565, 8.729706880526685, 8.302303071637995, 8.861597828124282, 9.063899747651996, 9.029550745056845, 9.06769304869403, 9.296543748808935]],[[9.03412023940386, 13.518649506834993, 14.526959912883157, 12.658918979031771, 11.089978667310428, 9.322751320405125, 9.30069296080538, 9.346784818407675, 8.235021843403887, 8.017241824267357, 7.644696980123943, 7.366395490552212, 7.376606095401183, 7.30400707828338, 6.949932152993812, 7.275013028484493, 7.0111301234851755, 7.107324440713878, 7.57251322050686, 7.692617425820757, 7.414061012450898, 7.260479642684806, 7.596232924740475, 7.836979027645355, 8.162039803832654, 8.065353003470227], [12.769548203702595, 11.112384817239098, 14.899001050437231, 14.613630381135376, 12.400650369523603, 11.076534774345644, 10.726486289959237, 11.625077950613168, 9.661138575562557, 9.69495389491283, 9.90682932581494, 10.090195154952594, 9.434147817529366, 9.183767793497223, 8.715685692296649, 8.633913967695674, 8.641719507622382, 8.582780864430038, 8.133724254186472, 8.542322473792353, 8.210223442147091, 8.376258727590265, 8.139682980523979, 8.284068954743658, 8.235925020375195, 8.362166715682028]],[[11.424137834943814, 10.085853002178563, 12.862122765270174, 12.576653349273593, 10.20254916729576, 9.219488495280633, 9.373390045424452, 9.357877975628506, 8.600888817531713, 8.47397765968635, 8.58382102046486, 8.27720909324648, 7.93584473500116, 8.191021051024109, 7.484674803809445, 7.401212022141757, 7.654804689652724, 7.557498646337436, 8.009968220973052, 7.746560765618663, 7.484771189549961, 8.00054878351955, 8.304221233175973, 8.442989808109127, 8.721724934544822, 8.730002609311736], [10.555777758292015, 11.643360564311592, 13.980073491821965, 12.568297997294152, 11.446027831721416, 9.756218120305801, 9.728077125713655, 9.765148135675624, 9.585293439442848, 8.614266048331904, 8.615220937380224, 7.551772371045072, 8.521582325940829, 8.555134636642714, 7.448775063647852, 7.07381319923296, 7.614909187179725, 7.502164973634132, 7.596505494307845, 7.895538604738647, 7.623944989050362, 7.780787576355988, 8.079612605036383, 8.675001575515486, 8.45945044675702, 8.335481868610673]],[[11.339924881627892, 11.91050350873885, 14.044047797989053, 10.18996299279974, 8.898458717567296, 7.1374527311176115, 8.290010537684145, 7.995964332993851, 9.250053060310904, 8.614669200135918, 8.336050954582245, 6.803523347128424, 6.57614018292247, 6.416057159035225, 6.744937184201118, 6.997177341735917, 7.760988755131393, 8.601666057404518, 8.016039911424581, 8.096856961044274, 8.167907048765388, 8.448273828519836, 8.638733360835454, 9.009551200630272, 8.959870573373973, 9.020326803747137], [11.41519130787772, 11.251708819057093, 14.781071327682843, 11.553869160456781, 10.680835958854669, 9.352033118206053, 9.601506018236558, 9.090750075896716, 8.97351580403465, 8.988647525200552, 8.830885430641231, 8.506360551991959, 8.515490843286178, 8.240679008003232, 7.858719402156842, 7.6502387956603926, 9.060670029288966, 9.944674828744606, 8.27514981693565, 8.729706880526685, 8.302303071637994, 8.86159782812428, 9.063899747651996, 9.029550745056845, 9.06769304869403, 9.296543748808935]],[[12.337607601941746, 12.075241609902042, 14.801469522621884, 12.015247841832803, 9.851322193204563, 8.340004448359837, 8.759903833068215, 9.699534210863874, 8.301465976891055, 7.967202104174968, 8.942621479249055, 8.378365766544155, 9.76667413190982, 9.846564868654157, 7.824144201516125, 7.343404325063851, 7.664119167734064, 8.177921493900703, 7.693692775277956, 7.480970087594753, 7.478821592934058, 7.822731661855628, 7.809808068634458, 7.979223225766389, 8.032366945685126, 8.178093514534925], [12.372301811420492, 13.7658025962131, 15.345725211798873, 14.049430089954136, 12.424406134879405, 10.110298928275993, 10.523721179392416, 12.272071857451907, 12.247071941611278, 10.249421713150362, 10.571276437666626, 10.262797525584276, 11.536972951118596, 11.57192224625575, 9.327644931670186, 8.65634492571402, 8.71596255934623, 9.10599314702398, 8.384811660316714, 8.44650988277943, 8.85338253446979, 8.309833853697278, 8.153444797011279, 8.213510383738681, 8.458436597012273, 8.743169985548427]],[[11.79932566688929, 12.540407527892558, 14.495354313668718, 12.70201803686418, 11.114674652229219, 9.801126884411936, 9.631852228695344, 10.653652264402826, 9.381675029574373, 9.06124688423497, 8.945593207696673, 8.868049344290705, 8.650060247912018, 8.448124162542731, 7.72949961306037, 7.979043810378034, 7.906983375372525, 8.264605714298026, 8.235593052074933, 8.600746478126132, 8.68157364697868, 8.432357861878929, 8.38674695658432, 8.553849378458464, 8.880908912961592, 8.662601806437992], [10.073273363663155, 13.78967592443841, 14.91161893841808, 12.585237538878216, 10.861879302942842, 8.638080594789876, 9.937856872976116, 10.643647365485757, 10.413763034399992, 9.088466263353787, 9.13140047627611, 8.836309764799417, 8.823465741942446, 8.005100044984856, 7.105597416466493, 7.952673718800668, 8.454879166582948, 8.709372703039092, 7.951227497911536, 8.320853357375897, 8.021994988264758, 8.118516754320266, 7.9563796401332185, 8.535100584186607, 8.99723695214834, 8.630443557423082]],[[12.092557194136207, 14.120236974572668, 14.827835711533737, 12.901786943861925, 11.196501611160311, 9.309206814777136, 10.152257287208203, 10.863331155757978, 9.045246659420172, 8.377257545795512, 8.223953944665725, 7.470840473511588, 7.801813983291069, 8.268822383889974, 6.937178831438787, 7.250172634231748, 7.818224958131472, 8.086292717698097, 8.123819193559008, 8.333280001514822, 8.215025414843412, 8.733040631062524, 9.058328956991843, 9.494441931918487, 9.655598791096503, 9.881259430658591], [13.15498976709768, 13.906304411347557, 14.550605018377798, 14.354705611825109, 12.387034795936131, 11.607729060422063, 11.950941794085695, 12.071974927758184, 10.87741707543021, 10.393186963358191, 10.589443437580744, 9.966035294114192, 9.848936943320295, 10.009377120680968, 9.475084294252078, 8.961675140665767, 8.834466063151792, 9.806903083441389, 9.382930405728988, 9.3351692284343, 9.488396513952715, 9.400092811761212, 9.66979398617856, 9.797914333068071, 9.75766373493154, 9.8573367927573]],[[12.146855204308387, 12.333330951685817, 13.915082715204747, 12.68781442970812, 11.185483090724912, 10.291178921301183, 10.044729755789955, 9.616193809492328, 9.28943840136261, 9.267252345838738, 8.877898032722154, 8.6320637817174, 9.006959241924458, 9.318022514340228, 8.251792986618762, 8.348749688235381, 8.205147177657777, 8.67545807334223, 8.971269234858447, 8.913086686828514, 8.934268876553277, 8.87887914050828, 9.138103959996865, 9.36497259605052, 9.337111107805242, 9.609212818256589], [11.190712297010673, 14.478166279168176, 15.401690260248214, 13.16466908176608, 11.118382691422418, 9.630765373653155, 10.499910002252452, 10.976803433366637, 9.393938958333985, 8.473335430843768, 8.810838517468179, 8.368336415661247, 9.508449577137764, 9.672189073711433, 8.644691972003816, 7.825432352385571, 8.427762850526602, 8.493412530935316, 8.470834803458736, 8.298024718446548, 8.746963603415553, 8.801955850673313, 8.825094256719732, 9.472128133360071, 9.308598750872145, 9.460270039824469]],[[11.021295163725856, 12.866072082231154, 14.251332964891633, 13.809471223194512, 10.797459839675728, 9.895097170624785, 9.825210934385895, 10.721661265149956, 10.51257540482129, 9.60538579233841, 8.833083227693393, 9.559663729256604, 8.754660243179378, 9.493368477989431, 9.164276365300383, 8.056517789076441, 7.899805512116316, 7.945717130108308, 7.902377055452735, 8.87512995711749, 8.789248411386595, 8.453145485483597, 8.633036794165765, 8.523416171624886, 8.82883708834761, 8.669539962113802], [12.846699160613419, 12.855319239848829, 14.703034932327048, 14.024385270580346, 9.852310175807563, 8.388243075200881, 8.959291239358764, 11.813963495275935, 11.183297025015815, 9.39470509041924, 9.319412643396733, 9.404265404886507, 8.293047041451645, 9.349388594616634, 8.426241141775858, 7.538713118249614, 8.417765003449718, 8.340531301878077, 7.90600257199404, 10.009167463279326, 10.070763591781398, 8.303455111842268, 8.25003907901426, 8.191403064928403, 8.55388481667114, 8.64305424451029]],[[10.913214617372903, 13.187792236571477, 14.285080618529614, 14.06986783368204, 11.073918293738343, 9.830742029072425, 10.324730373142247, 12.348863184046149, 12.366916613632343, 10.960078873658556, 11.957832277003241, 11.372931853047723, 8.005183115756353, 9.846513177064068, 8.781672063080517, 6.828791657549357, 7.785792412978606, 8.079657625373544, 7.552863484062169, 8.030837715236933, 7.487031790640491, 7.688277905327943, 8.023492621100532, 8.184598213112398, 8.659498358342328, 8.471226191527153], [12.63471180847289, 12.898350656410308, 14.804562745485022, 14.371076533910317, 10.822118597716285, 9.337911607512254, 9.46238380395354, 12.480573596309288, 12.752564366921723, 11.761598814727876, 12.41732811348525, 11.41991516521019, 8.559468136293448, 10.627047568096353, 9.021059815512636, 7.578673234900637, 9.061488247022375, 8.343547380103153, 7.210863162513631, 8.517467103467492, 8.215441769121218, 7.534690580055183, 7.875379979691834, 8.241176787866143, 8.536480748637764, 8.586240886389525]],[[12.627187128096455, 12.759432600539995, 14.168968075814702, 14.140345073624239, 10.236247595799984, 9.202388642934801, 8.89305744535444, 10.983030657691504, 11.790737683247448, 11.017016257618998, 11.455826184715765, 9.246819779730467, 7.50284265678585, 7.956353281253879, 7.709379764281865, 6.3243017492151905, 6.9741288950565945, 6.832692810809915, 7.251922699065398, 7.559384608560841, 7.364454028405031, 7.948778605759111, 7.832677032312866, 8.051913528297785, 8.148742128104528, 8.325907175255791], [11.597432061410576, 13.435200111390632, 14.616797878151601, 14.904523004115983, 11.667894504958298, 11.27800268795599, 11.13846734269669, 12.419687724149663, 12.84007401580659, 12.092259266737598, 12.684834643011822, 11.02151690038753, 8.968873970107692, 9.040043213101955, 8.847235204295286, 8.492351522036325, 8.270731917672212, 8.734130681672083, 8.096792025082609, 7.9567358711496965, 8.252563577491205, 8.295788088018673, 8.13587591535627, 8.147131769275328, 8.495860296832634, 8.526162514764614]],[[13.151913523806249, 12.668014514339532, 15.113066612859921, 14.31586974539518, 10.970966667524467, 9.966065351250608, 10.142471016167006, 12.628625219955918, 13.577340754275493, 11.404168599855408, 12.44846402167144, 11.461933844684593, 8.64830421864252, 10.071724607114747, 9.057927337197208, 8.011605924829633, 8.509703479485017, 8.56040036665087, 8.08900258147912, 8.679622865481756, 8.381698716423598, 8.098161090830905, 8.324671500246563, 8.525141038666217, 8.738796241361433, 8.850761920444219], [14.188411309719946, 12.326810920592715, 15.164356783335148, 14.046542561721578, 12.159925385068783, 10.905464889653214, 11.408010647457525, 13.46767864356056, 14.348339389040113, 11.7009656629386, 12.848127598686984, 11.534501425315053, 8.33053014458921, 9.072629245551617, 7.847896651281804, 7.893050984496978, 8.377387028770029, 8.3201652972908, 7.898275702380461, 8.832138743297525, 8.581833877309398, 7.994621182194677, 8.114232310008287, 8.392300024121305, 8.764223832340992, 8.85011064627981]],[[12.394583039350236, 13.446351894262932, 15.167024648102204, 14.371511046187075, 10.45910327237277, 8.212421292543048, 8.476060765060957, 12.365528846742961, 13.282226903521034, 11.584123679878502, 12.028847619858723, 9.360877127626473, 8.657786151735497, 9.471422399566656, 7.618144506396213, 6.666131717489331, 7.805454955925895, 7.786977913575888, 7.847683908695055, 8.274979865415995, 8.238634623684646, 8.353564834875387, 8.423836435640833, 8.61816735522814, 8.821349951929532, 8.615152526998866], [13.224258874435169, 13.084604760624304, 15.544974366962965, 14.68502377628981, 11.20763162114826, 10.158979856676122, 10.335055365435991, 13.15524248429038, 13.922578569359935, 10.892465450145444, 10.828001590280877, 8.37362845502852, 9.011475668802726, 9.259034478114216, 8.23314343402225, 7.740035211512739, 7.641887136604847, 7.581241255317547, 7.844037843108419, 7.960984744738451, 8.360953427972918, 8.464547694727306, 8.200694629579218, 8.652219464732802, 8.922387596877282, 8.785794905116838]],[[11.577509555055096, 13.10405546560257, 15.124691034248695, 13.547861457020971, 9.556467725888288, 7.020052830130049, 7.565106353927975, 9.99443857192241, 11.990400693974697, 11.41832151097993, 11.867806590951059, 8.995173169392507, 7.933546307573288, 9.719586233429073, 8.65877701230189, 8.387043198095602, 9.621650903324271, 9.1267543382506, 8.134354150416852, 8.449295752130766, 8.413104071493207, 8.34388199360043, 8.021204665076974, 8.330878413731671, 8.494645324908241, 8.554593768218684], [14.071263271127496, 10.853363131402896, 15.307566144779038, 12.797244149996216, 12.401933860343425, 10.33915377804097, 10.086013232067733, 11.832677822337807, 13.590465547206083, 12.393392490140547, 12.741107718037732, 9.957875097175616, 9.060672369523378, 9.685821224802776, 9.261864967554084, 9.250765614307666, 10.23545151883761, 9.083957094541756, 8.046329643480517, 9.047987178614875, 8.270842382331114, 8.044269488887473, 8.371490502392637, 8.606206016210374, 8.55810527557466, 8.680614507719877]],[[10.637513373330245, 11.109372632530118, 8.907849585038221, 7.2974333663593836, 7.071092601701154, 6.108058600974984, 6.387813297495464, 6.83683938437616, 7.020613320889404, 7.176944699509502, 6.881574882876024, 6.251110197142473, 7.053212518122165, 6.609513339806508, 6.88261870591924, 7.611730149991761, 7.779841133242843, 7.598102076428658, 8.347032537468442, 8.515331721482628, 8.511457859819915, 8.755841641129246, 9.207793449151323, 9.278435955318235, 9.26247381520839, 9.066461684521503], [10.696548434436725, 12.11082363363455, 12.136398481272131, 10.990223841685443, 7.764853798428077, 6.127061995721117, 6.3941324927449905, 8.627222500930095, 10.156178413010366, 9.949865597256846, 11.440546406752635, 10.449629077667279, 7.791675491805485, 7.944637005725087, 7.5748331547721275, 7.4376616844114505, 7.742372220990476, 7.891256400270253, 8.248526296512557, 8.752979700304481, 8.726902373394408, 8.905586088852077, 9.135780449828959, 9.139178987560296, 9.427838533544568, 9.354482319532165]],[[8.203443233687302, 12.955184519045305, 12.689587758381098, 12.100889302359795, 9.254822864909261, 7.0094852236484595, 6.536230351361547, 8.77902545712025, 10.912411196705621, 9.451877881156069, 8.911861398861722, 9.001292766908096, 6.544639915115037, 7.567308388720975, 7.969359717448797, 7.639769247060713, 7.000668050728307, 7.405183894915512, 7.336391596507094, 7.245389416196079, 8.262437580454309, 8.20612343032547, 8.056413228329063, 8.430147298875559, 8.450416668999981, 8.710153617039191], [11.346057928431051, 13.243583244423988, 13.349711616325056, 13.167973778210744, 10.879135745263842, 10.263617096232535, 9.871130303722827, 10.395889542429558, 11.399341351277698, 9.954646144207844, 9.96092875003031, 9.715385095561787, 7.190493660668184, 9.271249379449701, 8.616108470910433, 8.08007013381926, 8.914206333073553, 8.335001163650174, 8.204983912810915, 8.028883468028685, 8.267835713737917, 8.406881265192288, 8.708331660916562, 8.823123620059095, 8.892810528305723, 8.952819851045184]],[[9.257663307780684, 13.830105557300026, 13.98724479896967, 13.769861498491984, 10.693845104948089, 9.246288776100043, 9.713218126074167, 12.971424824947109, 13.799500052734068, 11.4825812447678, 13.36316016848632, 12.358685946570175, 10.39205361773844, 10.287902414875159, 10.133988324220395, 9.570242398108457, 9.470727112446463, 9.112131403362861, 9.175747096157487, 9.164044664896815, 8.963305764257827, 9.107167150341821, 8.765200718833109, 9.188352941734928, 9.146866941528828, 9.063653639424922], [12.15305501837083, 13.33182165702373, 15.019004404808491, 13.822295032787599, 10.715972061817611, 9.253432991066967, 9.234609625661108, 12.388007695798159, 13.298395996983368, 10.801180713315313, 12.417317590479986, 11.363648674057728, 9.231451322367079, 9.239618564310387, 8.885020354483904, 8.304913568780215, 8.454467844024203, 8.575580790540597, 8.242382970270958, 8.640212890843951, 8.259613831056555, 8.826897035743322, 8.631936111712868, 8.538421859247261, 8.942265734797648, 9.320921591270503]],[[11.709077502132608, 12.728216932909021, 14.828550072400418, 13.514827320950355, 9.636448352249316, 9.77304486831988, 10.043674796468393, 11.66964682658015, 11.933486610497342, 9.576365783377314, 11.422091922129365, 11.500512151726268, 8.943235579007093, 9.861486198348848, 8.79722861779686, 7.1771627530436275, 7.506658159868306, 7.1949047656058855, 7.632497939247811, 7.82963681599174, 7.608482344915761, 7.892758895355257, 8.275796004940105, 8.358671674212406, 8.629549980490232, 8.71155160973091], [12.293804684805, 13.027880077453059, 14.907530622364995, 13.501598237093067, 10.809613024947023, 8.96924914638489, 8.861339512840198, 10.744750710591678, 10.857574194337097, 8.866196342277417, 10.711072914688287, 9.83584948794279, 7.266277401611017, 8.557544086906598, 7.065926023645522, 7.277877850086497, 7.399133082272276, 7.561780593506858, 7.8531729996735375, 8.115601983587213, 8.301980372417129, 8.402998170069631, 8.24947770142952, 8.615510515327061, 8.535994206626436, 8.707019786534481]],[[11.986567054806207, 12.481609317444928, 15.018330018169792, 13.342206386702667, 11.266735113565513, 8.543533875296538, 11.156425465931857, 11.78184792905682, 9.408923866720773, 8.943863091042678, 11.006221679137544, 9.919106089226275, 9.964759105748199, 8.63344377489434, 7.466063450049549, 7.818908482029672, 9.112002562335231, 8.361996551877501, 7.8985533400155195, 8.40458518819726, 8.756449738602022, 9.057926421341953, 9.22815162852543, 9.162535282051035, 9.733202994855448, 9.576486424409092], [13.017580382797158, 10.505774903760365, 15.467196296788316, 13.994629578544874, 12.295380049399206, 11.500020721044796, 12.814682413807999, 12.405301247581304, 10.51227877962421, 10.093050978185415, 11.119570977670424, 10.204726395897113, 10.800779561003836, 9.457828486518427, 8.927681876203115, 9.068414014581366, 9.997155193555487, 9.240606796159534, 9.077494776399295, 8.993677335056654, 8.825297651351736, 8.908365211687155, 9.097864023561307, 9.462034436456037, 9.682537470951317, 10.05408142500233]],[[11.976501060862152, 12.591131586801884, 14.692702589146098, 11.953543452654937, 8.7373278930847, 8.688478711662354, 11.485430406265719, 11.333676708688666, 9.237960337637348, 9.501707608069248, 11.05700152541561, 9.43065289646998, 8.644523704864206, 7.876076704315992, 7.680890139766883, 7.894292190358373, 8.371560095440753, 8.516251388060928, 8.834437527401535, 8.798670178718691, 9.210637210372651, 9.59198904768071, 9.809479583122586, 10.220583996972756, 10.323693568116235, 10.164975061217769], [11.410774271461563, 14.391407310378165, 13.806984304909985, 12.292180051056539, 10.84689891932515, 9.481292179825163, 11.567444277822867, 11.87888678797729, 9.786339122683286, 8.829435135552455, 10.64531760746654, 8.593885617552408, 8.455384951913217, 8.218842756610757, 7.992715807892785, 7.573715925733623, 8.145924771470144, 8.440615254572421, 9.003743324234685, 9.023075680450727, 9.557180056561384, 9.350176085640788, 9.500151675529755, 10.095954655171175, 10.533437081502782, 10.52326587669481]],[[12.079454589242415, 11.957050852731816, 15.169890480834455, 10.126465738470205, 10.707992589298733, 9.39335881946074, 11.152737402034747, 10.546395177887302, 8.892995655455765, 7.662911805695332, 8.759148069658497, 8.110823624757204, 9.489233923883264, 9.10335757975599, 6.3574070930007744, 6.9047107028909664, 7.407479110851094, 6.906302691874481, 7.620548226658973, 7.560941113182007, 7.645084851227068, 7.9816051882598495, 8.447401037548453, 8.90704405700888, 9.142145825187828, 9.273382332826733], [12.333171150447223, 12.4971750035289, 15.900487089531739, 11.102706245225558, 12.453367722940417, 10.289086339560564, 10.824766655980127, 10.454539910650784, 9.895632713810162, 10.460413758812498, 10.710542591942449, 9.348742949011799, 10.376037477151048, 10.201983147988825, 9.284842924677578, 8.608778162027976, 8.520545860660572, 7.910677970510527, 7.948580585900412, 7.828718947223726, 8.069781626471174, 8.567665365919256, 8.81757864067404, 8.969069172240987, 9.335569544336211, 9.253791800671761]],[[11.92835605834499, 11.870280425431046, 10.953292464539286, 10.493804896403052, 10.308680729828414, 8.313768645658014, 7.978653422491731, 7.923817314320478, 8.270032769916435, 7.952727238518145, 10.141004956979573, 9.347867125910977, 7.030484378449776, 8.682332688415116, 8.181455019179593, 7.050433363335181, 7.669401580454367, 7.867464107094566, 8.226560068889485, 8.157919106350246, 8.727581334699812, 8.964462400682502, 9.216603409816706, 9.331709494652909, 9.669054916038622, 9.936982048075755], [9.10240028265291, 12.008475423073516, 11.334471598549992, 9.711956350441223, 9.825322319672244, 8.454833284742815, 7.39174564667827, 8.0299021235027, 8.705799760612905, 7.967219292947696, 10.528039415570525, 8.443382793567045, 6.967827495167761, 8.607056916694521, 7.875403376580569, 7.5804736921239435, 7.35336378294803, 7.868854342557661, 8.314942304200802, 8.569430558973101, 8.38758497441501, 8.570416662968434, 9.075700247698101, 9.176206557050305, 9.629690440442081, 10.006778398105656]],[[11.894983510521502, 13.116159929200533, 13.980426921097207, 13.138904263405456, 10.638877990650958, 9.2742041040652, 11.191332761782368, 11.482412317946713, 10.002937073892681, 9.198168897238148, 10.10677097536546, 8.2331032451674, 8.602374590250335, 8.15910260738954, 7.375914325193505, 7.538970144537744, 8.21286877266489, 8.21345139692796, 8.394089945474501, 7.930875217695074, 8.568759410573744, 8.818202697274385, 9.313115588475474, 9.714392717379555, 9.552193699008646, 9.709057967559728], [13.124031736946707, 12.610944628874467, 14.750792504376012, 14.154405324626113, 11.408839996121303, 10.147177430633533, 12.060891407680222, 12.681019324412501, 11.298799224581701, 10.429068932518781, 11.291688117595292, 9.30908817694566, 10.403733109270904, 9.48076065129952, 8.45442238435507, 8.136743923078713, 8.150884464799558, 8.567532063442563, 8.775136988646555, 8.701614071596342, 8.4039028211966, 8.922738377018419, 9.348019036138524, 9.352581135803842, 9.699340670536955, 10.028650507841107]],[[9.848586915576783, 11.248083557007325, 10.640230840600626, 8.568916351575446, 10.47525784413572, 9.476480872635225, 9.226234392278958, 9.755335725857359, 11.554803690085606, 11.153549652961795, 10.225341553477552, 8.973804297869005, 7.614905077720635, 8.16859827972677, 8.365887521697116, 9.077214497696595, 8.674975437493082, 8.426459702660203, 9.284110943105063, 9.236244377689836, 9.6645894036945, 9.782775936444015, 9.84150686735222, 10.019754827823585, 10.31706030870109, 10.231836968636859], [11.668863588410419, 11.97815000656401, 10.368237081179775, 8.909859755810013, 10.227764298361269, 9.108385204501632, 9.330783418481444, 9.818761787405787, 11.6498049711428, 11.717698230466024, 11.455553284007387, 9.580195903132163, 8.485040649344795, 7.906391105087843, 7.748762527193946, 9.004078683803517, 9.586175387797683, 8.901300508000729, 9.224574529051852, 9.39783478082586, 9.47622214283574, 9.73327674564442, 9.871530894756331, 10.063632389821986, 10.198676170028858, 10.267474890635832]],[[9.837081854942538, 8.332243407212998, 9.280446849649064, 8.69573339541742, 8.546449491926055, 8.399723071499269, 7.885783446801796, 7.4409556547144735, 8.530769130539033, 7.999194940079293, 8.25609369817409, 7.023575155422889, 7.407171027832994, 7.223426755682492, 7.613904764913468, 7.965713671161221, 9.031390251054455, 8.629281543314978, 9.732818302496842, 9.323789081886275, 9.53839204601329, 10.058718803266652, 9.950673731431998, 10.214421553325506, 10.326335424409633, 10.632634881311672], [8.068743047700073, 9.567904623074208, 10.250040710003004, 9.55631893317417, 8.965718501736355, 8.447958040933633, 7.595223620990699, 7.8945468895832125, 8.175088319316483, 8.573294451737484, 7.822052720795292, 6.996197655306681, 7.245256438696255, 7.707654494897842, 8.173336011608223, 8.652752083512777, 8.777093954163632, 8.576329393090724, 9.251937781233567, 8.944427776917658, 9.409212859984141, 9.737944401208278, 9.904850948926486, 10.40129354286525, 10.282850824029806, 10.586970332385796]],[[10.598519604009827, 12.631939122180867, 12.900765119324532, 13.98852257225502, 11.780360144206252, 10.930699202134372, 9.67091215882234, 9.619598221520262, 10.28383409788612, 14.173066900727061, 14.201085992101936, 12.385108333138138, 8.982105826466217, 9.625087937531196, 8.33949567226151, 7.1428615681503596, 7.417940512660719, 7.680225645735574, 8.022560764383396, 7.987601331628094, 8.322730873548172, 8.358937026339719, 8.605634555125292, 9.253872027232369, 9.040490790673422, 9.333092203484032], [9.029982366350707, 12.295881752681971, 12.597888905818106, 12.885599930762865, 10.427995198836738, 9.227989092741327, 7.921659673584149, 8.329141496869878, 9.3483991506168, 13.391464995227162, 13.809471323546415, 12.41457747417732, 10.173940896716191, 9.826090704560682, 9.107884905985303, 8.667943313055188, 8.668710252192728, 8.398443832099566, 8.574864625179643, 8.50676570271886, 8.667810205247395, 9.000155258258786, 8.95036251051093, 8.883505531432071, 9.269983272889675, 9.818116696572044]],[[12.90209927840129, 13.438703026718597, 13.883003791301642, 13.097652067931682, 8.189304325549976, 7.075532364891911, 8.582681729398816, 12.033084801274335, 12.911292463965129, 12.64182892491901, 13.699627050205649, 9.937371521874653, 9.590303525559909, 11.568562578072516, 9.752449991958583, 7.845740639801595, 8.666065310246763, 7.829120327112182, 7.384557308970136, 7.903189366089819, 7.844839286995406, 7.904156623995805, 8.427665619620262, 8.316649313981053, 8.256191360840303, 8.71151848285921], [14.15583092140273, 11.813453089817585, 14.554890872712893, 12.804722409325889, 11.697038896059363, 11.085452994669124, 10.931353118800288, 12.51887982683674, 13.427732308592534, 12.610575825269576, 13.414074690260337, 9.747397588830736, 9.723081562145625, 11.102653309378898, 10.014501466726536, 8.851091311440301, 8.97910902196609, 8.545947187451853, 8.52761391314278, 8.904707666857826, 8.74257526992265, 8.38591368834638, 8.088578346491508, 8.521879714422726, 8.84997466571081, 9.098970302339]],[[11.07339042060802, 7.548116041195823, 11.7864520188315, 12.345946008886242, 12.554173870036971, 9.328670667175874, 7.745408134678638, 8.74505687423244, 9.760694804955579, 10.463903030872736, 11.684250905515238, 9.665157456066508, 7.6078987018587645, 7.0814707742803344, 7.340482029661511, 7.025701968817928, 6.855743609820836, 6.8012271670737725, 6.6654895135082, 6.658506386194146, 6.961471181329022, 7.428944529666017, 7.21425937413799, 7.696127032152318, 7.990585702965649, 8.247615297022971], [10.117722454977425, 9.836349138402024, 12.188162279195623, 12.190586501470918, 13.630086526067497, 10.577624772297314, 9.142669307993733, 8.809227324781169, 10.106736547646097, 10.985951799344242, 11.051177308885654, 10.553775959867762, 9.327417691908328, 8.689870197794994, 8.243599769676708, 7.465471864026783, 7.345490613343414, 7.290180001801053, 7.766207313239692, 7.50826716706827, 7.474956455439918, 7.378769627704582, 7.6689913466827075, 7.972109900228953, 8.325681026394411, 8.17923606300609]]