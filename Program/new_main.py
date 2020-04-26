from jan20_CrossSections import CrossSections
#from ZieglerFiles_new import ziegler_files
#from feb20_zieglerfiles import ziegler   #newest with all cleaned files
#from single_decay_A0 import *
from des19_BeamCurrent import *

from BC_ziegler_run import *

#from feb20_activity import *
from foil_info import *

from simulated_CrossSectionData import SimCrossSectionData



f_list_FilesNames = 'ziegler_FilesNames.csv'
files = np.genfromtxt(f_list_FilesNames, dtype="str", delimiter='|', usecols=[0])
names = np.genfromtxt(f_list_FilesNames, dtype="str", delimiter='|', usecols=[1])
files = list(files)
names = list(names)

good_beamcurrents = ['B_+10_D_-2', 'B_+0,75_D_-3,25', 'B_+1_D_-1,75', 'B_+0,75_D_-2,75', 'B_+0,75_D_-3', 'B_+0,5_D_-4,25',
					'B_+0,5_D_-3,75', 'B_+0,25_D_-4,75', 'B_+0,5_D_-4', 'B_+0,25_D_-5', 'B_-2,5_D_+4', 'B_+1_D_+1,25', 'B_+1,25_D_+2',
					'B_+1,5_D_+2,5', 'B_+1,5_D_+2,75', 'B_+2,25_D_+5', 'B_+2_D_+3,75', 'B_+1,75_D_+3,25', 'B_+2,5_D_+4,5', 'B_+2,25_D_+4,75',
					'B_+0,5_D_+1,25', 'B_+1,5_D_+3', 'B_+2,5_D_+7,5', 'B_+1,75_D_+3,5', 'B_+2_D_+4,25', 'B_+10_D_+3', 'B_-2,25_D_-1,75', 'B_+10_D_+2,5',
					'B_+1_D_+2', 'B_0_D_0']


def find_index(list, element):
    return list.index(element)


good_files=['B_+1_D_+1,25', 'B_+1,25_D_+2', 'B_+1,5_D_+2,75', 'B_+2,25_D_+5','B_+2,5_D_+7,5','B_+1_D_+2', 'B_0_D_0']
#index = find_index(names, 'B_+0,5_D_+1,25')
index = find_index(names, 'B_+2_D_+4,25')  # looks good but downside: weird ziegler flux distribution
#index = find_index(names, 'B_+0,75_D_-2,75')
#index = find_index(names, 'B_0_D_0')
#index = find_index(names, good_files[-2])


name = names[index]


BC = BeamCurrent(files[index])
CS = CrossSections(files[index])
#BC.plot_distribution('all', files[index])
#BC.plot_distribution('Ir', files[index])


#BC.CurrentPlot_compartment(name=name, WABC = 'averaged_currents.csv', title='Beam current - after variance minimization')

### Ziegler filenames
ziegler_filename = './' + files[index] 
print(ziegler_filename)


### Matrices containing all data, which are going into Andrew's function Average_Beamcurrent in weighted_average.py
### Ni: 61Cu, 56Co, 58Co, Cu: 62Zn, 63Zn, 65Zn, Fe: 56Co
#A0, sigma_A0, lambda_, mass_density, sigma_mass_density, reaction_integral, uncertainty_integral, irr_time, sigma_irr_time = BC.reshaping_parameters()
### Making a new csv file. If ran once, the csv can be called like below: WABS_file
#weighted_average_BC, sigma_weighted_average_BC = Average_BeamCurrent(A0, sigma_A0, mass_density, sigma_mass_density,  lambda_, reaction_integral, uncertainty_integral, irr_time, sigma_irr_time, csv_filename=ziegler_filename, save_csv=True)

WABC_file = 'WABC_'+ ziegler_filename[10:-11] + '.csv'
#print(WABC_file)
#BC.CurrentPlot_compartment(names[index], WABC=WABC_file, title='After variance minimization')
#BC.CurrentPlot_compartment(names[index], WABC=WABC_file, title='Before variance minimization')
#BC.plot_distribution('all', name)
#BC.plot_distribution('all', name)
#BC.variance_minimization(3, name, include_56Co=True, MakePlot=True)
#BC.variance_minimization(6, name, include_56Co=True, MakePlot=True)
#BC.variance_minimization(9, name, include_56Co=True, MakePlot=True)



CS.mon_CS_test(Fe_56Co(), 'Fe', 'Fe_56Co.csv', 3, 'Fe_56Co', names[index], WABC_file)
CS.mon_CS_test(Ni_61Cu(), 'Ni', 'Ni_61Cu.csv', 10, 'Ni_61Cu', names[index], WABC_file)
CS.mon_CS_test(Ni_56Co(), 'Ni', 'Ni_56Co.csv', 10, 'Ni_56Co', names[index], WABC_file)
CS.mon_CS_test(Ni_58Co(), 'Ni', 'Ni_58Co.csv', 10, 'Ni_58Co', names[index], WABC_file)
CS.mon_CS_test(Cu_62Zn(), 'Cu', 'Cu_62Zn.csv', 10, 'Cu_62Zn', names[index], WABC_file)
CS.mon_CS_test(Cu_63Zn(), 'Cu', 'Cu_63Zn.csv', 10, 'Cu_63Zn', names[index], WABC_file)
CS.mon_CS_test(Cu_65Zn(), 'Cu', 'Cu_65Zn.csv', 10, 'Cu_65Zn', names[index], WABC_file)






# just a for loop testing various values of ziegler density and bc energy. 


"""
numb=1
for i in good:
	index = find_index(names, i)
	print(numb, i)

	BC = BeamCurrent(files[index])
	CS = CrossSections(files[index])

	#BC.plot_distribution('Ir', i)
	#BC.plot_distribution('Cu', i)
	#BC.plot_distribution('Ni', i)
	#BC.plot_distribution('Fe', i)
	BC.plot_distribution('all', i)

	#BC.CurrentPlot(i, SaveFig=True)
	BC.CurrentPlot_compartment(i, WABC = 'averaged_currents.csv', title=i)
	numb+=1
"""






####