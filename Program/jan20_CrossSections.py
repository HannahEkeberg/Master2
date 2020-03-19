import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import N_A, elementary_charge
#print(elementary_charge)
import pandas as pd
import os

#from simulated_CrossSectionData im

from foil_info import *
from beam_current_FoilReact import *
from ZieglerFiles_new import ziegler_files
from des19_BeamCurrent import *
#from npat import Reaction, Library


from simulated_CrossSectionData import *


from scipy.constants import N_A, elementary_charge

#files,names = ziegler_files()

dir = 'CrossSections'
dir_fig = 'CrossSections/CrossSections_curves'
dir_csv = 'CrossSections/CrossSections_CSV'
if not os.path.exists(dir):
    os.mkdir(dir)
if not os.path.exists(dir_fig):
    os.mkdir(dir_fig)
if not os.path.exists(dir_csv):
    os.mkdir(dir_csv)

class CrossSections:

    def __init__(self,ziegler_file):
        self.ziegler_file = ziegler_file
        self.current_class = BeamCurrent(self.ziegler_file)
        #current_class = BeamCurrent(self.ziegler_file,)
        #self.I, self.sigma_I_est = self.current_class.current_for_CS()   #nA
        #print(self.I)

        ### Need the beam current to be in deuterions/s and not nA.
        ### Must convert beamcurrent by dividing by number of seconds
        ### Must also make number of deuterions instead of [As] --> /elementary_charge
        ### Must also change units for monitor CS from mb to cm^2: *1e-27
        #unit_factor = 3600*1e-27/elementary_charge
        #self.I = np.true_divide(self.I, unit_factor)   #?????
        #self.dI = np.true_divide(self.dI, unit_factor)


        #self.I = np.ones(10)*128.5
        self.E_Fe, self.E_Ni, self.E_Cu, self.E_Ir, self.dE_Fe, self.dE_Ni, self.dE_Cu, self.dE_Ir = self.current_class.current_for_CS(return_energies=True)


        #print(self.E_Ir)
        self.irr_time       = 3600.    #seconds
        self.sigma_irr_time = 3.       #seconds
        self.path = os.getcwd() + '/activity_csv/'



    def get_variables(self, react_func, target_func):
        #react_func is eg. Fe_56Co()
        #target_func is eg. Ir_foil()
        lambda_ = react_func[-1]
        mass_density = target_func[-2]
        sigma_mass_density = target_func[-1]
        return lambda_, mass_density, sigma_mass_density

    def mass_density(self,foil):
        if foil == 'Ir':
            n=10
            mol_mass_Ir = 192.217 #g/mol
            mass_density = np.array((55.174, 55.601, 55.643, 56.000, 55.161, 55.731, 56.685, 58.030, 56.669, 55.065))/1e3
            sigma_mass_density = np.array((0.053, 0.238, 0.121, 0.109, 0.081, 0.088, 0.085, 0.130, 0.043, 0.055))/1e3
            mass_density = (mass_density*N_A)/mol_mass_Ir #nuclei/cm^2
            sigma_mass_density = (sigma_mass_density*N_A)/mol_mass_Ir
            E = self.E_Ir; dE = self.dE_Ir
        elif foil == 'Fe':
            n = 3 #number of foils
            mol_mass_Fe = 55.8450 #g/mol
            mass_density = np.array((20.030, 20.017, 19.948))/1e3
            sigma_mass_density = np.array((0.110, 0.034, 0.114))/1e3
            mass_density = (mass_density*N_A)/mol_mass_Fe #nuclei/cm^2
            sigma_mass_density = (sigma_mass_density*N_A)/mol_mass_Fe
            E = self.E_Fe; dE = self.dE_Fe
        elif foil == 'Ni':
            n = 10
            mol_mass_Ni = 58.69340 #g/mol
            mass_density = np.array((22.772, 23.118,22.338,20.704,21.768,22.861,23.092,22.409,21.741,23.093))/1e3   #g/cm^2, divide by 1e3 to get g instead of mg.
            sigma_mass_density = np.array((0.138, 0.096, 0.066, 0.068, 0.045, 0.123,0.078, 0.124, 0.073, 0.024))/1e3 #g/cm^2
            mass_density = (mass_density*N_A)/mol_mass_Ni #nuclei/cm^2
            sigma_mass_density = (sigma_mass_density*N_A)/mol_mass_Ni
            E = self.E_Ni; dE = self.dE_Ni
        elif foil == 'Cu':
            n = 10
            mol_mass_Cu = 63.546 #g/mol
            mass_density = np.array((22.338, 22.325, 22.313, 22.284, 22.443, 22.396, 22.320, 22.401, 22.425, 22.314)) /1e3
            sigma_mass_density = np.array((0.048, 0.028, 0.043, 0.027, 0.028, 0.012, 0.014, 0.033, 0.041, 0.047))/1e3
            mass_density = (mass_density*N_A)/mol_mass_Cu #nuclei/cm^2
            sigma_mass_density = (sigma_mass_density*N_A)/mol_mass_Cu
            E = self.E_Cu; dE = self.dE_Cu
            #print(mass_density[-1])

        return mass_density, sigma_mass_density, E, dE



    def get_var(self,react_func, foil, filename, n, reaction):#, plot_CS=False):
        ###  example :  cross_section(Cu_57Ni, 'Cu', 'Cu_57Ni.csv/', 10)
        lamb = react_func[-1]
        #print(react_func)
        #print(lamb, "in get_var")
        #print(lamb)
        mass_density, sigma_mass_density, E, dE = self.mass_density(foil)
        E  = np.flip(E)
        dE = np.flip(dE)
        A0 = np.zeros(n)
        sigma_A0 = np.zeros(n)
        #CS = np.zeros(n)
        #sigma_CS = np.zeros(n)
        filename = self.path + filename
        for i in range(n):
            A0_val = np.genfromtxt(filename, delimiter=',', usecols=[i])
            A0[i] = A0_val[0]
            sigma_A0[i] = A0_val[1]
            #import math
            #if math.isnan(A0[i]):
            #if isinstance(A0[i], NaN):
                #A0[i]=0

        return lamb, mass_density, sigma_mass_density, E, dE, A0, sigma_A0

    """
    def exfordata_npat(self):
        ### Search the TENDL-2015 neutron library for reactions producing 225RA from 226RA
        f, ax = None, None
        for lb in ['tendl_d_rp']:
                rx = Reaction('63CU(d,x)64CUg', lb)
                print(rx)
                f, ax = rx.plot(f=f, ax=ax, show=False, label='library', title=True)
                print(f)
                print(ax)

        plt.show()
    """


    def make_CS(self, react_func, foil, filename, n ,reaction, BC_csv_filename, Z, A, file_ending='.tot'):
        lamb, mass_density, sigma_mass_density, E, dE, A0, dA0 = self.get_var(react_func, foil, filename, n, reaction)
        #lamb, mass_density, sigma_mass_density, E, dE, A0, sigma_A0 = self.get_var(react_func, foil, filename, n, reaction)

        


        #I, dI = self.current_class.current_for_CS()   #nA
        #I_Fe, I_Ni, I_Cu, sigma_I = self.current_class.current_for_CS(mon_test=True)

        #print("I", I)
        #print("I_Ni", I_Ni)

        #I = I_Ni; dI=sigma_I


        ### The weighted average beam current  - made by Andrew

        I = np.genfromtxt(BC_csv_filename, delimiter=',', usecols=[1])
        #print(I)
        #weighted_average_beam = weighted_average_beam[::-1]
        dI = np.genfromtxt(BC_csv_filename, delimiter=',', usecols=[2])


        #print("I after", I)
        #print("I_Ni after", I_Ni)
        #I = self.I; dI = self.sigma_I_est
        CS, dCS= self.cross_section_calc(n, A0, dA0, mass_density, sigma_mass_density, I, dI, lamb, reaction)
        
        self.modelling('Tendl', foil, Z, A, reaction, file_ending)
        self.modelling('Talys', foil, Z, A, reaction, file_ending)
        self.modelling('Exfor', foil, Z, A, reaction, file_ending)
        #self.modelling('Alice', foil, Z, A, reaction, file_ending)

        if foil=='Ir':
            E = self.E_Ir; dE = self.dE_Ir
        elif foil=='Cu':
            E = self.E_Cu; dE = self.dE_Cu
        elif foil=='Ni':
            E = self.E_Ni; dE = self.dE_Ni
        elif foil=='Fe':
            E = self.E_Fe; dE = self.dE_Fe


        print("     E     ", "    CS    " )
        print(np.vstack((E,CS)).T)

        dE_tot = dE[0]+dE[1]
        csv_save_array = np.vstack((E, dE_tot, CS, dCS)).T
        #print(csv_save_array)
        path_to_cs_csv = os.getcwd() + '/CrossSections/CrossSections_csv/'

        np.savetxt(path_to_cs_csv  + reaction, csv_save_array, delimiter=',', header='E, dE, CS, dCS', fmt="%s"  )#, %.6f, %.6f")
        

        CS = [float('nan') if x==0 else x for x in CS]
        plt.errorbar(E, CS, marker='P', color='darkred',linewidth=0.0001, xerr=dE, yerr=dCS, elinewidth=1.0, capthick=1.0, capsize=3.0, label='this data')
        
        self.plot_CrossSections(reaction, A, foil)

        return E, dE, CS, dCS


    def modelling(self, model, foil, Z, A, reaction, file_ending):
        #print("modelling:", model, foil )
        SimCS = SimCrossSectionData() 
        if model == 'Alice':    # needs to come before chaning Z and A, since using the inputvalues
            try:
                E, CS = SimCS.ALICE(foil, A, Z)
                plt.plot(E, CS, label='Alice', color='green', linestyle=':')
            except:
                print("no Alice file found")
        if len(Z)==2: 
            Z = '0'+Z
        if len(A)==2: 
            A = '0'+A
        if model== 'Talys':
            try:
                E, CS = SimCS.TALYS(foil, A, Z, file_ending)
                plt.plot(E, CS, label='Talys', linestyle='-.', color='orange')
                #return E, CS
            except:
                print("no talys file found")
        elif model == 'Exfor':
            try:
                E, dE, CS, dCS, author =  SimCS.EXFOR(reaction)
                unique_author = [] 
                for auth in author: 
                    if auth not in unique_author:
                        unique_author.append(auth)


                colors = ['mediumpurple', 'cyan', 'palevioletred', 'darkorange', 'forestgreen', 'orchid', 'dodgerblue', 'lime', 'crimson', 'indianred']
                for i in range(len(E)):
                    for j in range(len(unique_author)):
                        if author[i]==unique_author[j]:
                            plt.errorbar(E[i], CS[i], marker='.', color=colors[j], markersize=1, linewidth=0.0001, xerr=dE[i], yerr=dCS[i], elinewidth=0.25, capthick=0.25, capsize=3.0, label=unique_author[j])
    

            except:
                print("No exfor file found")
                pass

        elif model == 'Tendl':
            #E, CS = SimCS.Tendl(foil, A, Z, file_ending)
            try:
                E, CS = SimCS.Tendl(foil, A, Z, file_ending)
                if E is not 0:
                    plt.plot(E, CS, label='Tendl', linestyle='--', color='blue')
            except: 
                print("Tendl files not found. Check file ending or fileproblem")
                pass
        elif model == 'Empire':
            pass 
        elif model == 'Coh':
            pass
        else:
            print("Provide a model")
        #return E, CS


    def cross_section_calc(self, n, A0, dA0, mass_density, sigma_mass_density, I, dI, lamb, reaction):
        CS = np.zeros(n)
        dCS = np.zeros(n)
        #dI = np.ones(n)*dI
        dlamb = lamb*0.001 #typical percent uncertainty
        #E =
        """
        print("A0: ", A0)
        print("dA0: ", dA0)
        print("% A0: ", 100*dA0/A0)
        print("I: ", I)
        print("dI: ", dI)
        print("% I: ", 100*dI/I)
        print("mass_density: ", mass_density)
        print("sigma_mass_density: ", sigma_mass_density)
        print("% mass_density: ", 100*sigma_mass_density/mass_density)
        print("lamb: ", lamb)
        print("dlamb: ", dlamb)
        print("% lamb: ", 100*dlamb/lamb)
        print("self.irr_time: ", self.irr_time)
        
        """

        for j in range(n):

            CS[j] = A0[j] / (mass_density[j] * I[j]*(1/(elementary_charge*1e9))   *(1-np.exp(-lamb*self.irr_time)))/(1e-27)   #mb  ###1 barn = 1e-24 cm^2
            #print(CS[j])
            if A0[j]==0:
                dCS[j]=0
            else:
                dCS[j] = CS[j]*np.sqrt( (dA0[j]/A0[j])**2 + (dI[j]/I[j])**2 + (sigma_mass_density[j]/mass_density[j])**2 + (dlamb/lamb)**2    )

            #path = os.getcwd() + '/CrossSections/'
            #np.savetxt(path + 'CrossSections_CSV/{}_CS'.format(reaction))

        #print(CS)
        #print(dCS, "******************")
        #print("% CS", 100*dCS/CS)
        return(CS, dCS)



    def mon_CS_test(self, react_func, foil, filename, n, reaction,scaling_parameter, BC_csv_filename):
        #print("*")
        I_Fe, I_Ni, I_Cu, sigma_I = self.current_class.current_for_CS(mon_test=True)
        sigma_I = np.ones(len(I_Ni))*sigma_I






        ### The weighted average beam current  - made by Andrew

        # weighted_average_beam = np.genfromtxt(BC_csv_filename, delimiter=',', usecols=[1])
        # #weighted_average_beam = weighted_average_beam[::-1]
        # sigma_weighted_average_beam = np.genfromtxt(BC_csv_filename, delimiter=',', usecols=[2])

        # I_Fe = weighted_average_beam[:3]; sigma_I_Fe=sigma_weighted_average_beam[:3]

        # I_Ni = weighted_average_beam; sigma_I=sigma_weighted_average_beam
        # I_Cu = weighted_average_beam; sigma_I=sigma_weighted_average_beam

        #print(sigma_I) 
        #unit_factor = 3600*1e-27/elementary_charge
        #unit_factor=1
        #I_Fe = np.true_divide(I_Fe, unit_factor)   #?????
        #I_Ni = np.true_divide(I_Ni, unit_factor)   #?????
        #I_Cu = np.true_divide(I_Cu, unit_factor)   #?????
        

        #I, sigma_I = self.current_class.current_for_CS()

        #print("I", I)
        #print("I_Ni", I_Ni)
        #I_Fe = I
        #I_Ni = I
        #I_Cu = I

        Cumulative_flag=False


        #sigma_I /= unit_factor

        lamb, mass_density, sigma_mass_density, E, dE, A0, sigma_A0 = self.get_var(react_func, foil, filename, n, reaction)
        path_to_monitor_data = os.getcwd() + '/../Monitor_datafiles/'


        if reaction=='Fe_56Co':
            sigma_I = sigma_I[:3]
            CS, dCS = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Fe, sigma_I, lamb, reaction)
            E = self.E_Fe; dE = self.dE_Fe
            filename =  path_to_monitor_data+'fed56cot/fed56cot.txt'
            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)

            self.modelling('Exfor', 'Fe', '26', '27', 'Fe_56Co', '.tot')

            #sigma_Cs = np.loadtxt(filename, usecols=[2], skiprows=6)
        if reaction=='Ni_61Cu':
            CS, dCS = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Ni, sigma_I, lamb, reaction)
            E = self.E_Ni;dE = self.dE_Ni
            filename =  path_to_monitor_data+'nid61cut/nid61cut.txt'
            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)

            self.modelling('Exfor', 'Ni', '28', '61', 'Ni_61Cu', '.tot')

        if reaction=='Ni_56Co':
            CS_56Co, dCS_56Co = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Ni, sigma_I, lamb, reaction)
            E = self.E_Ni;dE = self.dE_Ni
            filename =  path_to_monitor_data+'nid56cot/nid56cot.txt'

            lamb_, mass_density_, sigma_mass_density_, E_, dE_, A0_, sigma_A0_ = self.get_var(Ni_56Ni(), 'Ni', 'Ni_56Ni.csv', 10, 'Ni_56Ni')
            CS_56Ni, dCS_56Ni = self.cross_section_calc(n, A0_, sigma_A0_, mass_density, sigma_mass_density, I_Ni, sigma_I, lamb_, 'Ni_56Ni')
            self.modelling('Exfor', 'Ni', '28', '56', 'Ni_56Co', '.tot')
            CS = CS_56Co +  CS_56Ni

            Cumulative_flag = True

            dCS = CS*np.sqrt( (dCS_56Co/CS_56Co)**2 + (dCS_56Ni/CS_56Ni)**2)

            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)
            #print("     56Ni     ", "    56Co   " )
            #print(np.vstack((CS_56Ni,CS_56Co)).T)

        if reaction=='Ni_58Co':
            CS_58Co, dCS_58Co = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Ni, sigma_I, lamb, reaction)
            E = self.E_Ni;dE = self.dE_Ni
            filename =  path_to_monitor_data+'nid58cot/nid58cot.txt'
            self.modelling('Exfor', 'Ni', '28', '58', 'Ni_58Co', '.tot')

            lamb_, mass_density_, sigma_mass_density_, E_, dE_, A0_, sigma_A0_ = self.get_var(Ni_58mCo(), 'Ni', 'Ni_58mCo.csv', 10, 'Ni_58mCo')
            CS_58mCo, dCS_58mCo = self.cross_section_calc(n, A0_, sigma_A0_, mass_density, sigma_mass_density, I_Ni, sigma_I, lamb_, 'Ni_58mCo')

            Cumulative_flag = True

            CS = CS_58mCo +  CS_58Co
            dCS = CS*np.sqrt( (dCS_58Co/CS_58Co)**2 + (dCS_58mCo/CS_58mCo)**2)
            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)
            print("     58Co     ", "    58mCo   " )
            print(np.vstack((CS_58Co,CS_58mCo)).T)
        if reaction=='Cu_62Zn':
            CS, dCS = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Cu, sigma_I, lamb, reaction)
            E = self.E_Cu;dE = self.dE_Cu
            filename =  path_to_monitor_data+'cud62znt/cud62znt.txt'
            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)
            self.modelling('Exfor', 'Cu', '29', '62', 'Cu_62Zn', '.tot')
        if reaction=='Cu_63Zn':
            CS, dCS = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Cu, sigma_I, lamb, reaction)
            E = self.E_Cu;dE = self.dE_Cu
            filename =  path_to_monitor_data+'cud63znt/cud63znt.txt'
            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)
            self.modelling('Exfor', 'Cu', '29', '63', 'Cu_63Zn', '.tot')
        if reaction=='Cu_65Zn':
            CS, dCS = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Cu, sigma_I, lamb, reaction)
            E = self.E_Cu;dE = self.dE_Cu
            filename =  path_to_monitor_data+'cud65znt/cud65znt.txt'
            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)
            self.modelling('Exfor', 'Cu', '29', '65', 'Cu_65Zn', '.tot')


        #print(len(CS))
        #print(E)
        #plt.plot(E_mon, Cs_mon, label='monitor data')
        #plt.plot(E_)
        #self.plot_CrossSections(E, dE, CS, dCS, reaction)


        #self.setting_plotvalues(E_mon, 0, Cs_mon, 0, label='monitor data', )
        print(scaling_parameter)

        #if reaction == 'Ni_56Co' or reaction=='Ni_58Co':

        if Cumulative_flag:
            label = 'monitor data (cumulative)'
        else:
            label = 'monitor data'
        plt.plot(E_mon, Cs_mon, label=label)
        #self.setting_plotvalues(E, dE, CS, dCS, 'this data')
        plt.errorbar(E, CS, marker='P', markersize=4, color='red', linewidth=0.0001, xerr=dE, yerr=dCS, elinewidth=0.5, capthick=0.25, capsize=3.0, label=label )
        self.plot_CrossSections(reaction)

        #plt.plot(E_mon, Cs_mon, label='monitor data')
        #plt.plot(E, CS, 'o', label='this data')
        #plt.xlabel('Energy (MeV)')
        #plt.ylabel('Cross section (mb)')
        #plt.errorbar(E, CS, color='green', linewidth=0.001, xerr=dE,  yerr=dCS, elinewidth=0.5, ecolor='k', capthick=0.5 )
        #plt.title('Cross section for reaction {}'.format(reaction))
        #path_to_cs_figs = os.getcwd() + '/CrossSections/CrossSections_curves/'
        #plt.savefig(path_to_cs_figs + reaction +'{}.png'.format(scaling_parameter), dpi=300)
        #plt.legend()
        #plt.show()




    def setting_plotvalues(self, E, dE, CS, dCS, label):
        #print(len(E),len(dE), len(CS), len(dCS))
        #E = np.flip(E)#E.reverse()
        #dE = np.flip(dE)#dE.reverse()
        #plt.plot(E,CS, '.', label=label)
        #plt.errorbar(E, CS, color='green', linewidth=0.001, xerr=dE,  yerr=dCS, elinewidth=0.5, ecolor='k', capthick=0.5 )
        plt.errorbar(E, CS, marker='.', markersize=1, linewidth=0.0001, xerr=dE, yerr=dCS, elinewidth=0.25, capthick=0.25, capsize=3.0, label=label )
        #plt.show()



    def plot_CrossSections(self,  reaction, A=1, foil='foil'):

        #plt.plot(E_mon, Cs_mon, label='monitor data')
        #plt.plot(E, CS, 'o', label='this data')
        #fig, ax = plt.subplots()
        plt.xlabel('Energy (MeV)')
        plt.ylabel('Cross section (mb)')

    
        #title_name = r'$^\text{nat}' + foil + '(d,x)' + r'$^{}$'.format(A)
        plt.title('Cross section for reaction {}'.format(reaction))
        path_to_cs_figs = os.getcwd() + '/CrossSections/CrossSections_curves/'
        #plt.savefig(path_to_cs_figs + reaction +'{}.png'.format(scaling_parameter), dpi=300)
        #handles, labels = ax.get_legend_handles_labels()
        #unique = [(h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]]
        #ax.legend(*zip(*unique))
        #plt.legend()

        from collections import OrderedDict
        #import matplotlib.pyplot as plt

        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys(),fontsize='small')

        plt.gca().set_xlim(left=0, right=50)
        plt.savefig(path_to_cs_figs + reaction+'.png', dpi=300)
        plt.show()




if __name__ == '__main__':
    print("main")
else:
    print("jan20_CrossSections.py")


"""
    def plot_CrossSections(self, E, CS, reaction):

        plt.plot(E, CS, '.')
        plt.errorbar(E, CS, color='green', linewidth=0.001,  yerr=dCs, elinewidth=0.5, ecolor='k', capthick=0.5 )
        plt.xlabel('Beam energy (MeV)')
        plt.ylabel('Cross section (mb)')
        plt.title('Cross section for reaction {}_{}'.format(reaction))
        #path = os.getcwd()
        #plt.savefig(path + '/CrossSections/CrossSections_curves/{}_CS.png'.format(reaction),dpi=300)
        #plt.show()


"""













#CS = CrossSections(files[0])
#path = os.getcwd() + '/activity_csv/'
#file = path + 'Ni_61Cu.csv'

#file = path + 'Cu_57Ni.csv/'
#x = CS.cross_section(Cu_57Ni(), 'Cu', 'Cu_57Ni.csv', 10)

#x = CS.cross_section(Ir_193mPt(), 'Ir', 'Ir_193mPt.csv', 10, 'Ir_193mPt', plot_CS=True)
#x = CS.cross_section(Cu_57Ni(), 'Cu', 'Cu_57Ni.csv', 10, 'Cu_57Ni', plot_CS=True)
#x = CS.cross_section(Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu', plot_CS=True)
#print(x)

#CS.Get_CS(file, 10)
#CS.Cs(Ir_193mPt(), Ir_foil())
#CS.cross_section(file, 10)








"""
#from beam_current import *

path = os.getcwd() + '/activity_csv/'


I_weighted =125 #nA
irr_time = 3600 #seconds
lamb = Ni_56Ni()[-1]

def Fe():
    mol_mass_Fe = 55.8450 #g/mol
    mass_density = np.array((20.030, 20.017, 19.948))/1e3
    sigma_mass_density = np.array((0.110, 0.034, 0.114))/1e3
    mass_density = (mass_density*N_A)/mol_mass_Fe #nuclei/cm^2
    sigma_mass_density = (sigma_mass_density*N_A)/mol_mass_Fe
    return mass_density

def Cu():
    mol_mass_Cu = 63.546 #g/mol
    mass_density = np.array((22.338, 22.325, 22.313, 22.284, 22.443, 22.396, 22.320, 22.401, 22.425, 22.314)) /1e3
    sigma_mass_density = np.array((0.048, 0.028, 0.043, 0.027, 0.028, 0.012, 0.014, 0.033, 0.041, 0.047))/1e3
    mass_density = (mass_density*N_A)/mol_mass_Cu #nuclei/cm^2
    sigma_mass_density = (sigma_mass_density*N_A)/mol_mass_Cu
    return mass_density

def Ni():
    mol_mass_Ni = 58.69340 #g/mol
    mass_density = np.array((22.772, 23.118,22.338,20.704,21.768,22.861,23.092,22.409,21.741,23.093))/1e3   #g/cm^2, divide by 1e3 to get g instead of mg.
    sigma_mass_density = np.array((0.138, 0.096, 0.066, 0.068, 0.045, 0.123,0.078, 0.124, 0.073, 0.024))/1e3 #g/cm^2
    mass_density = (mass_density*N_A)/mol_mass_Ni #nuclei/cm^2
    sigma_mass_density = (sigma_mass_density*N_A)/mol_mass_Ni
    return mass_density

def weighted_beam_current(E):
    return 1.54991205 * E + 90.99143333

def cross_section(filename):
    mass_density = Ni()
    n = 10
    A0_array = np.zeros(n)
    sigma = np.zeros(n)
    for i in range(n):
        A0 = np.genfromtxt(filename, delimiter=',', usecols=[i])
        #A0_array[i] = A0[0]
    #print(A0_array)
    #for j in range(n):
    #    sigma[j] = A0_array[j] / (mass_density[j] * I_weighted*(1-np.exp(-lamb*irr_time)))   #I_weighted is suppose to be weighed chi squared for beam current.
    #return sigma

#cross_section('Ni_57Co.csv')
def plot_CrossSections(x, y, reaction):
    plt.plot(x,y, '.')
    plt.plot(x,y, '--', linewidth=0.1)
    plt.xlabel('Beam energy (MeV)')
    plt.ylabel('Cross section (barns)')
    plt.title('Cross section for reaction {}'.format(reaction))
    plt.savefig('{}_CS'.format(reaction), dpi=300)
    plt.show()

#E_mean =
#E = weighted_average_beam_energy(E_mean)
E = np.linspace(0,33,10)
#CS = cross_section('Cu_65Zn.csv')
#CS = cross_section('Ir_193mPt.csv')
#CS = cross_section('Ni_56Ni.csv')
#CS = cross_section('Ni_58Co.csv')
#CS = cross_section('Ni_58mCo.csv')
#CS = cross_section('Ni_56Co.csv')
#CS = cross_section('Ni_62Zn.csv')
#CS = cross_section('Ni_61Cu.csv')



CS = cross_section(path+'Ir_193mPt.csv')
#plot_CrossSections(E,CS, 'Ni_57Co')
"""
