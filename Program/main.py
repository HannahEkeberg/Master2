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


#COMPARTMENT 6 BEST CHI^2
selected_names = ['B_+2,25_D_+4,75','B_+2_D_+4','B_+2,25_D_+4,5','B_+1,75_D_+3,25','B_+2_D_+3,75','B_+1,75_D_+3,5',
'B_+2,5_D_+7,5','B_+2,25_D_+5','B_+2_D_+4,25','B_+1,5_D_+2,75','B_+1,5_D_+2,5','B_+1,25_D_+2','B_+1_D_+1,25']


#COMPARTMENT 3 BEST CHI^2
selected_names = [#'B_-2,5_D_+4','B_+0,25_D_-5',  'B_+0,5_D_-4','B_+0,25_D_-4,75','B_+0,5_D_-3,75','B_+0,5_D_-4,25', 
#'B_+0,75_D_-3', 'B_+0,75_D_-2,75','B_+1_D_-1,75','B_+0,75_D_-3,25',
'B_+10_D_-2']

selected_names = ['B_0_D_0']
"""

#index = find_index(names, 'B_-2,5_D_+4') #not super good: 
#index = find_index(names, 'B_+1_D_-2')
index = find_index(names, 'B_+2_D_+4,25')
print(files[index])



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





#A0, sigma_A0, lambda_, mass_density, sigma_mass_density, reaction_integral, uncertainty_integral, irr_time, sigma_irr_time = BC.reshaping_parameters()
#print(mass_density)
#print(lambda_)
#print(irr_time)
#print(sigma_irr_time)
#weighted_average_BC, sigma_weighted_average_BC = Average_BeamCurrent(A0, sigma_A0, mass_density, sigma_mass_density,  lambda_, reaction_integral, uncertainty_integral, irr_time, sigma_irr_time)

"""
numb = 0
csv_filename = './' + selected_names[numb] +'.csv'
print(selected_names)
#print(files[index])
index = find_index(names, selected_names[numb])
BC = BeamCurrent(files[index])
#assigning variables for weighted_average.py
A0, sigma_A0, lambda_, mass_density, sigma_mass_density, reaction_integral, uncertainty_integral, irr_time, sigma_irr_time = BC.reshaping_parameters()
weighted_average_BC, sigma_weighted_average_BC = Average_BeamCurrent(A0, sigma_A0, mass_density, sigma_mass_density,  lambda_, reaction_integral, uncertainty_integral, irr_time, sigma_irr_time, csv_filename=csv_filename)
#BC.
#selected_names = './' + selected_names[0] +'.csv'

BC.CurrentPlot_compartment(names[index], WABC=csv_filename)

#BC.CurrentPlot(names[index], SaveFig=True)


CS = CrossSections(files[index])


CS.mon_CS_test(Fe_56Co(), 'Fe', 'Fe_56Co.csv', 3, 'Fe_56Co', names[index], csv_filename)
CS.mon_CS_test(Ni_61Cu(), 'Ni', 'Ni_61Cu.csv', 10, 'Ni_61Cu', names[index], csv_filename)
CS.mon_CS_test(Ni_56Co(), 'Ni', 'Ni_56Co.csv', 10, 'Ni_56Co', names[index], csv_filename)
CS.mon_CS_test(Ni_58Co(), 'Ni', 'Ni_58Co.csv', 10, 'Ni_58Co', names[index], csv_filename)
CS.mon_CS_test(Cu_62Zn(), 'Cu', 'Cu_62Zn.csv', 10, 'Cu_62Zn', names[index], csv_filename)
CS.mon_CS_test(Cu_63Zn(), 'Cu', 'Cu_63Zn.csv', 10, 'Cu_63Zn', names[index], csv_filename)
CS.mon_CS_test(Cu_65Zn(), 'Cu', 'Cu_65Zn.csv', 10, 'Cu_65Zn', names[index], csv_filename)

#BC.CurrentPlot(names[index], SaveFig=True)
"""


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

csv_filename = './' + names[index] +'.csv'
CS = CrossSections(files[index])
#CS.make_CS(Ir_193mPt(), 'Ir', 'Ir_193mPt.csv', 10, 'Ir_193mPt',csv_filename )
#CS.make_CS(Cu_57Ni(), 'Cu', 'Cu_57Ni.csv', 10, 'Cu_57Ni')
#CS.make_CS(Ni_56Ni(), 'Ni', 'Ni_56Ni.csv', 10, 'Ni_56Ni')

#CS.make_CS(Ni_61Cu(), 'Ni', 'Ni_61Cu.csv', 10, 'Ni_61Cu', csv_filename)
#CS.mon_CS_test(Ni_61Cu(), 'Ni', 'Ni_61Cu.csv', 10, 'Ni_61Cu', names[index], csv_filename)
#print("**")

CS.make_CS(Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu', csv_filename)


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







#BC = BeamCurrent(files[numb])
#BC.variance_minimization(3-1, names[numb], include_56Co=False, MakePlot=True)

#BC.plot_simple_distribution('Cu', names[46])
#BC.plot_simple_distribution('Ni', names[46])
#BC.plot_simple_distribution('Fe', names[46])
#BC.plot_simple_distribution('Ir', names[46])


#BC.plot_distribution('Cu', names[45])

#print("**",files[1])

#sort_ziegler(files[1])
#for i in range(len(names)):
    #print(i, names[i])

#sort_ziegler(files[0])


#BC = BeamCurrent(files[253])
#BC.CurrentPlot_compartment(names[253])
#BC.current_for_CS(return_energies=False, mon_test=False)
#BC.CurrentPlot(names[0])
#BC.plot_distribution('Cu', names[numb])



#Important: these files are bad to use. Remove from files, names
list_of_bad_indices = [45, 62, 63, 71, 72, 80, 81,89, 90, 98, 99, 100, 107, 108, 109, 116, 117, 118,
                        125, 126, 127, 134, 136,143, 144, 145, 153, 154, 162, 163, 171, 172, 180, 181,
                        182, 189, 190, 191, 198, 199, 200, 207, 208, 209, 216, 217, 218, 225, 226, 227,
                        234, 235, 236, 243, 244, 245, 252, 253, 254, 255, 256, 259, 261, 262, 263, 264, 265 ]

#print(files[45])
#for i in list_of_bad_indices:
#    files.remove(files[i])
#    names.remove(names[i])
#files.remove(files[45])
#print(files[45])






"""
BC.plot_distribution('Cu', names[50])
BC.plot_distribution('Fe', names[50])
BC.plot_distribution('Ni', names[50])
I_Fe, I_Ni, I_Cu=BC.current_for_CS(mon_test=True)
print("Fe:",I_Fe)
print("Ni:",I_Ni)
print("Cu:",I_Cu)
"""

#CS.make_CS(Fe_56Co(), 'Fe', 'Fe_56Co.csv', 3, 'Fe_56Co')

"""
CS = CrossSections(files[numb])
CS.mon_CS_test(Fe_56Co(), 'Fe', 'Fe_56Co.csv', 3, 'Fe_56Co', names[numb])
CS.mon_CS_test(Ni_61Cu(), 'Ni', 'Ni_61Cu.csv', 10, 'Ni_61Cu', names[numb])
CS.mon_CS_test(Ni_56Co(), 'Ni', 'Ni_56Co.csv', 10, 'Ni_56Co', names[numb])
CS.mon_CS_test(Ni_58Co(), 'Ni', 'Ni_58Co.csv', 10, 'Ni_58Co', names[numb])
CS.mon_CS_test(Cu_62Zn(), 'Cu', 'Cu_62Zn.csv', 10, 'Cu_62Zn', names[numb])
CS.mon_CS_test(Cu_63Zn(), 'Cu', 'Cu_63Zn.csv', 10, 'Cu_63Zn', names[numb])
CS.mon_CS_test(Cu_65Zn(), 'Cu', 'Cu_65Zn.csv', 10, 'Cu_65Zn', names[numb])
"""


###FOR CROSS SECTIONS: Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu')

#I_Fe, I_Ni, I_Cu = BC.current_for_CS(mon_test=True)
#print(I_Fe)




#A0, E, CS, I = CS.cross_section(Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu',  plot_CS=False)






#BC = BeamCurrent(files[70])
#print(names[70])
#I = BC.current_for_CS(return_energies=False)[0]
#print(I)
#CS = CrossSections(files[57])
#path = os.getcwd() + '/activity_csv/'
#file = path + 'Ni_61Cu.csv'

#file = path + 'Cu_57Ni.csv/'
#x = CS.cross_section(Cu_57Ni(), 'Cu', 'Cu_57Ni.csv', 10)

#x = CS.cross_section(Ir_193mPt(), 'Ir', 'Ir_193mPt.csv', 10, 'Ir_193mPt', plot_CS=True)
#x = CS.cross_section(Cu_57Ni(), 'Cu', 'Cu_57Ni.csv', 10, 'Cu_57Ni', plot_CS=True)
#x = CS.cross_section(Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu', plot_CS=True)


#single_decay_data(Cu_64Cu(), "Cu_64Cu", 10, Save_csv=True)

def get_vals(react_func, target, csv_file, n, reaction):
    CS_class = CrossSections(files[25])
    A0, E, CS, I = CS_class.cross_section(react_func, target, csv_file, n, reaction, plot_CS=True)
    print("A0:", A0)
    print("E:",  E)
    print("CS:", CS)
    print("I:",  I)


if __name__ == "__main__":
    print(__name__)
