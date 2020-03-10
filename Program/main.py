from jan20_CrossSections import CrossSections
#from ZieglerFiles_new import ziegler_files
#from feb20_zieglerfiles import ziegler   #newest with all cleaned files
#from single_decay_A0 import *
from des19_BeamCurrent import *

from BC_ziegler_run import *

#from feb20_activity import *
from foil_info import *


#func=Cu_62Zn(); A0_guess=4000
#func=Ni_58Co(); A0_guess=[5000, 1000]
#func = Ni_61Cu(); A0_guess=4000
#func = Ni_56Co(); A0_guess=[150, 1500]
#func = Ni_58Co(); A0_guess=[8000, 1000]
#func = Ir_193mPt(); A0_guess=1500
#ACT = Activity(func, A0_guess, foilnumb=0)
#ACT.get_vals()
#ACT.knownparent_activity(Ni_56Ni())
#ACT.get_parent_activity(Ni_56Ni())

#from foil_info import *
#from beam_current_FoilReact import *
#from ZieglerFiles import ziegler_files

### GOOD LINES ARE
### 179 B+10%_D+0,5
### 139 B0%_D-1%
### 221 B+2,5%_D+3,5%
#BC= BeamCurrent(files[50])


#files,names = ziegler_files()

f_list_FilesNames = 'ziegler_FilesNames.csv'
files = np.genfromtxt(f_list_FilesNames, dtype="str", delimiter='|', usecols=[0])
names = np.genfromtxt(f_list_FilesNames, dtype="str", delimiter='|', usecols=[1])
files = list(files)
names = list(names)
#files, names = ziegler()
#print(names[8])
#print(type(files))
#
def find_index(list, element):
    return list.index(element)

#files = files[:10]
#names = names[:10]
#print(names[3])

"""
#COMPARTMENT 9 BEST CHI^2
selected_names = ['B_+1_D_+2', 'B_+10_D_+2,5', #'B_-2,25_D_-0,75', 'B_-2,25_D_-1,75', 
'B_+10_D_+3', 'B_+2_D_+4,25', 'B_+1,75_D_+3,75',
'B_+2_D_+4', #'B_-2,25_D_-1,25', 
'B_+1,5_D_+3,25', 'B_+1,25_D_+2,75', 'B_+1,75_D_+3,5', 'B_+2,5_D_+7,5', 'B_+1,5_D_+3', 'B_+0,5_D_+1,25']

# GOOD CANDIDATES: B_+1,5_D_+3,5


COMPARTMENT 6 BEST CHI^2
selected_names = ['B_+2,25_D_+4,75','B_+2_D_+4','B_+2,25_D_+4,5','B_+1,75_D_+3,25','B_+2_D_+3,75','B_+1,75_D_+3,5',
'B_+2,5_D_+7,5','B_+2,25_D_+5','B_+2_D_+4,25','B_+1,5_D_+2,75','B_+1,5_D_+2,5','B_+1,25_D_+2','B_+1_D_+1,25']


#COMPARTMENT 3 BEST CHI^2
selected_names = [#'B_-2,5_D_+4','B_+0,25_D_-5',  'B_+0,5_D_-4','B_+0,25_D_-4,75','B_+0,5_D_-3,75','B_+0,5_D_-4,25', 
#'B_+0,75_D_-3', 'B_+0,75_D_-2,75','B_+1_D_-1,75','B_+0,75_D_-3,25',
'B_+10_D_-2']

selected_names = ['B_0_D_0']
"""


index = find_index(names, 'B_+2_D_+4,25')   #the one used so far. 
#index = find_index(names, 'B_+1_D_+2')
print(files[index])
#RZ = Run_Ziegler(files, names)


BC = BeamCurrent(files[index])
#BC.calculate_beam_current('Ni', 'Ni_56Co', print_terms=True)
#BC.calculate_beam_current('Ni', 'Ni_58Co', print_terms=True)
#BC.calling_parameters_to_weightedaverage_func('Cu', 'Cu_62Zn')
#BC.calling_parameters_to_weightedaverage_func('Cu', 'Cu_63Zn')
#BC.calling_parameters_to_weightedaverage_func('Cu', 'Cu_65Zn')
#BC.calling_parameters_to_weightedaverage_func('Ni', 'Ni_61Cu')
BC.calling_parameters_to_weightedaverage_func('Ni', 'Ni_56Co')   ### prob 
#BC.calling_parameters_to_weightedaverage_func('Ni', 'Ni_58Co')
#BC.calling_parameters_to_weightedaverage_func('Fe', 'Fe_56Co')

#BC.variance_minimization(6, names[index], include_56Co=True, MakePlot=True)


#### positive B and positive D compensate each other- same for neg neg

#index = find_index(names, 'B_-2,5_D_-7,5')
#index = find_index(names, 'B_+10_D_0')
#index = find_index(names, 'B_0_D_-5')
#index = find_index(names, 'B_0_D_0')
#print(index)
#RZ = Run_Ziegler(files, names)
#RZ.run_beam_current()
#RZ.plot_ChiSq(3, chi_tol=2)
#RZ.plot_ChiSq(7, chi_tol=2)
#RZ.plot_ChiSq(9, chi_tol=2)
#RZ.plot_ChiSq(6, chi_tol=1)

#path_to_Chisq = os.getcwd() + '/BeamCurrent/chisq_dir_new/'






"""
###   This is where the csv file with the beam current is written  (assigned indexed ziegler file)
csv_filename = './' + files[index] 
#print("**", csv_filename)

BC = BeamCurrent(files[index])
#assigning variables for weighted_average.py
A0, sigma_A0, lambda_, mass_density, sigma_mass_density, reaction_integral, uncertainty_integral, irr_time, sigma_irr_time = BC.reshaping_parameters()

#print("A0: ", A0)
#print("dA0: ", sigma_A0)
#print("lamb: ", lambda_ )
#print("mass density: ", mass_density)
#print("sigma mass density: ", sigma_mass_density)
#print("reaction int: ", reaction_integral)
#print("uncert integral: ", uncertainty_integral) 
#print(irr_time, sigma_irr_time)


weighted_average_BC, sigma_weighted_average_BC = Average_BeamCurrent(A0, sigma_A0, mass_density, sigma_mass_density,  lambda_, reaction_integral, uncertainty_integral, irr_time, sigma_irr_time, csv_filename=csv_filename)
print(weighted_average_BC)
print(sigma_weighted_average_BC)
"""

#print(weighted_average_BC)
#BC.CurrentPlot_compartment(names[index], WABC=csv_filename)
#CS = CrossSections(files[index])



"""
CS.mon_CS_test(Fe_56Co(), 'Fe', 'Fe_56Co.csv', 3, 'Fe_56Co', names[index], csv_filename)
CS.mon_CS_test(Ni_61Cu(), 'Ni', 'Ni_61Cu.csv', 10, 'Ni_61Cu', names[index], csv_filename)
CS.mon_CS_test(Ni_56Co(), 'Ni', 'Ni_56Co.csv', 10, 'Ni_56Co', names[index], csv_filename)
CS.mon_CS_test(Ni_58Co(), 'Ni', 'Ni_58Co.csv', 10, 'Ni_58Co', names[index], csv_filename)
CS.mon_CS_test(Cu_62Zn(), 'Cu', 'Cu_62Zn.csv', 10, 'Cu_62Zn', names[index], csv_filename)
CS.mon_CS_test(Cu_63Zn(), 'Cu', 'Cu_63Zn.csv', 10, 'Cu_63Zn', names[index], csv_filename)
CS.mon_CS_test(Cu_65Zn(), 'Cu', 'Cu_65Zn.csv', 10, 'Cu_65Zn', names[index], csv_filename)
"""

#BC.CurrentPlot(names[index], SaveFig=True)



#BC.calculate_beam_current('Fe', 'Fe_56Co', print_terms=True)
#BC.calculate_beam_current('Fe', 'Fe_56Co', print_terms=True)
#BC.specified_currents()
#from weighted_average import *


#print(weighted_average_BC)
#CS.exfordata_npat()

#BC = BeamCurrent(files[index])
#BC.CurrentPlot_compartment(names[index])
#BC.variance_minimization(9, names[index], MakePlot=True )
#BC.CurrentPlot(names[index])
#BC.current_for_CS()


#Cu_57Ni()
#single_decay_data(Cu_57Ni(), "Cu_57Ni", 10, Save_csv=True)    #EXCELLENT
#single_decay_data(Cu_64Cu(), "Cu_64Cu", 10, Save_csv=True)      #EXCELLENT
#two_step_up_npat(Ni_58Co(), "Ni_58mCo_npat", "Ni_58Co_npat", 10, '58COm', '58COg', Save_csv=True)
#two_step_up_data(Ni_58Co(),"Ni_58mCo", "Ni_58Co", 10, Save_csv= True)
#two_step_kp_data(Ni_56Ni(), Ni_56Co(), "Ni_56Co", 10, Save_csv= True)



csv_filename = './' + files[index] 
#csv_filename = './' + names[index] + '.csv'
#print(csv_filename)
#I = np.genfromtxt(csv_filename, delimiter=',', usecols=[1])  #### NOT RIGHT   
#print("***")
#print(I)



#print("***", csv_filename)
#csv_filename = os.getcwd() + '/../ziegler_B_+2_D_+4,25_fluxes.csv'
#print("***", csv_filename)
CS = CrossSections(files[index]) 


"""
### Monitor reactions
CS.mon_CS_test(Fe_56Co(), 'Fe', 'Fe_56Co.csv', 3, 'Fe_56Co', names[index], csv_filename)
CS.mon_CS_test(Ni_61Cu(), 'Ni', 'Ni_61Cu.csv', 10, 'Ni_61Cu', names[index], csv_filename)
CS.mon_CS_test(Ni_56Co(), 'Ni', 'Ni_56Co.csv', 10, 'Ni_56Co', names[index], csv_filename)
CS.mon_CS_test(Ni_58Co(), 'Ni', 'Ni_58Co.csv', 10, 'Ni_58Co', names[index], csv_filename)
CS.mon_CS_test(Cu_62Zn(), 'Cu', 'Cu_62Zn.csv', 10, 'Cu_62Zn', names[index], csv_filename)
CS.mon_CS_test(Cu_63Zn(), 'Cu', 'Cu_63Zn.csv', 10, 'Cu_63Zn', names[index], csv_filename)
CS.mon_CS_test(Cu_65Zn(), 'Cu', 'Cu_65Zn.csv', 10, 'Cu_65Zn', names[index], csv_filename)
"""

### Ni reactions

#CS.make_CS(Ni_52Mn(), 'Ni', 'Ni_52Mn.csv', 10, 'Ni_52Mn', csv_filename, '25', '52')
#CS.make_CS(Ni_54Mn(), 'Ni', 'Ni_54Mn.csv', 10, 'Ni_54Mn', csv_filename, '25', '54')
#CS.make_CS(Ni_59Fe(), 'Ni', 'Ni_59Fe.csv', 10, 'Ni_59Fe', csv_filename, '26', '59')
#CS.make_CS(Ni_60Cu(), 'Ni', 'Ni_60Cu.csv', 10, 'Ni_60Cu', csv_filename, '29', '60')
#CS.make_CS(Ni_64Cu(), 'Ni', 'Ni_64Cu.csv', 10, 'Ni_64Cu', csv_filename, '29', '64')
#CS.make_CS(Ni_60Co(), 'Ni', 'Ni_60Co.csv', 10, 'Ni_60Co', csv_filename, '27', '60')
#CS.make_CS(Ni_65Ni(), 'Ni', 'Ni_65Ni.csv', 10, 'Ni_65Ni', csv_filename, '28', '65')
#CS.make_CS(Ni_56Co(), 'Ni', 'Ni_56Co.csv', 10, 'Ni_56Co', csv_filename, '27', '56')
#CS.make_CS(Ni_56Ni(), 'Ni', 'Ni_56Ni.csv', 10, 'Ni_56Ni', csv_filename, '28', '56')
#CS.make_CS(Ni_55Co(), 'Ni', 'Ni_55Co.csv', 10, 'Ni_55Co', csv_filename, '27', '55')
#CS.make_CS(Ni_56Mn(), 'Ni', 'Ni_56Mn.csv', 10, 'Ni_56Mn', csv_filename, '25', '56')
#CS.make_CS(Ni_57Ni(), 'Ni', 'Ni_57Ni.csv', 10, 'Ni_57Ni', csv_filename, '28', '57')


### Cu reactions
#CS.make_CS(Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu', csv_filename, '29', '64')
#CS.make_CS(Cu_65Ni(), 'Cu', 'Cu_65Ni.csv', 10, 'Cu_65Ni', csv_filename, '28', '65')
#CS.make_CS(Cu_52Mn(), 'Cu', 'Cu_52Mn.csv', 10, 'Cu_52Mn', csv_filename, '25', '52')   #Most likely false. Not in talys or exfor. 
#CS.make_CS(Cu_56Co(), 'Cu', 'Cu_56Co.csv', 10, 'Cu_56Co', csv_filename, '27', '56')    #Most likely false. In talys but no match, not in exfor. 
#CS.make_CS(Cu_57Ni(), 'Cu', 'Cu_57Ni.csv', 10, 'Cu_57Ni', csv_filename, '28', '57')    #Most likely false too, Qval is too low at these energies. 
#CS.make_CS(Cu_57Co(), 'Cu', 'Cu_57Co.csv', 10, 'Cu_57Co', csv_filename, '27', '57')    #Most likely false too, Qval is too low at these energies. 
#CS.make_CS(Cu_59Fe(), 'Cu', 'Cu_59Fe.csv', 10, 'Cu_59Fe', csv_filename, '26', '59')
#CS.make_CS(Cu_60Co(), 'Cu', 'Cu_60Co.csv', 10, 'Cu_60Co', csv_filename, '27', '60')   
#CS.make_CS(Cu_61Co(), 'Cu', 'Cu_61Co.csv', 10, 'Cu_61Co', csv_filename, '27', '61')  
#CS.make_CS(Cu_61Cu(), 'Cu', 'Cu_61Cu.csv', 10, 'Cu_61Cu', csv_filename, '29', '61')       #Not a good measurement? 
#CS.make_CS(Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu', csv_filename, '29', '64')
#CS.make_CS(Cu_65Ni(), 'Cu', 'Cu_65Ni.csv', 10, 'Cu_65Ni', csv_filename, '28', '65')     # Plot looks very weird. 

### Fe reactions
#CS.make_CS(Fe_48V(), 'Fe', 'Fe_48V.csv', 3, 'Fe_48V', csv_filename, '23', '48')   
#CS.make_CS(Fe_51Cr(), 'Fe', 'Fe_51Cr.csv', 3, 'Fe_51Cr', csv_filename, '24', '51')   
#CS.make_CS(Fe_52Mn(), 'Fe', 'Fe_52Mn.csv', 3, 'Fe_52Mn', csv_filename, '25', '52')   
#CS.make_CS(Fe_53Fe(), 'Fe', 'Fe_53Fe.csv', 3, 'Fe_53Fe', csv_filename, '26', '53')   
#CS.make_CS(Fe_54Mn(), 'Fe', 'Fe_54Mn.csv', 3, 'Fe_54Mn', csv_filename, '25', '54')   
#CS.make_CS(Fe_55Co(), 'Fe', 'Fe_55Co.csv', 3, 'Fe_55Co', csv_filename, '27', '55')   
#CS.make_CS(Fe_57Co(), 'Fe', 'Fe_57Co.csv', 3, 'Fe_57Co', csv_filename, '27', '57')   
#CS.make_CS(Fe_58Co(), 'Fe', 'Fe_58Co.csv', 3, 'Fe_58Co', csv_filename, '27', '58')   
#CS.make_CS(Fe_59Fe(), 'Fe', 'Fe_59Fe.csv', 3, 'Fe_59Fe', csv_filename, '26', '59')   


### Ir reactions  
#CS.make_CS(Ir_183Ta(), 'Ir', 'Ir_183Ta.csv', 10, 'Ir_183Ta', csv_filename, '73', '183')   
#CS.make_CS(Ir_186Re(), 'Ir', 'Ir_186Re.csv', 10, 'Ir_186Re', csv_filename, '75', '186')   
#CS.make_CS(Ir_186Ta(), 'Ir', 'Ir_186Ta.csv', 10, 'Ir_186Ta', csv_filename, '73', '186')   
#CS.make_CS(Ir_187W(), 'Ir', 'Ir_187W.csv', 10, 'Ir_187W', csv_filename, '74', '187')   
#CS.make_CS(Ir_188Pt(), 'Ir', 'Ir_188Pt.csv', 10, 'Ir_188Pt', csv_filename, '78', '188')   
#CS.make_CS(Ir_188Ir(), 'Ir', 'Ir_188Ir.csv', 10, 'Ir_188Ir', csv_filename, '77', '188')   
CS.make_CS(Ir_188Re(), 'Ir', 'Ir_188Re.csv', 10, 'Ir_188Re', csv_filename, '75', '188') # not working
#CS.make_CS(Ir_188mRe(), 'Ir', 'Ir_188mRe.csv', 10, 'Ir_188mRe', csv_filename, '75', '188')   not working      
#CS.make_CS(Ir_193mPt(), 'Ir', 'Ir_193mPt.csv', 10, 'Ir_193mPt', csv_filename, '78', '193')   

#CS.make_CS(Ir_189Pt(), 'Ir', 'Ir_189Pt.csv', 10, 'Ir_189Pt', csv_filename, '78', '189')    # 
#CS.make_CS(Ir_189Ir(), 'Ir', 'Ir_189Ir.csv', 10, 'Ir_189Ir', csv_filename, '77', '189')    # need work on activity 
#CS.make_CS(Ir_189Re(), 'Ir', 'Ir_189Re.csv', 10, 'Ir_189Re', csv_filename, '75', '189')     # needs work

#CS.make_CS(Ir_190Ir(), 'Ir', 'Ir_190Ir.csv', 10, 'Ir_190Ir', csv_filename, '77', '190')   
#CS.make_CS(Ir_191Pt(), 'Ir', 'Ir_191Pt.csv', 10, 'Ir_191Pt', csv_filename, '78', '191')   
#CS.make_CS(Ir_192Ir(), 'Ir', 'Ir_192Ir.csv', 10, 'Ir_192Ir', csv_filename, '77', '192')    
#CS.make_CS(Ir_194Ir(), 'Ir', 'Ir_194Ir.csv', 10, 'Ir_194Ir', csv_filename, '77', '194')    
#CS.make_CS(Ir_194m2Ir(), 'Ir', 'Ir_194m2Ir.csv', 10, 'Ir_194m2Ir', csv_filename, '77', '194')    

#get_vals(Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu', csv_filename)

#I = BC.current_for_CS()
#print(I)


#RZ.plot_ChiSq(3, 0.05)
#RZ.plot_ChiSq(7, 0.01)
#RZ.plot_ChiSq(9, 3)
#RZ.run_beam_current()
#print('Cu')
#RZ.flux_distribution('Cu')
#print('Ni')
#RZ.flux_distribution('Ni')
#print('Ir')
#RZ.flux_distribution('Ir')
#print('Fe')
#RZ.flux_distribution('Fe')





if __name__ == "__main__":
    print(__name__)
