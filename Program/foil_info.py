import numpy as np, matplotlib.pyplot as plt
from scipy import interpolate
from scipy.optimize import curve_fit
import os

m=60; h=m*60; d=h*24; y=d*356  #converters to seconds


#lambda_ = np.log(2)/(1925.28*d)

#print(1925.28*d)

#path = 'UsershannahDocumentsUIOMasteroppgavenDataData_analysiscsv'
#path = '/Users/hannahekeberg/Documents/Master_git/matlab/csv/'
path = os.getcwd() + '/../matlab/csv/'

####Cupper foils########
def Cu_62Zn(): #check,  #mon, single
    foil1 = path + 'Cu_62Zn_129.dat'
    foil2 = path + 'Cu_62Zn_229.dat'
    foil3 = path + 'Cu_62Zn_329.dat'
    foil4 = path + 'Cu_62Zn_429.dat'
    foil5 = path + 'Cu_62Zn_529.dat'
    foil6 = path + 'Cu_62Zn_629.dat'
    foil7 = path + 'Cu_62Zn_729.dat'
    foil8 = path + 'Cu_62Zn_829.dat'
    foil9 = path + 'Cu_62Zn_929.dat'
    foil10= path + 'Cu_62Zn_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    #print(np.log(2)/(9.193*h))
    t_half = 9.193*h
    sigma_t_half = 0.013*h
    lambda_ = np.log(2.)/(t_half)#(9.193*h)
    sigma_lambda_ = lambda_*(sigma_t_half / t_half)

    return list, lambda_#, sigma_lambda_
    #return list, lambda_    #mon, single

def Cu_63Zn(): #check #mon, single
    foil1 = path + 'Cu_63Zn_129.dat'
    foil2 = path + 'Cu_63Zn_229.dat'
    foil3 = path + 'Cu_63Zn_329.dat'
    foil4 = path + 'Cu_63Zn_429.dat'
    foil5 = path + 'Cu_63Zn_529.dat'
    foil6 = path + 'Cu_63Zn_629.dat'
    foil7 = path + 'Cu_63Zn_729.dat'
    foil8 = path + 'Cu_63Zn_829.dat'
    foil9 = path + 'Cu_63Zn_929.dat'
    foil10= path + 'Cu_63Zn_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(38.47*m)
    return list, lambda_    #mon, single

def Cu_65Zn(): #check,  #mon, single
    foil1 = path + 'Cu_65Zn_129.dat'
    foil2 = path + 'Cu_65Zn_229.dat'
    foil3 = path + 'Cu_65Zn_329.dat'
    foil4 = path + 'Cu_65Zn_429.dat'
    foil5 = path + 'Cu_65Zn_529.dat'
    foil6 = path + 'Cu_65Zn_629.dat'
    foil7 = path + 'Cu_65Zn_729.dat'
    foil8 = path + 'Cu_65Zn_829.dat'
    foil9 = path + 'Cu_65Zn_929.dat'
    foil10= path + 'Cu_65Zn_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(243.93*d)
    return list, lambda_    #mon

def Cu_52Mn(): #non-mon, BUT WAS PRODUCED, needs work ?????????
    foil1 = path + 'Cu_52Mn_129.dat'
    foil2 = path + 'Cu_52Mn_229.dat'
    foil3 = path + 'Cu_52Mn_329.dat'
    foil4 = path + 'Cu_52Mn_429.dat'
    foil5 = path + 'Cu_52Mn_529.dat'
    foil6 = path + 'Cu_52Mn_629.dat'
    foil7 = path + 'Cu_52Mn_729.dat'
    foil8 = path + 'Cu_52Mn_829.dat'
    foil9 = path + 'Cu_52Mn_929.dat'
    foil10= path + 'Cu_52Mn_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_parent = np.log(2)/(21.1*m) #52mMn
    lambda_daughter = np.log(2)/(5.591*d) #52Mn
    return list, lambda_daughter# lambda_parent, lambda_daughter


def Cu_56Co():   #single decay        #looks weird
    foil1 = path + 'Cu_56Co_129.dat'
    foil2 = path + 'Cu_56Co_229.dat'
    foil3 = path + 'Cu_56Co_329.dat'
    foil4 = path + 'Cu_56Co_429.dat'
    foil5 = path + 'Cu_56Co_529.dat'
    foil6 = path + 'Cu_56Co_629.dat'
    foil7 = path + 'Cu_56Co_729.dat'
    foil8 = path + 'Cu_56Co_829.dat'
    foil9 = path + 'Cu_56Co_929.dat'
    foil10 = path + 'Cu_56Co_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    #lambda_parent = np.log(2)/(6.075*d)
    lambda_ = np.log(2)/(77.236*d)
    return list, lambda_#parent, lambda_daughter




def Cu_57Co():   #double decay from 57Ni
    foil1 = path + 'Cu_57Co_129.dat'
    foil2 = path + 'Cu_57Co_229.dat'
    foil3 = path + 'Cu_57Co_329.dat'
    foil4 = path + 'Cu_57Co_429.dat'
    foil5 = path + 'Cu_57Co_529.dat'
    foil6 = path + 'Cu_57Co_629.dat'
    foil7 = path + 'Cu_57Co_729.dat'
    foil8 = path + 'Cu_57Co_829.dat'
    foil9 = path + 'Cu_57Co_929.dat'
    foil10 = path + 'Cu_57Co_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_parent = np.log(2)/(35.60*h)
    lambda_daughter = np.log(2)/(271.74*d)
    return list, lambda_daughter#lambda_parent, lambda_daughter


def Cu_57Ni():  #single decay
    foil1 = path + 'Cu_57Ni_129.dat'
    foil2 = path + 'Cu_57Ni_229.dat'
    foil3 = path + 'Cu_57Ni_329.dat'
    foil4 = path + 'Cu_57Ni_429.dat'
    foil5 = path + 'Cu_57Ni_529.dat'
    foil6 = path + 'Cu_57Ni_629.dat'
    foil7 = path + 'Cu_57Ni_729.dat'
    foil8 = path + 'Cu_57Ni_829.dat'
    foil9 = path + 'Cu_57Ni_929.dat'
    foil10 = path + 'Cu_57Ni_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(35.60*h)
    return list, lambda_


def Cu_58Co():   #double decay with unkown parent 58mCo   #weird acting
    foil1 = path + 'Cu_58Co_129.dat'
    foil2 = path + 'Cu_58Co_229.dat'
    foil3 = path + 'Cu_58Co_329.dat'
    foil4 = path + 'Cu_58Co_429.dat'
    foil5 = path + 'Cu_58Co_529.dat'
    foil6 = path + 'Cu_58Co_629.dat'
    foil7 = path + 'Cu_58Co_729.dat'
    foil8 = path + 'Cu_58Co_829.dat'
    foil9 = path + 'Cu_58Co_929.dat'
    foil10 = path + 'Cu_58Co_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_parent = np.log(2)/(9.10*h)      #isomer
    lambda_daughter = np.log(2)/(77.236*d)  #ground state

    return list, lambda_parent, lambda_daughter


def Cu_59Fe():   #single decay     #kind of weird but reasonable when looking in exfor
    foil1 = path + 'Cu_59Fe_129.dat'
    foil2 = path + 'Cu_59Fe_229.dat'
    foil3 = path + 'Cu_59Fe_329.dat'
    foil4 = path + 'Cu_59Fe_429.dat'
    foil5 = path + 'Cu_59Fe_529.dat'
    foil6 = path + 'Cu_59Fe_629.dat'
    foil7 = path + 'Cu_59Fe_729.dat'
    foil8 = path + 'Cu_59Fe_829.dat'
    foil9 = path + 'Cu_59Fe_929.dat'
    foil10 = path + 'Cu_59Fe_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(44.495*d)
    return list, lambda_


def Cu_60Co():  #two step decay via 60mCo, unkown though, since 60mCo is not observed   WEIRD LOOKING
    foil1 = path + 'Cu_60Co_129.dat'
    foil2 = path + 'Cu_60Co_229.dat'
    foil3 = path + 'Cu_60Co_329.dat'
    foil4 = path + 'Cu_60Co_429.dat'
    foil5 = path + 'Cu_60Co_529.dat'
    foil6 = path + 'Cu_60Co_629.dat'
    foil7 = path + 'Cu_60Co_729.dat'
    foil8 = path + 'Cu_60Co_829.dat'
    foil9 = path + 'Cu_60Co_929.dat'
    foil10 = path + 'Cu_60Co_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_parent = np.log(2)/(10.467*m)      #isomer
    lambda_daughter = np.log(2)/(1925.28*d)  #ground state
    return list, lambda_daughter  #lambda_parent, lambda_daughter



def Cu_61Co():   #in theory, 61 Fe feeds in, but half life=5.98 m. Unknown parent since not observed
    foil1 = path + 'Cu_61Co_129.dat'
    foil2 = path + 'Cu_61Co_229.dat'
    foil3 = path + 'Cu_61Co_329.dat'
    foil4 = path + 'Cu_61Co_429.dat'
    foil5 = path + 'Cu_61Co_529.dat'
    foil6 = path + 'Cu_61Co_629.dat'
    foil7 = path + 'Cu_61Co_729.dat'
    foil8 = path + 'Cu_61Co_829.dat'
    foil9 = path + 'Cu_61Co_929.dat'
    foil10 = path + 'Cu_61Co_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_parent = np.log(2)/(5.98*m)      #isomer
    lambda_daughter = np.log(2)/(1.649*h)  #ground state
    return list, lambda_daughter#lambda_parent, lambda_daughter


def Cu_61Cu():   #in theory, decay from 61Zn but half life in order seconds...
    foil1 = path + 'Cu_61Cu_129.dat'
    foil2 = path + 'Cu_61Cu_229.dat'
    foil3 = path + 'Cu_61Cu_329.dat'
    foil4 = path + 'Cu_61Cu_429.dat'
    foil5 = path + 'Cu_61Cu_529.dat'
    foil6 = path + 'Cu_61Cu_629.dat'
    foil7 = path + 'Cu_61Cu_729.dat'
    foil8 = path + 'Cu_61Cu_829.dat'
    foil9 = path + 'Cu_61Cu_929.dat'
    foil10 = path + 'Cu_61Cu_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(3.339*h)
    return list, lambda_

def Cu_64Cu():   #single decay
    foil1 = path + 'Cu_64Cu_129.dat'
    foil2 = path + 'Cu_64Cu_229.dat'
    foil3 = path + 'Cu_64Cu_329.dat'
    foil4 = path + 'Cu_64Cu_429.dat'
    foil5 = path + 'Cu_64Cu_529.dat'
    foil6 = path + 'Cu_64Cu_629.dat'
    foil7 = path + 'Cu_64Cu_729.dat'
    foil8 = path + 'Cu_64Cu_829.dat'
    foil9 = path + 'Cu_64Cu_929.dat'
    foil10 = path + 'Cu_64Cu_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(12.701*h)
    return list, lambda_


def Cu_65Ni():     #single decay
    foil1 = path + 'Cu_65Ni_129.dat'
    foil2 = path + 'Cu_65Ni_229.dat'
    foil3 = path + 'Cu_65Ni_329.dat'
    foil4 = path + 'Cu_65Ni_429.dat'
    foil5 = path + 'Cu_65Ni_529.dat'
    foil6 = path + 'Cu_65Ni_629.dat'
    foil7 = path + 'Cu_65Ni_729.dat'
    foil8 = path + 'Cu_65Ni_829.dat'
    foil9 = path + 'Cu_65Ni_929.dat'
    foil10 = path + 'Cu_65Ni_1029.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(2.51719*h)
    return list, lambda_

#####NICKEL FOILS######
#Lacking: 60Co

def Ni_56Ni(): #non-mon, single
    foil1 = path + 'Ni_56Ni_128.dat'
    foil2 = path + 'Ni_56Ni_228.dat'
    foil3 = path + 'Ni_56Ni_328.dat'
    foil4 = path + 'Ni_56Ni_428.dat'
    foil5 = path + 'Ni_56Ni_528.dat'
    foil6 = path + 'Ni_56Ni_628.dat'
    foil7 = path + 'Ni_56Ni_728.dat'
    foil8 = path + 'Ni_56Ni_828.dat'
    foil9 = path + 'Ni_56Ni_928.dat'
    foil10= path + 'Ni_56Ni_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(6.075*d)
    return list, lambda_

def Ni_56Co_old(return_two_list=False): #mon, two step, known parent activity 56Ni
    #type = "tskp"
    foil1 = path + 'Ni_56Co_128.dat'
    foil2 = path + 'Ni_56Co_228.dat'
    foil3 = path + 'Ni_56Co_328.dat'
    foil4 = path + 'Ni_56Co_428.dat'
    foil5 = path + 'Ni_56Co_528.dat'
    foil6 = path + 'Ni_56Co_628.dat'
    foil7 = path + 'Ni_56Co_728.dat'
    foil8 = path + 'Ni_56Co_828.dat'
    foil9 = path + 'Ni_56Co_928.dat'
    foil10= path + 'Ni_56Co_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_daughter = np.log(2)/(77.236*d) #56Co
    lambda_parent = np.log(2)/(6.075*d) #56Ni

    if return_two_list:
        list_parent = Ni_56Ni()[0]
        list_daughter = list
        return np.array((list_parent, list_daughter)), lambda_parent, lambda_daughter


    #return list, lambda_parent, lambda_daughter#[lambda_parent, lambda_daughter]
    return list,lambda_daughter#[lambda_parent, lambda_daughter]
    #return list, [lambda_parent, lambda_daughter]#[lambda_parent, lambda_daughter]

def Ni_56Co(two_step=False):  #only use foil 1-3 for two step decay with 56Ni.   
    #pass   #need another functions that does single decay on foil 4-10. 
    if two_step==True:
        foil1 = path + 'Ni_56Co_128.dat'
        foil2 = path + 'Ni_56Co_228.dat'
        foil3 = path + 'Ni_56Co_328.dat'

        list = [foil1, foil2, foil3]
        lambda_daughter =  np.log(2)/(77.236*d) #56Co
        lambda_parent = Ni_56Ni()[-1]
        return list, lambda_parent, lambda_daughter
    if two_step==False:
        foil4 = path + 'Ni_56Co_428.dat'
        foil5 = path + 'Ni_56Co_528.dat'
        foil6 = path + 'Ni_56Co_628.dat'
        foil7 = path + 'Ni_56Co_728.dat'
        foil8 = path + 'Ni_56Co_828.dat'
        foil9 = path + 'Ni_56Co_928.dat'
        foil10 = path + 'Ni_56Co_1028.dat'
        list = [foil4, foil5, foil6, foil7, foil8, foil9, foil10]
        lambda_daughter =  np.log(2)/(77.236*d) #56Co
        lambda_parent = Ni_56Ni()[-1]
        lambda_ = np.log(2)/(77.236*d) #56Co
        return list, lambda_





def Ni_58Co(): #mon, two step, unkown parent activity 58mCo
    #type = "tsup"
    foil1 = path + 'Ni_58Co_128.dat'
    foil2 = path + 'Ni_58Co_228.dat'
    foil3 = path + 'Ni_58Co_328.dat'
    foil4 = path + 'Ni_58Co_428.dat'
    foil5 = path + 'Ni_58Co_528.dat'
    foil6 = path + 'Ni_58Co_628.dat'
    foil7 = path + 'Ni_58Co_728.dat'
    foil8 = path + 'Ni_58Co_828.dat'
    foil9 = path + 'Ni_58Co_928.dat'
    foil10= path + 'Ni_58Co_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_isomer = np.log(2)/(9.10*h)
    #lambda_ground_state = np.log(2)/(77.236*d)  #Wrote wrong at first
    lambda_ground_state = np.log(2)/(70.86*d)
    #print(lambda_ground_state)
    return list, lambda_isomer, lambda_ground_state

def Ni_58mCo():
    lamb_ = np.log(2)/(9.10*h)
    return 'fake' ,lamb_

def Ni_61Cu(): #mon, single
    foil1 = path + 'Ni_61Cu_128.dat'
    foil2 = path + 'Ni_61Cu_228.dat'
    foil3 = path + 'Ni_61Cu_328.dat'
    foil4 = path + 'Ni_61Cu_428.dat'
    foil5 = path + 'Ni_61Cu_528.dat'
    foil6 = path + 'Ni_61Cu_628.dat'
    foil7 = path + 'Ni_61Cu_728.dat'
    foil8 = path + 'Ni_61Cu_828.dat'
    foil9 = path + 'Ni_61Cu_928.dat'
    foil10= path + 'Ni_61Cu_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(3.339*h)
    return list, lambda_

def Ni_57Ni(): #single decay
    foil1 = path + 'Ni_57Ni_128.dat'
    foil2 = path + 'Ni_57Ni_228.dat'
    foil3 = path + 'Ni_57Ni_328.dat'
    foil4 = path + 'Ni_57Ni_428.dat'
    foil5 = path + 'Ni_57Ni_528.dat'
    foil6 = path + 'Ni_57Ni_628.dat'
    foil7 = path + 'Ni_57Ni_728.dat'
    foil8 = path + 'Ni_57Ni_828.dat'
    foil9 = path + 'Ni_57Ni_928.dat'
    foil10 = path + 'Ni_57Ni_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(35.60*h)
    return list, lambda_


def Ni_57Co(): #double decay from 57Ni
    foil1 = path + 'Ni_57Co_128.dat'
    foil2 = path + 'Ni_57Co_228.dat'
    foil3 = path + 'Ni_57Co_328.dat'
    foil4 = path + 'Ni_57Co_428.dat'
    foil5 = path + 'Ni_57Co_528.dat'
    foil6 = path + 'Ni_57Co_628.dat'
    foil7 = path + 'Ni_57Co_728.dat'
    foil8 = path + 'Ni_57Co_828.dat'
    foil9 = path + 'Ni_57Co_928.dat'
    foil10= path + 'Ni_57Co_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_parent = np.log(2)/(35.60*h)
    lambda_daughter = np.log(2)/(271.74*d)
    return list, lambda_parent, lambda_daughter


def Ni_55Co(): #single, beta- from 55Ni too short half life..
    foil1 = path + 'Ni_55Co_128.dat'
    foil2 = path + 'Ni_55Co_228.dat'
    foil3 = path + 'Ni_55Co_328.dat'
    foil4 = path + 'Ni_55Co_428.dat'
    foil5 = path + 'Ni_55Co_528.dat'
    foil6 = path + 'Ni_55Co_628.dat'
    foil7 = path + 'Ni_55Co_728.dat'
    foil8 = path + 'Ni_55Co_828.dat'
    foil9 = path + 'Ni_55Co_928.dat'
    foil10= path + 'Ni_55Co_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(17.53*h)
    return list, lambda_   #gives weird activities

def Ni_52mMn():  #single decay, 52Fe not produced...
    foil1 = path + 'Ni_52mMn_128.dat'
    foil2 = path + 'Ni_52mMn_228.dat'
    foil3 = path + 'Ni_52mMn_328.dat'
    foil4 = path + 'Ni_52mMn_428.dat'
    foil5 = path + 'Ni_52mMn_528.dat'
    foil6 = path + 'Ni_52mMn_628.dat'
    foil7 = path + 'Ni_52mMn_728.dat'
    foil8 = path + 'Ni_52mMn_828.dat'
    foil9 = path + 'Ni_52mMn_928.dat'
    foil10 = path + 'Ni_52mMn_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(21.1*m)
    return list, lambda_

def Ni_52Mn(return_two_list=False): #double decay known parent 52mMn
    foil1 = path + 'Ni_52Mn_128.dat'
    foil2 = path + 'Ni_52Mn_228.dat'
    foil3 = path + 'Ni_52Mn_328.dat'
    foil4 = path + 'Ni_52Mn_428.dat'
    foil5 = path + 'Ni_52Mn_528.dat'
    foil6 = path + 'Ni_52Mn_628.dat'
    foil7 = path + 'Ni_52Mn_728.dat'
    foil8 = path + 'Ni_52Mn_828.dat'
    foil9 = path + 'Ni_52Mn_928.dat'
    foil10 = path + 'Ni_52Mn_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_parent = np.log(2)/(21.1*m)
    lambda_daughter = np.log(2)/(5.591*d)

    if return_two_list:
        list_parent = Ni_56Ni()[0]
        list_daughter = list
        return np.array((list_parent, list_daughter)), lambda_parent, lambda_daughter


    #return list, lambda_parent, lambda_daughter#[lambda_parent, lambda_daughter]
    #return list, lambda_parent, lambda_daughter
    return list, lambda_daughter

def Ni_54Mn(): #single decay
    foil1 = path + 'Ni_54Mn_128.dat'
    foil2 = path + 'Ni_54Mn_228.dat'
    foil3 = path + 'Ni_54Mn_328.dat'
    foil4 = path + 'Ni_54Mn_428.dat'
    foil5 = path + 'Ni_54Mn_528.dat'
    foil6 = path + 'Ni_54Mn_628.dat'
    foil7 = path + 'Ni_54Mn_728.dat'
    foil8 = path + 'Ni_54Mn_828.dat'
    foil9 = path + 'Ni_54Mn_928.dat'
    foil10 = path + 'Ni_54Mn_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(312.20*d)
    return list, lambda_

def Ni_59Fe():   #single decay
    foil1 = path + 'Ni_59Fe_128.dat'
    foil2 = path + 'Ni_59Fe_228.dat'
    foil3 = path + 'Ni_59Fe_328.dat'
    foil4 = path + 'Ni_59Fe_428.dat'
    foil5 = path + 'Ni_59Fe_528.dat'
    foil6 = path + 'Ni_59Fe_628.dat'
    foil7 = path + 'Ni_59Fe_728.dat'
    foil8 = path + 'Ni_59Fe_828.dat'
    foil9 = path + 'Ni_59Fe_928.dat'
    foil10 = path + 'Ni_59Fe_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(44.495*d)
    return list, lambda_

def Ni_60Cu():  #single decay  (probably not 60Zn, thalf=2m)
    foil1 = path + 'Ni_60Cu_128.dat'
    foil2 = path + 'Ni_60Cu_228.dat'
    foil3 = path + 'Ni_60Cu_328.dat'
    foil4 = path + 'Ni_60Cu_428.dat'
    foil5 = path + 'Ni_60Cu_528.dat'
    foil6 = path + 'Ni_60Cu_628.dat'
    foil7 = path + 'Ni_60Cu_728.dat'
    foil8 = path + 'Ni_60Cu_828.dat'
    foil9 = path + 'Ni_60Cu_928.dat'
    foil10 = path + 'Ni_60Cu_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(23.7*m)
    return list, lambda_


def Ni_56Mn():   #single
    foil1 = path + 'Ni_56Mn_128.dat'
    foil2 = path + 'Ni_56Mn_228.dat'
    foil3 = path + 'Ni_56Mn_328.dat'
    foil4 = path + 'Ni_56Mn_428.dat'
    foil5 = path + 'Ni_56Mn_528.dat'
    foil6 = path + 'Ni_56Mn_628.dat'
    foil7 = path + 'Ni_56Mn_728.dat'
    foil8 = path + 'Ni_56Mn_828.dat'
    foil9 = path + 'Ni_56Mn_928.dat'
    foil10 = path + 'Ni_56Mn_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(2.5789*h)
    return list, lambda_


"""
def Ni_60mCo():     # ONE STEP
    foil1 = path + 'Ni_60mCo_128.dat'
    foil2 = path + 'Ni_60mCo_228.dat'
    foil3 = path + 'Ni_60mCo_328.dat'
    foil4 = path + 'Ni_60mCo_428.dat'
    foil5 = path + 'Ni_60mCo_528.dat'
    foil6 = path + 'Ni_60mCo_628.dat'
    foil7 = path + 'Ni_60mCo_728.dat'
    foil8 = path + 'Ni_60mCo_828.dat'
    foil9 = path + 'Ni_60mCo_928.dat'
    foil10 = path + 'Ni_60mCo_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(10.467*m)
    return list, lambda_
"""

def Ni_60Co():    #Single decay, report cumulative cross section along with 60mCo 
    
    foil1 = path + 'Ni_60Co_128.dat'
    foil2 = path + 'Ni_60Co_228.dat'
    foil3 = path + 'Ni_60Co_328.dat'
    foil4 = path + 'Ni_60Co_428.dat'
    foil5 = path + 'Ni_60Co_528.dat'
    foil6 = path + 'Ni_60Co_628.dat'
    foil7 = path + 'Ni_60Co_728.dat'
    foil8 = path + 'Ni_60Co_828.dat'
    foil9 = path + 'Ni_60Co_928.dat'
    foil10 = path + 'Ni_60Co_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(1925.28*d)
    #print(lambda_)


    return list, lambda_

def Ni_64Cu():
    foil1 = path + 'Ni_64Cu_128.dat'
    foil2 = path + 'Ni_64Cu_228.dat'
    foil3 = path + 'Ni_64Cu_328.dat'
    foil4 = path + 'Ni_64Cu_428.dat'
    foil5 = path + 'Ni_64Cu_528.dat'
    foil6 = path + 'Ni_64Cu_628.dat'
    foil7 = path + 'Ni_64Cu_728.dat'
    foil8 = path + 'Ni_64Cu_828.dat'
    foil9 = path + 'Ni_64Cu_928.dat'
    foil10 = path + 'Ni_64Cu_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(12.701*h)
    return list, lambda_

def Ni_65Ni(): #single decay
    foil1 = path + 'Ni_65Ni_128.dat'
    foil2 = path + 'Ni_65Ni_228.dat'
    foil3 = path + 'Ni_65Ni_328.dat'
    foil4 = path + 'Ni_65Ni_428.dat'
    foil5 = path + 'Ni_65Ni_528.dat'
    foil6 = path + 'Ni_65Ni_628.dat'
    foil7 = path + 'Ni_65Ni_728.dat'
    foil8 = path + 'Ni_65Ni_828.dat'
    foil9 = path + 'Ni_65Ni_928.dat'
    foil10 = path + 'Ni_65Ni_1028.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(2.5175*h)
    return list, lambda_


#####IRON FOILS########

def Fe_56Co(): #mon, Single
    foil1 = path + 'Fe_56Co_126.dat'
    foil2 = path + 'Fe_56Co_226.dat'
    foil3 = path + 'Fe_56Co_326.dat'
    list = [foil1, foil2, foil3]
    lambda_ = np.log(2)/(77.236*d)
    return list, lambda_

def Fe_48V():  #single decay, 48Cr not produced
    foil1 = path + 'Fe_48V_126.dat'
    foil2 = path + 'Fe_48V_226.dat'
    foil3 = path + 'Fe_48V_326.dat'

    list = [foil1, foil2, foil3]
    lambda_ = np.log(2)/(15.9735*h)
    return list, lambda_

def Fe_51Mn():   #single decay
    foil1 = path + 'Fe_51Mn_126.dat'
    foil2 = path + 'Fe_51Mn_226.dat'
    foil3 = path + 'Fe_51Mn_326.dat'

    list = [foil1, foil2, foil3]
    lambda_ = np.log(2)/(46.2*m)
    return list, lambda_

def Fe_51Cr():  #double decay from 51Mn
    foil1 = path + 'Fe_51Cr_126.dat'
    foil2 = path + 'Fe_51Cr_226.dat'
    foil3 = path + 'Fe_51Cr_326.dat'

    list = [foil1, foil2, foil3]
    #lambda_parent = np.log(2)/(46.2*m)
    lambda_ = np.log(2)/(27.7025*d)
    return list, lambda_#parent, lambda_daughter

def Fe_52mMn():  #not produced?
    foil1 = path + 'Fe_52mMn_126.dat'
    foil2 = path + 'Fe_52mMn_226.dat'
    foil3 = path + 'Fe_52mMn_326.dat'

    list = [foil1, foil2, foil3]
    lambda_ = np.log(2)/(21.1*m)
    return list, lambda_


def Fe_52Mn():  #single update:
    foil1 = path + 'Fe_52Mn_126.dat'
    foil2 = path + 'Fe_52Mn_226.dat'
    foil3 = path + 'Fe_52Mn_326.dat'

    list = [foil1, foil2, foil3]
    #lambda_parent = np.log(2)/(21.1*m)
    lambda_ = np.log(2)/(5.591*d)
    return list, lambda_#parent, lambda_daughter


def Fe_53Fe():   #Single decay - two step from isomer but half life is 2 m, so exluded
    foil1 = path + 'Fe_53Fe_126.dat'
    foil2 = path + 'Fe_53Fe_226.dat'
    foil3 = path + 'Fe_53Fe_326.dat'

    list = [foil1, foil2, foil3]
    lambda_ = np.log(2)/(8.51*m)
    return list, lambda_

def Fe_54Mn():   #single decay
    foil1 = path + 'Fe_54Mn_126.dat'
    foil2 = path + 'Fe_54Mn_226.dat'
    foil3 = path + 'Fe_54Mn_326.dat'

    list = [foil1, foil2, foil3]
    lambda_ = np.log(2)/(312.20*d)
    return list, lambda_


def Fe_55Co():  #single decay
    foil1 = path + 'Fe_55Co_126.dat'
    foil2 = path + 'Fe_55Co_226.dat'
    foil3 = path + 'Fe_55Co_326.dat'

    list = [foil1, foil2, foil3]
    lambda_ = np.log(2)/(17.53*h)
    return list, lambda_

def Fe_57Co():  #single decay
    foil1 = path + 'Fe_57Co_126.dat'
    foil2 = path + 'Fe_57Co_226.dat'
    foil3 = path + 'Fe_57Co_326.dat'

    list = [foil1, foil2, foil3]
    lambda_ = np.log(2)/(271.74*d)
    return list, lambda_


def Fe_58Co():   #single decay
    foil1 = path + 'Fe_58Co_126.dat'
    foil2 = path + 'Fe_58Co_226.dat'
    foil3 = path + 'Fe_58Co_326.dat'

    list = [foil1, foil2, foil3]
    lambda_ = np.log(2)/(70.86*d)
    return list, lambda_


def Fe_59Fe(): #single decay
    foil1 = path + 'Fe_59Fe_126.dat'
    foil2 = path + 'Fe_59Fe_226.dat'
    foil3 = path + 'Fe_59Fe_326.dat'

    list = [foil1, foil2, foil3]
    lambda_ = np.log(2)/(44.495*d)
    return list, lambda_

###Iridium foils####

def Ir_183Ta():  #single decay, 183Hf prob not produced

    #### NOte 183Hf must have been produced, something is feeding in!!
    foil1 = path + 'Ir_183Ta_177.dat'
    foil2 = path + 'Ir_183Ta_277.dat'
    foil3 = path + 'Ir_183Ta_377.dat'
    foil4 = path + 'Ir_183Ta_477.dat'
    foil5 = path + 'Ir_183Ta_577.dat'
    foil6 = path + 'Ir_183Ta_677.dat'
    foil7 = path + 'Ir_183Ta_777.dat'
    foil8 = path + 'Ir_183Ta_877.dat'
    foil9 = path + 'Ir_183Ta_977.dat'
    foil10 = path + 'Ir_183Ta_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_daughter = np.log(2)/(5.1*d)
    lambda_parent = np.log(2)/(1.018*h)
    return list, lambda_parent, lambda_daughter

def Ir_186Ta():  #single decay

    foil1 = path + 'Ir_186Ta_177.dat'
    foil2 = path + 'Ir_186Ta_277.dat'
    foil3 = path + 'Ir_186Ta_377.dat'
    foil4 = path + 'Ir_186Ta_477.dat'
    foil5 = path + 'Ir_186Ta_577.dat'
    foil6 = path + 'Ir_186Ta_677.dat'
    foil7 = path + 'Ir_186Ta_777.dat'
    foil8 = path + 'Ir_186Ta_877.dat'
    foil9 = path + 'Ir_186Ta_977.dat'
    foil10 = path + 'Ir_186Ta_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(3.7186*d)
    return list, lambda_

def Ir_186Re():  #single decay
    foil1 = path + 'Ir_186Re_177.dat'
    foil2 = path + 'Ir_186Re_277.dat'
    foil3 = path + 'Ir_186Re_377.dat'
    foil4 = path + 'Ir_186Re_477.dat'
    foil5 = path + 'Ir_186Re_577.dat'
    foil6 = path + 'Ir_186Re_677.dat'
    foil7 = path + 'Ir_186Re_777.dat'
    foil8 = path + 'Ir_186Re_877.dat'
    foil9 = path + 'Ir_186Re_977.dat'
    foil10 = path + 'Ir_186Re_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(3.7186*d)
    return list, lambda_

def Ir_187W():  #single decay, parents decay too fast
    foil1 = path + 'Ir_187W_177.dat'
    foil2 = path + 'Ir_187W_277.dat'
    foil3 = path + 'Ir_187W_377.dat'
    foil4 = path + 'Ir_187W_477.dat'
    foil5 = path + 'Ir_187W_577.dat'
    foil6 = path + 'Ir_187W_677.dat'
    foil7 = path + 'Ir_187W_777.dat'
    foil8 = path + 'Ir_187W_877.dat'
    foil9 = path + 'Ir_187W_977.dat'
    foil10 = path + 'Ir_187W_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(24.0*h)
    return list, lambda_


def Ir_188Pt():  #single decay
    foil1 = path + 'Ir_188Pt_177.dat'
    foil2 = path + 'Ir_188Pt_277.dat'
    foil3 = path + 'Ir_188Pt_377.dat'
    foil4 = path + 'Ir_188Pt_477.dat'
    foil5 = path + 'Ir_188Pt_577.dat'
    foil6 = path + 'Ir_188Pt_677.dat'
    foil7 = path + 'Ir_188Pt_777.dat'
    foil8 = path + 'Ir_188Pt_877.dat'
    foil9 = path + 'Ir_188Pt_977.dat'
    foil10 = path + 'Ir_188Pt_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(10.2*d)
    return list, lambda_


def Ir_188Ir(return_two_list=False):  #Double decay from 188Pt
    foil1 = path + 'Ir_188Ir_177.dat'
    foil2 = path + 'Ir_188Ir_277.dat'
    foil3 = path + 'Ir_188Ir_377.dat'
    foil4 = path + 'Ir_188Ir_477.dat'
    foil5 = path + 'Ir_188Ir_577.dat'
    foil6 = path + 'Ir_188Ir_677.dat'
    foil7 = path + 'Ir_188Ir_777.dat'
    foil8 = path + 'Ir_188Ir_877.dat'
    foil9 = path + 'Ir_188Ir_977.dat'
    foil10 = path + 'Ir_188Ir_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]

    lambda_parent = np.log(2)/(10.2*d)
    lambda_daughter = np.log(2)/(41.5*h)
    if return_two_list:
        list_parent = Ir_188Pt()[0]
        list_daughter = list
        return np.array((list_parent, list_daughter)), lambda_parent, lambda_daughter

    else:
        #return list, lambda_daughter, lambda_parent
        return list, lambda_daughter


def Ir_188mRe():   #single decay, 188W not observed?
    foil1 = path + 'Ir_188mRe_177.dat'
    foil2 = path + 'Ir_188mRe_277.dat'
    foil3 = path + 'Ir_188mRe_377.dat'
    foil4 = path + 'Ir_188mRe_477.dat'
    foil5 = path + 'Ir_188mRe_577.dat'
    foil6 = path + 'Ir_188mRe_677.dat'
    foil7 = path + 'Ir_188mRe_777.dat'
    foil8 = path + 'Ir_188mRe_877.dat'
    foil9 = path + 'Ir_188mRe_977.dat'
    foil10 = path + 'Ir_188mRe_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(18.59*m)
    return list, lambda_

def Ir_188Re():  #double decay 188mRe
    foil1 = path + 'Ir_188Re_177.dat'
    foil2 = path + 'Ir_188Re_277.dat'
    foil3 = path + 'Ir_188Re_377.dat'
    foil4 = path + 'Ir_188Re_477.dat'
    foil5 = path + 'Ir_188Re_577.dat'
    foil6 = path + 'Ir_188Re_677.dat'
    foil7 = path + 'Ir_188Re_777.dat'
    foil8 = path + 'Ir_188Re_877.dat'
    foil9 = path + 'Ir_188Re_977.dat'
    foil10 = path + 'Ir_188Re_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    #lambda_parent = np.log(2)/(18.59*m)
    lambda_ = np.log(2)/(17.003*h)
    return list, lambda_#parent, lambda_daughter

def Ir_189Pt():  #single decay
    foil1 = path + 'Ir_189Pt_177.dat'
    foil2 = path + 'Ir_189Pt_277.dat'
    foil3 = path + 'Ir_189Pt_377.dat'
    foil4 = path + 'Ir_189Pt_477.dat'
    foil5 = path + 'Ir_189Pt_577.dat'
    foil6 = path + 'Ir_189Pt_677.dat'
    foil7 = path + 'Ir_189Pt_777.dat'
    foil8 = path + 'Ir_189Pt_877.dat'
    foil9 = path + 'Ir_189Pt_977.dat'
    foil10 = path + 'Ir_189Pt_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(10.87*h)
    return list, lambda_


def Ir_189Ir():  #double decay from 189Pt
    foil1 = path + 'Ir_189Ir_177.dat'
    foil2 = path + 'Ir_189Ir_277.dat'
    foil3 = path + 'Ir_189Ir_377.dat'
    foil4 = path + 'Ir_189Ir_477.dat'
    foil5 = path + 'Ir_189Ir_577.dat'
    foil6 = path + 'Ir_189Ir_677.dat'
    foil7 = path + 'Ir_189Ir_777.dat'
    foil8 = path + 'Ir_189Ir_877.dat'
    foil9 = path + 'Ir_189Ir_977.dat'
    foil10 = path + 'Ir_189Ir_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_parent = np.log(2)/(10.87*h)
    lambda_daughter = np.log(2)/(13.2*d)
    #return list, lambda_parent, lambda_daughter
    # instead we try single decay and remove timepoints before 60 hours after eob. 
    return list, lambda_daughter

def Ir_189W():  #single decay
    foil1 = path + 'Ir_189W_177.dat'
    foil2 = path + 'Ir_189W_277.dat'
    foil3 = path + 'Ir_189W_377.dat'
    foil4 = path + 'Ir_189W_477.dat'
    foil5 = path + 'Ir_189W_577.dat'
    foil6 = path + 'Ir_189W_677.dat'
    foil7 = path + 'Ir_189W_777.dat'
    foil8 = path + 'Ir_189W_877.dat'
    foil9 = path + 'Ir_189W_977.dat'
    foil10 = path + 'Ir_189W_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(10.7*m)
    return list, lambda_

def Ir_189Re():     #double decay from 189W
    foil1 = path + 'Ir_189Re_177.dat'
    foil2 = path + 'Ir_189Re_277.dat'
    foil3 = path + 'Ir_189Re_377.dat'
    foil4 = path + 'Ir_189Re_477.dat'
    foil5 = path + 'Ir_189Re_577.dat'
    foil6 = path + 'Ir_189Re_677.dat'
    foil7 = path + 'Ir_189Re_777.dat'
    foil8 = path + 'Ir_189Re_877.dat'
    foil9 = path + 'Ir_189Re_977.dat'
    foil10 = path + 'Ir_189Re_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    #lambda_parent = np.log(2)/(10.7*m)
    lambda_ = np.log(2)/(24.3*h)
    return list, lambda_#daughter, lambda_parent

def Ir_190Ir():   #Difficult, because lacking isomer gamma lines.... for 2 states (3-step)
    foil1 = path + 'Ir_190Ir_177.dat'
    foil2 = path + 'Ir_190Ir_277.dat'
    foil3 = path + 'Ir_190Ir_377.dat'
    foil4 = path + 'Ir_190Ir_477.dat'
    foil5 = path + 'Ir_190Ir_577.dat'
    foil6 = path + 'Ir_190Ir_677.dat'
    foil7 = path + 'Ir_190Ir_777.dat'
    foil8 = path + 'Ir_190Ir_877.dat'
    foil9 = path + 'Ir_190Ir_977.dat'
    foil10 = path + 'Ir_190Ir_1077.dat'  
    lambda_ = np.log(2)/(11.78*d)
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    return list, lambda_

def Ir_190mRe():   #single decay
    foil1 = path + 'Ir_190mRe_177.dat'
    foil2 = path + 'Ir_190mRe_277.dat'
    foil3 = path + 'Ir_190mRe_377.dat'
    foil4 = path + 'Ir_190mRe_477.dat'
    foil5 = path + 'Ir_190mRe_577.dat'
    foil6 = path + 'Ir_190mRe_677.dat'
    foil7 = path + 'Ir_190mRe_777.dat'
    foil8 = path + 'Ir_190mRe_877.dat'
    foil9 = path + 'Ir_190mRe_977.dat'
    foil10 = path + 'Ir_190mRe_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(3.1*m)
    return list, lambda_


def Ir_190Re():
    foil1 = path + 'Ir_190Re_177.dat'
    foil2 = path + 'Ir_190Re_277.dat'
    foil3 = path + 'Ir_190Re_377.dat'
    foil4 = path + 'Ir_190Re_477.dat'
    foil5 = path + 'Ir_190Re_577.dat'
    foil6 = path + 'Ir_190Re_677.dat'
    foil7 = path + 'Ir_190Re_777.dat'
    foil8 = path + 'Ir_190Re_877.dat'
    foil9 = path + 'Ir_190Re_977.dat'
    foil10 = path + 'Ir_190Re_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    #lambda_parent = np.log(2)/(3.1*m)
    #lambda_daughter = np.log(2)/(3.2*h)
    lambda_ = np.log(2)/(3.2*h)
    return list, lambda_#daughter, lambda_parent


def Ir_191Pt():   #single decay
    foil1 = path + 'Ir_191Pt_177.dat'
    foil2 = path + 'Ir_191Pt_277.dat'
    foil3 = path + 'Ir_191Pt_377.dat'
    foil4 = path + 'Ir_191Pt_477.dat'
    foil5 = path + 'Ir_191Pt_577.dat'
    foil6 = path + 'Ir_191Pt_677.dat'
    foil7 = path + 'Ir_191Pt_777.dat'
    foil8 = path + 'Ir_191Pt_877.dat'
    foil9 = path + 'Ir_191Pt_977.dat'
    foil10 = path + 'Ir_191Pt_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(2.83*d)
    return list, lambda_

def Ir_191Os():   #single decay
    foil1 = path + 'Ir_191Os_177.dat'
    foil2 = path + 'Ir_191Os_277.dat'
    foil3 = path + 'Ir_191Os_377.dat'
    foil4 = path + 'Ir_191Os_477.dat'
    foil5 = path + 'Ir_191Os_577.dat'
    foil6 = path + 'Ir_191Os_677.dat'
    foil7 = path + 'Ir_191Os_777.dat'
    foil8 = path + 'Ir_191Os_877.dat'
    foil9 = path + 'Ir_191Os_977.dat'
    foil10 = path + 'Ir_191Os_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(15.4*d)
    return list, lambda_


def Ir_192Ir():  #single decay, too short and long half life of isomers
    foil1 = path + 'Ir_192Ir_177.dat'
    foil2 = path + 'Ir_192Ir_277.dat'
    foil3 = path + 'Ir_192Ir_377.dat'
    foil4 = path + 'Ir_192Ir_477.dat'
    foil5 = path + 'Ir_192Ir_577.dat'
    foil6 = path + 'Ir_192Ir_677.dat'
    foil7 = path + 'Ir_192Ir_777.dat'
    foil8 = path + 'Ir_192Ir_877.dat'
    foil9 = path + 'Ir_192Ir_977.dat'
    foil10 = path + 'Ir_192Ir_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(78.829*d)
    return list, lambda_


def Ir_193mPt(): #Single decay
    foil1 = path + 'Ir_193mPt_177.dat'
    foil2 = path + 'Ir_193mPt_277.dat'
    foil3 = path + 'Ir_193mPt_377.dat'
    foil4 = path + 'Ir_193mPt_477.dat'
    foil5 = path + 'Ir_193mPt_577.dat'
    foil6 = path + 'Ir_193mPt_677.dat'
    foil7 = path + 'Ir_193mPt_777.dat'
    foil8 = path + 'Ir_193mPt_877.dat'
    foil9 = path + 'Ir_193mPt_977.dat'
    foil10= path + 'Ir_193mPt_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(4.33*d)  #days to seconds
    return list, lambda_    #mon, single"

def Ir_194m2Ir(): #single decay
    foil1 = path + 'Ir_194m2Ir_177.dat'
    foil2 = path + 'Ir_194m2Ir_277.dat'
    foil3 = path + 'Ir_194m2Ir_377.dat'
    foil4 = path + 'Ir_194m2Ir_477.dat'
    foil5 = path + 'Ir_194m2Ir_577.dat'
    foil6 = path + 'Ir_194m2Ir_677.dat'
    foil7 = path + 'Ir_194m2Ir_777.dat'
    foil8 = path + 'Ir_194m2Ir_877.dat'
    foil9 = path + 'Ir_194m2Ir_977.dat'
    foil10 = path + 'Ir_194m2Ir_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_ = np.log(2)/(171.0*d)
    return list, lambda_

def Ir_194Ir():    #two step from 194m2Ir (193m1Ir too short half life)
    foil1 = path + 'Ir_194Ir_177.dat'
    foil2 = path + 'Ir_194Ir_277.dat'
    foil3 = path + 'Ir_194Ir_377.dat'
    foil4 = path + 'Ir_194Ir_477.dat'
    foil5 = path + 'Ir_194Ir_577.dat'
    foil6 = path + 'Ir_194Ir_677.dat'
    foil7 = path + 'Ir_194Ir_777.dat'
    foil8 = path + 'Ir_194Ir_877.dat'
    foil9 = path + 'Ir_194Ir_977.dat'
    foil10 = path + 'Ir_194Ir_1077.dat'
    list = [foil1, foil2, foil3, foil4, foil5, foil6, foil7, foil8, foil9, foil10]
    lambda_parent = np.log(2)/(171.0*d)
    lambda_daughter = np.log(2)/(19.28*h)
    return list, lambda_parent, lambda_daughter
