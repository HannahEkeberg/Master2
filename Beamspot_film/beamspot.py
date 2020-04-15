import numpy as np 
import matplotlib.pyplot as plt
import os 

from sklearn.gaussian_process import GaussianProcessRegressor 



#from scipy.interpolate import UnivariateSpline
from scipy import interpolate

def interpolation(x,y):	
	#print(x)
	#plt.plot(x,y, label='data')


	x_new = np.linspace(0, 6.25, 1000)
	#spl = UnivariateSpline(x,y)
	#spl.set_smoothing_factor(10)
	#plt.plot(x_new, spl(x_new), 'g', lw=3, label='spline')
	#lt.legend()
	#plt.show()
	
	tck = interpolate.splrep(x, y, s=0)
	y_new = interpolate.splev(x_new, tck, der=0)

	return x_new, y_new


def fwhm(x, y, k=10):
    """
    Determine full-with-half-maximum of a peaked set of points, x and y.

    Assumes that there is only one peak present in the datasset.  The function
    uses a spline interpolation of order k.
    """
    from scipy.interpolate import splrep, sproot, splev
    half_max = np.amax(y)/2.0
    print(half_max)
    s = splrep(x, y - half_max, k=k)
    roots = sproot(s)

    if len(roots) > 2:
        raise MultiplePeaks("The dataset appears to have multiple peaks, and "
                "thus the FWHM can't be determined.")
    elif len(roots) < 2:
        raise NoPeaksFound("No proper peaks were found in the data set; likely "
                "the dataset is flat (e.g. all zeros).")
    else:
        return abs(roots[1] - roots[0])

path = os.getcwd() 
ss_front_h = 'ss_front_horizontal.csv'
ss_front_v = 'ss_front_vertical.csv'
ss_back_h = 'ss_back_horizontal.csv'
ss_back_v = 'ss_back_vertical.csv'


def read_csv(filename):
	x  = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0])
	y  = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[1])
	x = x.tolist(); y=y.tolist()


	fwhm_ = fwhm(x,y, k=2)
	print(fwhm_)

	y_pred =  gpr.predict(x_new)
	#print(y_pred)

	plt.plot(x,y, '.', label='data')
	

	



	x_new, y_new = interpolation(x,y)
	plt.plot(x_new, y_new, '--')
	plt.legend()
	plt.show()



	#from scipy.signal import chirp, find_peaks, peak_widths

	#peaks, _ = find_peaks(y)
	#results_half = peak_widths(y, peaks, rel_height=1)

	#print(results_half[0])

	#plt.plot(y)
	#print(type(peaks[0]))
	#plt.plot(y[peaks[20]], label='test')
	#plt.plot(peaks, y[peaks[0]], "y")

	#plt.plot(x,y)
	#plt.plot(x_new, y_new)
	#plt.legend()
	#plt.show()
	#print(type(results_half))
	"""
	index = y.index(np.max(y))
	#print(index)


	(mu,sigma)=norm.fit(x)
	#print(y[index])
	#print(y[index]-sigma)

	def gaus(x,a,x0, sigma):
		return a*exp(-(x-x0)**2/(2*sigma**2))

	plt.axvline(x[index])
	plt.axvline(x[index]-0.5*sigma)
	
	popt, pcov = curve_fit(gaus, x,y,p0=[1,mu,sigma])
	print(popt)
	plt.plot(x,y,'b+:',label='data')
	plt.plot(x,gaus(x,*popt),'ro:',label='fit')
	plt.legend()
	plt.title('Fig. 3 - Fit for Time Constant')
	plt.xlabel('Time (s)')
	plt.ylabel('Voltage (V)')
	#plt.show()
	"""



	





read_csv(ss_front_h)