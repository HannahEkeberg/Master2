import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import N_A, elementary_charge
#print(elementary_charge)
import pandas as pd
import os


import math 
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
        #print("Relative uncertainty in activity:", sigma_A0/A0*100)

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




    def make_CS(self, react_func, foil, filename, n ,reaction, BC_csv_filename, Z, A,  feeding=None, file_ending='.tot', save_text=True, independent=True, ylimit=None, isomer_state=None, CS_colonne_ALICE=4,BR=0, reaction_parent=None, force_legend=False, title_on_plot=False):
        lamb, mass_density, sigma_mass_density, E, dE, A0, dA0 = self.get_var(react_func, foil, filename, n, reaction)
        #lamb, mass_density, sigma_mass_density, E, dE, A0, sigma_A0 = self.get_var(react_func, foil, filename, n, reaction)

        print("Relative uncertainty in activity: ", dA0/A0*100)
        print("Relative uncertainty in m.d: ", sigma_mass_density/mass_density*100)


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

        print("Relative uncertainty in beam current: ", dI/I*100)


        #print("I after", I)
        #print("I_Ni after", I_Ni)
        #I = self.I; dI = self.sigma_I_est
        CS, dCS= self.cross_section_calc(n, A0, dA0, mass_density, sigma_mass_density, I, dI, lamb, reaction)
        
        print("Relative uncertainty in cross section: ", dCS/CS*100)
        #self.modelling('Tendl', foil, Z, A, reaction, file_ending)
        #self.modelling('Talys', foil, Z, A, reaction, file_ending)
        #self.modelling('Exfor', foil, Z, A, reaction, file_ending)
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

        for i in range(len(CS)):

            # print("E: {:.2f} {:.2f}".format(E[i], dE[0,1]))

            print("{:.1f} ({:.1f})".format(CS[i], dCS[i]))

        # print(np.vstack(({:.2f}, {:.2f}, {:.2f}).format(E, CS, dCS)).T)
    
        #print(E)
        #print(np.vstack((E, CS)).T)
        #print(np.vstack((dE, dCS)).T)
        print(np.vstack((E, dE)).T)

        dE_tot = dE[0]+dE[1]
        csv_save_array = np.vstack((E, dE[0], dE[1], CS, dCS)).T
        #print(csv_save_array)
        path_to_cs_csv = os.getcwd() + '/CrossSections/CrossSections_csv/'

        if independent==False:

            type_CS='_cumulative'
        else:
            type_CS='_independent'

        if save_text==True:
            np.savetxt(path_to_cs_csv  + reaction + type_CS, csv_save_array, delimiter=',', header='E, dE_l, dE_r, CS, dCS', fmt="%s"  )#, %.6f, %.6f")
        



        CS = [float('nan') if x==0 else x for x in CS]
        #print(type(A))
        #plt.errorbar(E, CS, marker='P', color='darkred',linewidth=0.0001, xerr=dE, yerr=dCS, elinewidth=1.0, capthick=1.0, capsize=3.0, label='this data')
        


        if isomer_state==None:
            state=''
        else:
            state=isomer_state

        nucl = reaction[-2]
        numbs = ['1', '2', '3', '4', '5', '6', '7', '8','9']
        if independent==True: 
            #nucl = reaction[-2]
            #numbs = ['1', '2', '3', '4', '5', '6', '7', '8','9']
            if nucl in numbs:
                title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A+state) + reaction[-1:]  + ' - Independent' 
            else:
                title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A+state) + reaction[-2:]  + ' - Independent' 
        else:
            if nucl in numbs: 
                title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A+state) + reaction[-1:]  + ' - Cumulative' 
            else:
                title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A+state) + reaction[-2:]  + ' - Cumulative' 
        
        #print(A+state)
        #print(force_legend)
        #print(dE)
        if save_text==True:
            plt.errorbar(E, CS, marker='P', color='darkred',linewidth=0.0001, xerr=dE, yerr=dCS, elinewidth=1.0, capthick=1.0, capsize=3.0, label='This Work')
            self.modelling('Tendl', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state)
            self.modelling('Talys', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state)
            self.modelling('Exfor', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state)
            self.modelling('Alice', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state)

            if reaction_parent!=False:
                self.modelling('CoH', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state, reaction_parent=reaction_parent)
                self.modelling('Empire', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state, reaction_parent=reaction_parent)
                
            else:
                self.modelling('CoH', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state, reaction_parent=None)
                self.modelling('Empire', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state, reaction_parent=None)
            self.plot_CrossSections(reaction, title, A, foil, ylimit, legend_force=force_legend)
        #print(E)
        #print("in cs calc, print force_legend")
        return E, dE, CS, dCS


    def make_CS_subtraction(self, end_reaction,  foil, n, csv_filename, react_func_parent, reaction_parent, filename_parent, Z_parent, A_parent, react_func_daughter, reaction_daughter, filename_daughter, Z_daughter, A_daughter, ylimit, independent, BR_daughter=1.0, isomer_state=None, file_ending='.tot', CS_colonne_ALICE=4, save_text=True, feeding=None, force_legend=False, title_on_plot=False):  # Necessary when subtracting
        
        E, dE, CS_parent, dCS_parent = self.make_CS(react_func_parent, foil, filename_parent, n, reaction_parent, csv_filename, Z_parent, A_parent, save_text=False)
        E, dE, CS_daughter, dCS_daughter = self.make_CS(react_func_daughter, foil, filename_daughter, n, reaction_daughter, csv_filename, Z_daughter, A_daughter,  save_text=False)

        #for i in range(n):
        #print("***")
        #S_parent = np.nan_to_num(CS_parent)
        #print(CS_parent)
        #CS_daughter = np.nan_to_num(CS_daughter)
        #print(CS_daughter)



            #if np.isnan(CS_parent[i]):
                
            #if np.isnan(CS_daughter[i]):
             #   CS_daughter[i]==0

        #print("**")
        #print(CS_parent)
        #print(CS_daughter)
        new_CS = []; new_dCS=[]
        if independent==True:
            for i in range(len(CS_parent)):
                #new_CS.append(CS_parent[i]-CS_daughter[i]*BR_daughter)
                #new_dCS.append(dCS_parent[i]-dCS_daughter[i]*BR_daughter)
                if CS_daughter[i]==0:
                    new_CS.append(0)
                    new_dCS.append(0)
                else:
                    if np.isnan(CS_parent[i]):
                        #print("Yes")
                        #print(i, CS_parent[i], "1")
                        #CS_parent[i]==0
                        new_CS.append(CS_daughter[i])       #here daughter is cumulative. Want independent CS
                    elif np.isnan(CS_daughter[i]):
                        #print(i, CS_daughter[i], "2")
                        new_CS.append(CS_parent[i]*BR_daughter) 
                    else:
                        print(i, CS_parent[i])
                        new_CS.append(CS_daughter[i]-CS_parent[i]*BR_daughter)       #here daughter is cumulative. Want independent CS
                    # new_dCS.append(dCS_daughter[i]-dCS_parent[i]*BR_daughter)
                    new_dCS.append(np.sqrt(dCS_daughter[i]**2+ (dCS_parent[i])**2*BR_daughter))
                    #print(CS_daughter[i], CS_parent[i]*BR_daughter) 
                    #print(CS_daughter[i]-CS_parent[i]*BR_daughter)
        elif independent==False:  
            for i in range(len(CS_parent)):
                #new_CS.append(CS_parent[i]-CS_daughter[i]*BR_daughter)
                #new_dCS.append(dCS_parent[i]-dCS_daughter[i]*BR_daughter)
                new_CS.append(CS_daughter[i]+CS_parent[i]*BR_daughter)        # here daughter is independent. Want cumulative CS
                new_dCS.append(np.sqrt(dCS_daughter[i]**2+ (dCS_parent[i])**2*BR_daughter))

        if end_reaction == 'daughter':
            reaction = reaction_daughter
            Z = Z_daughter; A= A_daughter
        elif end_reaction == 'parent':
            reaction = reaction_parent
            Z = Z_parent; A= A_parent

        if isomer_state==None:
            state=''
        else:
            state=isomer_state

        if independent==False:
            type_CS='_cumulative'
        elif independent==True:
            type_CS='_independent'
        elif isinstance(independent, str):
            type_CS = independent
        #print(type_CS)
        nucl = reaction[-2]
        numbs = ['1', '2', '3', '4', '5', '6', '7', '8','9']
        if nucl in numbs: 
            title = r'$^{nat}$' + foil +'(d,x)' + r'$^{{ {} }}$'.format(A+state) + reaction[-1:]  + ' - ' + type_CS[1:] 
        else:
            title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A+state) + reaction[-2:]  + ' - ' + type_CS[1:] 
        if title_on_plot!=False:
            title = title_on_plot
        """    
        #plt.errorbar(E, CS_parent, marker='.', color='blue',linewidth=0.0001, xerr=dE, yerr=dCS_parent, elinewidth=1.0, capthick=1.0, capsize=3.0, label='Parent')
        plt.errorbar(E, CS_daughter, marker='.', color='green',linewidth=0.0001, xerr=dE, yerr=dCS_daughter, elinewidth=1.0, capthick=1.0, capsize=3.0, label='Cumulative')    
        plt.errorbar(E, new_CS, marker='P', color='darkred',linewidth=0.0001, xerr=dE, yerr=new_dCS, elinewidth=1.0, capthick=1.0, capsize=3.0, label='Independent')

        self.modelling('Tendl', foil, Z, A, reaction, file_ending)
        self.modelling('ALICE', foil, Z, A, reaction, file_ending, CS_colonne=CS_colonne_ALICE)
        self.modelling('Talys', foil, Z, A, reaction, file_ending)
        #self.modelling('Exfor', foil, Z_parent, A_parent, reaction_parent, file_ending)
        #self.modelling('Exfor', foil, Z_daughter, A_daughter, reaction_daughter, file_ending)
        plt.legend()
        plt.title(title)
        #self.modelling('Alice', foil, Z, A, reaction, file_ending)
        plt.show()
        """
        #self.plot_CrossSections(reaction, title, A, foil, ylimit)  

        dE_tot = dE[0]+dE[1]
        #print("*****")
        #print(len(dE_tot))
        #print(len(E))
        #print(len(new_CS))
        #print(len(new_dCS))
        print("********" ,reaction_daughter)
        for i in range(len(new_CS)):
            print("{:.1f} ({:.1f})".format(new_CS[i], new_dCS[i]))



        csv_save_array = np.vstack((E, dE_tot, new_CS, new_dCS)).T
        #print(csv_save_array)
        path_to_cs_csv = os.getcwd() + '/CrossSections/CrossSections_csv/'

        #for i in range(len(new_CS))
        if save_text==True:
            CS_daughter = [float('nan') if x==0 else x for x in CS_daughter]
            CS_parent = [float('nan') if x==0 else x for x in CS_parent]
            new_CS = [float('nan') if x==0 else x for x in new_CS]
            np.savetxt(path_to_cs_csv  + reaction + type_CS, csv_save_array, delimiter=',', header='E, dE, CS, dCS', fmt="%s"  )#, %.6f, %.6f")
            if independent==True:
                plt.errorbar(E, CS_daughter, marker='.', color='green',linewidth=0.0001, xerr=dE, yerr=dCS_daughter, elinewidth=0.5, capthick=1.0, capsize=3.0, label=reaction_daughter + ' - Cumulative')    
                plt.errorbar(E, new_CS, marker='P', color='darkred',linewidth=0.0001, xerr=dE, yerr=new_dCS, elinewidth=1.0, capthick=1.0, capsize=3.0, label=reaction_daughter +  ' - Independent')
            elif independent==False:
                plt.errorbar(E, CS_daughter, marker='.', color='green',linewidth=0.0001, xerr=dE, yerr=dCS_daughter, elinewidth=1.0, capthick=1.0, capsize=3.0, label=reaction_daughter +' - Independent')    
                plt.errorbar(E, new_CS, marker='P', color='darkred',linewidth=0.0001, xerr=dE, yerr=new_dCS, elinewidth=1.0, capthick=1.0, capsize=3.0, label=reaction_daughter + ' - Cumulative')
            plt.errorbar(E, CS_parent, marker='.', color='magenta',linewidth=0.0001, xerr=dE, yerr=dCS_parent, elinewidth=0.5, capthick=1.0, capsize=3.0, label=reaction_parent + ' (Feeding: {}%)'.format(BR_daughter*100))
            self.modelling('Tendl', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR_daughter, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state)
            self.modelling('Alice', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR_daughter, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state)
            #print(feeding, "from subtraction func")
            self.modelling('Talys', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR_daughter, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state)
            #self.modelling('Exfor', foil, Z, A, reaction, file_ending, independent=independent, feeding=None, BR=BR_daughter)
            self.modelling('Exfor', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR_daughter, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state)
            self.modelling('CoH', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR_daughter, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state, reaction_parent=reaction_parent)
            self.modelling('Empire', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR_daughter, CS_colonne=CS_colonne_ALICE, isomer_state=isomer_state, reaction_parent=reaction_parent)
            self.plot_CrossSections(reaction, title, A, foil, ylimit, subtract='yes', legend_force=force_legend)



            #np.savetxt(path_to_cs_csv  + reaction + '', csv_save_array, delimiter=',', header='E, dE, CS, dCS', fmt="%s"  )#, %.6f, %.6f")
        #print(CS_daughter)
        #file_ending='.tot'
        #independent=False 
        #CS_parent, dCS_parent = self.make_CS(react_func_parent, foil, filename_parent, n, reaction_parent, csv_filename, Z_parent, A_parent)[-2:]
        #CS_daughter_cum, dCS_daughter_cum = self.make_CS(react_func_daughter, foil, filename_daughter, n, reaction_daughter, csv_filename, Z_daughter, A_daughter)[-2:]
        

        #CS_daughter = CS_daughter_cum - CS_parent


    def make_CS_isomerSub(self, foil, n, csv_filename, reaction_isomer, Z, A, react_func_cumulative, reaction_cumulative, filename_cumulative, react_func_groundstate, reaction_groundstate, filename_groundstate, ylimit, independent, BR, isomer_state, file_ending='.tot', CS_colonne_ALICE=4,save_text=True, feeding=None):
        E, dE, CS_cum, dCS_cum = self.make_CS(react_func_cumulative, foil, filename_cumulative, n, reaction_cumulative, csv_filename, Z, A, save_text=False)
        E, dE, CS_gs, dCS_gs = self.make_CS(react_func_groundstate, foil, filename_groundstate, n, reaction_groundstate, csv_filename, Z, A,  save_text=False)
        #print("***")
        #print(type(CS_cum))

        new_CS = []; new_dCS=[]
        if independent==True:
            for i in range(len(CS_cum)):
                #new_CS.append(CS_parent[i]-CS_daughter[i]*BR_daughter)
                #new_dCS.append(dCS_parent[i]-dCS_daughter[i]*BR_daughter)
                if CS_gs[i]==0:
                    new_CS.append(0)
                    new_dCS.append(0)
                else:
                    #new_CS.append(CS_gs[i]-CS_cum[i]*BR)       #here daughter is cumulative. Want independent CS
                    #new_dCS.append(dCS_gs[i]-dCS_cum[i]*BR)
                    
                    new_CS.append(CS_cum[i]-CS_gs[i]*(1-BR))
                    new_dCS.append(dCS_cum[i]-dCS_gs[i]*(1-BR))
                    #print(CS_daughter[i], CS_parent[i]*BR_daughter) 
                    #print(CS_daughter[i]-CS_parent[i]*BR_daughter)
        elif independent==False:  
            for i in range(len(CS_cum)):
                #new_CS.append(CS_parent[i]-CS_daughter[i]*BR_daughter)
                #new_dCS.append(dCS_parent[i]-dCS_daughter[i]*BR_daughter)
                new_CS.append(CS_gs[i]+CS_cum[i]*BR)        # here daughter is independent. Want cumulative CS
                new_dCS.append(dCS_gs[i]+dCS_gs[i]*BR) 




        if isomer_state==None:
            state='g'
        else:
            state=isomer_state

        if independent==False:
            type_CS='_cumulative'
        elif independent==True:
            type_CS='_independent'
        elif isinstance(independent, str):
            type_CS = independent

        reaction = reaction_isomer
        nucl = reaction[-2]
        numbs = ['1', '2', '3', '4', '5', '6', '7', '8','9']
        if nucl in numbs:
            title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A+state) + reaction[-1:]  + ' - ' + type_CS[1:] 
        else:
            title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A+state) + reaction[-2:]  + ' - ' + type_CS[1:] 

        
        dE_tot = dE[0]+dE[1]
        csv_save_array = np.vstack((E, dE_tot, new_CS, new_dCS)).T
        path_to_cs_csv = os.getcwd() + '/CrossSections/CrossSections_csv/'
        print("     E     ", "    CS    " )
        print(np.vstack((E,new_CS)).T)

        #CS_cum = [i * BR for i in CS_cum]; dCS_cum = [i * BR for i in dCS_cum]

        if save_text==True:
            CS_gs = [float('nan') if x==0 else x for x in CS_gs]
            CS_cum = [float('nan') if x==0 else x for x in CS_cum]
            new_CS = [float('nan') if x==0 else x for x in new_CS]
            np.savetxt(path_to_cs_csv  + reaction + type_CS+'_subtracted', csv_save_array, delimiter=',', header='E, dE, CS, dCS', fmt="%s"  )#, %.6f, %.6f")
            if independent==True:
                plt.errorbar(E, CS_gs, marker='.', color='green',linewidth=0.0001, xerr=dE, yerr=dCS_gs, elinewidth=0.5, capthick=1.0, capsize=3.0, label=reaction_groundstate + ' - Independent')    
                plt.errorbar(E, new_CS, marker='P', color='darkred',linewidth=0.0001, xerr=dE, yerr=new_dCS, elinewidth=1.0, capthick=1.0, capsize=3.0, label=reaction +  ' - Independent')
            elif independent==False:
                plt.errorbar(E, CS_gs, marker='.', color='green',linewidth=0.0001, xerr=dE, yerr=dCS_gs, elinewidth=1.0, capthick=1.0, capsize=3.0, label=reaction_groundstate +' - Independent')    
                plt.errorbar(E, new_CS, marker='P', color='darkred',linewidth=0.0001, xerr=dE, yerr=new_dCS, elinewidth=1.0, capthick=1.0, capsize=3.0, label=reaction + ' - Cumulative')
            plt.errorbar(E, CS_cum, marker='.', color='magenta',linewidth=0.0001, xerr=dE, yerr=dCS_cum, elinewidth=0.5, capthick=1.0, capsize=3.0, label=reaction_cumulative)
            self.modelling('Tendl', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE)
            #self.modelling('ALICE', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE)
            self.modelling('Alice', foil, Z, A, reaction_cumulative, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE)
            self.modelling('Talys', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE)
            self.modelling('Exfor', foil, Z, A, reaction, file_ending, independent=independent, feeding=feeding, BR=BR, CS_colonne=CS_colonne_ALICE)
            self.plot_CrossSections(reaction, title, A, foil, ylimit, subtract='yes')



            #np.savetxt(path_to_cs_csv  + reaction + '', csv_save_array, delimiter=',', header='E, dE, CS, dCS', fmt="%s"  )#, %.6f, %.6f")
        #print(CS_daughter)
        #file_ending='.tot'
        #independent=False 
        #CS_parent, dCS_parent = self.make_CS(react_func_parent, foil, filename_parent, n, reaction_parent, csv_filename, Z_parent, A_parent)[-2:]
        #CS_daughter_cum, dCS_daughter_cum = self.make_CS(react_func_daughter, foil, filename_daughter, n, reaction_daughter, csv_filename, Z_daughter, A_daughter)[-2:]
        

        #CS_daughter = CS_daughter_cum - CS_parent



#CS.make_CS(Ir_189Ir(), 'Ir', 'Ir_189Ir.csv', 10, 'Ir_189Ir', csv_filename, '77', '189')    # need work on activity 

    def modelling(self, model, foil, Z, A, reaction, file_ending,  independent, feeding, CS_colonne, BR, isomer_state, reaction_parent=False, isomer_feeding=False):
        #print("modelling:", model, foil )
        #print(feeding)
        SimCS = SimCrossSectionData() 
        #print(model)
        #print("****")
        if model == 'Alice':    # needs to come before chaning Z and A, since using the inputvalues
            try:
                #print("ALICE")
                #E, CS = SimCS.ALICE(foil, A, Z, CS_colonne)
                #plt.plot(E, CS, label='Alice', color='green', linestyle=':')

                #if isinstance(CS_colonne, list):     # To calculate if there is feeding from isomer. 
                #    print("yes")
                #else:
                #print("foil: ", foil)
                #print("A: ", A)
                #print("Z: ", Z)
                #print("Colonne: ", CS_colonne)






                # if feeding == None:
                if feeding!= 'beta+' or feeding!='beta-':

                    E, CS = SimCS.ALICE(foil, A, Z, CS_colonne)
                    #else:
                    #    pass
                    #print("foil: ", foil)
                    #print("A: ", A_p)
                    #print("Z: ", Z_p)
                    #print("Colonne: ", CS_colonne)
                    plt.plot(E, CS, label='ALICE-2017', color='green', linestyle=':')
                else:
                    E, CS = SimCS.ALICE(foil, A, Z, CS_colonne)
                    if feeding=='beta+':
                        Z_p = int(Z)+1; A_p = A
                        Z_p = str(Z_p)
                    elif feeding == 'beta-':
                        Z_p = int(Z)-1; A_p = A
                        Z_p = str(Z_p)






            


                    
                    #print("foil: ", foil)
                    #print("A: ", A_p)
                    #print("Z: ", Z_p)
                    #print("Colonne: ", CS_colonne)
                    #E_p, CS_p = SimCS.ALICE('Ir', '189', '78', 4)


                    E_p, CS_p = SimCS.ALICE(foil, A_p, Z_p, CS_colonne)

                    #print(E)
                    #print(CS_p)
                    CS_tot = CS + CS_p*BR
                    plt.plot(E, CS_tot, label='ALICE-2017', color='green', linestyle=':')
                #print("ALICE: ", feeding)
                #print(Z_p, A)






                """
                if feeding==None:
                    E, CS = SimCS.ALICE(foil, A, Z, CS_colonne)
                    plt.plot(E, CS, label='Alice', color='green', linestyle=':')
                else:



                """
            except:
                print("no Alice file found")
                pass
        
        elif model == 'Empire':
            #print("EMPIRE")
            #print(Z, A)
            try:
                #print("INDEPENDENT")
                #print("coh feeding: ", feeding)
                if isomer_state=='m':
                    isomer_state='M'
                elif isomer_state=='g':
                    isomer_state='G'
                elif isomer_state=='m1+g': 
                    isomer_state=None
                elif isomer_state==None:
                    isomer_state=None

                #if independent==True or feeding==None:
                #rint(feeding)
                if feeding==None:
                    #print("runs feeding=None")
                    #print(foil)
                    #print(A)
                    #print(Z)
                    #print(reaction)
                    #print(isomer_state)

                    E, CS = SimCS.EMPIRE(foil, A, Z, reaction, isomer=isomer_state)
                    #print(E)
                    plt.plot(E, CS, label='EMPIRE-3.2.3', linestyle='--', color='red', linewidth=0.7)
                    #print(E)



                elif feeding=='isomer_M':

                    #print("EMPIRE", feeding)
                    #print(BR)
                    E, CS = SimCS.EMPIRE(foil, A, Z, reaction, isomer=isomer_state)
                    E_p, CS_p = SimCS.EMPIRE(foil, A, Z, reaction=reaction_parent, isomer='M')
                    
                    CS_tot = CS+ CS_p*BR
                    #print(CS)
                    plt.plot(E, CS_tot, label='EMPIRE-3.2.3', linestyle='--', color='red', linewidth=0.7)
                elif feeding== 'isomer_M2':
                    E, CS = SimCS.EMPIRE(foil, A, Z, reaction, isomer=isomer_state)
                    E_p, CS_p = SimCS.EMPIRE(foil, A, Z, reaction=reaction_parent, isomer='M2')
                    CS_tot = CS+ CS_p*BR
                    plt.plot(E, CS_tot, label='EMPIRE-3.2.3', linestyle='--', color='red', linewidth=0.7)
                elif independent==False and feeding!=None:
                    #print("EMPIRE RUNS IF TEST")
                    E, CS = SimCS.EMPIRE(foil, A, Z, reaction, isomer=isomer_state)
                    #print(E)
                    #E, CS = SimCS.EMPIRE('Ni', '52', '25', 'Ni_52Mn', isomer=None)
                    #print("works:")
                    #print(foil)
                    #print(A)
                    #print(Z)
                    #print(reaction)
                    #print(isomer_state)
                    #print(E)
                    if feeding=='beta+':
                        Z_p = int(Z)+1; A_p = A
                        Z_p = str(Z_p)
                        if foil=='Ir':    # BAD LINE; SHOULD CHANGE IF POSSIBLE. 
                            reaction_new = reaction[:-2] + 'Pt'
                        #elif foil == 'Ni':
                        E_p, CS_p = SimCS.EMPIRE(foil, A_p, Z_p, reaction=reaction_parent, isomer=isomer_state)
                    elif feeding=='beta-':
                        Z_p = int(Z)-1; A_p = A
                        Z_p =  str(Z_p)
                        E_p, CS_p = SimCS.EMPIRE(foil, A_p, Z_p, reaction=reaction_parent, isomer=isomer_state)


                    
                    
                    
                    #elif feeding == 'isomer':
                    #    isomer_state_p='M'
                    #    print(isomer_state_p)
                    #    E_p, CS_p = SimCS.EMPIRE(foil, A, Z, reaction=reaction_parent, isomer=isomer_state_p)

                        #reaction_new = reaction[:-2] + 'Pt'
                    #print("Not working:")
                    #print(foil)
                    #print(A_p)
                    #print(Z_p)
                    #print(reaction_parent)
                    #print(isomer_state)    
                    #print("Z_p: ", Z_p, "A_p: ", A_p)
                    #print(reaction_parent)
                    #print(foil)
                    

                    #E_p, CS_p = SimCS.EMPIRE(foil, A_p, Z_p, reaction=reaction_parent, isomer=isomer_state)

                    CS_tot = CS+ CS_p*BR
                    plt.plot(E, CS_tot, label='EMPIRE-3.2.3', linestyle='--', color='red', linewidth=0.7)


            except:
                print("EMPIRE file not found")
                pass
            #label=EMPIRE-3.2.3

        if len(Z)==2: 
            Z = '0'+Z
        if len(A)==2: 
            A = '0'+A
        if model== 'Talys':
            #print("talys")
            try:
                #print(independent, feeding)
                if independent==True or feeding!='beta+' and feeding!='beta-':
                #if independent==True or feeding==None:    ### SINCE TALYS & TENDL ONLY GIVE INDEPENDENT MEASUREMENTS, take beta-feeding into account
                    #print("talys_ind")
                    E, CS = SimCS.TALYS(foil, A, Z, file_ending)
                    plt.plot(E, CS, label='TALYS-1.9', linestyle='-.', color='orange')
                elif independent==False and feeding!=None:
                    #print("FALSEEEEE")
                    E, CS = SimCS.TALYS(foil, A, Z, file_ending)
                    #plt.plot(E, CS, label='Talys_ind', linestyle='-.', color='yellow')
                    if feeding=='beta+':
                        #print(Z, Z-1)
                        #print("He")
                        Z_p = int(Z)+1; A_p = A
                        Z_p = '0' + str(Z_p)
                    elif feeding=='beta-':
                        Z_p = int(Z)-1; A_p = A
                        if len(str(Z_p))==2:
                            Z_p = '0' + str(Z_p)
                        else: 
                            Z_p = str(Z_p)
                    #print("Cs_ind", CS)
                    #print("Cs_cum", CS_p)
                    
                    E_p, CS_p = SimCS.TALYS(foil, A_p, Z_p, file_ending)
                    CS_tot = CS+ CS_p*BR
                    plt.plot(E, CS_tot, label='TALYS-1.9', linestyle='-.', color='orange')

            except:
                print("no talys file found")

        elif model == 'Exfor':

            #print("exfor function")
            try:
                #print("exfor function 2")
                #print(reaction, independent )
                E, dE, CS, dCS, author =  SimCS.EXFOR(reaction, independent)
                #print(E)
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
            #print("tendl")
            try:
                #if independent==True or feeding==None:
                if independent==True or feeding!='beta+' and feeding!='beta-':
                    E, CS = SimCS.Tendl(foil, A, Z, file_ending)
                #print(E)
                    if E is not 0:
                        plt.plot(E, CS, label='TENDL-2019', linestyle='--', color='blue')
                elif independent==False and feeding!=None:
                    E, CS = SimCS.Tendl(foil, A, Z, file_ending)
                    if feeding=='beta+':
                        Z_p = int(Z)+1; A_p = A
                        Z_p = '0' + str(Z_p)
                    elif feeding=='beta-':
                        Z_p = int(Z)-1; A_p = A
                        Z_p = '0' + str(Z_p)

                    E_p, CS_p = SimCS.Tendl(foil, A_p, Z_p, file_ending)
                    CS_tot = CS + CS_p*BR
                    if E is not 0:
                        plt.plot(E, CS_tot, label='TENDL-2019', linestyle='--', color='blue')
                    #plt.plot(E, CS_tot, label='Talys', linestyle='-.', color='orange')

            except: 
                print("Tendl files not found. Check file ending or fileproblem")
                pass

        elif model == 'CoH':

            try:
                #print("INDEPENDENT")
                #print("coh feeding: ", feeding)
                if isomer_state=='m':
                    isomer_state='M'
                elif isomer_state=='g':
                    isomer_state='G'
                elif isomer_state=='m1+g': 
                    isomer_state=None
                elif isomer_state==None:
                    isomer_state=None

                #if independent==True or feeding==None:
                
                if feeding==None:
                    
                    E, CS = SimCS.COH(foil, A, Z, reaction, isomer=isomer_state)
                    #print(E)
                    plt.plot(E, CS, label='CoH-3.5.3', linestyle='-', color='dodgerblue', linewidth=0.7)
                
                elif feeding=='isomer_M':

                    #print("EMPIRE", feeding)
                    #print(BR)
                    E, CS = SimCS.COH(foil, A, Z, reaction, isomer=isomer_state)
                    E_p, CS_p = SimCS.COH(foil, A, Z, reaction=reaction_parent, isomer='M')
                    
                    CS_tot = CS+ CS_p*BR
                    #print(CS)
                    plt.plot(E, CS_tot, label='CoH-3.5.3', linestyle='-', color='dodgerblue', linewidth=0.7)
                elif feeding== 'isomer_M2':
                    E, CS = SimCS.COH(foil, A, Z, reaction, isomer=isomer_state)
                    E_p, CS_p = SimCS.COH(foil, A, Z, reaction=reaction_parent, isomer='M2')
                    CS_tot = CS+ CS_p*BR
                    plt.plot(E, CS_tot, label='CoH-3.5.3', linestyle='-', color='dodgerblue', linewidth=0.7)

                elif independent==False and feeding!=None:
                    E, CS = SimCS.COH(foil, A, Z, reaction, isomer=isomer_state)
                    #print("works:")
                    #print(foil)
                    #print(A)
                    #print(Z)
                    #print(reaction)
                    #print(isomer_state)
                    #print(E)
                    if feeding=='beta+':
                        Z_p = int(Z)+1; A_p = A
                        Z_p = '0' + str(Z_p)
                        if foil=='Ir':    # BAD LINE; SHOULD CHANGE IF POSSIBLE. 
                            reaction_new = reaction[:-2] + 'Pt'
                        #elif foil == 'Ni':
                    elif feeding=='beta-':
                        Z_p = int(Z)-1; A_p = A
                        Z_p = '0' + str(Z_p)
                        #reaction_new = reaction[:-2] + 'Pt'
                    #print("Not working:")
                    #print(foil)
                    #print(A_p)
                    #print(Z_p)
                    #print(reaction_parent)
                    #print(isomer_state)    
                    #print("Z_p: ", Z_p, "A_p: ", A_p)
                    #print(reaction_parent)
                    #print(foil)
                    E_p, CS_p = SimCS.COH(foil, A_p, Z_p, reaction=reaction_parent, isomer=isomer_state)

                    CS_tot = CS+ CS_p*BR
                    plt.plot(E, CS_tot, label='CoH-3.5.3', linestyle='-', color='dodgerblue', linewidth=0.7)


            except:
                print("CoH file not found")
                pass
                
                """
                
                if isomer_state=='m':
                    isomer_state= 'M'
                elif isomer_state=='g':
                    isomer_state= 'G'
                #elif 'm2' in isomer_state:
                    #isomer_state = ''
                elif isomer_state == 'g' or isomer_state==None:  # not take the wrong coh file. 
                    isomer_state=None
                E, CS = SimCS.COH(foil, A, Z, reaction, isomer=isomer_state)
                plt.plot(E, CS, label='CoH', linestyle='-', color='dodgerblue', linewidth=0.7)
            except:
                print("no coh file found")
                pass
                """

                """
                if independent==True or feeding==None:
                    E, CS = SimCS.COH(foil, A, Z, reaction, isomer=isomer_state)
                    if E is not 0:
                        plt.plot(E, CS, label='CoH', linestyle='-', color='dodgerblue', linewidth=0.7)
                elif independent==False and feeding!=None:
                    E, CS = SimCS.COH(foil, A, Z, reaction, isomer=isomer_state)
                    if feeding=='beta+':
                        Z_p = int(Z)+1; A_p = A
                        Z_p = '0' + str(Z_p)
                        if foil=='Ir':    # BAD LINE; SHOULD CHANGE IF POSSIBLE. 
                            reaction_new = reaction[:-2] + 'Pt'
                        #elif foil == 'Ni':
                    elif feeding=='beta-':
                        Z_p = int(Z)-1; A_p = A
                        Z_p = '0' + str(Z_p)
                        #reaction_new = reaction[:-2] + 'Pt'
                    print("Z_p: ", Z_p, "A_p: ", A_p)

                    E_p, CS_p = SimCS.COH(foil, A_p, Z_p, reaction_new, isomer=None)
                    CS_tot = CS + CS_p*BR
                    if E is not 0:
                        plt.plot(E, CS_tot, label='CoH', linestyle='-', color='dodgerblue', linewidth=0.7)
                """
            #except:
            #    print("no Coh file found")
            #    pass
            #print("Provide a model in cross section class")
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



    def mon_CS_test(self, react_func, foil, filename, n, reaction,scaling_parameter, BC_csv_filename=False):
        #print("*")
        I_Fe, I_Ni, I_Cu, sigma_I = self.current_class.current_for_CS(mon_test=True)
        sigma_I = np.ones(len(I_Ni))*sigma_I

        """
        if BC_csv_filename!=False:
            I = np.genfromtxt(BC_csv_filename, delimiter=',', usecols=[1])
            #print(I)
            #weighted_average_beam = weighted_average_beam[::-1]
            dI = np.genfromtxt(BC_csv_filename, delimiter=',', usecols=[2])

            I_Fe =I 
            I_Ni = I
            I_Cu = I 
            sigma_I = I
        """



        ### The weighted average beam current  - made by Andrew

        # weighted_average_beam = np.genfromtxt(BC_csv_filename, delimiter=',', usecols=[1])
        # weighted_average_beam = weighted_average_beam[::-1]
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
        

        # I, sigma_I = self.current_class.current_for_CS()

        #print("I", I)
        #print("I_Ni", I_Ni)
        #I_Fe = I
        #I_Ni = I
        #I_Cu = I

        Cumulative_flag=False
        yscale=None


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
            dCs_mon = np.loadtxt(filename, usecols=[2], skiprows=6)
            #print(dCs_mon)

            self.modelling('Exfor', 'Fe', '26', '56', 'Fe_56Co', '.tot', independent=True, feeding=None, CS_colonne=5, BR=1.0, isomer_state=None)
            #self.modelling('')

            #self.modelling('Talys', 'Fe', '26', '56', 'Fe_56Co', '.tot')
            #self.modelling('Tendl', 'Fe', '26', '56', 'Fe_56Co', '.tot')
            A = '56'; foil='Fe'; title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A) + reaction[-2:]  + ' - Independent' 

            #sigma_Cs = np.loadtxt(filename, usecols=[2], skiprows=6)
        if reaction=='Ni_61Cu':
            CS, dCS = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Ni, sigma_I, lamb, reaction)
            E = self.E_Ni;dE = self.dE_Ni
            filename =  path_to_monitor_data+'nid61cut/nid61cut.txt'
            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)
            dCs_mon = np.loadtxt(filename, usecols=[2], skiprows=6)


            
            self.modelling('Exfor', 'Ni', '28', '61', 'Ni_61Cu', '.tot', independent=True, feeding=None, CS_colonne=5, BR=1.0, isomer_state=None)
            A = '61'; foil='Ni'; title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A) + reaction[-2:]  + ' - Independent' 

        if reaction=='Ni_56Co':
            CS_56Co, dCS_56Co = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Ni, sigma_I, lamb, reaction)
            E = self.E_Ni;dE = self.dE_Ni
            filename =  path_to_monitor_data+'nid56cot/nid56cot.txt'

            lamb_, mass_density_, sigma_mass_density_, E_, dE_, A0_, sigma_A0_ = self.get_var(Ni_56Ni(), 'Ni', 'Ni_56Ni.csv', 10, 'Ni_56Ni')
            CS_56Ni, dCS_56Ni = self.cross_section_calc(n, A0_, sigma_A0_, mass_density, sigma_mass_density, I_Ni, sigma_I, lamb_, 'Ni_56Ni')
        
            self.modelling('Exfor', 'Ni', '28', '56', 'Ni_56Co', '.tot', independent=False, feeding=None, CS_colonne=5, BR=1.0, isomer_state=None)
            CS = CS_56Co +  CS_56Ni

            for i in range(len(E)):
                print("56Co: {:.1f}".format(sigma_A0[i]/A0[i]*100))
                if i <3:
                    print("56Ni: {:.1f}".format(sigma_A0_[i]/A0_[i]*100))
                    print("tot: {:.1f}".format(np.sqrt((sigma_A0_[i]/A0_[i])**2 +  (sigma_A0[i]/A0[i])**2 )*100))
                else:
                    #print("tot: {:.1f}".format(sigma_A0[i]))
                    pass
                print("********")


            Cumulative_flag = True
            yscale=100
            #fraction_56Ni = dCS_56Ni/CS_56Ni
            #for i in fraction_56Ni:
            #       np.nan_to_num(i)
            fraction_56Ni=[]
            frac = dCS_56Ni/CS_56Ni
            for i in range(len(CS)):
                if np.isnan(frac[i]) == True:
                    fraction_56Ni.append(0)
                else:
                    fraction_56Ni.append(frac[i])
                    #print("Y")
                    #i == 0
            fraction_56Ni= np.array((fraction_56Ni))
            #dCS = CS*np.sqrt( (dCS_56Co/CS_56Co)**2 + (dCS_56Ni/CS_56Ni)**2)
            dCS = CS*np.sqrt( (dCS_56Co/CS_56Co)**2 + (fraction_56Ni)**2)




            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)
            dCs_mon = np.loadtxt(filename, usecols=[2], skiprows=6)
            A = '56'; foil='Ni'; title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A) + reaction[-2:]  + ' - Cumulative' 
            #print("     56Ni     ", "    56Co   " )
            #print(np.vstack((CS_56Ni,CS_56Co)).T)

        if reaction=='Ni_58Co':
            CS_58Co, dCS_58Co = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Ni, sigma_I, lamb, reaction)
            E = self.E_Ni;dE = self.dE_Ni
            #print("groundstate: {:.1f}".format(sigma_A0/A0*100))
            filename =  path_to_monitor_data+'nid58cot/nid58cot.txt'
            self.modelling('Exfor', 'Ni', '28', '58', 'Ni_58Co', '.tot', independent=False, feeding=None, CS_colonne=5, BR=1.0, isomer_state=None)

            lamb_, mass_density_, sigma_mass_density_, E_, dE_, A0_, sigma_A0_ = self.get_var(Ni_58mCo(), 'Ni', 'Ni_58mCo.csv', 10, 'Ni_58mCo')
            for i in range(len(E)):
                print("groundstate: {:.1f}".format(sigma_A0[i]/A0[i]*100))
                print("isomer: {:.1f}".format(sigma_A0_[i]/A0_[i]*100))
                print("total: {:.1f}".format(np.sqrt((sigma_A0_[i]/A0_[i])**2 + (sigma_A0[i]/A0[i])**2 )*100))
                print("***************")
            CS_58mCo, dCS_58mCo = self.cross_section_calc(n, A0_, sigma_A0_, mass_density, sigma_mass_density, I_Ni, sigma_I, lamb_, 'Ni_58mCo')

            Cumulative_flag = True

            CS = CS_58mCo +  CS_58Co
            dCS = CS*np.sqrt( (dCS_58Co/CS_58Co)**2 + (dCS_58mCo/CS_58mCo)**2)
            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)
            dCs_mon = np.loadtxt(filename, usecols=[2], skiprows=6)
            A = '58'; foil='Ni'; title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A) + reaction[-2:]  + ' - Cumulative' 
            #print("     58Co     ", "    58mCo   " )
            #print(np.vstack((CS_58Co,CS_58mCo)).T)
        if reaction=='Cu_62Zn':
            yscale=40
            CS, dCS = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Cu, sigma_I, lamb, reaction)
            E = self.E_Cu;dE = self.dE_Cu
            filename =  path_to_monitor_data+'cud62znt/cud62znt.txt'
            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)
            dCs_mon = np.loadtxt(filename, usecols=[2], skiprows=6)
            self.modelling('Exfor', 'Cu', '29', '62', 'Cu_62Zn', '.tot', independent=True, feeding=None, CS_colonne=5, BR=1.0, isomer_state=None)
            A = '62'; foil='Cu'; title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A) + reaction[-2:]  + ' - Cumulative' 
        if reaction=='Cu_63Zn':
            CS, dCS = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Cu, sigma_I, lamb, reaction)
            E = self.E_Cu;dE = self.dE_Cu
            filename =  path_to_monitor_data+'cud63znt/cud63znt.txt'
            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)
            dCs_mon = np.loadtxt(filename, usecols=[2], skiprows=6)
            self.modelling('Exfor', 'Cu', '29', '63', 'Cu_63Zn', '.tot', independent=True, feeding=None, CS_colonne=5, BR=1.0, isomer_state=None)
            A = '63'; foil='Cu'; title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A) + reaction[-2:]  + ' - Cumulative' 
        if reaction=='Cu_65Zn':
            CS, dCS = self.cross_section_calc(n, A0, sigma_A0, mass_density, sigma_mass_density, I_Cu, sigma_I, lamb, reaction)
            E = self.E_Cu;dE = self.dE_Cu
            filename =  path_to_monitor_data+'cud65znt/cud65znt.txt'
            E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
            Cs_mon = np.loadtxt(filename, usecols=[1], skiprows=6)
            dCs_mon = np.loadtxt(filename, usecols=[2], skiprows=6)
            self.modelling('Exfor', 'Cu', '29', '65', 'Cu_65Zn', '.tot', independent=True, feeding=None, CS_colonne=5, BR=1.0, isomer_state=None)
            A = '65'; foil='Cu'; title = r'$^{nat}$' + foil + '(d,x)' + r'$^{{ {} }}$'.format(A) + reaction[-2:]  + ' - Cumulative' 


        #print(len(CS))
        #print(E)
        #plt.plot(E_mon, Cs_mon, label='monitor data')
        #plt.plot(E_)
        #self.plot_CrossSections(E, dE, CS, dCS, reaction)


        #self.setting_plotvalues(E_mon, 0, Cs_mon, 0, label='monitor data', )
        #print(scaling_parameter)

        #if reaction == 'Ni_56Co' or reaction=='Ni_58Co':

        if Cumulative_flag:
            label = 'Monitor Data (cumulative)'
        else:
            label = 'Monitor Data'



        CS = [float('nan') if x==0 else x for x in CS]

        if foil == 'Ni':
            I = I_Ni
        elif foil == 'Cu':
            I = I_Cu
        elif foil == 'Fe':
            I = I_Fe

        for i in range(len(CS)):
            print("foil: ", i+1)
            print("cross section: {:.1f} ({:.1f})".format(CS[i], dCS[i]))
            print("Relative uncertainty activity:  {:.1f}%".format((sigma_A0[i]/A0[i]*100)))
            print("Relative uncertainty mass density:  {:.1f}%".format((sigma_mass_density[i]/mass_density[i]*100)))
            print("Relative uncertainty beam current:  {:.1f}%".format((sigma_I[i]/I[i]*100)))
            
            print("Relative uncertainty CS: {:.1f}% ".format((dCS[i]/ CS[i]*100)))
            print("------------------------------------------")



        plt.plot(E_mon, Cs_mon, label='Recommended CS (IAEA)')
        plt.fill_between(E_mon, Cs_mon+dCs_mon, Cs_mon-dCs_mon, color='blue', alpha=0.1)
        #self.setting_plotvalues(E, dE, CS, dCS, 'this data')
        #plt.errorbar(E, CS, marker='P', markersize=4, color='darkred', linewidth=0.0001, xerr=dE, yerr=dCS, elinewidth=0.5, capthick=0.25, capsize=3.0, label=label )
        plt.errorbar(E, CS, marker='P', markersize=4, color='darkred', linewidth=0.0001, xerr=dE, yerr=dCS, elinewidth=1.0, capthick=1.0, capsize=3.0, label=label)
        if yscale!=None:
            self.plot_CrossSections(reaction, title, A=1, foil='foil', max_CS=yscale)
        else:
            self.plot_CrossSections(reaction, title, A=1, foil='foil')


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



    def plot_CrossSections(self, reaction, title, A=1, foil='foil', max_CS=None, subtract=None, legend_force=False):

        #plt.plot(E_mon, Cs_mon, label='monitor data')
        #plt.plot(E, CS, 'o', label='this data')
        #fig, ax = plt.subplots()
        #print("max CS: ", max_CS)
        plt.xlabel('Deuteron Energy (MeV)')
        plt.ylabel('Cross Section (mb)')

    
        #title_name = r'$^\text{nat}' + foil + '(d,x)' + r'$^{}$'.format(A)
        #plt.title('Cross section for reaction {}'.format(reaction))
        plt.title(title)
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
        #plt.legend(by_label.values(), by_label.keys(),fontsize='x-small', loc='best')
        
        if legend_force == False:
            plt.legend(by_label.values(), by_label.keys(),fontsize='small', loc='best')
        else: 
            plt.legend(by_label.values(), by_label.keys(),fontsize='x-small', loc=legend_force)
        plt.gca().set_xlim(left=0, right=40)
        if max_CS==None:
            plt.gca().set_ylim(bottom=0)
        else: 
            plt.gca().set_ylim(bottom=0, top=max_CS)

        if subtract!= None:
            plt.savefig(path_to_cs_figs + reaction+'_subtracted.png', dpi=300)
        else:
            
            plt.savefig(path_to_cs_figs + reaction+'.png', dpi=300)
        

        plt.show()
        #plt.close()




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
