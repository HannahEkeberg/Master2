import curie as ci
import pandas as pd
from CrossSectionData import *
import os
import numpy as np
from collections import OrderedDict
import matplotlib.pyplot as plt
from tools import *

### Curie documentation --> https://jtmorrell.github.io/curie/build/html/api/

colors=Tools().colors()

#### Products [188Pt, 189Pt, 191Pt, 193mPt] Should also 192/194Ir?
products = ['188PT', '189PT', '191PT', '193MPT'] # In curie notation

class ThickTargetYield:

    def __init__(self, targetIsotope, beamParticle, Zbeam, t_irr): 
        # 'Ir', 'd'
        self.element = ci.Element(targetIsotope)
        self.molarMass = self.element.mass
        self.beamParticle = beamParticle
        self.Zbeam = Zbeam * 1.602e19
        self.t_irr = t_irr
        # E --> MeV, beamCurrent --> deuterons/second
        # E_max, E_min are the integral limits. E_max is incident beam energy.
        # E_max is zero if target is thicker than beam range, or reaction threshold otherwise
        pass

    def thickTargetYield(self, E, Cs, isotope): 
        # E, Cs, 193PTm
        Cs = Cs * (1e-27) # For converting from mb to cm2
        E = np.flip(E)
        decayConstant = ci.Isotope(isotope).decay_const(units = 'h', unc = True) # decay constant 1/h with uncertainty
        stoppingPower = self.element.S(energy = E, particle = self.beamParticle, density = 1E-3) * 1E3 # MeV/(g/cm^2)
        y = np.empty_like(E)
        for i, item in enumerate(Cs):
            y[i] = np.trapezoid ( 
                y = (Cs[0:i+1] / (self.Zbeam * 1.602e-19) ) / stoppingPower[0:i+1],
                x = E[0:i+1] 
                ) * (6.022e23/self.molarMass) / (1E6 * 1E6)
        #                     cm2             # particles/A      MeV/(g/cm^2)       MeV              # nuclei       MBq    uA
        
        #     np.trapz( 
        #         (smooth_xs[0:i+1] / (Z_beam*1.602e-19)) / (S_pw[0:i+1]), 
        #         x=e_range[0:i+1]   ) 
        #         *(6.022e23/MM) / (1E6 * 1E6)
        tty_eob = (1-np.exp(-decayConstant[0]*self.t_irr)) * y
        tty_saturation = y
        tty_physical = decayConstant[0] * y
        return E, tty_eob, tty_saturation, tty_physical

    def assembleThickTargetYields(self):
        # plt.plot(E,tty, label=label, color=color)
        # plt.xlabel('Deuteron energy (MeV)')
        plt.xlabel('Deuteron energy (MeV)')
        # plt.ylabel(r'MBq/$\mu$A $\cdot h$')
        plt.legend()
        plt.show()
    
    def plotPhysicalYield(self, E, y, label, color):
        print(len(E))
        print(len(y))
        E_new, y_new = Tools().interpolate(E, y)
        plt.plot(E_new, y_new,label=label, color=color)
        plt.ylabel('Physical Thick Target Yield (MBq/C)')
        # plt.yscale('log')


result = CrossSection(os.getcwd() + '/CrossSections/CrossSections_csv/')
E_193mPt, Cs_193mPt, dE_193mPt, dCs_193mPt = result.retrieveCrossSectionData('Ir_193mPt')
E_191Pt, Cs_191Pt, dE_191Pt, dCs_191Pt = result.retrieveCrossSectionData('Ir_191Pt')
E_189Pt, Cs_189Pt, dE_189Pt, dCs_189Pt = result.retrieveCrossSectionData('Ir_189Pt')


tty = ThickTargetYield('Ir', 'd', 1, 1)
# tty.plotThickTargetYields(E, tty_eob, 'log', '193mPt', 'red')
E1, tty_eob1, tty_saturation1, tty_physical1 = tty.thickTargetYield(E_193mPt, Cs_193mPt, '193PTm')
tty.plotPhysicalYield(E1, tty_physical1/0.0036, r'$^{193m}Pt$', color=colors[0]) 

E2, tty_eob2, tty_saturation2, tty_physical2 = tty.thickTargetYield(E_191Pt, Cs_191Pt, '191PT')
tty.plotPhysicalYield(E2, tty_physical2/0.0036, r'$^{191}Pt$', color=colors[1])

E3, tty_eob3, tty_saturation3, tty_physical3 = tty.thickTargetYield(E_189Pt, Cs_189Pt, '189PT')
tty.plotPhysicalYield(E2, tty_physical3/0.0036, r'$^{189}Pt$', color=colors[2])
tty.assembleThickTargetYields()
