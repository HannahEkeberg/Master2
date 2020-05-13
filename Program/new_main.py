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
# index = find_index(names, 'B_0_D_0')
#index = find_index(names, good_files[-2])
#index= find_index(names, good_files[0])

print(names[index])
name = names[index]


BC = BeamCurrent(files[index])
CS = CrossSections(files[index])
#BC.plot_distribution('all', files[index])
#BC.plot_distribution('Ir', files[index])



# RZ = Run_Ziegler(files, names)
# RZ.plot_ChiSq(6)


#BC.CurrentPlot_compartment(name=name, WABC = 'averaged_currents.csv', title='Beam current - after variance minimization')

### Ziegler filenames
ziegler_filename = './' + files[index] 
#print(ziegler_filename)


### Matrices containing all data, which are going into Andrew's function Average_Beamcurrent in weighted_average.py
### Ni: 61Cu, 56Co, 58Co, Cu: 62Zn, 63Zn, 65Zn, Fe: 56Co
#A0, sigma_A0, lambda_, mass_density, sigma_mass_density, reaction_integral, uncertainty_integral, irr_time, sigma_irr_time = BC.reshaping_parameters()

#Making a new csv file. If ran once, the csv can be called like below: WABS_file
#weighted_average_BC, sigma_weighted_average_BC = Average_BeamCurrent(A0, sigma_A0, mass_density, sigma_mass_density,  lambda_, reaction_integral, uncertainty_integral, irr_time, sigma_irr_time, csv_filename=ziegler_filename, save_csv=True)



"""
### TESTING IF ANY OTHER BC's IMPROVES 63Zn
for i in good_files:
	index=find_index(names, i)  # looks good but downside: weird ziegler flux distribution
	#print(index)
	BC = BeamCurrent(files[index])
	CS = CrossSections(files[index])
	ziegler_filename = './' + files[index] 
	WABC_file = 'WABC_'+ ziegler_filename[10:-11] + '.csv'
	CS.mon_CS_test(Cu_63Zn(), 'Cu', 'Cu_63Zn.csv', 10, 'Cu_63Zn', names[index], WABC_file)
"""
#BC.plot_distribution('all', files[index])
#BC.plot_distribution('Ir', files[index])


#BC.CurrentPlot_compartment(name=name, WABC = 'averaged_currents.csv', title='Beam current - after variance minimization')

### Ziegler filenames
ziegler_filename = './' + files[index] 

WABC_file = 'WABC_'+ ziegler_filename[10:-11] + '.csv'

#print(WABC_file)
# BC.CurrentPlot_compartment(names[index], WABC=WABC_file, title='After variance minimization')
# BC.CurrentPlot_compartment(names[index], WABC=WABC_file, title='Before variance minimization')
#BC.plot_distribution('all', name)
#BC.plot_distribution('all', name)
#BC.variance_minimization(3, name, include_56Co=True, MakePlot=True)
#BC.variance_minimization(6, name, include_56Co=True, MakePlot=True)
#BC.variance_minimization(9, name, include_56Co=True, MakePlot=True)


#MONITOR REACTIONS

# CS.mon_CS_test(Fe_56Co(), 'Fe', 'Fe_56Co.csv', 3, 'Fe_56Co', names[index], WABC_file)
# CS.mon_CS_test(Ni_61Cu(), 'Ni', 'Ni_61Cu.csv', 10, 'Ni_61Cu', names[index], WABC_file)
# CS.mon_CS_test(Ni_56Co(), 'Ni', 'Ni_56Co.csv', 10, 'Ni_56Co', names[index], WABC_file)
# CS.mon_CS_test(Ni_58Co(), 'Ni', 'Ni_58Co.csv', 10, 'Ni_58Co', names[index], WABC_file)
# CS.mon_CS_test(Cu_62Zn(), 'Cu', 'Cu_62Zn.csv', 10, 'Cu_62Zn', names[index], WABC_file)
# CS.mon_CS_test(Cu_63Zn(), 'Cu', 'Cu_63Zn.csv', 10, 'Cu_63Zn', names[index], WABC_file)
# CS.mon_CS_test(Cu_65Zn(), 'Cu', 'Cu_65Zn.csv', 10, 'Cu_65Zn', names[index], WABC_file)



### Ni reactions

# CS.make_CS(Ni_52Mn(), 'Ni', 'Ni_52Mn.csv', 10, 'Ni_52Mn', WABC_file, '25', '52', independent=False, ylimit=10, CS_colonne_ALICE=5, file_ending='.tot', isomer_state=None)   # using 1434 keV line 
# CS.make_CS(Ni_54Mn(), 'Ni', 'Ni_54Mn.csv', 10, 'Ni_54Mn', WABC_file, '25', '54', ylimit=40, independent=True, CS_colonne_ALICE=5)


#!!!!!
# CS.make_CS(Ni_56Mn(), 'Ni', 'Ni_56Mn.csv', 10, 'Ni_56Mn', WABC_file, '25', '56', ylimit=1.2, independent=False, CS_colonne_ALICE=5)  #, very uncertain on this cross section measurement. Used all strong lines, only points from 12 hours or less and took out high activities. 
#!!!!!

# CS.make_CS(Ni_59Fe(), 'Ni', 'Ni_59Fe.csv', 10, 'Ni_59Fe', WABC_file, '26', '59', independent=False,CS_colonne_ALICE=5, ylimit=1)   # first in decay chain
# CS.make_CS(Ni_55Co(), 'Ni', 'Ni_55Co.csv', 10, 'Ni_55Co', WABC_file, '27', '55', ylimit=45,independent=False,CS_colonne_ALICE=5) # first in decay chain

# CS.make_CS(Ni_60Co(), 'Ni', 'Ni_60Co.csv', 10, 'Ni_60Co', WABC_file, '27', '60', ylimit=55, independent=False,CS_colonne_ALICE=5) # first in decay chain
# CS.make_CS(Ni_65Ni(), 'Ni', 'Ni_65Ni.csv', 10, 'Ni_65Ni', WABC_file, '28', '65', independent=True,CS_colonne_ALICE=5) # first in decay chain
# CS.make_CS(Ni_60Cu(), 'Ni', 'Ni_60Cu.csv', 10, 'Ni_60Cu', WABC_file, '29', '60',CS_colonne_ALICE=5, ylimit=75)
# CS.make_CS(Ni_64Cu(), 'Ni', 'Ni_64Cu.csv', 10, 'Ni_64Cu', WABC_file, '29', '64',CS_colonne_ALICE=5)


# CS.make_CS(Ni_58mCo(), 'Ni', 'Ni_58mCo.csv', 10, 'Ni_58mCo', WABC_file, '27', '58', ylimit=270, independent=True,CS_colonne_ALICE=7, isomer_state='m', file_ending='.L01')
# CS.make_CS(Ni_58Co(), 'Ni', 'Ni_58Co.csv', 10, 'Ni_58Co', WABC_file, '27', '58', ylimit=200, independent=True,CS_colonne_ALICE=6, isomer_state=None, file_ending='.L00')
# CS.make_CS_subtraction('daughter', 'Ni', 10, WABC_file, Ni_58mCo(), 'Ni_58mCo', 'Ni_58mCo.csv', '28', '58',  Ni_58Co(), 'Ni_58Co', 'Ni_58Co.csv', '27', '58', BR_daughter=1.0, ylimit=None, isomer_state=None, independent=False, file_ending='.tot', save_text=True, feeding=None, CS_colonne_ALICE=5, force_legend='upper right')  # Necessary when subtracting

# CS.make_CS(Ni_57Co(), 'Ni', 'Ni_57Co.csv', 10, 'Ni_57Co', WABC_file, '27', '57', ylimit=600, independent=True,CS_colonne_ALICE=5, file_ending='.tot', feeding='beta+') # first in decay chain)
# CS.make_CS(Ni_57Ni(), 'Ni', 'Ni_57Ni.csv', 10, 'Ni_57Ni', WABC_file, '28', '57', ylimit=125, independent=False,CS_colonne_ALICE=5, file_ending='.tot') # first in decay chain)
# CS.make_CS_subtraction('daughter', 'Ni', 10, WABC_file, Ni_57Ni(), 'Ni_57Ni', 'Ni_57Ni.csv', '28', '57',  Ni_57Co(), 'Ni_57Co', 'Ni_57Co.csv', '27', '57', BR_daughter=1.0, ylimit=None, isomer_state=None, independent=False, file_ending='.tot', save_text=True, feeding='beta+', CS_colonne_ALICE=5)  # Necessary when subtracting


# CS.make_CS(Ni_56Ni(), 'Ni', 'Ni_56Ni.csv', 10, 'Ni_56Ni', WABC_file, '28', '56', ylimit=2.0, independent=False, BR=None, CS_colonne_ALICE=5) # first in decay chain)
# CS.make_CS_subtraction('daughter', 'Ni', 10, WABC_file, Ni_56Ni(), 'Ni_56Ni', 'Ni_56Ni.csv', '28', '56',  Ni_56Co(), 'Ni_56Co', 'Ni_56Co.csv', '27', '56', BR_daughter=1.0, ylimit=80, isomer_state=None, independent=False, file_ending='.tot', save_text=True, feeding='beta+', CS_colonne_ALICE=5, force_legend="upper center")  # Necessary when subtracting
# CS.make_CS(Ni_56Co(), 'Ni', 'Ni_56Co.csv', 10, 'Ni_56Co', WABC_file, '27', '56', independent=True, CS_colonne_ALICE=5, ylimit=80) # first in decay chain)


### Cu reactions

# CS.make_CS(Cu_59Fe(), 'Cu', 'Cu_59Fe.csv', 10, 'Cu_59Fe', WABC_file, '26', '59', ylimit=1, independent=False, CS_colonne_ALICE=5) # first in decay chain
# CS.make_CS(Cu_60Co(), 'Cu', 'Cu_60Co.csv', 10, 'Cu_60Co', WABC_file, '27', '60', ylimit=25, independent=False, CS_colonne_ALICE=5) # first in decay chain)   
# CS.make_CS(Cu_61Co(), 'Cu', 'Cu_61Co.csv', 10, 'Cu_61Co', WABC_file, '27', '61', ylimit=4, independent=False,CS_colonne_ALICE=5) # first in decay chain)  
# CS.make_CS(Cu_65Ni(), 'Cu', 'Cu_65Ni.csv', 10, 'Cu_65Ni', WABC_file, '28', '65', CS_colonne_ALICE=5)
# CS.make_CS(Cu_61Cu(), 'Cu', 'Cu_61Cu.csv', 10, 'Cu_61Cu', WABC_file, '29', '61', ylimit=110, independent=False, CS_colonne_ALICE=5) # first in decay chain)   
# CS.make_CS(Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu', WABC_file, '29', '64', CS_colonne_ALICE=5, ylimit=300, force_legend="upper center")

### Fe reactions 
# CS.make_CS(Fe_48V(), 'Fe', 'Fe_48V.csv', 3, 'Fe_48V', WABC_file, '23', '48', independent=False, file_ending='.tot', ylimit=0.176, CS_colonne_ALICE=5)   
# CS.make_CS(Fe_51Cr(), 'Fe', 'Fe_51Cr.csv', 3, 'Fe_51Cr', WABC_file, '24', '51', independent=False, ylimit=20, CS_colonne_ALICE=5)   
# CS.make_CS(Fe_52Mn(), 'Fe', 'Fe_52Mn.csv', 3, 'Fe_52Mn', WABC_file, '25', '52', ylimit=50, independent=False, CS_colonne_ALICE=5)   
# CS.make_CS(Fe_54Mn(), 'Fe', 'Fe_54Mn.csv', 3, 'Fe_54Mn', WABC_file, '25', '54', independent=True, ylimit=125, CS_colonne_ALICE=5)   
# CS.make_CS(Fe_53Fe(), 'Fe', 'Fe_53Fe.csv', 3, 'Fe_53Fe', WABC_file, '26', '53', independent=False, CS_colonne_ALICE=5)   
# CS.make_CS(Fe_59Fe(), 'Fe', 'Fe_59Fe.csv', 3, 'Fe_59Fe', WABC_file, '26', '59', independent=True, CS_colonne_ALICE=5)   # only produced via 58Fe(d,n). abundance is low so had to redo energy. Ask Andrew about energy. 
# CS.make_CS(Fe_55Co(), 'Fe', 'Fe_55Co.csv', 3, 'Fe_55Co', WABC_file, '27', '55', independent=True, CS_colonne_ALICE=5)   
# CS.make_CS(Fe_57Co(), 'Fe', 'Fe_57Co.csv', 3, 'Fe_57Co', WABC_file, '27', '57', independent=True, CS_colonne_ALICE=5)   
# CS.make_CS(Fe_58Co(), 'Fe', 'Fe_58Co.csv', 3, 'Fe_58Co', WABC_file, '27', '58', independent=False, CS_colonne_ALICE=5)   



### Ir reactions
#CS.make_CS(Ir_188Pt(), 'Ir', 'Ir_188Pt.csv', 10, 'Ir_188Pt', WABC_file, '78', '188', ylimit=300, independent=True)   
#CS.make_CS(Ir_188Ir(), 'Ir', 'Ir_188Ir.csv', 10, 'Ir_188Ir', WABC_file, '77', '188', ylimit=15, independent=False, isomer_state='m1+g', CS_colonne_ALICE=4, feeding='beta+', BR=1.0, reaction_parent='Ir_188Pt')
#CS.make_CS_subtraction('daughter', 'Ir', 10, WABC_file, Ir_188Pt(), 'Ir_188Pt', 'Ir_188Pt.csv', '78', '188',  Ir_188Ir(), 'Ir_188Ir', 'Ir_188Ir.csv', '77', '188', ylimit=15, BR_daughter=1.0, isomer_state='m1+g', independent=True, file_ending='.tot', CS_colonne_ALICE=4, save_text=True, feeding=None)  # Necessary when subtracting


#CS.make_CS(Ir_189Pt(), 'Ir', 'Ir_189Pt.csv', 10, 'Ir_189Pt', WABC_file, '78', '189', ylimit=520, independent=True)    # 
#CS.make_CS(Ir_189Ir(), 'Ir', 'Ir_189Ir.csv', 10, 'Ir_189Ir', WABC_file, '77', '189', independent=False, feeding='beta+', BR=1.0, reaction_parent='Ir_189Pt')    # need work on activity 

#CS.make_CS_subtraction('daughter', 'Ir', 10, WABC_file, Ir_189Pt(), 'Ir_189Pt', 'Ir_189Pt.csv', '78', '189',  Ir_189Ir(), 'Ir_189Ir', 'Ir_189Ir.csv', '77', '189', ylimit=500, independent=True, file_ending='.tot', CS_colonne_ALICE=4, BR_daughter=1.0)  # Necessary when subtracting



# CS.make_CS(Ir_190Ir(), 'Ir', 'Ir_190Ir.csv', 10, 'Ir_190Ir', WABC_file, '77', '190', independent=False, CS_colonne_ALICE=4)     # file_ending=.tot because of decay from m1 m2 isomer. 
# CS.make_CS(Ir_190m2Ir(), 'Ir', 'Ir_190m2Ir.csv', 10, 'Ir_190m2Ir', WABC_file, '77', '190', file_ending='.L37', isomer_state='m2', independent=True, CS_colonne_ALICE=6)   # 0.0860   
#CS.make_CS_subtraction('daughter', 'Ir', 10, WABC_file, Ir_190m2Ir(), 'Ir_190m2Ir', 'Ir_190m2Ir.csv', '77', '190',  Ir_190Ir(), 'Ir_190Ir', 'Ir_190Ir.csv', '77', '190', BR_daughter=0.0860, ylimit=None, isomer_state='m1+g', independent=True)#independent='_cumulative_190m1+190Ir', file_ending='.tot')  # Necessary when subtracting

# CS.make_CS(Ir_191Pt(), 'Ir', 'Ir_191Pt.csv', 10, 'Ir_191Pt', WABC_file, '78', '191', independent=True, ylimit=800) 

# CS.make_CS(Ir_192Ir(), 'Ir', 'Ir_192Ir.csv', 10, 'Ir_192Ir', WABC_file, '77', '192', file_ending='.tot', independent=False)    

# CS.make_CS(Ir_194Ir(), 'Ir', 'Ir_194Ir.csv', 10, 'Ir_194Ir', WABC_file, '77', '194', file_ending='.L00', independent=False)    
# CS.make_CS(Ir_194m2Ir(), 'Ir', 'Ir_194m2Ir.csv', 10, 'Ir_194m2Ir', WABC_file, '77', '194', file_ending='not', isomer_state='m2', independent=True, CS_colonne_ALICE=6)     #talys=.L34
# CS.make_CS(Ir_193mPt(), 'Ir', 'Ir_193mPt.csv', 10, 'Ir_193mPt', WABC_file, '78', '193', file_ending='.L05', isomer_state='m', independent=True, CS_colonne_ALICE=6, ylimit=300)   







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



"""
##### INCLUDE IN THEORY!!!!!!!

from scipy.constants import e, epsilon_0
#print(e)
print(epsilon_0)
def coulomb_barrier(Z_a, Z_b, A_a, A_b):
	r0 = 1.25#1.25 #fm,   ca. constant, for nuclear rad

	if Z_a ==1 and A_a==1:
		R_a = 0.877 #fm
	if Z_a ==2 and A_a ==4:
		R_a = 0.923 #fm
	else:	
		R_a = r0*A_a**(1/3)# *1e-15 #m
	R_b = r0*A_b**(1/3)# *1e-15 #m
	#print("particle radius: ", R_a, A_a)
	#print("nuclear radius: ", R_b, A_b)

	#print(R_a)
	#print(r0)
	#K = (4*np.pi*epsilon_0)**(-1)
	K = 1.44 #  constant: ke^2 = MeV/fm
	#epsilon_0 = F/m = e**2/(J*m) = e**2/(6.24*1e18 eV)*m 
	#conversion_unit =  e**2/ (6.24*1e15) # C/(MeV*m ) 

	#Coulomb constant: eV aangstroem per c^2 ---- > MeV fm /c^2:
	#K = 14.3996 *1e3 * 1e-5


	#print(K)
 
	#return e**2/ (4*np.pi*epsilon_0*conversion_unit)   * ( (Z_a*Z_b)/(R_a+R_b)) 
	return K* ( (Z_a*Z_b)/(R_a+R_b)) 
	#return 1

#proton, 193Ir
b1 = coulomb_barrier(1, 78, 1, 193)
b2 = coulomb_barrier(1, 78, 1, 195)
print("mean:", np.mean((b1, b2)))
print("Coulomb barrier for compound nucleus 193Pt: ", b1, "MeV")  
print("Coulomb barrier for compound nucleus 195t: ", b2, "MeV") 
print("***")
b1 = coulomb_barrier(1, 29, 1, 60)
b2 = coulomb_barrier(1, 29, 1, 62)
b3 = coulomb_barrier(1, 29, 1, 63)
b4 = coulomb_barrier(1, 29, 1, 64)
b5 = coulomb_barrier(1, 29, 1, 66)
print("mean:", np.mean((b1, b2, b3, b4)))
print("Coulomb barrier for compound nucleus 60Cu: ", b1, "MeV")  
print("Coulomb barrier for compound nucleus 62Cu: ", b2, "MeV")  
print("Coulomb barrier for compound nucleus 63Cu: ", b3, "MeV")  
print("Coulomb barrier for compound nucleus 64Cu: ", b4, "MeV")  
print("Coulomb barrier for compound nucleus 66Cu: ", b5, "MeV")  
print("***")
b1 = coulomb_barrier(1, 30, 1, 65)
b2 = coulomb_barrier(1, 30, 1, 67)
print("mean:", np.mean((b1, b2)))
print("Coulomb barrier for compound nucleus 65Zn: ", b1, "MeV")  
print("Coulomb barrier for compound nucleus 67Zn: ", b2, "MeV")  
print("***")
b1 = coulomb_barrier(1, 27, 1, 56)
b2 = coulomb_barrier(1, 27, 1, 58)
b3 = coulomb_barrier(1, 27, 1, 59)
b4 = coulomb_barrier(1, 27, 1, 60)
print("mean:", np.mean((b1, b2, b3, b4)))
print("Coulomb barrier for compound nucleus 56Co: ", b1, "MeV")  
print("Coulomb barrier for compound nucleus 58Co: ", b2, "MeV")  
print("Coulomb barrier for compound nucleus 59Co: ", b3, "MeV")  
print("Coulomb barrier for compound nucleus 60Co: ", b4, "MeV")  
"""

"""
def plot_WABC():
	wabc_before = 'WABC_B_0_D_0.csv'
	wabc_after1 = 'WABC_B_+2_D_+4,25.csv'
	wabc_after2 = 'WABC_B_+1_D_+2.csv'
	wabc_after3 = 'WABC_B_+2,25_D_+5.csv'
	wabc_after4 = 'WABC_B_+0,5_D_+1,25.csv'
	E = [30.65, 28.40, 26.03, 23.54, 21.38, 19.03, 16.43, 13.51, 10.09, 5.63]
	colors = ['mediumpurple', 'cyan', 'palevioletred', 'darkorange', 'forestgreen', 'orchid', 'dodgerblue', 'navy', 'crimson', 'indianred']

	wabc0 = np.genfromtxt(wabc_before, delimiter=',', usecols=[1])
	d_wabc0 = np.genfromtxt(wabc_before, delimiter=',', usecols=[2])
	wabc1 = np.genfromtxt(wabc_after1, delimiter=',', usecols=[1])
	d_wabc1 = np.genfromtxt(wabc_after1, delimiter=',', usecols=[2])
	wabc2 = np.genfromtxt(wabc_after2, delimiter=',', usecols=[1])
	d_wabc2 = np.genfromtxt(wabc_after2, delimiter=',', usecols=[2])
	wabc3 = np.genfromtxt(wabc_after3, delimiter=',', usecols=[1])
	d_wabc3 = np.genfromtxt(wabc_after3, delimiter=',', usecols=[2])
	wabc4 = np.genfromtxt(wabc_after4, delimiter=',', usecols=[1])
	d_wabc4 = np.genfromtxt(wabc_after4, delimiter=',', usecols=[2])

	plt.errorbar(E, wabc0, color=colors[0], marker='P', linewidth=0.001, yerr=d_wabc0, elinewidth=0.5, capthick=0.5, capsize=3.0,label='B: 0%, D: 0%')
	plt.errorbar(E, wabc1, color=colors[1], marker='P', linewidth=0.001, yerr=d_wabc1, elinewidth=0.5, capthick=0.5, capsize=3.0,label='B: +2%, D: +4.25%')
	plt.errorbar(E, wabc2, color=colors[2], marker='P', linewidth=0.001, yerr=d_wabc2, elinewidth=0.5, capthick=0.5, capsize=3.0,label='B: +1%, D: +2%')
	plt.errorbar(E, wabc3, color=colors[3], marker='P', linewidth=0.001, yerr=d_wabc3, elinewidth=0.5, capthick=0.5, capsize=3.0,label='B: +2.25%, D: +5%')
	plt.errorbar(E, wabc4, color=colors[4], marker='P', linewidth=0.001, yerr=d_wabc4, elinewidth=0.5, capthick=0.5, capsize=3.0,label='B: +0.25%, D: +1%')
	plt.legend()
	plt.show()

plot_WABC()
"""

"""

def read_XCOM(file, foil):
	path = os.getcwd() 
	f = path + '/../matlab/'+ file
	
	E = np.genfromtxt(f, usecols=[0], skip_header=4)
	E*=1e3
	A = np.genfromtxt(f, usecols=[1], skip_header=4)

	plt.plot(E,A)
	plt.title('Attenuation curve for {}'.format(foil))
	#plt.gca().set_ylim(bottom=0, top=500)
	plt.gca().set_xlim(left=0, right=500)
	plt.ylabel(r'Total attenuation coefficienct (cm$^2$)/g')
	plt.xlabel('Photon energy (keV)')
	plt.show()

# read_XCOM('ir_xcom.txt', 'Ir')
# read_XCOM('ni_xcom.txt', 'Ni')
"""



####