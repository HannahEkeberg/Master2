import numpy as np, matplotlib.pyplot as plt
from scipy import interpolate
from scipy.constants import N_A, elementary_charge
import sys
from scipy.stats import norm
from scipy.optimize import curve_fit, minimize_scalar



from beam_current_FoilReact import *    #Program where info regarding foil reaction.
from ziegler_sorting import *  #sorting of ziegler list etc

from ZieglerFiles import ziegler_files

#files,names = ziegler_files()
#print(files)



"""
Ziegler energies and fluxes are used to first find energy and fluxes in different reactions
Function get_FWHM() returns FWHM for specific type of foils in a list for each foil.
Function beam_current() takes in foil and reaction, and returns the dI and I beamcurrent.
Uses functions data and E_flux_integral to get spline and integrals, from equation used
Function WABE (weighted average beam energy) returns the average energy for each foil, and dE
Finally plotting E,I with errorbars.

"""

from scipy.signal import chirp, find_peaks, peak_widths

"""
class Dense:
    def __init__(self, compartment, files, names):
        self.compartment = compartment-1
        self.files = files
        self.names = names

    def var_min(self):
        if type(self.files) == str:
            beam_curr = BeamCurrent(self.files, sort_ziegler, Fe_foil, Ni_foil, Cu_foil)
            E_Ni, chi_sq = beam_curr.variance_minimization(self.compartment, self.names)
            print(E_Ni, chi_sq)
        else:
            chi_squared = []
            Ni_energies = []
            for i in range(len(self.files)):
                beam_curr = BeamCurrent(self.files[i], sort_ziegler, Fe_foil, Ni_foil, Cu_foil)
                E_Ni, chi_sq = beam_curr.variance_minimization(self.compartment, self.names[i])
                Ni_energies.append(E_Ni)
                chi_squared.append(chi_sq)
            #print(chi_sqaured)
            #self.plot_func(Ni_energies, chi_squared)
            self.lowest_val(chi_squared, self.names, Ni_energies)

    def plot_func(self, x, y):
        plt.plot(x,y, '.')
        plt.show()

    def lowest_val(self,chi,name, E):
        if type(chi) == list:
            #print(min(chi))
            index = chi.index(min(chi))
            print(name[index], chi[index], E[index])
        else:
            pass


"""
root_dir = 'BeamCurrent'
current_dir = 'BeamCurrent/current_all'
chi_dir = 'BeamCurrent/chi_minimization'
flux_dir = 'BeamCurrent/beam_fluxes'
if not os.path.exists(root_dir):
    os.mkdir(root_dir)
if not os.path.exists(current_dir):
    os.mkdir(current_dir)
if not os.path.exists(chi_dir):
    os.mkdir(chi_dir)
if not os.path.exists(flux_dir):
    os.mkdir(flux_dir)


class BeamCurrent:
    def __init__(self, ziegler_file):
        self.file = ziegler_file
        self.sort = sort_ziegler    # from ziegler_sorting.py
        self.Fe_foil = Fe_foil      # from beam_current_FoilReact
        self.Ni_foil = Ni_foil      # from beam_current_FoilReact
        self.Cu_foil = Cu_foil      # from beam_current_FoilReact
        self.E_Ni, self.F_Ni, self.E_Cu, self.F_Cu, self.E_Fe, self.F_Fe, self.E_Ir, self.F_Ir = self.sort(self.file)
        self.path = os.getcwd()

    def get_sigmaE(self, E, F, foil, makePlot=False):

        ### for cupper, flux is going up in end, delete those points!

        dEr = np.zeros(len(E))    # right uncertainty
        dEl = np.zeros(len(E))    # left uncertainty
        fwhm = np.zeros(len(E))
        half_max = []
        mu_array = np.zeros(len(E))
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
            (mu,sigma) = norm.fit(E[i])
            fwhm[i] = hmx[1]-hmx[0]
            dEl[i] = mu-hmx[0]; dEr[i] = hmx[1]-mu   #left and right uncertainty in energy
            mu_array[i] = mu
        if makePlot:
            self.Plot_energy_distribution(E,F,mu_array, fwhm, half_max, foil)  #make plot of energy distribution
        else:
            return dEl, dEr   #return left and right uncertainty

    def plot_distribution(self, foil, name):
        if foil == 'Ni':
            #print('way')
            self.get_sigmaE(self.E_Ni, self.F_Ni, foil, makePlot=True)

        elif foil == 'Cu':
            #print('way')
            self.get_sigmaE(self.E_Cu, self.F_Cu, foil, makePlot=True)

        elif foil == 'Fe':
            self.get_sigmaE(self.E_Fe, self.F_Fe, foil, makePlot=True)

        elif foil == 'Ir':
            self.get_sigmaE(self.E_Ir, self.F_Ir, foil, makePlot=True)
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
        plt.legend()
        #plt.savefig(path_to_folder + foil + '_flux_distribution'+name+'.png', dpi=300)
        #plt.show()


    def data(self, filename):   #Function that interpolates over energies and cross sections provided by IAEA
        E_mon = np.loadtxt(filename, usecols=[0], skiprows=6)
        Cs = np.loadtxt(filename, usecols=[1], skiprows=6)
        sigma_Cs = np.loadtxt(filename, usecols=[2], skiprows=6)

        tck = interpolate.splrep(E_mon, Cs, s=0)
        sigma_tck = interpolate.splrep(E_mon, sigma_Cs, s=0)
        return E_mon, Cs, sigma_Cs, tck, sigma_tck

    def E_flux_integral(self, Cs, sigma_Cs, tck, sigma_tck, E, F):
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

        return uncertainty_integral, reaction_integral


    def calculate_beam_current(self, foil, react, print_terms=False):   # For non-cumulative cross sections from IAEA.
        irr_time = 3600; sigma_irr_time = 3 #seconds

        if foil == 'Fe':
            F = self.F_Fe
            E = self.E_Fe

            IAEA_Cs, A0, sigma_A0, lambda_, mass_density, sigma_mass_density = self.Fe_foil(react)  #from beam_current_FoilReact
            E_mon, Cs, sigma_Cs, tck, sigma_tck = self.data(IAEA_Cs) #from monitor foils


        elif foil == 'Ni':
            F = self.F_Ni
            E = self.E_Ni
            if react == 'Ni_61Cu':
                IAEA_Cs, A0, sigma_A0, lambda_, mass_density, sigma_mass_density = self.Ni_foil(react)  #from beam_current_FoilReact
            else:  # Cumulative activities
                IAEA_Cs, A0_dir, sigma_A0_dir, A0_nondir, sigma_A0_nondir, lambda_dir, lambda_nondir, mass_density, sigma_mass_density = self.Ni_foil(react)

            E_mon, Cs, sigma_Cs, tck, sigma_tck = self.data(IAEA_Cs) #from monitor foils

        elif foil == 'Cu':
            F = self.F_Cu
            E = self.E_Cu

            IAEA_Cs, A0, sigma_A0, lambda_, mass_density, sigma_mass_density = self.Cu_foil(react)  #from beam_current_FoilReact
            E_mon, Cs, sigma_Cs, tck, sigma_tck = self.data(IAEA_Cs) #from monitor foils


        uncertainty_integral, reaction_integral = self.E_flux_integral(Cs, sigma_Cs, tck, sigma_tck, E, F)
        uncertainty_integral = np.array((uncertainty_integral))

        if react=='Ni_58Co' or react=='Ni_56Co':
            BR = 1.0
            sigma_BR = 0.0 # no BR for these reactions.

            I = 1/(mass_density * reaction_integral)  * ( A0_dir*elementary_charge*1e9/(1-np.exp(-lambda_dir*irr_time)) + BR*A0_nondir*elementary_charge*1e9/ (1-np.exp(-lambda_nondir*irr_time)) )
            dI = I * np.sqrt((sigma_A0_dir/A0_dir)**2 + (sigma_A0_nondir/A0_nondir)**2  + (sigma_BR/BR)**2 + (sigma_mass_density/mass_density)**2 + (sigma_irr_time/irr_time)**2 + uncertainty_integral**2)

            if print_terms:
                print("mass density", mass_density)
                print("reaction integral", reaction_integral)
                print("underctainty integral", uncertainty_integral)
                print("activity direct", A0_dir)
                print("activity non-direct", A0_nondir)

        else:
            I = A0 *elementary_charge*1e9 / (mass_density*(1-np.exp(-lambda_*irr_time))*reaction_integral)
            dI = I * np.sqrt((sigma_A0/A0)**2 + (sigma_mass_density/mass_density)**2 + (sigma_irr_time/irr_time)**2 + uncertainty_integral**2)

        if print_terms:
            print("mass density", mass_density)
            print("reaction integral", reaction_integral)
            print("underctainty integral", uncertainty_integral)
            print("activity", A0)

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
        if uncertainty:
            return dI_Fe_56Co, dI_Ni_61Cu, dI_Ni_56Co, dI_Ni_58Co, dI_Cu_62Zn, dI_Cu_63Zn, dI_Cu_65Zn
        else:
            return I_Fe_56Co, I_Ni_61Cu, I_Ni_56Co, I_Ni_58Co, I_Cu_62Zn, I_Cu_63Zn, I_Cu_65Zn

    def specified_energies(self, uncertainty=False):
        E_Fe, dE_Fe = self.WABE('Fe')
        E_Ni, dE_Ni = self.WABE('Ni')
        E_Cu, dE_Cu = self.WABE('Cu')
        E_Ir, dE_Ir = self.WABE('Ir')

        if uncertainty:
            return dE_Fe, dE_Ni, dE_Cu, dE_Ir
        else:
            return E_Fe, E_Ni, E_Cu, E_Ir

    def variance_minimization(self, compartment, name, MakePlot=False):


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

        I_Ni = np.array((I_Ni_61Cu, I_Ni_56Co, I_Ni_58Co))
        dI_Ni = np.array((dI_Ni_61Cu, dI_Ni_56Co, dI_Ni_58Co))
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

        if compartment <= len(I_Fe_56Co):
            I_Fe = I_Fe_56Co[compartment]; dI_Fe = dI_Fe_56Co[compartment]
            WE_Fe = WE_Fe[compartment]

            I = np.append(I, I_Fe)
            dI = np.append(dI, dI_Fe)
            E = np.append(E, WE_Fe)
            dWE_Fe = np.array(([sigma_WE_Fe[0][compartment]], [sigma_WE_Fe[1][compartment]] ))


        index = np.where(I>0)
        E=E[index]; I=I[index]; dI=dI[index]

        popt, pcov = curve_fit(I_model, E, I, p0=128, sigma=dI, absolute_sigma=True)
        sigma_I_est = float( np.sqrt(np.diagonal(pcov)) ) #Uncertainty in the fitting parameters
        I_est = popt[0]

        chi_sq = self.chi_sqaured(I, I_est, dI)

        if MakePlot == True:

            plt.plot(WE_Ni, I_Ni_61Cu, marker='o', label=r'$Ni(d,x)^{61}Cu$')
            plt.errorbar(WE_Ni, I_Ni_61Cu, color='green', linewidth=0.001,xerr=dWE_Ni, yerr=dI_Ni_61Cu, elinewidth=0.5, ecolor='k', capthick=2 )
            plt.plot(WE_Ni, I_Ni_56Co, marker='o', label=r'$Ni(d,x)^{56}Co$ (CUM)')
            plt.errorbar(WE_Ni, I_Ni_56Co, color='green', linewidth=0.001,xerr=dWE_Ni, yerr=dI_Ni_56Co, elinewidth=0.5, ecolor='k', capthick=0.5 )
            plt.plot(WE_Ni, I_Ni_58Co, marker='o', label=r'$Ni(d,x)^{58}Co (CUM)$')
            plt.errorbar(WE_Ni, I_Ni_58Co, color='green', linewidth=0.001,xerr=dWE_Ni, yerr=dI_Ni_58Co, elinewidth=0.5, ecolor='k', capthick=0.5 )


            #plt.plot(WE_Ni, I_Ni_61Cu‚ '.', label='Ni')
            #i = np.where(I_Cu_62Zn>0)
            #j = np.where(I_Cu_63Zn>0)
            plt.plot(WE_Cu, I_Cu_62Zn, marker='o', label=r'$Cu(d,x)^{62}Zn$')
            plt.errorbar(WE_Cu, I_Cu_62Zn, color='green', linewidth=0.001,xerr=dWE_Cu, yerr=dI_Cu_62Zn, elinewidth=0.5, ecolor='k', capthick=0.5 )
            plt.plot(WE_Cu, I_Cu_63Zn, marker='o', label=r'$Cu(d,x)^{63}Zn$')
            plt.errorbar(WE_Cu, I_Cu_63Zn, color='green', linewidth=0.001,xerr=dWE_Cu, yerr=dI_Cu_63Zn, elinewidth=0.5, ecolor='k', capthick=0.5 )
            plt.plot(WE_Cu, I_Cu_65Zn, marker='o', label=r'$Cu(d,x)^{65}Zn$')
            plt.errorbar(WE_Cu, I_Cu_65Zn, color='green', linewidth=0.001,xerr=dWE_Cu, yerr=dI_Cu_65Zn, elinewidth=0.5, ecolor='k', capthick=0.5 )

            if compartment <= len(I_Fe_56Co):
                plt.plot(WE_Fe, I_Fe,marker='o', label=r'$Fe(d,x)^{56}Co$')
                plt.errorbar(WE_Fe, I_Fe, color='green', linewidth=0.001,xerr=dWE_Fe, yerr=dI_Fe, elinewidth=0.5, ecolor='k', capthick=0.5 )

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
            plt.show()

        return WE_Ni, chi_sq, I_est, sigma_I_est

    def chi_sqaured(self, data, model, error): #error = stdv
        dof = 5
        #return np.sum( (data - model/error )**2 )#( / (len(data-dof))
        n = len(data)
        #stdv = np.sqrt(1./n *  (np.sum(data-model)**2))
        #return np.sum((data-model)**2 / stdv**2)
        print(len(error))
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

    def CurrentPlot(self, name):
        I_Fe_56Co, I_Ni_61Cu, I_Ni_56Co, I_Ni_58Co, I_Cu_62Zn, I_Cu_63Zn, I_Cu_65Zn = self.specified_currents()
        dI_Fe_56Co, dI_Ni_61Cu, dI_Ni_56Co, dI_Ni_58Co, dI_Cu_62Zn, dI_Cu_63Zn, dI_Cu_65Zn = self.specified_currents(uncertainty=True)
        WE_Fe, WE_Ni, WE_Cu, WE_Ir = self.specified_energies()
        sigma_WE_Fe, sigma_WE_Ni, sigma_WE_Cu, sigma_WE_Ir = self.specified_energies(uncertainty=True)



        plt.axhline(128.5, linestyle='-.', linewidth=0.4, label='Monitor current 128.5 nA')


        plt.plot(WE_Ni,I_Ni_61Cu, '.', label=r'$^{nat}$Ni(d,x)$^{61}$Cu')
        plt.errorbar(WE_Ni, I_Ni_61Cu, color='green', linewidth=0.001, xerr=sigma_WE_Ni, yerr=dI_Ni_61Cu, elinewidth=0.5, ecolor='k', capthick=0.5 )

        plt.plot(WE_Ni,I_Ni_56Co, '.', label=r'$^{nat}$Ni(d,x)$^{56}$Co (CUM)')
        plt.errorbar(WE_Ni, I_Ni_56Co, color='green', linewidth=0.001, xerr=sigma_WE_Ni, yerr=dI_Ni_56Co, elinewidth=0.5, ecolor='k', capthick=0.5 )

        plt.plot(WE_Ni,I_Ni_58Co, '.', label=r'$^{nat}$Ni(d,x)$^{58}$Co (CUM)')
        plt.errorbar(WE_Ni, I_Ni_58Co, color='green', linewidth=0.001, xerr=sigma_WE_Ni, yerr=dI_Ni_58Co, elinewidth=0.5, ecolor='k', capthick=0.5 )

        #index = zero_to_nan(I_Cu_62Zn)[-1]
        #plt.plot(WE_Cu[index],I_Cu_62Zn[index], '.', label=r'$^{nat}$Cu(d,x)$^{62}$Zn')
        #plt.errorbar(WE_Cu[index], I_Cu_62Zn[index], color='green', linewidth=0.001, xerr=sigma_WE_Cu[index], yerr=dI_Cu_62Zn[index], elinewidth=0.5, ecolor='k', capthick=0.5 )
        plt.plot(WE_Cu,I_Cu_62Zn, '.', label=r'$^{nat}$Cu(d,x)$^{62}$Zn')
        plt.errorbar(WE_Cu, I_Cu_62Zn, color='green', linewidth=0.001, xerr=sigma_WE_Cu, yerr=dI_Cu_62Zn, elinewidth=0.5, ecolor='k', capthick=0.5 )

        #index = zero_to_nan(I_Cu_63Zn)[-1]
        #plt.plot(WE_Cu[index],I_Cu_63Zn[index], '.', label=r'$^{nat}$Cu(d,x)$^{63}$Zn')
        #plt.errorbar(WE_Cu[index], I_Cu_63Zn[index], color='green', linewidth=0.001, xerr=sigma_WE_Cu[index], yerr=dI_Cu_63Zn[index], elinewidth=0.5, ecolor='k', capthick=0.5 )
        plt.plot(WE_Cu,I_Cu_63Zn, '.', label=r'$^{nat}$Cu(d,x)$^{63}$Zn')
        plt.errorbar(WE_Cu, I_Cu_63Zn, color='green', linewidth=0.001, xerr=sigma_WE_Cu, yerr=dI_Cu_63Zn, elinewidth=0.5, ecolor='k', capthick=0.5 )

        plt.plot(WE_Cu,I_Cu_65Zn, '.', label=r'$^{nat}$Cu(d,x)$^{65}$Zn')
        plt.errorbar(WE_Cu, I_Cu_65Zn, color='green', linewidth=0.001, xerr=sigma_WE_Cu, yerr=dI_Cu_65Zn, elinewidth=0.5, ecolor='k', capthick=0.5 )
        #namez = names[file]
        plt.plot(WE_Fe,I_Fe_56Co, '.', label=r'$^{nat}$Fe(d,x)$^{56}$Co')
        plt.errorbar(WE_Fe, I_Fe_56Co, color='green', linewidth=0.001, xerr=sigma_WE_Fe, yerr=dI_Fe_56Co, elinewidth=0.5, ecolor='k', capthick=0.5 )

        plt.title('Beam current monitor foils - {}'.format(name))
        plt.xlabel('Energy, MeV')
        plt.ylabel('Measured deuteron beam current, nA')
        plt.ylim(0,350)
        plt.xlim(0,35)
        #ylim(top=350)
        #ylim(bottom=0)
        plt.legend(fontsize='x-small')
        path = os.getcwd()
        plt.savefig(path + '/BeamCurrent/current_all/' + name  + '.png',dpi=300)
        #plt.savefig(path+'/BeamCurrent/' + name +'.png', dpi=300)
        plt.show()

    def current_for_CS(self,return_energies=False):
        ### Making one current per compartment, ie one array length 10.

        I_Fe_56Co, I_Ni_61Cu, I_Ni_56Co, I_Ni_58Co, I_Cu_62Zn, I_Cu_63Zn, I_Cu_65Zn = self.specified_currents()
        dI_Fe_56Co, dI_Ni_61Cu, dI_Ni_56Co, dI_Ni_58Co, dI_Cu_62Zn, dI_Cu_63Zn, dI_Cu_65Zn = self.specified_currents(uncertainty=True)
        WE_Fe, WE_Ni, WE_Cu, WE_Ir = self.specified_energies()
        #print(WE_Fe, WE_Ni, WE_Cu)
        sigma_WE_Fe, sigma_WE_Ni, sigma_WE_Cu, sigma_WE_Ir = self.specified_energies(uncertainty=True)

        n = 10
        l = 3

        #print("56Co", I_Fe_56Co)
        #print("61Cu", I_Ni_61Cu)
        #print("56Co", I_Ni_56Co)
        #print("58Co", I_Ni_58Co)
        #print("62Zn", I_Cu_62Zn)
        #print("63Zn",I_Cu_63Zn)
        #print("65Zn",I_Cu_65Zn)


        def mean_val(list_of_vals):
            return np.mean(list_of_vals, axis=0)

        I   = []
        ### Making I_Fe_56Co a 10-lenght array filling empty spaces with zeros
        I_Fe_56Co = np.pad(I_Fe_56Co, (0, n-len(I_Fe_56Co)),'constant')
        I_list = [I_Fe_56Co, I_Ni_61Cu, I_Ni_56Co, I_Ni_58Co, I_Cu_62Zn, I_Cu_63Zn, I_Cu_65Zn]

        for i in range(n):
            list_of_vals = []
            for currents in I_list:
                if currents[i]>0:   #Not including values that are zero.
                    list_of_vals.append(currents[i])
            I.append(mean_val(list_of_vals))
        if return_energies==True:
            return WE_Fe, WE_Ni, WE_Cu, WE_Ir, sigma_WE_Fe, sigma_WE_Ni, sigma_WE_Cu, sigma_WE_Ir
        else:
            return I







"""
myclass = BeamCurrent(files[25])#, sort_ziegler, Fe_foil, Ni_foil, Cu_foil)
#myclass.plot_distribution('Ir', names[25])
myclass.variance_minimization(6, names[25], MakePlot=True)
myclass.CurrentPlot(names[25])
I = myclass.current_for_CS(return_energies=False)
print(I)
"""

class run_BeamCurrent:

    def __init__(self, files, names):
        self.files = files
        self.names = names

    def run_beam_current(self):
        if type(self.names) == str:
            #print(names, files)
            myclass = BeamCurrent(self.files)
            #myclass = BeamCurrent(self.file)
            myclass.CurrentPlot(self.names)
        else:
            n = len(self.names)
            for i in range(n):
                myclass = BeamCurrent(self.files[i])
                myclass.CurrentPlot(self.names[i])




    def flux_distribution(self, foil):
        if type(self.names) == str:
            myclass = BeamCurrent(self.files)
            myclass.plot_distribution(foil, self.names)
        else:
            n = len(self.names)
            for i in range(n):
                myclass = BeamCurrent(self.files[i])
                myclass.plot_distribution(foil, self.names[i])


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
            chi_sq_Ni      = []#np.zeros(n)
            chi_sq_Cu      = []#np.zeros(n)
            chi_sq_Fe      = []#np.zeros(n)
            chi_sq_SS      = []#np.zeros(n)
            I           = []   #np.zeros(n)
            dI          = []   #np.zeros(n)
            for i in range(n):
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

                plt.plot(Ni_en_Ni, chi_sq_Ni, label=r'$\chi^2$ Ni')
                plt.plot(Ni_en_Cu, chi_sq_Cu, label=r'$\chi^2$ Cu')
                plt.plot(Ni_en_Fe, chi_sq_Fe, label=r'$\chi^2$ Fe')
                plt.plot(Ni_en_SS, chi_sq_SS, label=r'$\chi^2$ SS')
                #plt.show()

                #plt.plot(Ni_energies, chi_sq_, '.')
                plt.title(r'$\chi^2$ minimization - Compartment {}'.format(compartment+1))
                plt.xlabel('Deuteron energy entering stack compartment number {} (MeV)'.format(compartment+1))
                plt.ylabel(r'$\chi^2$')
                plt.legend()
                plt.savefig('BeamCurrent/Chi_minimization/chi_squared_comp_{}'.format(compartment+1), dpi=300)
                plt.show()
