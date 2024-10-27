import numpy as np
import matplotlib.pyplot as plt

class CrossSection:

    def __init__(self, crossSectionCsvPath):
        self.crossSectionCsvPath = crossSectionCsvPath

    def retrieveCrossSectionData(self, reaction):
        # example: reaction = 'Ir_189Pt'
        csvFile = self.crossSectionCsvPath + reaction
        print(csvFile)
        E = np.genfromtxt(csvFile, delimiter=',', usecols=[0])
        dE = np.genfromtxt(csvFile, delimiter=',', usecols=[1])
        Cs = np.genfromtxt(csvFile, delimiter=',', usecols=[2])
        dCs = np.genfromtxt(csvFile, delimiter=',', usecols=[3])
        Cs = [float('nan') if x==0 else x for x in Cs]
        return E, dE, Cs, dCs

    def plotCrossSection(self, reaction):
        E, dE, Cs, dCs = self.retrieveCrossSectionData(reaction)
        plt.errorbar(E, Cs, marker='P', color='darkred',linewidth=0.0001,
        xerr=dE, yerr=dCs, elinewidth=1.0, capthick=1.0, capsize=3.0,
        label='This Work')
