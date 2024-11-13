import os
import numpy as np
from tools import *
import matplotlib.pyplot as plt

class Alice:

    def __init__(self, aliceFilepath):
        self.aliceFilepath = aliceFilepath

    def aliceData(self, productZ, productA, targetFoil, nuclearState = 'total'):
        # nuclearState = total, groundState, isomer1, isomer2
        E, Cs = self.extractDataFromAliceFile(productZ, productA, targetFoil, nuclearState)
        E, Cs = Tools().interpolate(E, Cs)
        return E, Cs

    def plotAlice(self, productZ, productA, targetFoil, nuclearState = None, betaFeeding = None, branchingRatio = None, parentNuclearState = None):
        if nuclearState == None:
            nuclearState = 'total'
        E, Cs = self.aliceData(productZ, productA, targetFoil, nuclearState)
        if betaFeeding:
            if parentNuclearState == None:
                parentNuclearState = 'total'
            CsParent = self.correctForBetaFeeding(productZ, productA, targetFoil, betaFeeding, branchingRatio, parentNuclearState)[0]
            Cs = Cs + CsParent
        plt.plot(E, Cs, label='ALICE-2020', color='green', linestyle=':')

    def extractDataFromAliceFile(self, productZ, productA, targetFoil, nuclearState):
        filename = self.aliceFilepath + 'plot_' + targetFoil + '_data'
        csColumn = self.getCsColumnFromNuclearState(nuclearState)
        E = []; Cs = [];
        with open(filename) as f:
            content = f.readlines()
        for line in range(len(content)):
            formatLine = ",".join(content[line].split())
            newLine = formatLine.split(",")
            Z = newLine[1]; A = newLine[2]
            if (Z == productZ) and (A == productA):
                E.append(newLine[0])
                Cs.append(newLine[csColumn])
        return E, Cs

    def correctForBetaFeeding(self, productZ, productA,  targetFoil, betaFeeding, branchingRatio, parentNuclearState):
        if (betaFeeding  == 'beta+'):
            parentZ = str(int(productZ)+1); parentA = productA
        elif (betaFeeding == 'beta-'):
            parentZ = str(int(productZ)-1); parentA = productA
        csColumnParent = self.getCsColumnFromNuclearState(parentNuclearState)
        E, Cs = self.aliceData(parentZ, parentA, targetFoil, parentNuclearState)
        return E, Cs*branchingRatio

    def getCsColumnFromNuclearState(self, nuclearState):
        if nuclearState == 'total':
            return 3
        elif nuclearState == 'groundState':
            return 5
        elif nuclearState == 'isomer1':
            return 7
        elif nuclearState == 'isomer2':
            return 9
        else:
            raise Exception("Invalid nuclear state for Alice: " + nuclearState)

# alicePath = os.getcwd() + '/../alice2020/'
# alice = Alice(alicePath).aliceData('24', '53', 'Ni', 'total')
# alice = Alice(alicePath).aliceData('78', '193', 'Ir', 'total')
# alice = Alice(alicePath).extractDataFromAliceFile('78', '193', 'Ir', 'isomer1')
# alice = Alice(alicePath).plotAlice('78', '193', 'Ir', 'isomer1')


# Alice(alicePath).formatAliceFileInNewFile("Ir")
