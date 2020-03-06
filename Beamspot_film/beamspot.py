import numpy as np 
import matplotlib.pyplot as plt
import os 
from scipy.optimize import curve_fit, minimize_scalar
from scipy import asarray as ar,exp
from scipy.stats import norm


from scipy.interpolate import interp1d, UnivariateSpline


path = os.getcwd() 
ss_front_h = 'ss_front_horizontal.csv'
ss_front_v = 'ss_front_vertical.csv'
ss_back_h = 'ss_back_horizontal.csv'
ss_back_v = 'ss_back_vertical.csv'


def read_csv(filename):
	x  = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0])
	y  = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[1])
	x = x.tolist(); y=y.tolist()

	from scipy.signal import chirp, find_peaks, peak_widths

	peaks, _ = find_peaks(y)
	results_half = peak_widths(y, peaks, rel_height=1)

	print(results_half[0])

	#plt.plot(y)
	#print(type(peaks[0]))
	plt.plot(y[peaks[20]], label='test')
	#plt.plot(peaks, y[peaks[0]], "y")
	plt.legend()
	plt.show()
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