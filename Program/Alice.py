import os
import numpy as np
from tools import *
import matplotlib.pyplot as plt

class Alice:

    def __init__(self, aliceFilepath):
        self.aliceFilepath = aliceFilepath

    def aliceData(self, productZ, productA, targetFoil, nuclearState = 'groundState'):
        # nuclearState = total, groundState, isomer1, isomer2
        E, Cs = self.extractDataFromAliceFile(productZ, productA, targetFoil, nuclearState)
        E, Cs = Tools().interpolate(E, Cs)
        plt.plot(E, Cs, label='ALICE-2020', color='green', linestyle=':')
        plt.legend()
        plt.show()
        return E, Cs

    def extractDataFromAliceFile(self, productZ, productA, targetFoil, nuclearState):
        filename = self.aliceFilepath + 'plot_' + targetFoil + '_data'
        csColumn = self.getCsColumnFromNuclearState(nuclearState)
        with open(filename) as f:
            content = f.readlines()[2:]
            for s in content:
                line = " ".join(s.split())
        E_all = np.genfromtxt(filename, delimiter=' ', usecols=[0])
        # Cs_all = np.genfromtxt(filename, delimiter=' ', usecols=[4])
        E = []; Cs = []; Z = ' ' + productZ + ' '; A = ' ' + productA + ' '
        print("Attempting column: " + str(csColumn))
        for line in range(len(content)):
            if (A in content[line]) and (Z in content[line]):
                print(content[line])
                E.append(E_all[line])
                # Cs.append(Cs_all[line])
        return E, Cs

    def getCsColumnFromNuclearState(self, nuclearState):
        if nuclearState == 'total':
            return 6
        elif nuclearState == 'groundState':
            return 8
        elif nuclearState == 'isomer1':
            return 14
        elif nuclearState == 'isomer2':
            return 15
        else:
            raise Exception("Invalid nuclear state for Alice: " + nuclearState)

alicePath = os.getcwd() + '/../alice2020/'
# alice = Alice(alicePath).aliceData('24', '53', 'Ni', 'total')
# alice = Alice(alicePath).aliceData('78', '193', 'Ir', 'isomer1')
alice = Alice(alicePath).extractDataFromAliceFile('78', '193', 'Ir', 'isomer1')
