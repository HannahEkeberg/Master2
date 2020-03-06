import numpy as np, matplotlib.pyplot as plt
from scipy import interpolate
from scipy.constants import N_A, elementary_charge
#print(elementary_charge)
import sys
from scipy.stats import norm
from scipy.optimize import curve_fit, minimize_scalar

#print(sys.version)

from beam_current_FoilReact import *    #Program where info regarding foil reaction.
from ziegler_sorting import *  #sorting of ziegler list etc

from ZieglerFiles_new import ziegler_files


from weighted_average import * # Andrew's covariance program

#files,names = ziegler_files()
#print(files)
import os


"""
Ziegler energies and fluxes are used to first find energy and fluxes in different reactions
Function get_FWHM() returns FWHM for specific type of foils in a list for each foil.
Function beam_current() takes in foil and reaction, and returns the dI and I beamcurrent.
Uses functions data and E_flux_integral to get spline and integrals, from equation used
Function WABE (weighted average beam energy) returns the average energy for each foil, and dE
Finally plotting E,I with errorbars.

"""

from scipy.signal import chirp, find_peaks, peak_widths


root_dir = 'BeamCurrent'
current_dir = 'BeamCurrent/current_all'
chi_dir = 'BeamCurrent/chi_minimization'
flux_dir = 'BeamCurrent/beam_fluxes'
comp_dir = 'BeamCurrent/compartment_compare'

if not os.path.exists(root_dir):
    os.mkdir(root_dir)
if not os.path.exists(current_dir):
    os.mkdir(current_dir)
if not os.path.exists(chi_dir):
    os.mkdir(chi_dir)
if not os.path.exists(flux_dir):
    os.mkdir(flux_dir)
if not os.path.exists(comp_dir):
    os.mkdir(comp_dir)


class BeamCurrent:
    def __init__(self, ziegler_file):
        path_to_ziegler_files = os.getcwd() + '/cleaned_zieglerfiles/'
        #print(ziegler_file)
        self.file = path_to_ziegler_files + ziegler_file
        self.sort = sort_ziegler    # from ziegler_sorting.py
        self.Fe_foil = Fe_foil      # from beam_current_FoilReact
        self.Ni_foil = Ni_foil      # from beam_current_FoilReact
        self.Cu_foil = Cu_foil      # from beam_current_FoilReact
        #print("*****",self.file)
        self.E_Ni, self.F_Ni, self.E_Cu, self.F_Cu, self.E_Fe, self.F_Fe, self.E_Ir, self.F_Ir = self.sort(self.file)
        self.path = os.getcwd()


        #self.list_of_bad_indices = [45, 62, 63, 71, 72, 80, 81,89, 90, 98, 99, 100, 107, 108, 109, 116, 117, 118,
        #                        125, 126, 127, 134, 136,143, 144, 145, 153, 154, 162, 163, 171, 172, 180, 181,
        #                        182, 189, 190, 191, 198, 199, 200, 207, 208, 209, 216, 217, 218, 225, 226, 227,
        #                        234, 235, 236, 243, 244, 245, 252, 253, 254, 255, 256, 259, 261, 262, 263, 264, 265 ]

    def get_sigmaE(self, E, F, foil, makePlot=False):

        ### for cupper, flux is going up in end, delete those points!

        dEr = np.zeros(len(E))    # right uncertainty
        dEl = np.zeros(len(E))    # left uncertainty
        fwhm = np.zeros(len(E))
        half_max = []
        mu_array = np.zeros(len(E))
        #E = np.array((E))
        #F = np.array((F))
        for i in range(len(E)):
            M_F = np.max(F[i])     #max Flux
            Min_F = np.min(F[i])
            HM_F = 0.5*M_F         #Half max Flux

            def lin_interp(x, y, i, half):
                return x[i] + (x[i+1] - x[i]) * ((half - y[i]) / (y[i+1] - y[i]))

            def half_max_F(E,F):
                half = max(F)/2.0
                signs = np.sign(np.add(F, -half))
                zero_crossings = (signs[0:-2] != signs[1:-1])
                zero_crossings_i = np.where(zero_crossings)[0]
                return [lin_interp(E, F, zero_crossings_i[0], half),
                        lin_interp(E, F, zero_crossings_i[1], half)]


            hmx = half_max_F(E[i], F[i])
            half_max.append(hmx)
            #(mu,sigma) = norm.fit(E[i])
            E[i] = np.array(E[i])
            mu = np.trapz(F[i]*E[i], E[i])/np.trapz(F[i],E[i])
            fwhm[i] = hmx[1]-hmx[0]
            dEl[i] = mu-hmx[0]; dEr[i] = hmx[1]-mu   #left and right uncertainty in energy
            mu_array[i] = mu


        #if return_fwhm:
            #return fwhm
        #if fwhm[-1]<fwhm[-2]:
        #    print(fwhm)
        if makePlot:
            self.Plot_energy_distribution(E,F,mu_array, fwhm, half_max, foil)  #make plot of energy distribution
        else:
            return dEl, dEr   #return left and right uncertainty


    def plot_simple_distribution(self, foil, name):
        if foil=='Ni':
            E = self.E_Ni; F=self.F_Ni
        elif foil =='Cu':
            E = self.E_Cu; F=self.F_Cu
        elif foil =='Fe':
            E = self.E_Fe; F=self.F_Fe
        elif foil=='Ir':
            E = self.E_Ir; F=self.F_Ir




        for j in range(len(E)):
            plt.plot(E[j], F[j], color='navy', linewidth=0.7)

        #plt.plot(self.E_Ni, self.F_Ni,'.')
        #plt.plot(self.E_Ni, self.F_Ni)
        plt.title(foil+ ' - '+name)
        plt.show()

    def plot_distribution(self, foil, name):
        if foil == 'Ni':
            #print('way')
            self.get_sigmaE(self.E_Ni, self.F_Ni, foil, makePlot=True)
            plt.legend()

        elif foil == 'Cu':
            #print('way')
            self.get_sigmaE(self.E_Cu, self.F_Cu, foil, makePlot=True)
            plt.legend()

        elif foil == 'Fe':
            self.get_sigmaE(self.E_Fe, self.F_Fe, foil, makePlot=True)
            plt.legend()

        elif foil == 'Ir':
            self.get_sigmaE(self.E_Ir, self.F_Ir, foil, makePlot=True)
            print("test")
            plt.legend()
        elif foil == 'all':
            self.get_sigmaE(self.E_Ir, self.F_Ir, foil, makePlot=True)
            self.get_sigmaE(self.E_Fe, self.F_Fe, foil, makePlot=True)
            self.get_sigmaE(self.E_Cu, self.F_Cu, foil, makePlot=True)
            self.get_sigmaE(self.E_Ni, self.F_Ni, foil, makePlot=True)
            #print('way')
        path_to_folder = self.path + '/BeamCurrent/beam_fluxes/'
        plt.title('Energy distribution for {}-foils - '.format(foil) + name)
        plt.savefig(path_to_folder + foil + '_flux_distribution_'+name+'.png', dpi=300)
        #plt.close()
        plt.show()

    def Plot_energy_distribution(self, E, F, mu, fwhm, half_max, foil):
        #print(half_max[0])
        #path_to_folder = self.path + '/BeamCurrent/'

        colors = ['mediumpurple', 'cyan', 'palevioletred', 'darkorange', 'forestgreen', 'orchid', 'dodgerblue', 'lime', 'crimson', 'indianred']
        for j in range(len(E)):
            plt.plot(E[j], F[j], color='navy', linewidth=0.7)
            half = np.max(F[j])*0.5
            plt.plot(half_max[j], [half, half], linewidth=0.8, color=colors[j], label='fwhm={0:.2f}'.format(fwhm[j]))
            plt.vlines(mu[j], ymin=0.0, ymax = np.max(F[j]), linewidth=0.4, linestyle='--')#, label=r'$\mu=${}'.format(mu))
        #plt.title('Energy distribution for {}-foils'.format(foil))
        plt.xlabel('Energy, MeV')
        plt.ylabel(r'Relative deuteron flux, $d\phi/dE$')
        #plt.legend()
        #plt.savefig(path_to_folder + foil + '_flux_distribution'+name+'.png', dpi=300)
        #plt.show()

    def data(self, filename):
        # Function that interpolates over energies and cross sections provided by IAEA
        # Filename is provided in calculate  beam current
        E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
        Cs = np.loadtxt(filename, usecols=[1], skiprows=6)
        sigma_Cs = np.loadtxt(filename, usecols=[2], skiprows=6)

        tck = interpolate.splrep(E_mon, Cs, s=0)
        sigma_tck = interpolate.splrep(E_mon, sigma_Cs, s=0)
        return E_mon, Cs, sigma_Cs, tck, sigma_tck

    def E_flux_integral(self, Cs, sigma_Cs, tck, sigma_tck, E, F, return_interp_CS=False):
        reaction_integral = []    # from beam current equation
        uncertainty_integral = [] # make relative uncertainty, by interpolating over ziegler E
        for i in range(len(E)):
            Cs_ = interpolate.splev(E[i], tck, der=0)*1e-27 #mb--> 1e-27 cm^2. #gives interpolated cross section
            sigma_Cs_ = interpolate.splev(E[i], sigma_tck, der=0) * 1e-27
            relative_sigma_Cs = sigma_Cs_/ Cs_

            #print("relative sigma Cs:", relative_sigma_Cs)
            int_uncertainty = np.trapz(F[i]*relative_sigma_Cs, E[i])/np.trapz(F[i],E[i])
            uncertainty_integral.append(int_uncertainty)

            int_reaction = np.trapz(F[i]*Cs_, E[i])/np.trapz(F[i],E[i])
            reaction_integral.append(int_reaction)

        if return_interp_CS:
            #print(tck)
            E_new = np.linspace(0,60,100)
            #print("*",len(E_new))
            Cs_ = interpolate.splev(E_new, tck, der=0)
            return E_new, Cs_

        return uncertainty_integral, reaction_integral

    def calculate_beam_current(self, foil, react, print_terms=False):   # For non-cumulative cross sections from IAEA.
        irr_time = 3600; sigma_irr_time = 3 #seconds

        if foil == 'Fe':
            F = self.F_Fe
            E = self.E_Fe


            IAEA_Cs, A0, sigma_A0, lambda_, mass_density, sigma_mass_density = self.Fe_foil(react)  #from beam_current_FoilReact
            E_mon, Cs, sigma_Cs, tck, sigma_tck = self.data(IAEA_Cs) #from monitor foils

            """   TESTING THE SPLINES W/ IAEA CS DATA
            E_interp_Cs, interp_Cs = self.E_flux_integral( Cs, sigma_Cs, tck, sigma_tck, E, F, return_interp_CS=True)    # take away later
            #print(len(E_interp_Cs), len(interp_Cs))
            plt.plot(E_mon, Cs, label='IAEA')
            plt.plot(E_interp_Cs, interp_Cs, label='interp',linestyle='--')
            plt.legend()
            plt.show()
            """

        elif foil == 'Ni':
            F = self.F_Ni
            E = self.E_Ni
            if react == 'Ni_61Cu':
                IAEA_Cs, A0, sigma_A0, lambda_, mass_density, sigma_mass_density = self.Ni_foil(react)  #from beam_current_FoilReact
            else:  # Cumulative activities
                IAEA_Cs, A0_dir, sigma_A0_dir, A0_nondir, sigma_A0_nondir, lambda_dir, lambda_nondir, mass_density, sigma_mass_density = self.Ni_foil(react)

            E_mon, Cs, sigma_Cs, tck, sigma_tck = self.data(IAEA_Cs) #from monitor foils
            """
            E_interp_Cs, interp_Cs = self.E_flux_integral( Cs, sigma_Cs, tck, sigma_tck, E, F, return_interp_CS=True)    # take away later
            #print(len(E_interp_Cs), len(interp_Cs))
            plt.plot(E_mon, Cs, label='IAEA')
            plt.plot(E_interp_Cs, interp_Cs, label='interp',linestyle='--')
            plt.legend()
            plt.show()
            """


        elif foil == 'Cu':
            F = self.F_Cu
            E = self.E_Cu

            IAEA_Cs, A0, sigma_A0, lambda_, mass_density, sigma_mass_density = self.Cu_foil(react)  #from beam_current_FoilReact
            E_mon, Cs, sigma_Cs, tck, sigma_tck = self.data(IAEA_Cs) #from monitor foils

            #print(len(E_mon), len(Cs))
            """
            E_interp_Cs, interp_Cs = self.E_flux_integral( Cs, sigma_Cs, tck, sigma_tck, E, F, return_interp_CS=True)    # take away later
            #print(len(E_interp_Cs), len(interp_Cs))
            plt.plot(E_mon, Cs, label='IAEA')
            plt.plot(E_interp_Cs, interp_Cs, label='interp',linestyle='--')
            plt.legend()
            plt.show()
            """

        uncertainty_integral, reaction_integral = self.E_flux_integral(Cs, sigma_Cs, tck, sigma_tck, E, F)
        uncertainty_integral = np.array((uncertainty_integral))
        #print("reaction integral: ", reaction_integral)
        #print("uncertainty integral: ", uncertainty_integral)


        ## CUMULATIVE CURRENTS, see Andrew's note for derivation
        if react=='Ni_58Co' or react=='Ni_56Co':
            BR = 1.0
            sigma_BR = 0.0 # no BR for these reactions.

            #print("dir: ", A0_dir)
            #print("nondir: ", A0_nondir)

            #I = 1/(mass_density * reaction_integral)  * ( A0_dir*elementary_charge*1e9/(1-np.exp(-lambda_dir*irr_time)) + BR*A0_nondir*elementary_charge*1e9/ (1-np.exp(-lambda_nondir*irr_time)) )
            I = ( 1/(mass_density * reaction_integral) ) * (A0_dir + BR*A0_nondir*(lambda_dir/lambda_nondir))*elementary_charge*1e9/(1-np.exp(-lambda_dir*irr_time))
            #print(reaction_integral)
            #dI = np.zeros(len(I))
            dI = np.zeros(len(I))
            #print(dI)
            for i in range(len(A0_nondir)):      #this testing is for 56Co, where the activities of 56Ni is zero for E less than 20MeV. 
                #print("**", i)

                if A0_nondir[i]==0:    
                    #print(A0_nondir[i])
                    #print("yes")
                    dI[i] = I[i] * np.sqrt((sigma_A0_dir[i]/A0_dir[i])**2 + (sigma_BR/BR)**2 + (sigma_mass_density[i]/mass_density[i])**2 + (sigma_irr_time/irr_time)**2 + uncertainty_integral[i]**2)   
                    #print("nondir = 0: ", dI[i])
                    #print(dI)
                else:
                    #print("non_dir")
                    #print(A0_nondir[i])
                    dI[i] = I[i] * np.sqrt((sigma_A0_dir[i]/A0_dir[i])**2 + (sigma_A0_nondir[i]/A0_nondir[i])**2  + (sigma_BR/BR)**2 + (sigma_mass_density[i]/mass_density[i])**2 + (sigma_irr_time/irr_time)**2 + uncertainty_integral[i]**2)
                    #print("nondir != 0: ", dI[i])

            #dI = I * np.sqrt((sigma_A0_dir/A0_dir)**2 + (sigma_A0_nondir/A0_nondir)**2  + (sigma_BR/BR)**2 + (sigma_mass_density/mass_density)**2 + (sigma_irr_time/irr_time)**2 + uncertainty_integral**2)
            #print(dI)

            if print_terms:
                print("mass density", mass_density)
                print("reaction integral", reaction_integral)
                print("underctainty integral", uncertainty_integral)
                print("activity direct", A0_dir)
                print("activity non-direct", A0_nondir)
                print("Beam Current: ", I)
                print("Beam Current uncertainty: ", dI)

        else:
            I  = A0 *elementary_charge*1e9 / (mass_density*(1-np.exp(-lambda_*irr_time))*reaction_integral)
            dI = I * np.sqrt((sigma_A0/A0)**2 + (sigma_mass_density/mass_density)**2 + (sigma_irr_time/irr_time)**2 + uncertainty_integral**2)

            """
            Units: I = nA
            A0 = Bq = s^-1
            e^- = 1.60e-19 C = 1.60e-27 As
            dphi/dE = #deuterions * e^-   #needed to change from # deuterions to C.

            A --> nA:  *1e9


            """


            if print_terms:
                print("mass density", mass_density)
                print("reaction integral", reaction_integral)
                print("underctainty integral", uncertainty_integral)
                print("activity", A0)
                print("I", I)
                print("dI", dI)

        I = np.array(I)



        return I, dI

    def WABE(self, foil): #weighted average beam energy

        if foil == 'Ni':
            E = self.E_Ni; F  = self.F_Ni
        elif foil == 'Cu':
            E = self.E_Cu; F  = self.F_Cu
        elif foil == 'Fe':
            E = self.E_Fe; F  = self.F_Fe
        elif foil == 'Ir':
            E = self.E_Ir; F = self.F_Ir

        dEl, dEr = self.get_sigmaE(E, F, foil)
        energy = []
        for index, item in enumerate(E):
            E[index] = np.array(E[index])
            E_int = np.trapz(F[index]*E[index], E[index])/np.trapz(F[index],E[index])
            energy.append(E_int)

        energy=np.array(energy)

        return energy, [dEl, dEr]

    def specified_currents(self, uncertainty=False):
        I_Fe_56Co, dI_Fe_56Co = self.calculate_beam_current('Fe', 'Fe_56Co')
        I_Ni_61Cu, dI_Ni_61Cu = self.calculate_beam_current('Ni', 'Ni_61Cu')
        I_Ni_56Co, dI_Ni_56Co = self.calculate_beam_current('Ni', 'Ni_56Co')
        I_Ni_58Co, dI_Ni_58Co = self.calculate_beam_current('Ni', 'Ni_58Co')
        I_Cu_62Zn, dI_Cu_62Zn = self.calculate_beam_current('Cu', 'Cu_62Zn')    ##causes some problem in dI    RuntimeWarning: invalid value encountered in true_divide (in dI)
        I_Cu_63Zn, dI_Cu_63Zn = self.calculate_beam_current('Cu', 'Cu_63Zn')    ##causes some problem in dI. Caused by I=0
        I_Cu_65Zn, dI_Cu_65Zn = self.calculate_beam_current('Cu', 'Cu_65Zn')

        """
        print("Ni 61Cu: ", I_Ni_61Cu, dI_Ni_61Cu )
        print("Ni 56Co: ", I_Ni_56Co, dI_Ni_56Co  )
        print("Ni 58Co: ", I_Ni_58Co, dI_Ni_58Co  )
        print("Cu 62Zn: ", I_Cu_62Zn, dI_Cu_62Zn )
        print("Cu 63Zn: ", I_Cu_63Zn, dI_Cu_63Zn)
        print("Cu 65Zn: ", I_Cu_65Zn, dI_Cu_65Zn)
        print("Cu 56Co: ", I_Fe_56Co, dI_Fe_56Co )
        """

        #print(I_Ni_56Co, "56Co")
        #print(I_Ni_58Co, "58Co")
        if uncertainty:
            return dI_Fe_56Co, dI_Ni_61Cu, dI_Ni_56Co, dI_Ni_58Co, dI_Cu_62Zn, dI_Cu_63Zn, dI_Cu_65Zn
        else:
            return I_Fe_56Co, I_Ni_61Cu, I_Ni_56Co, I_Ni_58Co, I_Cu_62Zn, I_Cu_63Zn, I_Cu_65Zn

    def specified_energies(self, uncertainty=False):
        E_Fe, dE_Fe = self.WABE('Fe')
        E_Ni, dE_Ni = self.WABE('Ni')
        E_Cu, dE_Cu = self.WABE('Cu')
        E_Ir, dE_Ir = self.WABE('Ir')

        #print(E_Ni)

        if uncertainty:
            return dE_Fe, dE_Ni, dE_Cu, dE_Ir
        else:
            return E_Fe, E_Ni, E_Cu, E_Ir

    def variance_minimization(self, compartment, name, include_56Co=False, MakePlot=False):
        compartment=compartment-1


        # Compartment means foil number positions
        #variance minimization & standard deviation
        I_Fe_56Co, I_Ni_61Cu, I_Ni_56Co, I_Ni_58Co, I_Cu_62Zn, I_Cu_63Zn, I_Cu_65Zn = self.specified_currents()
        dI_Fe_56Co, dI_Ni_61Cu, dI_Ni_56Co, dI_Ni_58Co, dI_Cu_62Zn, dI_Cu_63Zn, dI_Cu_65Zn = self.specified_currents(uncertainty=True)
        WE_Fe, WE_Ni, WE_Cu, WE_Ir = self.specified_energies()
        #print(WE_Fe, WE_Ni, WE_Cu)
        sigma_WE_Fe, sigma_WE_Ni, sigma_WE_Cu, sigma_WE_Ir = self.specified_energies(uncertainty=True)

        #print(type(I_Ni_61Cu[0]))
        #print(compartment)
        #print(I_Ni_61Cu[compartment])

        I_Ni_61Cu = I_Ni_61Cu[compartment]; dI_Ni_61Cu = dI_Ni_61Cu[compartment]
        I_Ni_56Co = I_Ni_56Co[compartment]; dI_Ni_56Co = dI_Ni_56Co[compartment]
        I_Ni_58Co = I_Ni_58Co[compartment]; dI_Ni_58Co = dI_Ni_58Co[compartment]
        I_Cu_62Zn = I_Cu_62Zn[compartment]; dI_Cu_62Zn = dI_Cu_62Zn[compartment]
        I_Cu_63Zn = I_Cu_63Zn[compartment]; dI_Cu_63Zn = dI_Cu_63Zn[compartment]
        I_Cu_65Zn = I_Cu_65Zn[compartment]; dI_Cu_65Zn = dI_Cu_65Zn[compartment]


        WE_Ni = WE_Ni[compartment]
        WE_Cu = WE_Cu[compartment]
        dWE_Ni = np.array(([sigma_WE_Ni[0][compartment]], [sigma_WE_Ni[1][compartment]]))
        dWE_Cu = np.array(([sigma_WE_Cu[0][compartment]], [sigma_WE_Cu[1][compartment]] ))


        ### TURN ON TO INCLUDE 56Co
        #I_Ni = np.array((I_Ni_61Cu, I_Ni_56Co, I_Ni_58Co))
        #dI_Ni = np.array((dI_Ni_61Cu, dI_Ni_56Co, dI_Ni_58Co))

        ### NEW Ni WITHOUT 56Co
        if include_56Co:
            I_Ni = np.array((I_Ni_61Cu, I_Ni_56Co, I_Ni_58Co))
            dI_Ni = np.array((dI_Ni_61Cu, dI_Ni_56Co, dI_Ni_58Co))
        else:
            I_Ni = np.array((I_Ni_61Cu, I_Ni_58Co))
            dI_Ni = np.array((dI_Ni_61Cu, dI_Ni_58Co))


        I_Cu = np.array((I_Cu_62Zn, I_Cu_63Zn, I_Cu_65Zn))
        dI_Cu = np.array((dI_Cu_62Zn, dI_Cu_63Zn, dI_Cu_65Zn))
        E_Ni = np.ones(len(I_Ni)) * WE_Ni
        E_Cu = np.ones(len(I_Cu)) * WE_Cu
        I = np.concatenate((I_Ni, I_Cu))
        dI = np.concatenate((dI_Ni, dI_Cu))
        E = np.concatenate((E_Ni, E_Cu))

        def I_model(x,b):
            # Linear model, with slope set to 0.
            # Since nothing between foil Cu07 and Ni07, the current degradation=0.
            m = 0
            b = np.ones(len(x))*b
            return x*m + b
        if compartment < len(I_Fe_56Co):
            I_Fe = I_Fe_56Co[compartment]; dI_Fe = dI_Fe_56Co[compartment]
            WE_Fe = WE_Fe[compartment]

            I = np.append(I, I_Fe)
            dI = np.append(dI, dI_Fe)
            E = np.append(E, WE_Fe)
            dWE_Fe = np.array(([sigma_WE_Fe[0][compartment]], [sigma_WE_Fe[1][compartment]] ))


        index = np.where(I>5)
        E=E[index]; I=I[index]; dI=dI[index]

        popt, pcov = curve_fit(I_model, E, I, p0=128, sigma=dI, absolute_sigma=True)
        sigma_I_est = float( np.sqrt(np.diagonal(pcov)) ) #Uncertainty in the fitting parameters
        I_est = popt[0]

        chi_sq = self.chi_sqaured(I, I_est, dI)

        if MakePlot == True:
            plt.errorbar(WE_Ni, I_Ni_61Cu, color='magenta', marker='.', linewidth=0.001, xerr=dWE_Ni, yerr=dI_Ni_61Cu, elinewidth=0.5, capthick=0.5, capsize=3.0,label=r'$^{nat}$Ni(d,x)$^{61}$Cu' )
            plt.errorbar(WE_Ni, I_Ni_56Co, color='blue', marker='.', linewidth=0.001, xerr=dWE_Ni, yerr=dI_Ni_56Co, elinewidth=0.5, capthick=0.5, capsize=3.0, label=r'$^{nat}$Ni(d,x)$^{56}$Co (CUM)' )
            plt.errorbar(WE_Ni, I_Ni_58Co, color='black', marker='.', linewidth=0.001, xerr=dWE_Ni, yerr=dI_Ni_58Co, elinewidth=0.5, capthick=0.5, capsize=3.0, label=r'$^{nat}$Ni(d,x)$^{58}$Co (CUM)' )
            
            plt.errorbar(WE_Cu, I_Cu_62Zn, color='mediumpurple', marker='.', linewidth=0.001, xerr=dWE_Cu, yerr=dI_Cu_62Zn, elinewidth=0.5, capthick=0.5, capsize=3.0, label=r'$^{nat}$Cu(d,x)$^{62}$Zn' )
            plt.errorbar(WE_Cu, I_Cu_63Zn, color='teal', marker='.', linewidth=0.001, xerr=dWE_Cu, yerr=dI_Cu_63Zn, elinewidth=0.5, capthick=0.5, capsize=3.0, label=r'$^{nat}$Cu(d,x)$^{63}$Zn' )
            plt.errorbar(WE_Cu, I_Cu_65Zn, color='crimson', marker='.', linewidth=0.001, xerr=dWE_Cu, yerr=dI_Cu_65Zn, elinewidth=0.5, capthick=0.5, capsize=3.0, label=r'$^{nat}$Cu(d,x)$^{65}$Zn' )
            
            #plt.plot(WE_Ni, I_Ni_61Cu, marker='o', label=r'$Ni(d,x)^{61}Cu$')
            #plt.errorbar(WE_Ni, I_Ni_61Cu, color='green', linewidth=0.001,xerr=dWE_Ni, yerr=dI_Ni_61Cu, elinewidth=0.5, ecolor='k', capthick=2 )
            #plt.plot(WE_Ni, I_Ni_56Co, marker='o', label=r'$Ni(d,x)^{56}Co$ (CUM)')
            #plt.errorbar(WE_Ni, I_Ni_56Co, color='green', linewidth=0.001,xerr=dWE_Ni, yerr=dI_Ni_56Co, elinewidth=0.5, ecolor='k', capthick=0.5 )
            #plt.plot(WE_Ni, I_Ni_58Co, marker='o', label=r'$Ni(d,x)^{58}Co (CUM)$')
            #plt.errorbar(WE_Ni, I_Ni_58Co, color='green', linewidth=0.001,xerr=dWE_Ni, yerr=dI_Ni_58Co, elinewidth=0.5, ecolor='k', capthick=0.5 )

            #i = np.where(I_Cu_62Zn>0)
            #j = np.where(I_Cu_63Zn>0)
            #plt.plot(WE_Cu, I_Cu_62Zn, marker='o', label=r'$Cu(d,x)^{62}Zn$')
            #plt.errorbar(WE_Cu, I_Cu_62Zn, color='green', linewidth=0.001,xerr=dWE_Cu, yerr=dI_Cu_62Zn, elinewidth=0.5, ecolor='k', capthick=0.5 )
            #plt.plot(WE_Cu, I_Cu_63Zn, marker='o', label=r'$Cu(d,x)^{63}Zn$')
            #plt.errorbar(WE_Cu, I_Cu_63Zn, color='green', linewidth=0.001,xerr=dWE_Cu, yerr=dI_Cu_63Zn, elinewidth=0.5, ecolor='k', capthick=0.5 )
            #plt.plot(WE_Cu, I_Cu_65Zn, marker='o', label=r'$Cu(d,x)^{65}Zn$')
            #plt.errorbar(WE_Cu, I_Cu_65Zn, color='green', linewidth=0.001,xerr=dWE_Cu, yerr=dI_Cu_65Zn, elinewidth=0.5, ecolor='k', capthick=0.5 )
            if compartment < len(I_Fe_56Co):
                plt.errorbar(WE_Fe, I_Fe, color='darkorange', marker='.',  linewidth=0.001, xerr=dWE_Fe, yerr=dI_Fe, elinewidth=0.5, capthick=0.5, capsize=3.0,  label=r'$^{nat}$Fe(d,x)$^{56}$Co' )
                #plt.plot(WE_Fe, I_Fe,marker='o', label=r'$Fe(d,x)^{56}Co$')
                #plt.errorbar(WE_Fe, I_Fe, color='green', marker='.', linewidth=0.001,xerr=dWE_Fe, yerr=dI_Fe, elinewidth=0.5, ecolor='k', capthick=0.5 )

            xplot = np.linspace(min(E)-1.2, max(E)+1.2,len(E))
            plt.plot(xplot, I_model(E, *popt), label=r'Linear fit I={:.2f} $\pm$ {:.2f} nA'.format(I_est, sigma_I_est), linestyle='--', color='red')
            plt.plot(xplot,I_model(E,*(popt+sigma_I_est)), color='blue', linewidth=0.4, linestyle='-.')
            plt.plot(xplot,I_model(E,*(popt-sigma_I_est)), color='blue', linewidth=0.4,linestyle='-.', label=r'Uncertainty in fit, 1$\sigma$')
            plt.fill_between(xplot, I_model(E,*(popt+sigma_I_est)),I_model(E,*(popt-sigma_I_est)), color='blue', alpha=0.1)
            plt.xlabel('Energy, MeV')
            plt.ylabel('Beam Current, nA')

            plt.title(r'Linear fit for foils compartment {} - {}. $\chi^2$={:.2f} '.format(compartment+1, name, chi_sq))
            plt.legend(fontsize='x-small')
            plt.savefig('BeamCurrent/chi_minimization/minimization_{}_'.format(compartment+1)+name+'.png', dpi=300)
            #plt.close()
            plt.show()
        return WE_Ni, chi_sq, I_est, sigma_I_est

    def chi_sqaured(self, data, model, error): #error = stdv
        dof = 5
        #return np.sum( (data - model/error )**2 )#( / (len(data-dof))
        n = len(data)
        #stdv = np.sqrt(1./n *  (np.sum(data-model)**2))
        #return np.sum((data-model)**2 / stdv**2)
        #print(len(error))
        chi_sq = np.sum((data - model)**2/error**2) / (len(error) - 1)

        ### Number of datapoints - number of parameters in model.

        #print(stdv)
        #print(stdv)
        #pass
        return chi_sq

    def run_variance_minimization(self, name, compartment):
        chi_squared = []
        Ni_energies = []
        #if type(names) == str:
        WE_Ni, chi_sq = self.variance_minimization(compartment, name)
        print(name, chi_sq)

    def linear_fit(self, makePlot=False):
        from sklearn import linear_model
        I = self.specified_currents()
        I = np.concatenate(I)
        WE = self.specified_energies()
        E = np.array((WE[0], WE[1], WE[1], WE[1], WE[-1], WE[-1], WE[-1]))
        E = np.concatenate(E)

        index = np.where (I > 0)
        I = I[index].reshape(-1,1)
        E = E[index].reshape(-1,1)

        linreg = linear_model.LinearRegression().fit(I,E)
        I_pred = linreg.predict(E)

        beta = linreg.coef_
        intercept = linreg.intercept_

        chi = self.least_squares(I, I_pred)


        if makePlot:
            plt.plot(E, I_pred, label='test')
            plt.show()

    def CurrentPlot(self, name,SaveFig=False):
        I_Fe_56Co, I_Ni_61Cu, I_Ni_56Co, I_Ni_58Co, I_Cu_62Zn, I_Cu_63Zn, I_Cu_65Zn = self.specified_currents()
        dI_Fe_56Co, dI_Ni_61Cu, dI_Ni_56Co, dI_Ni_58Co, dI_Cu_62Zn, dI_Cu_63Zn, dI_Cu_65Zn = self.specified_currents(uncertainty=True)
        WE_Fe, WE_Ni, WE_Cu, WE_Ir = self.specified_energies()
        sigma_WE_Fe, sigma_WE_Ni, sigma_WE_Cu, sigma_WE_Ir = self.specified_energies(uncertainty=True)

        #colors = ['mediumpurple', 'cyan', 'palevioletred', 'darkorange', 'forestgreen', 'orchid', 'dodgerblue', 'lime', 'crimson', 'indianred']

        plt.axhline(128.5, linestyle='-.', linewidth=0.4, label='Monitor current 128.5 nA')


        #plt.plot(WE_Ni,I_Ni_61Cu, '.', label=r'$^{nat}$Ni(d,x)$^{61}$Cu')
        plt.errorbar(WE_Ni, I_Ni_61Cu, color='magenta', marker='.', linewidth=0.001, xerr=sigma_WE_Ni, yerr=dI_Ni_61Cu, elinewidth=0.5, capthick=0.5, capsize=3.0,label=r'$^{nat}$Ni(d,x)$^{61}$Cu' )

        #plt.plot(WE_Ni,I_Ni_56Co, '.', label=r'$^{nat}$Ni(d,x)$^{56}$Co (CUM)')
        plt.errorbar(WE_Ni, I_Ni_56Co, color='blue', marker='.', linewidth=0.001, xerr=sigma_WE_Ni, yerr=dI_Ni_56Co, elinewidth=0.5, capthick=0.5, capsize=3.0, label=r'$^{nat}$Ni(d,x)$^{56}$Co (CUM)' )

        #plt.plot(WE_Ni,I_Ni_58Co, '.', label=r'$^{nat}$Ni(d,x)$^{58}$Co (CUM)')
        plt.errorbar(WE_Ni, I_Ni_58Co, color='black', marker='.', linewidth=0.001, xerr=sigma_WE_Ni, yerr=dI_Ni_58Co, elinewidth=0.5, capthick=0.5, capsize=3.0, label=r'$^{nat}$Ni(d,x)$^{58}$Co (CUM)' )

        #index = zero_to_nan(I_Cu_62Zn)[-1]
        #plt.plot(WE_Cu[index],I_Cu_62Zn[index], '.', label=r'$^{nat}$Cu(d,x)$^{62}$Zn')
        #plt.errorbar(WE_Cu[index], I_Cu_62Zn[index], color='green', linewidth=0.001, xerr=sigma_WE_Cu[index], yerr=dI_Cu_62Zn[index], elinewidth=0.5, ecolor='k', capthick=0.5 )
        #plt.plot(WE_Cu,I_Cu_62Zn, '.', )
        plt.errorbar(WE_Cu, I_Cu_62Zn, color='mediumpurple', marker='.', linewidth=0.001, xerr=sigma_WE_Cu, yerr=dI_Cu_62Zn, elinewidth=0.5, capthick=0.5, capsize=3.0, label=r'$^{nat}$Cu(d,x)$^{62}$Zn' )

        #index = zero_to_nan(I_Cu_63Zn)[-1]
        #plt.plot(WE_Cu[index],I_Cu_63Zn[index], '.', label=r'$^{nat}$Cu(d,x)$^{63}$Zn')
        #plt.errorbar(WE_Cu[index], I_Cu_63Zn[index], color='green', linewidth=0.001, xerr=sigma_WE_Cu[index], yerr=dI_Cu_63Zn[index], elinewidth=0.5, ecolor='k', capthick=0.5 )
        #plt.plot(WE_Cu,I_Cu_63Zn, '.', label=r'$^{nat}$Cu(d,x)$^{63}$Zn')
        plt.errorbar(WE_Cu, I_Cu_63Zn, color='teal', marker='.', linewidth=0.001, xerr=sigma_WE_Cu, yerr=dI_Cu_63Zn, elinewidth=0.5, capthick=0.5, capsize=3.0, label=r'$^{nat}$Cu(d,x)$^{63}$Zn' )

        #plt.plot(WE_Cu,I_Cu_65Zn, '.', label=r'$^{nat}$Cu(d,x)$^{65}$Zn')
        plt.errorbar(WE_Cu, I_Cu_65Zn, color='crimson', marker='.', linewidth=0.001, xerr=sigma_WE_Cu, yerr=dI_Cu_65Zn, elinewidth=0.5, capthick=0.5, capsize=3.0, label=r'$^{nat}$Cu(d,x)$^{65}$Zn' )
        #namez = names[file]
        #plt.plot(WE_Fe,I_Fe_56Co, '.', label=r'$^{nat}$Fe(d,x)$^{56}$Co')
        plt.errorbar(WE_Fe, I_Fe_56Co, color='darkorange', marker='.',  linewidth=0.001, xerr=sigma_WE_Fe, yerr=dI_Fe_56Co, elinewidth=0.5, capthick=0.5, capsize=3.0,  label=r'$^{nat}$Fe(d,x)$^{56}$Co' )

        plt.title('Beam current monitor foils - {}'.format(name))
        plt.xlabel('Energy, MeV')
        plt.ylabel('Measured deuteron beam current, nA')
        plt.ylim(-5,350)
        plt.xlim(0,35)
        #ylim(top=350)
        #ylim(bottom=0)

        #WABC = 'averaged_currents.csv' ## weighted average beam current filename
        #weighted_average_beam = np.genfromtxt(WABC, delimiter=',', usecols=[1])
        #weighted_average_beam = weighted_average_beam[::-1]
        #sigma_weighted_average_beam = np.genfromtxt(WABC, delimiter=',', usecols=[2])
        #sigma_weighted_average_beam = sigma_weighted_average_beam[::-1]
        #plt.errorbar(WE_Ir, weighted_average_beam, color='black', marker='P', linewidth=0.001, xerr=sigma_WE_Ir, yerr=sigma_weighted_average_beam, elinewidth=0.5, capthick=0.5, capsize=3.0,label='weighted average beam current' )
        if SaveFig:
            plt.legend(fontsize='x-small')
            path = os.getcwd()
            plt.savefig(path + '/BeamCurrent/current_all/' + name  + '.png',dpi=300)
            #plt.savefig(path+'/BeamCurrent/' + name +'.png', dpi=300)
            plt.show()

    def CurrentPlot_compartment(self, name, WABC = 'averaged_currents.csv'):
        compartment = [3,7,9]
        WE_Ir, sigma_WE_Ir = self.WABE('Ir')
        #WABC = 'averaged_currents.csv' ## weighted average beam current filename
        #weighted_average_beam = np.genfromtxt(WABC, delimiter=',', usecols=[1])
        #weighted_average_beam = weighted_average_beam[::-1]
        #sigma_weighted_average_beam = np.genfromtxt(WABC, delimiter=',', usecols=[2])
        #sigma_weighted_average_beam = sigma_weighted_average_beam[::-1]

        colors = ['darkorange', 'forestgreen', 'palevioletred']#, 'darkorange', 'forestgreen', 'orchid', 'dodgerblue', 'lime', 'crimson', 'indianred']
        for i in range(len(compartment)):
            WE_Ni, chi_sq, I_est, sigma_I_est = self.variance_minimization(compartment[i], name)
            labelling = r'compartment {} - $\chi^2=${:.2f}'.format(compartment[i], chi_sq)
            plt.axhline(I_est, color=colors[i], linestyle='--', linewidth=0.7, label=labelling)# label='compartment {}'.format(compartment[i]))
            #plt.errorbar(WE_Ni, weighted_average_beam, color='black', marker='o', linewidth=0.001, xerr=sigma_weighted_average_beam, yerr=dI_Ni_61Cu, elinewidth=0.5, capthick=0.5, capsize=3.0,label=r'$^{nat}$Ni(d,x)$^{61}$Cu' )
        #plt.legend()
        #plt.show()
        self.CurrentPlot(name)
        #self.variance_minimization(compartment, name, MakePlot=True)
        #plt.legend()
        #WABC = 'averaged_currents.csv' ## weighted average beam current filename
        weighted_average_beam = np.genfromtxt(WABC, delimiter=',', usecols=[1])
        #weighted_average_beam = weighted_average_beam[::-1]
        sigma_weighted_average_beam = np.genfromtxt(WABC, delimiter=',', usecols=[2])
        #sigma_weighted_average_beam = sigma_weighted_average_beam[::-1]
        plt.errorbar(WE_Ir, weighted_average_beam, color='black', marker='P', linewidth=0.001, xerr=sigma_WE_Ir, yerr=sigma_weighted_average_beam, elinewidth=0.5, capthick=0.5, capsize=3.0,label='weighted average beam current' )
        plt.legend(fontsize='x-small')
        plt.savefig('BeamCurrent/compartment_compare/comp_compared_{}.png'.format(name), dpi=300)
        plt.show()
        #plt.close()
        #plt.title('')

    def current_for_CS(self, return_energies=False, mon_test=False):
        ### Making one current per compartment, ie one array length 10.

        I_Fe_56Co, I_Ni_61Cu, I_Ni_56Co, I_Ni_58Co, I_Cu_62Zn, I_Cu_63Zn, I_Cu_65Zn = self.specified_currents()
        dI_Fe_56Co, dI_Ni_61Cu, dI_Ni_56Co, dI_Ni_58Co, dI_Cu_62Zn, dI_Cu_63Zn, dI_Cu_65Zn = self.specified_currents(uncertainty=True)

        #FROM MY SCRIPT
        WE_Fe, WE_Ni, WE_Cu, WE_Ir = self.specified_energies()



        #print(WE_Fe, WE_Ni, WE_Cu)
        sigma_WE_Fe, sigma_WE_Ni, sigma_WE_Cu, sigma_WE_Ir = self.specified_energies(uncertainty=True)

        WE_Ni_chi, chi_sq, I_est, sigma_I_est = self.variance_minimization(2, 'varmin_comp3')
        #print(WE_Ni, "*** beam current program")
        #print(sigma_I_est, '***')


        n = 10
        #l = 3

        #print("56Co", I_Fe_56Co)
        #print("61Cu", I_Ni_61Cu)
        #print("56Co", I_Ni_56Co)
        #print("58Co", I_Ni_58Co)
        #print("62Zn", I_Cu_62Zn)
        #print("*",dI_Cu_62Zn, "*")
        #print("63Zn",I_Cu_63Zn)
        #print("*",dI_Cu_63Zn, "*")
        #print("65Zn",I_Cu_65Zn)
        #print("*",dI_Cu_65Zn, "*")

        def mean_val(list_of_vals, list_of_dvals):
            ### Average weighted Beam current
            weight = []
            for i in list_of_dvals:
                weight.append(1/i**2)

            av = np.average(list_of_vals, axis=None, weights=weight)
            #av = np.average(list_of_vals, axis=None)
            return av

        I   = []    #general one to use
        I_Ni = []; dI_Ni=[]   #These are just for testing the monitor currents on CS
        I_Fe = []; dI_Fe=[]
        I_Cu = []; dI_Cu=[]



        #print("Above:", I_Cu_62Zn)

        ### Making I_Fe_56Co a 10-lenght array filling empty spaces with zeros
        I_Fe_56Co = np.pad(I_Fe_56Co, (0, n-len(I_Fe_56Co)),'constant')
        dI_Fe_56Co = np.pad(dI_Fe_56Co, (0, n-len(dI_Fe_56Co)),'constant')
        #I_list = [I_Fe_56Co, I_Ni_61Cu, I_Ni_56Co, I_Ni_58Co, I_Cu_62Zn, I_Cu_63Zn, I_Cu_65Zn]
        #dI_list = [dI_Fe_56Co, dI_Ni_61Cu, dI_Ni_56Co, dI_Ni_58Co, dI_Cu_62Zn, dI_Cu_63Zn, dI_Cu_65Zn]
        I_list = [I_Fe_56Co, I_Ni_61Cu,I_Ni_58Co, I_Cu_62Zn, I_Cu_63Zn, I_Cu_65Zn]
        dI_list = [dI_Fe_56Co, dI_Ni_61Cu, dI_Ni_58Co, dI_Cu_62Zn, dI_Cu_63Zn, dI_Cu_65Zn]
        #print("62Zn", I_list[-3])
        #print("63Zn",I_list[-2])
        #print("65Zn",I_list[-1])
        #print("dI: 56Co Fe", dI_list[0])

        for val in dI_list:
            # For values where I ==0 and dI =NaN. Change to zero.  (62,63Zn)
            for i,e in enumerate(val):
                import math
                if math.isnan(e)==True:
                    e = np.nan_to_num(e)
                    val[i] = e

        for i in range(n):
            I_list_new = []
            dI_list_new = []

            I_Fe_new = []; dI_Fe_new = []
            I_Ni_new = []; dI_Ni_new = []
            I_Cu_new = []; dI_Cu_new = []

            for index, currents in enumerate(I_list):
                #print(index)
                if currents[i]>10:
                    #print("*", index)
                    #print(currents[i])
                    ## Not taking average of values that are zero.
                    I_list_new.append(currents[i])
                    #print(I_list[index])
                    #print(dI_list[index])
                    sigma_currents = dI_list[index]
                    #print("*", sigma_currents)
                    #print("*", type(sigma_currents), len(sigma_currents))
                    dI_list_new.append(sigma_currents[i])

                    if index == 0:
                        I_Fe.append(currents[i])
                        dI_Fe.append(sigma_currents[i])
                        #element_dI.append(dI_list[index])
                        #dI_Fe.append(sigma_Fe)
                    if index==1 or index==2 or index==3:
                        I_Ni_new.append(currents[i])
                        dI_Ni_new.append(sigma_currents[i])
                    if index==4 or index==5 or index==6:
                        I_Cu_new.append(currents[i])
                        dI_Cu_new.append(sigma_currents[i])





            """
            for index, currents in enumerate(I_list):
                if currents[i]>0:
                    #print(currents[i])
                    ## Not taking average of values that are zero.
                    I_list_new.append(currents[i])
                    sigma_currents = dI_list[index]
                    print("*", type(sigma_currents), len(sigma_currents))
                    dI_list_new.append(sigma_currents[i])

                    if index == 0:
                        I_Fe.append(currents[i])
                        sigma_Fe = dI_list[index]
                        dI_Fe.append(sigma_Fe)
                    if index==1 or index==2 or index==3:
                        I_Ni.append(currents[i])
                    if index==4 or index==5 or index==6:
                        I_Cu.append(currents[i])

            """

            #I_mean = mean_val(list_of_vals, list_of_dvals)

            #I_Fe= mean_val(I_Fe_new, dI_Fe_new)
            I.append(mean_val(I_list_new, dI_list_new ))
            I_Ni.append(mean_val(I_Ni_new, dI_Ni_new))
            try:
                I_Cu.append(mean_val(I_Cu_new, dI_Cu_new))
            except:
                print("Cu does not have any current in compartment {}, setting it to zero. ".format(index))
                I_Cu.append(0)
        #print(I_Cu)
        #print(I_Cu, "**")

        #print("I:", I)
        #print("I_Ni", I_Ni)
        if mon_test:
            return I_Fe, I_Ni, I_Cu, sigma_I_est
        if return_energies==True:
            return WE_Fe, WE_Ni, WE_Cu, WE_Ir, sigma_WE_Fe, sigma_WE_Ni, sigma_WE_Cu, sigma_WE_Ir
        else:
            return I, sigma_I_est     #, dI_list_new  #Correct?????


    ###
    def reshaping_parameters(self):
        params_Ni_61Cu = self.calling_parameters_to_weightedaverage_func('Ni', 'Ni_61Cu')
        params_Ni_56Co = self.calling_parameters_to_weightedaverage_func('Ni', 'Ni_56Co')
        params_Ni_58Co = self.calling_parameters_to_weightedaverage_func('Ni', 'Ni_58Co')
        params_Cu_62Zn = self.calling_parameters_to_weightedaverage_func('Cu', 'Cu_62Zn')
        params_Cu_63Zn = self.calling_parameters_to_weightedaverage_func('Cu', 'Cu_63Zn')
        params_Cu_65Zn = self.calling_parameters_to_weightedaverage_func('Cu', 'Cu_65Zn')
        params_Fe_56Co = self.calling_parameters_to_weightedaverage_func('Fe', 'Fe_56Co')
        #print(params_Fe_56Co[0])
        #print(params_Ni_61Cu[0])
        #print(params_Fe_56Co[-1][2])
        #print(len(params_Ni_61Cu[0]))

        matrix_A0 = np.zeros((10,7))
        matrix_sigma_A0 = np.zeros((10,7))
        matrix_lambda_ = np.zeros((10,7))
        matrix_mass_density = np.zeros((10,7))
        matrix_sigma_mass_density = np.zeros((10,7))
        matrix_reaction_integral = np.zeros((10,7))
        matrix_uncertainty_integral = np.zeros((10,7))
        matrix_irr_time = np.zeros((10,1))
        matrix_sigma_irr_time = np.zeros((10,1))

        list_of_params = [params_Ni_61Cu, params_Ni_56Co, params_Ni_58Co, params_Cu_62Zn, params_Cu_63Zn, params_Cu_65Zn, params_Fe_56Co]
        list_of_params = np.array((list_of_params))
        #print(list_of_params[0,2])
        #print(list_of_params.shape)
        #print(type(list_of_params))

        n = len(list_of_params)
        A0 = np.zeros(n)
        sigma_A0 = np.zeros(n)
        lambda_ = np.zeros(n)
        mass_density = np.zeros(n)
        sigma_mass_density =  np.zeros(n)
        reaction_integral = np.zeros(n)
        uncertainty_integral = np.zeros(n)
        matrix_irr_time = np.transpose(np.ones(10)*3600)
        #print(irr_time)
        matrix_sigma_irr_time = np.transpose(np.ones(10)*3)

        shape_cols = (10,)
        for i in range(len(list_of_params)):
            A0 = list_of_params[i,0]
            sigma_A0 = list_of_params[i,1]
            lambda_ = list_of_params[i,2]
            mass_density = list_of_params[i,3]
            sigma_mass_density = list_of_params[i,4]
            reaction_integral = list_of_params[i,5]
            uncertainty_integral = list_of_params[i,6]
            #irr_time = list_of_params[i,7]
            #sigma_irr_time = list_of_params[i,8]

            try:

                matrix_lambda_[:, i] = lambda_
                #matrix_irr_time[i] = irr_time
                #matrix_sigma_irr_time[i] = sigma_irr_time
                matrix_A0[:,i] = A0
                matrix_sigma_A0[:,i] = sigma_A0
                matrix_mass_density[:,i] = mass_density

                matrix_sigma_mass_density[:,i] = sigma_mass_density
                matrix_reaction_integral[:,i]  = reaction_integral
                matrix_uncertainty_integral[:,i]  = uncertainty_integral
            except:
                #print("Shape problem with Fe_56Co ")
                A0 = np.pad(A0, (0, 7), 'constant')
                sigma_A0 = np.pad(sigma_A0, (0, 7), 'constant')
                mass_density = np.pad(mass_density, (0, 7), 'constant')
                sigma_mass_density = np.pad(sigma_mass_density, (0, 7), 'constant')
                reaction_integral = np.pad(reaction_integral, (0, 7), 'constant')
                uncertainty_integral = np.pad(uncertainty_integral, (0, 7), 'constant')
                matrix_A0[:,i] = A0
                matrix_sigma_A0[:,i] = sigma_A0
                matrix_mass_density[:,i] = mass_density
                matrix_sigma_mass_density[:,i] = sigma_mass_density
                matrix_reaction_integral[:,i]  = reaction_integral
                matrix_uncertainty_integral[:,i]  = uncertainty_integral

            
        ### NEED TO REMOVE inf from sigma_A0 (which was caused by changing A0 for 56Ni to 0 in foil 4-10.
        ### Gave inf problems in zero division.  )
        rows = matrix_A0.shape[0]
        cols = matrix_A0.shape[1]
        for i in range(rows):
            for j in range(cols):
                if np.isinf(matrix_sigma_A0[i,j]):
                 matrix_sigma_A0[i,j]=0
        #print(matrix_sigma_A0)
                #print(matrix_sigma_A0[i,j])

        #print(matrix_sigma_A0)
        #print(matrix_lambda_.shape)
        #print(matrix_irr_time)
        #print(matrix_sigma_irr_time)
        #print(matrix_A0)
        #print(matrix_sigma_A0)
        #print(matrix_mass_density)
        #print(sigma_matrix_mass_density)
        #print(matrix_reaction_integral)
        #print(matrix_uncertainty_integral)


        return matrix_A0, matrix_sigma_A0, matrix_lambda_, matrix_mass_density, matrix_sigma_mass_density, matrix_reaction_integral, matrix_uncertainty_integral, matrix_irr_time, matrix_sigma_irr_time

        """
        ### PARAMETERS
        ### A0, sigma_A0, lambda_, mass_density, sigma_mass_density, reaction_integral, uncertainty_integral, irr_time, sigma_irr_time
        #matrix_A0[] = params_Ni_61Cu[0]
        n  = len(list_of_params)
        col_A0 = np.zeros(n); col_dA0
        shape_cols = (10,)
        for i in range(n):
            col_A0 = list_of_params[i,0]
            col_dA0 = list_of_params[i,1]



            #if len(col_A0)<10:
            #    col_A0 = np.pad(col_A0, (0, 7), 'constant')
            #matrix_A0[:, i]=col_A0.T

        """
        #print(matrix_A0)
        #print(matrix_lambda_)


    def calling_parameters_to_weightedaverage_func(self, foil, react):
        irr_time = 3600; sigma_irr_time = 3 #seconds
        if foil == 'Fe':
            F = self.F_Fe
            E = self.E_Fe
            IAEA_Cs, A0, sigma_A0, lambda_, mass_density, sigma_mass_density = self.Fe_foil(react)  #from beam_current_FoilReact
            E_mon, Cs, sigma_Cs, tck, sigma_tck = self.data(IAEA_Cs) #from monitor foils
            uncertainty_integral, reaction_integral =  self.E_flux_integral(Cs, sigma_Cs, tck, sigma_tck, E, F, return_interp_CS=False)
        elif foil == 'Ni':
            F = self.F_Ni
            E = self.E_Ni
            if react =='Ni_56Co' or react=='Ni_58Co':
                IAEA_Cs, A0_dir, sigma_A0_dir, A0_nondir, sigma_A0_nondir, lambda_dir, lambda_nondir, mass_density, sigma_mass_density = self.Ni_foil(react)
                A0 = (A0_dir + A0_nondir*(lambda_dir/lambda_nondir))  # From the function calculate_beam_current, see book for further description, but we managed to find a different way to express A0 withot any changes. We hope
                
                ### For 56Co: Sigma A0 is inf high due to values set to 1. Doesnt really apply for 58Co. 
                sigma_A0 = np.zeros(len(A0_dir))
                for i in range(len(sigma_A0_nondir)):
                    if sigma_A0_nondir[i]==1:
                        sigma_A0[i] = np.sqrt( (sigma_A0_dir[i]/A0_dir[i])**2+ (lambda_dir*0.001/lambda_dir)**2 + (lambda_nondir*0.001/lambda_nondir)**2 )
                        #print(i)
                        #print(sigma_A0[i])
                    else:
                        sigma_A0[i] = np.sqrt( (sigma_A0_dir[i]/A0_dir[i])**2+ (sigma_A0_nondir[i]/A0_nondir[i])**2 + (lambda_dir*0.001/lambda_dir)**2 + (lambda_nondir*0.001/lambda_nondir)**2 )
                        #print(i)
                        #print(sigma_A0[i])

                #sigma_A0 = np.sqrt( (sigma_A0_dir/A0_dir)**2+ (sigma_A0_nondir/A0_nondir)**2 + (lambda_dir*0.001/lambda_dir)**2 + (lambda_nondir*0.001/lambda_nondir)**2 )
                lambda_=lambda_dir
               #print("Final dA0: ",sigma_A0)


                #print(A0)
                #print("dA0 dir: ", sigma_A0_dir)
                #print("dA0 nondir: ", sigma_A0_nondir)
                #print(sigma_A0)
            else:
                IAEA_Cs, A0, sigma_A0, lambda_, mass_density, sigma_mass_density = self.Ni_foil(react)  #from beam_current_FoilReact
            E_mon, Cs, sigma_Cs, tck, sigma_tck = self.data(IAEA_Cs) #from monitor foils
            uncertainty_integral, reaction_integral =  self.E_flux_integral(Cs, sigma_Cs, tck, sigma_tck, E, F, return_interp_CS=False)
        elif foil == 'Cu':
            F = self.F_Cu
            E = self.E_Cu
            IAEA_Cs, A0, sigma_A0, lambda_, mass_density, sigma_mass_density = self.Cu_foil(react)  #from beam_current_FoilReact
            E_mon, Cs, sigma_Cs, tck, sigma_tck = self.data(IAEA_Cs) #from monitor foils
            uncertainty_integral, reaction_integral =  self.E_flux_integral(Cs, sigma_Cs, tck, sigma_tck, E, F, return_interp_CS=False)


        #print("A0: ", A0)
        #print("dA0: ", sigma_A0)
        #print("lamb: ", lambda_ )
        #print("mass density: ", mass_density)
        #print("sigma mass density: ", sigma_mass_density)
        #print("reaction int: ", reaction_integral)
        #print("uncert integral: ", uncertainty_integral) 
        #print(irr_time, sigma_irr_time)
        return A0, sigma_A0, lambda_, mass_density, sigma_mass_density, reaction_integral, uncertainty_integral, irr_time, sigma_irr_time

        #E_Fe, E_Ni, E_Cu, E_Ir = self.WABE(foil)
