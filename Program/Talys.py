import os
from tools import *
import numpy as np
import matplotlib.pyplot as plt

class Talys:

    def __init__(self, talysFilepath):
        self.talysFilepath = talysFilepath

    def talysData(self, productZ, productA, targetFoil, isomerLevel = None):
        product = self.product(productZ, productA) #78, 198 --> 078193
        fileEnding = self.talysFileEnding(isomerLevel)
        filename = self.talysFilepath + targetFoil + '/rp' + product + fileEnding
        print(filename)
        talysData = np.genfromtxt(filename)
        E = talysData[:,0]
        Cs = talysData[:,1]
        E, Cs = Tools().interpolate(E, Cs)
        return E, Cs

    def plotTalys(self,
    productZ,
    productA,
    targetFoil,
    isomerLevel = None,
    ):
        try:
            E, Cs = self.talysData(productZ, productA, targetFoil, isomerLevel)
            plt.plot(E, Cs, label='TALYS-2.04', linestyle='-.', color='orange')
        except:
            print("No talys file found for targetfoil: " + targetFoil + "and product Z: " + productZ + "and product A: " + productA)
   
    def plotdataWithMultipleFeeding(self, productZ, productA, targetFoil, isomerLevel= None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None):
        # {isotope: [productZ, branchingRatio isomerLevel]} #beta+/beta-
        # {isotope: [branchingRatio isomerLevel]} #isomer
        try:
            E, Cs = self.talysData(productZ, productA, targetFoil, isomerLevel)
            Cs_betaplus = []; Cs_betaminus = []; Cs_isomer = []
            if betaPlusDecayChain:
                for i in list(betaPlusDecayChain.keys()):
                    Z = betaPlusDecayChain[i][0]
                    branchingRatio= betaPlusDecayChain[i][1]
                    isomerLevel = betaPlusDecayChain[i][2]
                    E_bp, Cs_bp = self.talysData(Z, productA, targetFoil, isomerLevel)
                    Cs_betaplus.append(Cs_bp*branchingRatio)
            if betaMinusDecayChain:
                for i in list(betaMinusDecayChain.keys()):
                    Z = betaMinusDecayChain[i][0]
                    branchingRatio= betaMinusDecayChain[i][1]
                    isomerLevel = betaMinusDecayChain[i][2]
                    E_bm, Cs_bm = self.talysData(Z, productA, targetFoil, isomerLevel)
                    Cs_betaminus.append(Cs_bm*branchingRatio)
            if isomerDecayChain:
                for i in list(isomerDecayChain.keys()):
                    branchingRatio= isomerDecayChain[i][0]
                    isomerLevel = isomerDecayChain[i][1]
                    E_i, Cs_i = self.talysData(productZ, productA, targetFoil, isomerLevel)
                    Cs_isomer.append(Cs_i*branchingRatio)
            totCs = Cs + sum(Cs_betaplus) + sum(Cs_betaminus) + sum(Cs_isomer)
            plt.plot(E, totCs, label='TALYS-2.04', linestyle='-.', color='orange')
        except:
            print("No talys file found for targetfoil: " + targetFoil + "and product Z: " + productZ + "and product A: " + productA)
            print("OR decay parents") 

    def product(self, productZ, productA):
        if len(productZ) <= 2:
            productZ = '0' + productZ
        else:
            productZ = productZ
        if len(productA) <= 2:
            productA = '0' + productA
        else:
            productA = productA
        return productZ + productA

    def talysFileEnding(self, isomerLevel=None):
        return '.tot' if isomerLevel==None else '.L'+ isomerLevel


# talysFilePath = os.getcwd() + '/../talys_v2.04/'
# Talys(talysFilePath).plotTalys(productZ = '77',
#     productA = '188',
#     targetFoil = 'Ir',
#     isomerLevel = None,
#     betaFeeding = 'beta+', # only beta+ beta-
#     branchingRatio = 1.0,
#     parentIsomerLevel = None)
# plt.show()

# reaction = 'Ir_188Ir', # 'Ir_193mPt'
# targetFoil = 'Ir',
# productZ = '77',
# productA = '188',
# isomerLevel = None, #'05', tot (tendl, talys)
# isomerState = None, #m, m2 (empire, coh)
# nuclearState = None, # groundState, isomer1, isomer2 (alice)
# feeding = 'beta+', #beta+, beta-, isomer (empire only) (empire, coh, alice))
# branchingRatio = 1.0, #1, 0.5 (empire, coh, alice)
# parentIsomerLevel = None,
# parentNuclearState = None,
# parentIsomerState = None,
# reactionParent = 'Ir_188Pt'