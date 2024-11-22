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
    betaFeeding = None, # only beta+ beta-
    branchingRatio = None,
    parentIsomerLevel = None,
    ):
        try:
            E, Cs = self.talysData(productZ, productA, targetFoil, isomerLevel)
            if betaFeeding:
                CsParent = self.correctForBetaFeeding(productZ, productA, targetFoil, betaFeeding, branchingRatio, parentIsomerLevel)[-1] # only cross section
                Cs = Cs + CsParent
            plt.plot(E, Cs, label='TALYS-2.04', linestyle='-.', color='orange')
        except:
            print("No talys file found for targetfoil: " + targetFoil + "and product Z: " + productZ + "and product A: " + productA)

    def correctForBetaFeeding(self, productZ, productA, targetFoil, betaFeeding, branchingRatio, parentIsomerLevel):
        if (betaFeeding  == 'beta+'):
            parentZ = str(int(productZ)+1); parentA = productA
        elif (betaFeeding == 'beta-'):
            parentZ = str(int(productZ)-1); parentA = productA
        E, Cs = self.talysData(parentZ, parentA, targetFoil, parentIsomerLevel)
        return E, Cs*branchingRatio

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