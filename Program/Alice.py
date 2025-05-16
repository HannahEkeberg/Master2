import os
import numpy as np
from tools import *
import matplotlib.pyplot as plt

class Alice:

    def __init__(self, aliceFilepath):
        self.aliceFilepath = aliceFilepath

    def aliceData(self, productZ, productA, targetFoil, nuclearState = 'total', threshold=None):
        # nuclearState = total, groundState, isomer1, isomer2
        E, Cs = self.extractDataFromAliceFile(productZ, productA, targetFoil, nuclearState) 
        Cs = self.checkIfValidCs(Cs)
        E, Cs = Tools().interpolate(E, Cs, True)
        if threshold != None:
            E,Cs = Tools().setThreshold(E, Cs, threshold)
        return E, Cs

    def plotAlice(self, productZ, productA, targetFoil, nuclearState = None, threshold=None): #, betaFeeding = None, branchingRatio = None, parentNuclearState = None):
        try:
            if nuclearState == None:
                nuclearState = 'total'
            E, Cs = self.aliceData(productZ, productA, targetFoil, nuclearState, threshold)
            E, Cs = Tools().zeroPadding(E, Cs)
            plt.plot(E, Cs, label='ALICE-2020', color='green', linestyle=':')
        except:
            print("No alice file found for targetfoil: " + targetFoil + " and product Z: " + productZ + " and product A: " + productA)

    def plotAliceWithFeeding(self, productZ, productA, targetFoil, nuclearState = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None, threshold=None):
        # {isotope: [productZ, branchingRatio, nuclearState]} beta +/-
        # {isotope: [branchingRatio, nuclearState]} isomer
        if nuclearState == None:
                nuclearState = 'total'
        E, Cs = self.aliceData(productZ, productA, targetFoil, nuclearState, threshold)
        Cs_betaplus = []; Cs_betaminus = []; Cs_isomer = []
        if betaPlusDecayChain:
            for i in list(betaPlusDecayChain.keys()):
                Z = betaPlusDecayChain[i][0]
                branchingRatio= betaPlusDecayChain[i][1]
                state = betaPlusDecayChain[i][2]
                nuclearState= state if state is not None else 'total'
                E_bp, Cs_bp = self.aliceData(Z, productA, targetFoil, nuclearState, threshold)
                Cs_betaplus.append(Cs_bp*branchingRatio)
        if betaMinusDecayChain:
            for i in list(betaMinusDecayChain.keys()):
                Z = betaMinusDecayChain[i][0]
                branchingRatio= betaMinusDecayChain[i][1]
                state = betaMinusDecayChain[i][2]
                nuclearState= state if state is not None else 'total'
                E_bm, Cs_bm = self.aliceData(Z, productA, targetFoil, nuclearState, threshold)
                Cs_betaminus.append(Cs_bm*branchingRatio)
        if isomerDecayChain:
            for i in list(isomerDecayChain.keys()):
                branchingRatio= isomerDecayChain[i][0]
                state = isomerDecayChain[i][1]
                nuclearState= state if state is not None else 'total'
                E_i, Cs_i = self.aliceData(productZ, productA, targetFoil, nuclearState, threshold)
                Cs_isomer.append(Cs_i*branchingRatio)
        totCs = Cs + sum(Cs_betaplus) + sum(Cs_betaminus) + sum(Cs_isomer)
        plt.plot(E, totCs, label='ALICE-2020', color='green', linestyle=':')
        pass

    def extractDataFromAliceFile(self, productZ, productA, targetFoil, nuclearState):
        filename = self.aliceFilepath + 'plot_' + targetFoil #+ '_data'
        csColumn = self.getCsColumnFromNuclearState(nuclearState)
        E = []; Cs = []
        content = self.getDataFromAliceFile(filename)
        for line in range(len(content)):
            formatLine = ",".join(content[line].split())
            newLine = formatLine.split(",")
            Z = newLine[1]; A = newLine[2]
            if (Z == productZ) and (A == productA):
                E.append(newLine[0])
                Cs.append(newLine[csColumn])
        return E, Cs

    def getDataFromAliceFile(self, filename):
        beginMark =   ' (MeV)            cs.      cs.       cs.        cs        cs        cs         cs       cs       m1 to tot m2 to tot \n'
        endMark   =   ' Ebeam ='
        with open(filename) as f:
            content_full = f.readlines()
        ind_begin = [line for line in range(len(content_full)) if beginMark in content_full[line]][0]+1  # only one element but want it as integer
        ind_end   = [line for line in range(len(content_full)) if endMark in content_full[line]][0]-2  # list of different, only want the first element
        return content_full[ind_begin:ind_end]

    # def correctForBetaFeeding(self, productZ, productA,  targetFoil, betaFeeding, branchingRatio, parentNuclearState):
    #     if (betaFeeding  == 'beta+'):
    #         parentZ = str(int(productZ)+1); parentA = productA
    #     elif (betaFeeding == 'beta-'):
    #         parentZ = str(int(productZ)-1); parentA = productA
    #     csColumnParent = self.getCsColumnFromNuclearState(parentNuclearState)
    #     E, Cs = self.aliceData(parentZ, parentA, targetFoil, parentNuclearState)
    #     return E, Cs*branchingRatio

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

    def checkIfValidCs(self, Cs):
        for i in range(len(Cs)):
            if "*" in Cs[i]:
                Cs[i] = 0
        return Cs

# alicePath = os.getcwd() + '/../alice2020/'
# alice = Alice(alicePath).aliceData('78', '193', 'Ir', 'total')
# alice = Alice(alicePath).extractDataFromAliceFile('78', '193', 'Ir', 'isomer1')
# alice = Alice(alicePath).plotAlice('78', '193', 'Ir', 'isomer1')
# plt.show()
# alice = Alice(alicePath).extractDataFromAliceFile('78', '193', 'Ir', 'isomer1')


# Alice(alicePath).formatAliceFileInNewFile("Ir")
