import numpy as np 
import matplotlib.pyplot as plt
import os 


from scipy.optimize import curve_fit
from scipy.stats import norm




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


path = os.getcwd() 
ss_front_h = 'ss_front_horizontal.csv'
ss_front_v = 'ss_front_vertical.csv'
ss_back_h = 'ss_back_horizontal.csv'
ss_back_v = 'ss_back_vertical.csv'


def Gauss(x, mu, sigma, A, B):

	#return   (  (1/(sigma*np.sqrt(2*np.pi))) * (np.exp(-0.5*((x-mu)**2/sigma**2) )  +A)  ) 
	return   (  A+ (B/(sigma*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mu)**2/sigma**2) ) ) 

def read_csv(filename):
	x  = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0])
	y  = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[1])
	#x = x.tolist(); y=y.tolist()
	#print(x)
	
	#idx   = np.argsort(x)
	#x = x[idx]; y = y[idx]






	#fwhm_ = fwhm(x,y, k=2)
	#print(fwhm_)

	#y_pred =  gpr.predict(x_new)
	#print(y_pred)
	x_new = np.linspace(0, max(x), len(x))
	
	#mu = 3; sigma=0.01; A=3000
	mu = 3; sigma=0.01; A=100; B=120
	#(mu,sigma)=norm.fit(x)
	A=120
	print(mu, sigma)

	popt, pcov=curve_fit(Gauss, x,y , p0=np.array([mu, sigma,A, B]), absolute_sigma=True)


	#print(popt)

	hmx = popt[2] + popt[3]/2

	#half_fwhm = fwhm/2 
	fwhm = 2.35*popt[1]
	one_half = popt[0] - fwhm/2
	two_half = popt[0] + fwhm/2

	print(one_half, two_half, popt[0])
	print(hmx)
	#plt.axvline(two_half)
	#plt.axvline(one_half)

	fig, ax = plt.subplots()

	ax.plot(x,y, '.', label='data')

	ax.axhline(y=hmx, xmin=one_half, xmax=two_half, color='r')
	#plt.axhline(hmx)#, xmin=one_half, xmax=two_half)


	
	print("fwhm: ", fwhm)
	#plt.plot(x,y, '.', label='data')
	#plt.axvline(popt[0], linestyle='-.', linewidth=0.3, label=r'$\mu$')
	#plt.axhline(hmx)


	gauss_fit = Gauss(x, popt[0], popt[1], popt[2], popt[3])
	ax.plot(x, gauss_fit, label='Fit')
	#plt.plot(x_new, Gauss(x_new, popt[0], popt[1], popt[2]))


	#y_new = Gauss(x_new, 3, 0.25, 120)


	


	



	#x_new, y_new = interpolation(x,y)
	#plt.plot(x_new, y_new, '--')
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