import numpy as np, matplotlib.pyplot as plt
from scipy import interpolate
from scipy.optimize import curve_fit

#import fme, os
import os
from npat import DecayChain
import csv

from foil_info import *

m=60; h=m*60; d=h*24; y=d*356  #converters to seconds

"""
NOTES ON PROGRAM
If driving single decay, activate plot in function, and assign reaction function in end of program.
If driving two step with known parent activity, turn of plot in single decay function. Assign parent reaction and daughter reaction.
If driving two step with unknown parent activity, assign reaction function in end  of program.

All info should be in reaction functions, ie Cu_62Zn, however, guesses are assigned in decay functions. Might need to be changed for some reactions?
"""
dir_fig = 'activity_curves'
dir_csv = 'activity_csv'
if not os.path.exists(dir_fig):
    os.mkdir(dir_fig)
if not os.path.exists(dir_csv):
    os.mkdir(dir_csv)


####FUNCTIONS

def A0_single_decay(filename_activity_time, lambda_, makePlot=False):
    #ID = filename_activity_time[-8:-4]
    #Nucleus = filename_activity_time[-12:-8]
   

    #name = filename_activity_time[-13:-4]
    name = filename_activity_time[-14:-4]  #change back to above only for nice plotting of 193mPt

    #print(name)

    #print(filename_activity_time)
   # with open(filename_activity_time) as f:
        #  print(f.readlines())
    #print("****", name)
    #print('foil{}_{}'.format(ID, Nucleus))
    time = np.genfromtxt(filename_activity_time, delimiter=',', usecols=[0]) #hours since e.o.b
    A = np.genfromtxt(filename_activity_time, delimiter=',', usecols=[1])
    sigma_A = np.genfromtxt(filename_activity_time, delimiter=',', usecols=[2])

    index = ~(np.isnan(A) | np.isnan(sigma_A))  #if either eps OR sigma eps is NaN

    t = np.max(time[index])

    xplot = np.linspace(0,t,1000)

    A0_guess=600
    #Single decay mode
    def direct_decay(time, A0_guess):
        A_est=A0_guess*np.exp(-lambda_*time)
        return A_est

    popt, pcov=curve_fit(direct_decay, time[index]*3600, A[index], p0=A0_guess, sigma=sigma_A[index], absolute_sigma=True)
    sigma_activity_estimated = np.sqrt(np.diagonal(pcov))   #Uncertainty in the fitting parameters
    full_width = np.abs(direct_decay(xplot*3600,*(popt+sigma_activity_estimated))-direct_decay(xplot*3600,*(popt-sigma_activity_estimated))) #full width of confidence band
    percent_uncert = full_width/(2*direct_decay(xplot*3600,*popt))  #Distance from fitted line. Half width, sigma_A0/A0 along the line.
    #print("Relative uncertainty of A0 (estimated) {}".format(percent_uncert[0]))
    sigma_A0_estimated = (full_width/2)[0]  #uncertainty in the estimated A0. just taking out the first point.
    A0_estimated = direct_decay(0, popt)
    #print("Activity: {} ({})".format(A0_estimated,sigma_A0_estimated))


    if makePlot == True:
        plt.plot(xplot,direct_decay(xplot*3600,*popt),'r-', color='red')
        plt.plot(xplot,direct_decay(xplot*3600,*(popt+sigma_activity_estimated)), color='blue', linewidth=0.4)
        plt.plot(xplot,direct_decay(xplot*3600,*(popt-sigma_activity_estimated)), color='blue', linewidth=0.4)
        plt.plot(time[index],A[index], '.')
        plt.errorbar(time[index], A[index], color='green', linewidth=0.001,yerr=sigma_A[index], elinewidth=0.5, ecolor='k', capthick=0.5)   # cap thickness for error bar color='blue')
        #plt.title('Activity for foil {} nucleus {}'.format(ID, Nucleus) )
        plt.xlabel('time since eob, hours')
        plt.ylabel('Activity, Bq')
        plt.legend(['Fit', r'1$\sigma$ uncertainty'] )
        save_curves_to = os.getcwd()+'/activity_curves/'
        #save_csv_to = os.getcwd()+'/activity_csv/'
        #np.savetxt("{}.csv".format(save_results_to +  reaction), np.array((A0, sigma_A0)), delimiter=",")
        #plt.savefig('{}.png'.format(save_curves_to, name), dpi=300)
       
       
        #print(name[0])
        if name[0]=='/':   #only the first statement is original. 
            print(name[1:])
            name = name[1:]
        elif name[1] == '/':
            print(name[2:])
            name = name[2:]
        #else:
        #    print(name[0:])
        #    name = name[0:]
        #print(name)
        #foil_numb = name[-4:]
        #if foil_numb[0]=='_':
        #    foil_numb = foil_numb[1:]
        plt.title('Activity for {}'.format(name) )
        #plt.title(r'Activity $^{193m}$Pt - foil' + foil_numb[:-2])#.format(name[0]))
        plt.savefig(save_curves_to + '_activity_{}.png'.format(name), dpi=300)
        plt.show()




    return A0_estimated, sigma_A0_estimated

def A0_double_decay_unknown_parent(filename_activity_time, lambda_parent, lambda_daughter, makePlot=False):
    ID = filename_activity_time[-8:-4]
    Nucleus = filename_activity_time[-12:-8]
    print('foil{}_{}'.format(ID, Nucleus))
    name=name = filename_activity_time[-13:-4]

    time = np.genfromtxt(filename_activity_time, delimiter=',', usecols=[0]) #hours since e.o.b
    A = np.genfromtxt(filename_activity_time, delimiter=',', usecols=[1])
    sigma_A = np.genfromtxt(filename_activity_time, delimiter=',', usecols=[2])

    index = ~(np.isnan(A) | np.isnan(sigma_A))  #if either eps OR sigma eps is NaN
    t = np.max(time[index])
    xplot = np.linspace(0,t,1000)

    #non direct decay
    A0_parent_guess=1600; A0_daughter_guess=80000

    def non_direct_decay(time, A0_parent_guess, A0_daughter_guess):  #if there are no gammas to be detected from parent
        A_est = A0_parent_guess*lambda_daughter / (lambda_parent-lambda_daughter) *( np.exp(-lambda_daughter*time)-np.exp(-lambda_parent*time)) + A0_daughter_guess*np.exp(-lambda_daughter *time)
        return A_est




    popt, pcov = curve_fit(non_direct_decay, time[index]*3600, A[index], p0=np.array((A0_parent_guess, A0_daughter_guess)), sigma=sigma_A[index], absolute_sigma=True)
    sigma_activity_estimated = np.sqrt(np.diagonal(pcov))   #Uncertainty in the fitting parameters
    full_width = np.abs(non_direct_decay(xplot*3600,*(popt+sigma_activity_estimated))-non_direct_decay(xplot*3600,*(popt-sigma_activity_estimated))) #full width of confidence band
    percent_uncert = full_width/(2*non_direct_decay(xplot*3600,*popt))  #Distance from fitted line. Half width, sigma_A0/A0 along the line.
    sigma_A0_estimated_isomer = (full_width/2)[0]
    #sigma_A0_estimated_ground_state = (full_width/2)[1]  #uncertainty in the estimated A0. just taking out the first point.
    A0_estimated_isomer = popt[0]
    A0_estimated_ground_state = popt[1]
    sigma_A0_estimated = full_width/2 #for 1: isomer, 2: gs of 58Co
    A0_estimated = non_direct_decay(0, popt[0], popt[1])  #58Co  #for 1: isomer, 2: gs of 58Co

    def uncertainty_cov_A0(popt,pcov, lambda_parent, lambda_daughter, time):
        #Analytical derivations. can also use numerical
        #dA0_d = np.zeros(len(time))
        #for i in time:
        deriv_Ad_Ap = lambda_daughter/(lambda_parent-lambda_daughter)*(np.exp(-lambda_daughter*time)-np.exp(-lambda_parent*time))
        deriv_Ad_Ad = np.exp(-lambda_daughter*time)
        J = np.array((deriv_Ad_Ap, deriv_Ad_Ad)) #Jacobian

        dA0_d = np.sqrt( np.dot(np.dot(J,pcov),J.T ) )
        #print(dA0_d)
        return dA0_d

    sigma_A0_estimated_ground_state=np.zeros(len(xplot))
    for i in range(len(xplot)):
        sigma_A0_estimated_ground_state[i] = uncertainty_cov_A0(popt, pcov, lambda_parent, lambda_daughter, i)







    #plot
    if makePlot == True:
        plt.plot(xplot, non_direct_decay(xplot*3600,*popt), 'r-', color='red')
        #plt.plot(xplot,non_direct_decay(xplot*3600,*(popt+sigma_activity_estimated)), color='blue', linewidth=0.4)
        #plt.plot(xplot,non_direct_decay(xplot*3600,*(popt-sigma_activity_estimated)), color='green', linewidth=0.4)
        plt.plot(xplot,non_direct_decay(xplot*3600,*popt)+sigma_A0_estimated_ground_state, color='green', linewidth=0.4)
        plt.plot(xplot,non_direct_decay(xplot*3600,*popt)-sigma_A0_estimated_ground_state, color='green', linewidth=0.4)

        plt.plot(time[index],A[index], '.')
        plt.errorbar(time[index], A[index], color='green', linewidth=0.001,yerr=sigma_A[index], elinewidth=0.5, ecolor='k', capthick=0.5)   # cap thickness for error bar color='blue')
        plt.title('Activity for foil {} nucleus {}'.format(ID, Nucleus) )
        plt.xlabel('time since eob, hours')
        plt.ylabel('Activity, Bq')
        save_results_to = os.getcwd()+'/activity_curves/'
        #np.savetxt("{}.csv".format(save_results_to +  reaction), np.array((A0, sigma_A0)), delimiter=",")
        #plt.savefig('{}foil_{}.png'.format(save_results_to, Nucleus+ID), dpi=300)
        #plt.savefig('foil_{}_{}'.format(Nucleus, ID), dpi=300)
        plt.show()

    #return (A0_estimated)
    sigma_A0_estimated_ground_state=sigma_A0_estimated_ground_state[0]
    return A0_estimated_isomer, sigma_A0_estimated_isomer, A0_estimated_ground_state, sigma_A0_estimated_ground_state

def A0_double_decay_known_parent(filename_activity_time, A0_parent, lambda_parent, lambda_daughter, makePlot=False):
    ID = filename_activity_time[-8:-4]
    Nucleus = filename_activity_time[-12:-8]
    print('foil{}_{}'.format(ID, Nucleus))
    name =  filename_activity_time[-13:-4]

    time = np.genfromtxt(filename_activity_time, delimiter=',', usecols=[0]) #hours since e.o.b
    A = np.genfromtxt(filename_activity_time, delimiter=',', usecols=[1])
    sigma_A = np.genfromtxt(filename_activity_time, delimiter=',', usecols=[2])

    index = ~(np.isnan(A) | np.isnan(sigma_A))  #if either eps OR sigma eps is NaN
    t = np.max(time[index])
    xplot = np.linspace(0,t,1000)

    #non direct decay
    A0_daughter_guess=40000

    def non_direct_decay_known_parent(time,A0_daughter_guess):  #if there are no gammas to be detected from parent
        A_est        = A0_parent  *lambda_daughter / (lambda_parent-lambda_daughter) * (np.exp(-lambda_daughter*time)-np.exp(-lambda_parent*time)) + A0_daughter_guess*np.exp(-lambda_daughter*time)
        #A_est = A0_parent *lambda_daughter / (lambda_daughter-lambda_parent) * (np.exp(-lambda_daughter*time)-np.exp(-lambda_parent*time)) + A0_daughter_guess*np.exp(-lambda_daughter*time)
        #A_est = A0_parent_guess*lambda_daughter / (lambda_parent-lambda_daughter) *( np.exp(-lambda_daughter*time)-np.exp(-lambda_parent*time)) + A0_daughter_guess*np.exp(-lambda_daughter *time)
        return A_est

    popt, pcov=curve_fit(non_direct_decay_known_parent, time[index]*3600, A[index], p0=A0_daughter_guess, sigma=sigma_A[index], absolute_sigma=True)
    sigma_activity_estimated = np.sqrt(np.diagonal(pcov))   #Uncertainty in the fitting parameters
    full_width = np.abs(non_direct_decay_known_parent(xplot*3600,*(popt+sigma_activity_estimated))-non_direct_decay_known_parent(xplot*3600,*(popt-sigma_activity_estimated))) #full width of confidence band
    percent_uncert = full_width/(2*non_direct_decay_known_parent(xplot*3600,*popt))  #Distance from fitted line. Half width, sigma_A0/A0 along the line.
    #print("Relative uncertainty of A0 (estimated) {}".format(percent_uncert[0]))
    sigma_A0_estimated = (full_width/2)[0]  #uncertainty in the estimated A0. just taking out the first point.
    A0_estimated = non_direct_decay_known_parent(0, popt)
    #print("Activity: {} ({})".format(A0_estimated,sigma_A0_estimated))



    #plot
    if makePlot == True:
        plt.plot(xplot, non_direct_decay_known_parent(xplot*3600,*popt), 'r-', color='red')
        plt.plot(xplot,non_direct_decay_known_parent(xplot*3600,*(popt+sigma_activity_estimated)), color='blue', linewidth=0.4)
        plt.plot(xplot,non_direct_decay_known_parent(xplot*3600,*(popt-sigma_activity_estimated)), color='green', linewidth=0.4)
        plt.plot(time[index],A[index], '.')
        plt.errorbar(time[index], A[index], color='green', linewidth=0.001,yerr=sigma_A[index], elinewidth=0.5, ecolor='k', capthick=0.5)   # cap thickness for error bar color='blue')
        #plt.title('Activity for foil {} nucleus {}'.format(ID, Nucleus) )
        plt.xlabel('time since eob, hours')
        plt.ylabel('Activity, Bq')
        save_curves_to = os.getcwd()+'/activity_curves/'
        plt.title(name)
        #np.savetxt("{}.csv".format(save_results_to +  reaction), np.array((A0, sigma_A0)), delimiter=",")
        #plt.savefig('{}foil_{}.png'.format(save_results_to, Nucleus+ID), dpi=300)
        plt.savefig(save_curves_to + '_activity_{}.png'.format(name), dpi=300)
        plt.show()

    return A0_estimated, sigma_A0_estimated


def npat_decaychain(name_of_csv_file, parent_str, daughter_str):
    #'58COm', '58CO'      parent_str, daughter_str
    #'56NI', '56Co'




    t_irradiation = 1.0     # in hours
    #list, lambda_parent, lambda_daughter = func   #Ni_58Co()

    ### 58m/gCo decay chain, units of hours, assumed 2:1 production rate, for t_irradiation hours
    dc = DecayChain(parent_str, 'h', R={daughter_str:1.0, parent_str:2.0}, time=t_irradiation)

    ### Read in numbers of decays from csv file
    def decomment(csvfile):
        for row in csvfile:
            raw = row.split('#')[0].strip()
            if raw: yield raw



    if len(name_of_csv_file)== 2:
        print(name_of_csv_file[0])

        results_parent = []
        results_daughter = []
        with open(name_of_csv_file[0]) as csvfile:
            reader = csv.reader(decomment(csvfile))
            for row in reader:
                results_parent.append(row)
        with open(name_of_csv_file[1]) as csvfile:
            reader = csv.reader(decomment(csvfile))
            for row in reader:
                results_daughter.append(row)

        #print(results)

        results_daughter = np.asarray(results_daughter, dtype=float)
        results_parent = np.asarray(results_parent, dtype=float)

        # Reshape csv data structure
        list_of_counts_daughter = results_daughter[:, np.r_[0, 0, 3, 4]]
        list_of_counts_daughter[:,1] = list_of_counts_daughter[:,1] + (results_daughter[:,5] / 3600)
        list_of_counts_parent = results_parent[:, np.r_[0, 0, 3, 4]]
        list_of_counts_parent[:,1] = list_of_counts_parent[:,1] + (results_parent[:,5] / 3600)
        #print(list_of_counts)

        ### Calculate decay over timespan of all counts
        dc.append(DecayChain(parent_str, 'h', time=max(list_of_counts_daughter[:,1])))
        #dc.append(DecayChain(parent_str, 'h', time=700.0))
        # dc.plot()

        ### Measured counts: [start_time (d), stop_time (d), decays, unc_decays]
        ### Times relative to last appended DecayChain, i.e. EoB time
        dc.counts = {parent_str:list_of_counts_parent, daughter_str:list_of_counts_daughter}

    else:
        results = []
        with open(name_of_csv_file) as csvfile:
            reader = csv.reader(decomment(csvfile))
            for row in reader:
                results.append(row)

        results = np.asarray(results, dtype=float)

        # Reshape csv data structure
        list_of_counts = results[:, np.r_[0, 0, 3, 4]]
        list_of_counts[:,1] = list_of_counts[:,1] + (results[:,5] / 3600)
        #print(list_of_counts)

        ### Calculate decay over timespan of all counts
        dc.append(DecayChain(parent_str, 'h', time=max(list_of_counts[:,1])))
        # dc.plot()

        ### Measured counts: [start_time (d), stop_time (d), decays, unc_decays]
        ### Times relative to last appended DecayChain, i.e. EoB time
        dc.counts = {daughter_str:list_of_counts}






    ### Find the scaled production rate that gives us these counts
    dc.fit_R( unc=True)
    #dc.fit_A0( unc=True)
    ### Only plot the 5 most active isotopes in the decay chain
    dc.plot(N_plot=5)
    print('              ', dc.isotopes)
    print('Activity (Bq):',dc.A0)
    

    A_parent = dc.A0[0]
    A_daughter = dc.A0[1]
    dc.fit_A0( unc=True)
    print('Uncertainty in Activity (Bq):', dc._unc_A0_fit)
    dA_parent  = dc._unc_A0_fit[0]
    dA_daughter = dc._unc_A0_fit[1]

    return A_parent, dA_parent, A_daughter, dA_daughter

    #return dc.A0, dc._unc_A0_fit


def two_step_up_npat(func, reaction_parent, reaction_daughter, n, parent_str, daughter_str, Save_csv=False):
    list, lambda_parent, lambda_daughter = func
    #plt.title('Test')
    if len(list)==2:
        A0_parent = np.zeros(n); sigma_A0_parent = np.zeros(n)
        A0_daughter = np.zeros(n); sigma_A0_daughter = np.zeros(n)
        for i, e in enumerate(list[0]):
            print(np.append(list[0,i], list[1,i]))
            array_join = np.append(list[0,i], list[1,i])
            A0_estimated_parent, sigma_A0_estimated_parent, A0_estimated_daughter, sigma_A0_estimated_daughter = npat_decaychain(array_join, parent_str, daughter_str)
            #A0_double_decay_unknown_parent(e, lambda_parent, lambda_daughter, makePlot=True)
            A0_parent[i] = A0_estimated_parent
            sigma_A0_parent[i] = sigma_A0_estimated_parent
            A0_daughter[i] = A0_estimated_daughter
            sigma_A0_daughter[i] = sigma_A0_estimated_daughter
            #sigma_A0_daughter = sigma_A0_estimated_daughter[0]
            print('Parent: ', A0_parent)
            print('Daughter: ', A0_daughter)
            if Save_csv == True:
                save_results_to = os.getcwd()+'/activity_csv/'
                #print(type(reaction_daughter))
                print(type(A0_daughter),len(A0_daughter),type(sigma_A0_daughter), len(sigma_A0_daughter) )
                print(save_results_to+reaction_parent)
                np.savetxt("{}.csv".format(save_results_to + reaction_parent), np.array((A0_parent, sigma_A0_parent)), delimiter=",")
                np.savetxt("{}.csv".format(save_results_to + reaction_daughter), np.array((A0_daughter, sigma_A0_daughter)), delimiter=",")
    else:
        A0_parent = np.zeros(n); sigma_A0_parent = np.zeros(n)
        A0_daughter = np.zeros(n); sigma_A0_daughter = np.zeros(n)
        for i, e in enumerate(list):
            A0_estimated_parent, sigma_A0_estimated_parent, A0_estimated_daughter, sigma_A0_estimated_daughter = npat_decaychain(e, parent_str, daughter_str) #A0_double_decay_unknown_parent(e, lambda_parent, lambda_daughter, makePlot=True)
            A0_parent[i] = A0_estimated_parent
            sigma_A0_parent[i] = sigma_A0_estimated_parent
            A0_daughter[i] = A0_estimated_daughter
            sigma_A0_daughter[i] = sigma_A0_estimated_daughter
            #sigma_A0_daughter = sigma_A0_estimated_daughter[0]
            print('Parent: ', A0_parent)
            print('Daughter: ', A0_daughter)
            if Save_csv == True:
                save_results_to = os.getcwd()+'/activity_csv/'
                #print(type(reaction_daughter))
                print(type(A0_daughter),len(A0_daughter),type(sigma_A0_daughter), len(sigma_A0_daughter) )
                print(save_results_to+reaction_parent)
                np.savetxt("{}.csv".format(save_results_to + reaction_parent), np.array((A0_parent, sigma_A0_parent)), delimiter=",")
                np.savetxt("{}.csv".format(save_results_to + reaction_daughter), np.array((A0_daughter, sigma_A0_daughter)), delimiter=",")


def single_decay_data(func, reaction, n, Save_csv=False):  #function, string
    list, lambda_ = func
    A0 = np.zeros(n); sigma_A0 = np.zeros(n)
    #print(len(list))

    for i,e in enumerate(list):
        #print(i,e)
        #print(i)
        A0_estimated, sigma_A0_estimated = A0_single_decay(e, lambda_, makePlot=True)
        A0[i] = A0_estimated; sigma_A0[i] = sigma_A0_estimated
        #print("foil ", i, ": ", A0_estimated)
        #print(A0)
        #print("A0: ", A0)
        if Save_csv == True:
            save_results_to = os.getcwd()+'/activity_csv/'
            np.savetxt("{}.csv".format(save_results_to + reaction), np.array((A0, sigma_A0)), delimiter=",")

        #print("A0: {}, sigmaA0: {}".format(A0_estimated, sigma_A0_estimated))
        #print("*****************************************")
    return A0, sigma_A0
def two_step_kp_data(func_parent, func_daughter, reaction, n, Save_csv=False):
    list_parent, lambda_parent = func_parent
    A0 = np.zeros(n); sigma_A0 = np.zeros(n)
    A0_list = []; dA0_list = []
    for i,e in enumerate(list_parent):
        A0_estimated_parent, sigma_A0_estimated_parent = A0_single_decay(e,lambda_parent, makePlot=False)
        A0_list.append(A0_estimated_parent)  #add is all A0's for Ni56 from single decay function.
        dA0_list.append(sigma_A0_estimated_parent)

    list_daughter, lambda_parent, lambda_daughter = func_daughter
    #print(A0_list)
    for i,e in enumerate(list_daughter):
        A0_estimated_daughter, sigma_A0_estimated_daughter = A0_double_decay_known_parent(e, A0_list[i], lambda_parent, lambda_daughter, makePlot=True)
        A0[i] = A0_estimated_daughter; sigma_A0[i] = sigma_A0_estimated_daughter
        if Save_csv == True:
            save_results_to = os.getcwd()+'/activity_csv/'
            np.savetxt("{}.csv".format(save_results_to +  reaction), np.array((A0, sigma_A0)), delimiter=",")
        #print("A0: {}, sigmaA0: {}".format(A0_estimated_daughter, sigma_A0_estimated_daughter))
        #print("*****************************************")
    #print(A0)

    return A0, sigma_A0
def two_step_up_data(func, reaction_parent, reaction_daughter, n, Save_csv=False):
    list, lambda_parent, lambda_daughter = func
    A0_parent = np.zeros(n); sigma_A0_parent = np.zeros(n)
    A0_daughter = np.zeros(n); sigma_A0_daughter = np.zeros(n)
    for i, e in enumerate(list):
        A0_estimated_parent, sigma_A0_estimated_parent, A0_estimated_daughter, sigma_A0_estimated_daughter = A0_double_decay_unknown_parent(e, lambda_parent, lambda_daughter, makePlot=True)
        A0_parent[i] = A0_estimated_parent
        sigma_A0_parent[i] = sigma_A0_estimated_parent
        A0_daughter[i] = A0_estimated_daughter
        sigma_A0_daughter[i] = sigma_A0_estimated_daughter
        #sigma_A0_daughter = sigma_A0_estimated_daughter[0]
        if Save_csv == True:
            save_results_to = os.getcwd()+'/activity_csv/'
            #print(type(reaction_daughter))
            print(type(A0_daughter),len(A0_daughter),type(sigma_A0_daughter), len(sigma_A0_daughter) )
            print(save_results_to+reaction_parent)
            np.savetxt("{}.csv".format(save_results_to + reaction_parent), np.array((A0_parent, sigma_A0_parent)), delimiter=",")
            np.savetxt("{}.csv".format(save_results_to + reaction_daughter), np.array((A0_daughter, sigma_A0_daughter)), delimiter=",")
    
            #np.savetxt("{}.csv".format(reaction_parent), np.array((A0_parent, sigma_A0_parent)), delimiter=",")
            #np.savetxt("{}.csv".format(reaction_daughter), np.array((A0_daughter, sigma_A0_daughter)), delimiter=",")
        #print("Isomer -  A0: {}, sigma A0: {}".format(A0_estimated_parent, sigma_A0_estimated_parent))
        #print("Ground state -  A0: {}, sigma A0: {}".format(A0_estimated_daughter, sigma_A0_estimated_daughter))
        #print("***************************************")
        #print(A0_daughter,sigma_A0_daughter)
        #print(save_results_to+reaction_parent)
### MON FILES:

#single_decay_data(Cu_62Zn(), "Cu_62Zn", 10, Save_csv=True)
#single_decay_data(Cu_63Zn(), "Cu_63Zn", 10, Save_csv=True)
#single_decay_data(Cu_65Zn(), "Cu_65Zn", 10, Save_csv=True)
#single_decay_data(Ni_61Cu(), "Ni_61Cu", 10, Save_csv=True)
#two_step_kp_data(Ni_56Ni(), Ni_56Co(), "Ni_56Co", 10, Save_csv= True)
#two_step_up_npat(Ni_58Co(), "Ni_58mCo_npat", "Ni_58Co_npat", 10, '58COm', '58COg', Save_csv=True)
#two_step_up_npat(Ni_56Co(return_two_list=True), "Ni_56Ni_npat", "Ni_56Co_npat", 10, '56NI', '56CO', Save_csv=True)


"""
### For 56Co: Need two_step_kp_data for foil 1,2,3. Need single decay for foil 4,5,6,7,8,9,10
A0_single, sigma_A0_single = single_decay_data(Ni_56Co(False), "Ni_56Co", 7)
#print(A0_single)
A0_twostep, sigma_A0_twostep = two_step_kp_data(Ni_56Ni(), Ni_56Co(True), "Ni_56Co",3)
#print(A0_twostep)

A0 = np.concatenate((A0_twostep, A0_single))
print(A0)
sigma_A0 = np.concatenate((sigma_A0_twostep, sigma_A0_single))
print(sigma_A0)
save_results_to = os.getcwd()+'/activity_csv/'
np.savetxt("{}.csv".format(save_results_to +  'Ni_56Co'), np.array((A0, sigma_A0)), delimiter=",")
"""




#two_step_kp_data(Ni_56Ni(), Ni_56Co(), "Ni_56Co", 10, Save_csv= True)


#single_decay_data(Ni_56Ni(), "Ni_56Ni", 10, Save_csv=True)
#single_decay_data(Fe_56Co(), "Fe_56Co", 3, Save_csv=True)

#two_step_kp_data(Ni_56Ni(), Ni_56Co(), "Ni_56Co", 10, Save_csv= True)


#single_decay_data(Cu_62Zn(), "Cu_62Zn", 10, Save_csv=True)
#single_decay_data(Cu_63Zn(), "Cu_63Zn", 10, Save_csv=True)
#single_decay_data(Cu_65Zn(), "Cu_65Zn", 10, Save_csv=True)
#single_decay_data(Ni_57Co(), "Ni_57Co", 10, Save_csv=True)
#single_decay_data(Ni_61Cu(), "Ni_61Cu", 10, Save_csv=True)
#single_decay_data(Cu_65Zn(), "Cu_65Zn", 10, Save_csv=True)
#two_step_kp_data(Ni_56Ni(), Ni_56Co(), "Ni_56Co", 10, Save_csv= True)
#two_step_up_data(Ni_58Co(), "Ni_58mCo", "Ni_58Co", 10, Save_csv = True)
#two_step_up_data(Cu_52Mn(), "Cu_52mMn", "Cu_52Mn", 10, Save_csv = True)
#single_decay_data(Fe_56Co(), "Fe_56Co", 3, Save_csv=True)


###Cu
#single_decay_data(Cu_52Mn(), "Cu_52Mn", 10, Save_csv=True)



#two_step_up_data(Cu_56Co(), "Cu_56Ni", "Cu_56Co", 10, Save_csv = True)

#single_decay_data(Cu_56Co(), "Cu_56Co", 10, Save_csv=True)
#single_decay_data(Cu_57Co(), "Cu_57Co", 10, Save_csv=True)

#single_decay_data(Cu_57Ni(), "Cu_57Ni", 10, Save_csv=True)

#two_step_up_data(Cu_58Co(), "Cu_58mCo", "Cu_58Co", 10, Save_csv = True)     #WEIRD
#two_step_up_npat(Cu_58Co(), "Cu_58mCo_npat", "Cu_58Co_npat", 10, '58COm', '58COg', Save_csv=True)

#single_decay_data(Cu_59Fe(), "Cu_59Fe", 10, Save_csv=True)      #OK

#two_step_up_data(Cu_60Co(), "Cu_60mCo", "Cu_60Co", 10, Save_csv = True)   #WEIRD
#single_decay_data(Cu_60Co(), "Cu_60Co", 10, Save_csv=True)  #REporing as cumulative instead

#two_step_up_data(Cu_61Co(), "Cu_61Fe", "Cu_61Co", 10, Save_csv = True)   #OK
#single_decay_data(Cu_61Co(), "Cu_61Co", 10, Save_csv=True)

#single_decay_data(Cu_61Cu(), "Cu_61Cu", 10, Save_csv=True)      #some weird values

#single_decay_data(Cu_64Cu(), "Cu_64Cu", 10, Save_csv=True)      #EXCELLENT

#single_decay_data(Cu_65Ni(), "Cu_65Ni", 10, Save_csv=True)      #EXCELLENT


### Ni
#single_decay_data(Ni_56Ni(), "Ni_56Ni", 10, Save_csv=True)      #EXCELLENT

#single_decay_data(Ni_57Ni(), "Ni_57Ni", 10, Save_csv=True)      #EXCELLENT

#two_step_kp_data(Ni_57Ni(), Ni_57Co(), "Ni_57Co", 10, Save_csv= True)    #WEIRD


#single_decay_data(Ni_55Co(), "Ni_55Co", 10, Save_csv=True)      #EXCELLENT


#single_decay_data(Ni_52mMn(), "Ni_52mMn", 10, Save_csv=True)      #WEIRD
#two_step_up_npat(Ni_52Mn(return_two_list=True), "Ni_52mMn_npat", "Ni_52Mn_npat", 10, '52MNm', '52MN', Save_csv=True)


#single_decay_data(Ni_52Mn(), "Ni_52Mn", 10, Save_csv=True)   #since could not distinguish isomer + gs, do single decay and report cumulative yield. 
#two_step_up_npat(Ni_52Mn(return_two_list=False), "Ni_52Mn_npat", 10, '52MNm', '52MN', Save_csv=True)
#two_step_kp_data(Ni_52mMn(), Ni_52Mn(), "Ni_52Mn", 10, Save_csv= True)    #NOT WORKING



#single_decay_data(Ni_52Mn(), "Ni_52Mn", 10, Save_csv=True)   #since could not distinguish isomer + gs, do single decay and report cumulative yield. 
#single_decay_data(Ni_54Mn(), "Ni_54Mn", 10, Save_csv=True)      #done

#single_decay_data(Ni_59Fe(), "Ni_59Fe", 10, Save_csv=True)      #only in foil number 1, 3, 5

#single_decay_data(Ni_60Cu(), "Ni_60Cu", 10, Save_csv=True)      #EXCELLENT

#single_decay_data(Ni_60Cu(), "Ni_60Cu", 10, Save_csv=True)      #EXCELLENT

#single_decay_data(Ni_60mCo(), "Ni_60mCo", 10, Save_csv=True)     NOT PRODUCED 

#single_decay_data(Ni_64Cu(), "Ni_64Cu", 10, Save_csv=True)     #not produced?
#single_decay_data(Ni_60Co(), "Ni_60Co", 10, Save_csv=True)     #Report cumulative cross section with isomer + gs

#single_decay_data(Ni_56Ni(), "Ni_56Ni", 10, Save_csv=True)     #not produced?
#single_decay_data(Ni_65Ni(), "Ni_65Ni", 10, Save_csv=True)     #not produced?
#single_decay_data(Ni_55Co(), "Ni_55Co", 10, Save_csv=True)     #not produced?
#single_decay_data(Ni_56Mn(), "Ni_56Mn", 10, Save_csv=True)     #not produced?
#single_decay_data(Ni_57Ni(), "Ni_57Ni", 10, Save_csv=True)     #not produced?


###Fe

#single_decay_data(Fe_48V(), "Fe_48V", 3, Save_csv=True)     #EXCELLENT, but could not save fig..
#single_decay_data(Fe_51Mn(), "Fe_51Mn", 3, Save_csv=True)     # not produced?
#single_decay_data(Fe_51Cr(), "Fe_51Cr", 3, Save_csv=True)     #EXCELLENT

#single_decay_data(Fe_52mMn(), "Fe_52mMn", 3, Save_csv=True)     #not produced?
#single_decay_data(Fe_52Mn(), "Fe_52Mn", 3, Save_csv=True)     #EXCELLENT
#single_decay_data(Fe_53Fe(), "Fe_53Fe", 3, Save_csv=True)     #EXCELLENT

#single_decay_data(Fe_54Mn(), "Fe_54Mn", 3, Save_csv=True)     #EXCELLENT
#single_decay_data(Fe_55Co(), "Fe_55Co", 3, Save_csv=True)     #EXCELLENT

#single_decay_data(Fe_57Co(), "Fe_57Co", 3, Save_csv=True)     #EXCELLENT
#single_decay_data(Fe_58Co(), "Fe_58Co", 3, Save_csv=True)     #EXCELLENT

#single_decay_data(Fe_59Fe(), "Fe_59Fe", 3, Save_csv=True)     #EXCELLENT



###Ir

#single_decay_data(Ir_183Ta(), "Ir_183Ta", 10, Save_csv=True)    #183Hf was produced!!!!!. Not correct then
#two_step_up_npat(Ir_183Ta(), "Ir_183Hf_npat", "Ir_183Ta_npat", 10, '183HF', '183TA', Save_csv=False)

#single_decay_data(Ir_186Ta(), "Ir_186Ta", 10, Save_csv=True)     #WEIRD LOOKING
#single_decay_data(Ir_186Re(), "Ir_186Re", 10, Save_csv=True)    #seems ok
#single_decay_data(Ir_187W(), "Ir_187W", 10, Save_csv=True)    # kind of weird looking?

#single_decay_data(Ir_188Pt(), "Ir_188Pt", 10, Save_csv=True)    #USED
#two_step_kp_data(Ir_188Pt(), Ir_188Ir(), "Ir_188Ir", 10, Save_csv= True)   #ok
#two_step_up_npat(Ir_188Ir(return_two_list=True), "Ir_188Pt", "Ir_188Ir", 10, '188PT', '188IR', Save_csv=True)
#single_decay_data(Ir_188Ir(), "Ir_188Ir", 10, Save_csv=True)    #USED

#single_decay_data(Ir_188mRe(), "Ir_188mRe", 10, Save_csv=True)    #WEIRD, prob not produced?
#single_decay_data(Ir_188Re(), "Ir_188Re", 10, Save_csv=True)    #ok




#single_decay_data(Ir_189Pt(), "Ir_189Pt", 10, Save_csv=True)    #EXCELLENT
#two_step_kp_data(Ir_189Pt(), Ir_189Ir(), "Ir_189Ir", 10, Save_csv= True)   #try single instead
#single_decay_data(Ir_189Ir(), "Ir_189Ir", 10, Save_csv=True)    #works but gives wrong result. 
#try: npat
two_step_up_npat(Ir_189Ir(), "Ir_189Pt_npat", "Ir_189Ir_npat", 10, '189PT', '189IR', Save_csv=False)   #crashes after first plot.



#single_decay_data(Ir_189W(), "Ir_189W", 10, Save_csv=True)    #Prob not oberved
#single_decay_data(Ir_189Re(), "Ir_189Re", 10, Save_csv=True)    #two gamma lines, does not agree
#single_decay_data(Ir_190mRe(), "Ir_190mRe", 10, Save_csv=True)    #prob not observed?
#single_decay_data(Ir_190Re(), "Ir_190Re", 10, Save_csv=True)    #must go through false peaks

#single_decay_data(Ir_190Ir(), "Ir_190Ir", 10, Save_csv=True)  
#single_decay_data(Ir_191Pt(), "Ir_191Pt", 10, Save_csv=True)    #two gamma lines, does not agree
#single_decay_data(Ir_192Ir(), "Ir_192Ir", 10, Save_csv=True)    #must go through false peaks

###  single_decay_data(Ir_193mPt(), "Ir_193mPt", 10, Save_csv=True)   
#single_decay_data(Ir_194m2Ir(), "Ir_194m2Ir", 10, Save_csv=True)    #ok, must go through false peaks
#two_step_kp_data(Ir_194m2Ir(), Ir_194Ir(), "Ir_194Ir", 10, Save_csv= True)  


#HH
