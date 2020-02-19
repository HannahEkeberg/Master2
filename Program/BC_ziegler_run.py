
from des19_BeamCurrent import BeamCurrent
import numpy as np


import matplotlib.pyplot as plt


"""
Testing variance minimization for all ziegler files. 

run_beam_current: 
makes plots of the beam current with and without the compartment estimated current. 


run_beam_current_in_compartment:
Estimates the chi^2, and gives a plot of the chosen compartmen with estimated energy. 

flux_distribution:
gives the flux distribution for each foil. 

plot_ChiSq:
Plots the chi^2 for the chosen compartment. And provides a csv file with the chi^2 values with the files with chi^2 within the tolerance.
Tolerance is how large values to include from the min value. 

run_varmin:
Not in use anymore?? 


"""

class Run_Ziegler:

    def __init__(self, files, names):
        self.files = files
        self.names = names

        #self.list_of_bad_indices = [45, 62, 63, 71, 72, 80, 81,89, 90, 98, 99, 100, 107, 108, 109, 116, 117, 118,
        #                        125, 126, 127, 134, 136,143, 144, 145, 153, 154, 162, 163, 171, 172, 180, 181,
        #                        182, 189, 190, 191, 198, 199, 200, 207, 208, 209, 216, 217, 218, 225, 226, 227,
        #                        234, 235, 236, 243, 244, 245, 252, 253, 254, 255, 256, 259, 261, 262, 263, 264, 265 ]

        #for ind in self.list_of_bad_indices:
            #self.files.remove(self.files[ind])
            #self.names.remove(self.names[ind])

    def run_beam_current(self):
        #if type(self.names) == str:
            #print(names, files)
        #    myclass = BeamCurrent(self.files)
            #myclass = BeamCurrent(self.file)
        #    myclass.CurrentPlot(self.names)
        #else:
        n = len(self.names)
        print(n)
        for i in range(n):
            try:
                myclass = BeamCurrent(self.files[i])
                myclass.CurrentPlot_compartment(self.names[i])
                print(i)
            except:
                print("the following index does not work", i)
                print("name of file: ",  self.names[i])
                pass

                #myclass.CurrentPlot(self.names[i])

    def run_beam_current_in_compartment(self, compartment):
        for i in range(len(self.names)):
            myclass = BeamCurrent(self.files[i])
            variance_minimization(compartment, self.names[i], MakePlot=True)


    def chi_squared(self, compartment):
        pass


    def run_beamcurrent_compartment(self, compartment):
        pass
        #if type(self.names) == str:
            #print(names, files)
            #myclass = BeamCurrent(self.files)
            #myclass = BeamCurrent(self.file)
            #myclass.CurrentPlot(self.names)
    #else:
        #n = len(self.names)
        #for i in range(n):
    #        myclass = BeamCurrent(self.files[i])
            #myclass.variance_minimization(compartment, self.names[i], MakePlot=True)

                #myclass = BeamCurrent(self.files[i])
                #myclass.CurrentPlot(self.names[i])


    def flux_distribution(self, foil):
        if type(self.names) == str:
            myclass = BeamCurrent(self.files)
            myclass.plot_distribution(foil, self.names)
        else:
            n = len(self.names)
            for i in range(n):
                myclass = BeamCurrent(self.files[i])
                try:
                    myclass.plot_distribution(foil, self.names[i])
                    print(i)

                except:
                    print("the following index does not work: ", i)
                    print("name of file: ",  self.names[i])
                    myclass.plot_simple_distribution(foil, self.names[i])
                    pass


    def plot_ChiSq(self, compartment, chi_tol=2):
        chi_sq_list = []
        E_Ni_list = []
        colors = ['darkorange', 'forestgreen', 'palevioletred']#, 'darkorange', 'forestgreen', 'orchid', 'dodgerblue', 'lime', 'crimson', 'indianred']
        for i in range(len(self.names)):
            try:
                myclass = BeamCurrent(self.files[i])
                WE_Ni, chi_sq, I_est, sigma_I_est = myclass.variance_minimization(compartment-1, self.names[i], MakePlot=False)
                chi_sq_list.append(chi_sq)
                E_Ni_list.append(WE_Ni)


            except:
                print("bad file:",i)
                pass

        #print(min(chi))
        index = chi_sq_list.index(min(chi_sq_list))    #min_chi = min(chi_sq)

        print(index)
        zf = self.names[index]

        list_of_chi   = []
        list_of_names = []
        for i in chi_sq_list:
            if i < min(chi_sq_list)+chi_tol:
                index = chi_sq_list.index(i)
                plt.axvline(E_Ni_list[index], linestyle='--', linewidth=0.2, label=self.names[index]+r' -$\chi^2=${:.2f} '.format(chi_sq_list[index]))
                list_of_chi.append(chi_sq_list[index])
                list_of_names.append(self.names[index])

        csv_save = np.vstack((list_of_names, list_of_chi)).T
        #print(type(csv_save))
        
        np.savetxt('min_chi_comp{}.csv'.format(compartment), csv_save, delimiter='|', header='Filename, Chi^2', fmt="%s"  )#, %.6f, %.6f")

        #plt.axvline(E_Ni_list[index], color=colors[0], label=zf+r' -$\chi^2=${:.2f} '.format(chi_sq_list[index])
        plt.plot(E_Ni_list, chi_sq_list,'.')
        plt.title('Variance minimization of compartment {}'.format(compartment))
        plt.ylabel(r'$\chi^2$')
        plt.legend(fontsize='xx-small', loc='best')
        plt.xlabel('Deuteron energy entering stack compartment number {} (MeV)'.format(compartment))
        plt.savefig('BeamCurrent/Chi_minimization/chi_squared_comp_{}'.format(compartment), dpi=300)

        plt.show()


    def run_varmin(self, files, names, compartment, makePlot=False):

        compartment = compartment-1
        #arrays are indexed from zero, compartments entering this function is true position 1,2,3,4,5..
        if type(names) == str:
            #print(names, files)
            myclass = BeamCurrent(self.files)
            WE_Ni, chi, I_est, dI_est = myclass.variance_minimization(compartment, names, MakePlot=True)

        else:
            n           = len(names)
            Ni_en_Ni = []   #np.zeros(n)
            Ni_en_Cu = []   #np.zeros(n)
            Ni_en_Fe = []   #np.zeros(n)
            Ni_en_SS = []   #np.zeros(n)
            Ni_en_BC = []   #np.zeros(n)
            chi_sq_Ni      = []#np.zeros(n)
            chi_sq_Cu      = []#np.zeros(n)
            chi_sq_Fe      = []#np.zeros(n)
            chi_sq_SS      = []#np.zeros(n)
            chi_sq_BC      = []
            I           = []   #np.zeros(n)
            dI          = []   #np.zeros(n)
            for i in range(n):
                print("File:", i)
                myclass = BeamCurrent(files[i])
                WE_Ni, chi, I_est, dI_est = myclass.variance_minimization(compartment, names[i], MakePlot=True)
                #Ni_energies.append(WE_Ni)
                if 'Ni' in names[i]:
                    chi_sq_Ni.append(chi)
                    Ni_en_Ni.append(WE_Ni)
                if 'Cu' in names[i]:
                    chi_sq_Cu.append(chi)
                    Ni_en_Cu.append(WE_Ni)
                if 'Fe' in names[i]:
                    chi_sq_Fe.append(chi)
                    Ni_en_Fe.append(WE_Ni)
                if 'SS' in names[i]:
                    chi_sq_SS.append(chi)
                    Ni_en_SS.append(WE_Ni)
                if 'BC' in names[i]:
                    chi_sq_BC.append(chi)
                    Ni_en_BC.append(WE_Ni)

                #chi_sq.append(chi)
                I.append(I_est)
                dI.append(dI_est)

                I = myclass.current_for_CS()
                #print(names[i], I)


            #Ni_energies, chi_sq = zip(*sorted(zip(Ni_energies, chi_sq)))

            #index = chi_sq.index(min(chi_sq))
            #print("Compartment:", compartment+1)
            #print(r"Lowest $\chi^2$:", chi_sq[index])
            #print("Scaling parameter:", names[index])
            #print("Beam current:", I[index], r'$\pm$', dI[index]  )
            #print(len(Ni_energies))
            #print(len(chi_sq_Cu))


            if makePlot==True:

                plt.plot(Ni_en_Ni, chi_sq_Ni, '.', label=r'$\chi^2$ Ni')
                plt.plot(Ni_en_Cu, chi_sq_Cu, '.', label=r'$\chi^2$ Cu')
                plt.plot(Ni_en_Fe, chi_sq_Fe, '.', label=r'$\chi^2$ Fe')
                plt.plot(Ni_en_SS, chi_sq_SS, '.', label=r'$\chi^2$ SS')
                plt.plot(Ni_en_BC, chi_sq_BC, '.', label=r'$\chi^2$ BC')
                #plt.show()

                #plt.plot(Ni_energies, chi_sq_, '.')
                plt.title(r'$\chi^2$ minimization - Compartment {}'.format(compartment+1))
                plt.xlabel('Deuteron energy entering stack compartment number {} (MeV)'.format(compartment+1))
                plt.ylabel(r'$\chi^2$')
                plt.legend()
                plt.savefig('BeamCurrent/Chi_minimization/chi_squared_comp_{}'.format(compartment+1), dpi=300)
                plt.show()


if __name__=='__main__':
    print("Run from BC_zieger_run.py")

