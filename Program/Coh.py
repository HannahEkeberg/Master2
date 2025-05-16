import os
import numpy as np
import matplotlib.pyplot as plt
from tools import *

class Coh:
    def __init__(self, target, cohFilepath):
        # target = {"Ir191": 0.373, "Ir193": 0.627}
        # TODO must figure out how to get files.... 
        self.target = target
        self.cohFilepath = cohFilepath

    def cohData(self, productZ, productA, reaction, isomerState = None, threshold=None):
        #reaction = 'Fe_51Cr'
        targetFoil = list(self.target.keys())[0][0:2]
        filePath = self.cohFilepath + targetFoil + '/'
        productA = self.formatAtomicNumber(productA)
        productZ = self.formatAtomicNumber(productZ)
        E = []; Cs = []
        for t in self.target.keys():
            data = self.retrieveDataFromCohFile(filePath, t, productZ, productA, reaction, isomerState)
            E.append(data[0])
            Cs.append(data[1])
        # if len(E)==0 or len(Cs)==0:
        if all(v is None for v in E):
            print("No coh file found for target foil: " + targetFoil + " with productZ " + productZ + " and productA " + productA)
            raise Exception("No file found for ...")
        CsSummed = sum(Cs)
        E = next(item for item in E if item is not None) # Use first not None energy for reaction files
        E, Cs = Tools().interpolate(E, CsSummed, zeroPadding=True)
        print(threshold)
        print("Threshold on coh active")
        if threshold != None:
            print("Threshold on coh active")
            E,Cs = Tools().setThreshold(E, Cs, threshold)
        return E, Cs

    def plotCoh(self, productZ, productA, reaction, isomerState = None,
        feeding = None, parentIsomerState = None, branchingRatio = None,reactionParent = None, threshold=None):
        try:
            E, Cs = self.cohData(productZ, productA, reaction, isomerState, threshold)
            plt.plot(E, Cs, label='CoH-3.6.0', linestyle='-', color='dodgerblue', linewidth=0.7)
        except:
            print("Unable to model CoH for reaction: " + reaction)

    def plotdataWithMultipleFeeding(self, productZ, productA, reaction, isomerState, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=None):
        # Decay chain {"189Pt": [78, 1.0, None]} --> {nucleus: [productZ, branchingRatio, state]}
        #{isotope: [Z, br, isomerState, reaction]} beta+/-
        #{isotope: [br, isomerState, reaction]} isomer
        try:
            E, Cs = self.cohData(productZ, productA, reaction, isomerState, threshold)
            Cs_betaplus = []; Cs_betaminus = []; Cs_isomer = []
            try:
                if betaPlusDecayChain:
                    for i in list(betaPlusDecayChain.keys()):
                        Z = betaPlusDecayChain[i][0]
                        branchingRatio= betaPlusDecayChain[i][1]
                        isomerState=betaPlusDecayChain[i][2]
                        reaction = betaPlusDecayChain[i][3]
                        E_bp, Cs_bp = self.cohData(Z, productA, reaction, isomerState, threshold)
                        Cs_betaplus.append(Cs_bp*branchingRatio)
                if betaMinusDecayChain:
                    for i in list(betaMinusDecayChain.keys()):
                        Z = betaMinusDecayChain[i][0]
                        branchingRatio= betaMinusDecayChain[i][1]
                        isomerState=betaMinusDecayChain[i][2]
                        reaction = betaMinusDecayChain[i][3]
                        E_bm, Cs_bm = self.cohData(Z, productA, reaction, isomerState, threshold)
                        Cs_betaminus.append(Cs_bm*branchingRatio)
                if isomerDecayChain:
                    for i in list(isomerDecayChain.keys()):
                        branchingRatio= isomerDecayChain[i][0]
                        isomerState=isomerDecayChain[i][1]
                        reaction = isomerDecayChain[i][2]
                        E_i, Cs_i = self.cohData(productZ, productA, reaction, isomerState, threshold)
                        Cs_isomer.append(Cs_i*branchingRatio)
            except:
                pass
            totCs = Cs + sum(Cs_betaplus) + sum(Cs_betaminus) + sum(Cs_isomer)
            plt.plot(E, totCs, label='CoH-3.6.0', linestyle='-', color='dodgerblue', linewidth=0.7)
        except:
            print("Unable to model CoH for reaction: " + reaction)
        

    def correctForBetaFeeding(self, feeding, productZ, productA, parentIsomerState, reactionParent, branchingRatio):
        if (feeding  == 'beta+'):
            parentZ = str(int(productZ)+1); parentA = productA
        elif (feeding == 'beta-'):
            parentZ = str(int(productZ)-1); parentA = productA
        elif feeding == 'isomer':
            parentZ = productZ; parentA = productA
        else:
            raise Exception("Feeding invalid: " + feeding)
        E, Cs_parent = self.empireData(parentZ, parentA, reactionParent, parentIsomerState)
        return E, Cs_parent*branchingRatio
    
    def correctForIsomerFeeding(self, feeding, productZ, productA, parentIsomerState, reactionParent, branchingRatio):
        if (feeding  == 'isomer'):
            parentZ = str(int(productZ)+1); parentA = productA
        elif (feeding == 'beta-'):
            parentZ = str(int(productZ)-1); parentA = productA
            raise Exception("Feeding invalid: " + feeding)
        E, Cs_parent = self.empireData(parentZ, parentA, reactionParent, parentIsomerState)
        return E, Cs_parent*branchingRatio

    def retrieveDataFromCohFile(self, filepath, target, productZ, productA, reaction, isomerState):
        targetIsotopeNumber = target[2:]; targetFoil = target[:2]
        product = self.getProductFromReaction(reaction, isomerState) # feks Co, PtM, ptG V
        cohFile = (filepath + targetIsotopeNumber + targetFoil + '/plots/'
            + productZ + '-' + productA + product + '_coh.txt')
        if os.path.isfile(cohFile):
            Cs = np.genfromtxt(cohFile, delimiter='\t', usecols=[1])
            E = np.genfromtxt(cohFile, delimiter='\t', usecols=[0])
        else:
            print("No CoH file for:" + target + ' --> ' + reaction)
            print("No CoH found on:" + cohFile)
            Cs = 0; E = None
        abundance = self.target[target]
        return E, Cs*abundance

    def cohIsomerState(self, isomerState):
        if isomerState == 'm':
            isomerState =  'M1'
        elif isomerState == 'm2':
            isomerState =  'M2'
        elif isomerState == 'g':
            isomerState = 'G'
        else:
            isomerState = None
        return isomerState

    def getProductFromReaction(self, reaction, isomerState):
        product = reaction[-2:] # If product is two letters
        for i in range(1,9):
            if reaction[-2]==i:
                # If product is single letter.
                # For instance 48V --> reaction[-2:] = 8V instead of just V
                product = reaction[-1]
        if isomerState != None:
            # return for instance PtM1 for isomer of platinum.
            return product + self.cohIsomerState(isomerState)
        else:
            return product

    def formatAtomicNumber(self, number):
        if len(number) <= 2:
            return '0' + number
        else:
            return number

# cohFilePath = os.getcwd() + '/../coh_v3.6.0/'
# coh = Coh({"Ir191": 0.373, "Ir193": 0.627}, cohFilePath)
# E,Cs = coh.dataWithMultipleFeeding('77', '189', 'Ir_189Ir', isomerState='g', betaPlusDecayChain={"189Pt": ['78', 1.0, None, 'Ir_189Pt']}, betaMinusDecayChain=None, isomerDecayChain={"189mIr": [1.0, 'm', 'Ir_189mIr']})
# coh.plotCoh(productZ='77', productA='189', reaction='Ir_189Ir', isomerState = 'g',feeding =None, parentIsomerState = None, branchingRatio = None,reactionParent = None)
# plt.plot(E, Cs, label='withSum')
# plt.legend()
# plt.show()
# print(coh.cohIsomerState('m'))
# coh.plotCoh('78', '191', 'Ir_191Pt', None)
# coh.plotCoh('78', '193', 'Ir_191Pt', 'm')
