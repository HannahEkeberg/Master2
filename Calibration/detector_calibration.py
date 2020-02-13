import npat
# from npat import Spectrum, Calibration
import scipy.io
import numpy as np

import os
path = os.getcwd()
cb_sp = npat.Spectrum(path +'/room131/text_Spe/BN20190205_Ba133_60cm_room131.Spe')
# cb_sp.plot()

cb_sp.meta = {'istp':['133BA'],#, '133BA', '137CS', '60CO'],
				'A0':[39.89E3],#, 38.59E3, 36.7E3, 38.52E3],
				'ref_date':'01/01/2009 12:00:00'}

cb_sp2 = npat.Spectrum(path +'/room131/text_Spe/BO20190206_Eu152_60cm_room131.Spe')
# cb_sp.plot()

cb_sp2.meta = {'istp':['152EU'],#, '133BA', '137CS', '60CO'],
				'A0':[39.29E3],#, 38.59E3, 36.7E3, 38.52E3],
				'ref_date':'01/01/2009 12:00:00'}

cb_sp3 = npat.Spectrum(path +'/room131/text_Spe/BM20190206_Cs137_60cm_room131.Spe')
# cb_sp.plot()

cb_sp3.meta = {'istp':['137CS'],#, '133BA', '137CS', '60CO'],
				'A0':[38.55E3],#, 38.59E3, 36.7E3, 38.52E3],
				'ref_date':'01/01/2009 12:00:00'}


cb_sp.fit_config = {'xrays':True, 'E_min':55.0, 'bg_fit':True}
# cb_sp.auto_calibrate()
# cb_sp.summarize()

### Plot ADC channels instead of energy
# cb_sp.plot(xcalib=False)

### Pick out a few peaks for manual calibration
# cb_data = [[1890, 356.0]]#,
                        # [1338.5, 244.7],
                        # [1882.5, 344.3],
                        # [2428, 444],
                        # [7698, 1408]]
cb_sp3.fit_config = {'xrays':True, 'E_min':55.0, 'bg_fit':True}
cb_sp2.fit_config = {'xrays':True, 'E_min':55.0, 'bg_fit':True, 'I_min':0.1}  # I_min: for X-ray fitting

# cb_sp.auto_calibrate(data=cb_data)


# cb_sp2.plot()

cb = npat.Calibration()
# cb_sp.cb = cb
# cb_sp.cb.plot()



sp = npat.Spectrum(path +'/room131/text_Spe/BN20190205_Ba133_60cm_room131.Spe')
# sp.meta = {'istp':['58CO','40K','210BI','212BI','210PB','212PB','226RA']}
sp.meta = {'istp':['133BA']}

prev_calib = list(sp.cb.engcal)
sp.fit_config = {'xrays':True,'E_min':55.0, 'bg_fit':True}
# , 'bg_fit':True}
#
# cb = npat.Calibration()
cb.calibrate([cb_sp, cb_sp3, cb_sp2,sp])
sp.auto_calibrate()
exp_engcal = list(sp.cb.engcal)
cb.plot()
#
sp.summarize()
sp.plot()




print(sp.cb.eff(120.0))
print(sp.cb.unc_eff(120.0))

print("Functional efficiency parameters:")
print(sp.cb.effcal)

print("Functional efficiency covariance matrix:")
print(sp.cb.unc_effcal)

#scipy.io.savemat('eff_IDM3_40.mat', {'popt_IDM3_40': sp.cb.effcal,'pcov_IDM3_40': sp.cb.unc_effcal})
scipy.io.savemat('eff_room131_60.mat', {'popt_room131_60': sp.cb.effcal,'pcov_room131_60': sp.cb.unc_effcal})
