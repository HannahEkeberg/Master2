import numpy as np, matplotlib.pyplot as plt
from scipy import interpolate
from scipy.optimize import curve_fit


#import fme, os
import os


from foil_info_new import *

m=60; h=m*60; d=h*24; y=d*356  #converters to seconds


dir_fig = 'activity_feb19_curves'
dir_csv = 'activity_feb19_csv'
if not os.path.exists(dir_fig):
    os.mkdir(dir_fig)
if not os.path.exists(dir_csv):
    os.mkdir(dir_csv)

path = os.getcwd() + '/../matlab/csv_backup_feb20/'
filename = path + '62Zn_129.dat'
lamb = np.log(2.)/(9.193*h)

class Decay:

    def __init__(self, file, lamb, A0_guess):

        self.file=file
        self.time = np.genfromtxt(self.file, delimiter=',', usecols=[0]) #hours since e.o.b
        self.A = np.genfromtxt(self.file, delimiter=',', usecols=[1])
        self.sigma_A = np.genfromtxt(self.file, delimiter=',', usecols=[2])

        self.lamb = lamb
        self.A0_guess = A0_guess


        self.name = file[-13:-4]
        if self.name[0]=='/':
            #print(self.name[1:])
            self.name = self.name[1:]

        #print(self.A0_guess)
    def decay_type(self, t, A0_guess):  ### Not using anymore
        #print(A0_guess)
        #A0_guess= self.A0_guess
        if isinstance(A0_guess, list):  # if more than one value of A0 was provided, then two step
            #print("two step: ", A0_guess)
            #print(A0_guess)

            A_est = A0_guess[0]*self.lamb[1] / (self.lamb[0]-self.lamb[1]) *( np.exp(-self.lamb[1]*t)-np.exp(-self.lamb[0]*t)) + A0_guess[1]*np.exp(-self.lamb[1] *t)
            #print(p0)
        else:
            #print("single: ", A0_guess)
            A_est = A0_guess*np.exp(-self.lamb*t)
            #print(p0)

        return A_est


    def single(self, t, A0_guess):
        A_est = A0_guess*np.exp(-self.lamb*t)
        return A_est

    def twostep_up(self, t, A0_parent, A0_daughter):
        A_est = A0_parent*self.lamb[1] / (self.lamb[0]-self.lamb[1]) *( np.exp(-self.lamb[1]*t)-np.exp(-self.lamb[0]*t)) + A0_daughter*np.exp(-self.lamb[1] *t)
        return A_est

    def twostep_kp(self, t, A0_daughter):
        A0_parent = self.A0_guess[0]
        A_est = A0_parent*self.lamb[1] / (self.lamb[0]-self.lamb[1]) *( np.exp(-self.lamb[1]*t)-np.exp(-self.lamb[0]*t)) + A0_daughter*np.exp(-self.lamb[1] *t)
        return A_est

    def npat_twostep(self):
        pass


    def uncertainties(self, t, cov=False):

        deriv_Ad_Ap = self.lamb[1]/(self.lamb[0]-self.lamb[1])*(np.exp(-self.lamb[1]*t)-np.exp(-self.lamb[0]*t))
        deriv_Ad_Ad = np.exp(-self.lamb[0]*t)
        J = np.array((deriv_Ad_Ap, deriv_Ad_Ad)) #Jacobian

        dA0_dt = np.sqrt( np.dot(np.dot(J,pcov),J.T ) )
        return dA0_dt
        #else:
        #    dA0 = np.sqrt(np.diagonal(pcov))   #Uncertainty in the fitting parameters
            #sigma_activity_estimated = np.sqrt(np.diagonal(pcov))   #Uncertainty in the fitting parameters
            #return dA0

    def make_fit(self, known_parent=False, cov=False, plotfig=True):

        index = ~(np.isnan(self.A) | np.isnan(self.sigma_A))  #if either eps OR sigma eps is NaN
        t = np.max(self.time[index])
        xplot = np.linspace(0,t,1000)
        lamb = self.lamb
        t=self.time[index]

        if isinstance(self.A0_guess, list):
            if known_parent:
                #A0_parent = self.A0_guess[0]
                #print("known parent")
                popt, pcov = curve_fit(self.twostep_kp, self.time[index]*3600, self.A[index], p0=self.A0_guess[1], sigma=self.sigma_A[index], absolute_sigma=True)
                sigma_activity_estimated = np.sqrt(np.diagonal(pcov))   #Uncertainty in the fitting parameters
                self.plot_curve(self.twostep_kp, xplot, popt, index, sigma_activity_estimated )
            else:
                popt, pcov = curve_fit(self.twostep_up, self.time[index]*3600, self.A[index], p0=np.array((self.A0_guess[0], self.A0_guess[1])), sigma=self.sigma_A[index], absolute_sigma=True)
                sigma_activity_estimated = self.uncertainties(t)
                self.plot_curve(self.twostep_up, xplot, popt, index, sigma_activity_estimated )

        else:
            p0_input=self.A0_guess
            #print("single")
            popt, pcov = curve_fit(self.single, self.time[index]*3600, self.A[index], p0=np.array((self.A0_guess)), sigma=self.sigma_A[index], absolute_sigma=True)
            sigma_activity_estimated = np.sqrt(np.diagonal(pcov))   #Uncertainty in the fitting parameters
            if plotfig:
                self.plot_curve(self.single, xplot, popt, index, sigma_activity_estimated )


        return popt, sigma_activity_estimated

    def plot_curve(self, decay_func, xplot, popt, index, sigma_activity_estimated):
        #print(popt)
        plt.plot(xplot, decay_func(xplot*3600, *popt), 'r-', label='Fit')
        plt.plot(xplot, decay_func(xplot*3600,*(popt+sigma_activity_estimated)), color='blue', linewidth=0.4, label='uncertainty band')
        plt.plot(xplot, decay_func(xplot*3600,*(popt-sigma_activity_estimated)), color='blue', linewidth=0.4)
        plt.fill_between(xplot, decay_func(xplot*3600,*(popt+sigma_activity_estimated)),decay_func(xplot*3600,*(popt-sigma_activity_estimated)), color='blue', alpha=0.1)

        plt.plot(self.time[index],self.A[index], '.')
        plt.errorbar(self.time[index], self.A[index], color='green', linewidth=0.001,yerr=self.sigma_A[index], elinewidth=0.5, ecolor='k', capthick=0.5)   # cap thickness for error bar color='blue')
        plt.xlabel('time since eob, hours')
        plt.ylabel('Activity, Bq')
        plt.legend()
        plt.title('Activity curve for ' + self.name)
        plt.show()


class Activity:

    def __init__(self, foil_func, A0_guess, foilnumb='all'):

        self.foil = foil_func
        self.list = foil_func[0]
        self.lamb = foil_func[-1]
        self.A0_guess = A0_guess
        self.foilnumb = foilnumb


    def get_vals(self):
        if self.foilnumb=='all':
            for f in self.list:
                dec = Decay(f, self.lamb, self.A0_guess)
                dec.make_fit()

        elif isinstance(self.foilnumb, int):
            dec = Decay(self.list[self.foilnumb], self.lamb, self.A0_guess)
            #popt, pcov = dec.make_fit()
            #print(popt)

    def write_csvfile(self, A0, reaction):
        save_results_to = os.getcwd()+'/activity_csv/'
        if isinstance(A0, list):


        #print(type(A0_daughter),len(A0_daughter),type(sigma_A0_daughter), len(sigma_A0_daughter) )
        #print(save_results_to+reaction_parent)
        #np.savetxt("{}.csv".format(save_results_to + reaction_parent), np.array((A0_parent, sigma_A0_parent)), delimiter=",")
        #np.savetxt("{}.csv".format(save_results_to + reaction_daughter), np.array((A0_daughter, sigma_A0_daughter)), delimiter=",")

    def singledecay_activity(self, reaction):
        pass


    def unknownparent_activiy(self, reaction):
        pass


    def knownparent_activity(self, parent_func):  #for 56Co
        #print("test")
        list_parent = parent_func[0]
        lamb_parent = parent_func[-1]
        #print(lamb_parent)

        parent_activity = []
        if isinstance(self.foilnumb, int):
            dec_p = Decay(list_parent[self.foilnumb], lamb_parent, self.A0_guess[0])
            A0_p, dA0_p = dec_p.make_fit()
            print("single parent: ", popt_p)
            A0_guess_new = [A0_p[0], self.A0_guess[-1]]

            dec_d = Decay(self.list[self.foilnumb], self.lamb, A0_guess_new)
            A0, sigma_activity_estimated = dec_d.make_fit(known_parent=True)
            print("Double daughter: ", popt_d)
        else:
            print("only single for this atm. Please give a integer")

        return A0, sigma_activity_estimated

        #elif isinstance(self.foilnumb, int):
            #for i in list_parent:
                #dec = Decay(list_parent[i], lamb_parent, self.A0_guess[0])
                #popt, pcov = dec.make_fit()
                #print(popt)
                #parent_activity.append(popt)



            #dec = Decay()
            #print(lamb_parent)
            #print(self.lamb)











#func = Ni_56Co(); A0=[8000, 1000]
#func=Cu_62Zn(); A0=40000
#Activ = Activity(func, A0)




"""
class Activity:

    def __init__(self, file, lamb):


        #print(react_func[0])
        #print(react_func[1])
        #print(react_func)

        self.file = file
        self.time = np.genfromtxt(self.file, delimiter=',', usecols=[0]) #hours since e.o.b
        self.A = np.genfromtxt(self.file, delimiter=',', usecols=[1])
        self.sigma_A = np.genfromtxt(self.file, delimiter=',', usecols=[2])
        self.lamb = lamb

        self.name = file[-13:-4]
        if self.name[0]=='/':
            #print(self.name[1:])
            self.name = self.name[1:]

        #D = Decay(self.time, self.A, self.lamb, )



        #print(self.A.shape)

        #index = ~(np.isnan(A) | np.isnan(sigma_A))  #if either eps OR sigma eps is NaN
        #t = np.max(time[index])
        #xplot = np.linspace(0,t,1000)

    def single_decay(self, time, A0_guess):

        A_est=A0_guess*np.exp(-self.lamb*time)
        return A_est

    def twostep_decay(self, A0_parent, A0_daughter, lamb_parent, lamb_daughter): #Provide A0 parent (or guess if no observed gammas), and A0 daughter guess
        A_est = A0_parent*lamb_daughter / (lambda_parent-lamb_daughter) *( np.exp(-lamb_daughter*self.time)-np.exp(-lamb_parent*self.time)) + A0_daughter*np.exp(-lamb_daughter *self.time)
        return A_est


    def make_fit(self, decay_func):

        if isinstance(A0_guess, list):
            print(ok)

    def return_A0(self):
        t=np.linspace(0,10,10)
        A0 = self.make_fit(self.single_decay(t, A0_guess[0]), 8000)
        print(A0)


    def make_fit_singledecay(self, A0_guess):
        index = ~(np.isnan(self.A) | np.isnan(self.sigma_A))  #if either eps OR sigma eps is NaN
        t = np.max(self.time[index])
        xplot = np.linspace(0,t,1000)
        lamb = np.log(2.)/(9.193*h)
        #A_est = self.single_decay(2000, lamb)

        popt, pcov=curve_fit(self.single_decay, self.time[index]*3600, self.A[index], p0=A0_guess, sigma=self.sigma_A[index], absolute_sigma=True)
        A0_est = self.single_decay(0, popt)
        sigma_A0_est = np.sqrt(np.diagonal(pcov)) #uncertainty in fitting parameters
        self.plot_curve_singledecay(xplot, popt, index, sigma_A0_est)

    def plot_curve_singledecay(self, xplot, popt, index, sigma_activity_estimated):
        plt.plot(xplot,self.single_decay(xplot*3600,*popt),'r-', color='red', label='Fit')
        plt.plot(xplot,self.single_decay(xplot*3600,*(popt+sigma_activity_estimated)), color='blue', linewidth=0.4)
        plt.plot(xplot,self.single_decay(xplot*3600,*(popt-sigma_activity_estimated)), color='blue', linewidth=0.4)
        plt.plot(self.time[index],self.A[index], '.')
        plt.errorbar(self.time[index], self.A[index], color='green', linewidth=0.001,yerr=self.sigma_A[index], elinewidth=0.5, ecolor='k', capthick=0.5)   # cap thickness for error bar color='blue')
        plt.xlabel('time since eob, hours')
        plt.ylabel('Activity, Bq')
        plt.legend()
        plt.title('Activity curve for ' + self.name)
        plt.show()
    """



#Act = Activity(filename, lamb =(np.log(2.)/(9.193*h)))
#Act.make_fit_singledecay(2000)
#Act.return_A0([8800,579])

#A_est = A.single_decay(7000, lamb)
#print(A_est)
