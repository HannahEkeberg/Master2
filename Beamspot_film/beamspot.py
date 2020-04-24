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


Zn_16MeV_front = '16MeV_Zn_front.csv'


def Gauss(x, mu, sigma, A, B):

	#return   (  (1/(sigma*np.sqrt(2*np.pi))) * (np.exp(-0.5*((x-mu)**2/sigma**2) )  +A)  ) 
	return   (  A+ (B/(sigma*np.sqrt(2*np.pi))) * np.exp(-0.5*((x-mu)**2/sigma**2) ) ) 

def lin_interp(x,y,i,half): 
	return x[i] + (x[i+1] - x[i]) * ((half - y[i]) / (y[i+1] - y[i]))


def half_max(x,y, popt):
	#print(popt) 
	half = (np.max(y)-popt[2])/2 + popt[2]    # 0.5*(max value - background) + background

	#print(half)
	signs = np.sign(np.add(y, -half))  #try using B instead of y?
	zero_crossings = (signs[0:-2] != signs[1:-1])
	zero_crossings_i = np.where(zero_crossings)[0]

	#print(zero_crossings_i)

	return [lin_interp(x, y, zero_crossings_i[0], half),
                       lin_interp(x, y, zero_crossings_i[1], half)]





def read_csv(filename, title, save_title, mu=3, sigma=0.01, A=100, B=120):
	x  = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[0])
	y  = np.loadtxt(filename, delimiter=',', skiprows=1, usecols=[1])
	#print(x)
	#plt.plot(x,y)
	#plt.show()

	x_new = np.linspace(0, max(x), len(x))

	fig, ax = plt.subplots()
	
	ax.plot(x,y, '.', label='data')

	
	#mu = 3; sigma=0.01; A=3000
	#mu = 3; sigma=0.01; A=100; B=120
	#(mu,sigma)=norm.fit(x)
	#A=120; B= 200
	#print(mu, sigma)


	popt, pcov=curve_fit(Gauss, x,y , p0=np.array([mu, sigma,A, B]), absolute_sigma=True)
	gauss_fit = Gauss(x, popt[0], popt[1], popt[2], popt[3])
	
	#half = (popt[3]-popt[2])/2
	#signs = np.sign(np.add(gauss_fit, -half))
	#print(len(gauss_fit))
	#print(len(x))
	
	hmx = half_max(x_new, gauss_fit, popt) 
	half = (np.max(gauss_fit)-popt[2])/2 + popt[2]
	
	fwhm = hmx[1]-hmx[0]
	fwhm_estimated = 2.35*popt[1]

	print("fwhm: ", fwhm)
	print("fwhm estimated: ", fwhm_estimated)
	print("mu: ", popt[0])
	print("sigma: ", popt[1])
	print("sigma^2: ", popt[1]**2)
	print("A: ", popt[2])
	print("B: ", popt[3])
	

	
	#ax.plot(x, gauss_fit, label='Fit')
	#plt.plot(hmx, [half, half], label='FWHM: {:.2f} cm'.format(fwhm))


	#plt.title(title)
	#plt.xlabel('Distance (cm)')
	#plt.ylabel('Distance (cm)')
	#plt.legend()
	#plt.savefig(save_title, dpi=300)
	#plt.show()




read_csv(Zn_16MeV_front, title='Horizontal beamprofile - front stack', save_title='ss_front_h.png')


#read_csv(ss_front_h, title='Horizontal beamprofile - front stack', save_title='ss_front_h.png')
#print("**")
#read_csv(ss_back_h, title='Horizontal beamprofile - back stack', save_title='ss_back_h.png')
#print("**")
#read_csv(ss_front_v, title='Vertical beamprofile - front stack', save_title='ss_front_v.png')
#print("**")
#read_csv(ss_back_v, title='Vertical beamprofile - back stack', save_title='ss_back_v.png', mu=2, sigma=0.01, A=120, B=130)





#