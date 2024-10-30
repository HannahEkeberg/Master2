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
        E, Cs = self.talysData(productZ, productA, targetFoil, isomerLevel)
        if betaFeeding:
            CsParent = self.correctForBetaFeeding(productZ, productA, targetFoil, betaFeeding, branchingRatio, parentIsomerLevel)
            Cs = Cs + CsParent
        plt.plot(E, Cs, label='TALYS-2.04', linestyle='-.', color='orange')

    def correctForBetaFeeding(self, productZ, productA, targetFoil, betaFeeding, branchingRatio, parentIsomerLevel):
        if (feeding  == 'beta+'):
            parentZ = str(int(productZ)+1); parentA = productA
        elif (feeding == 'beta-'):
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
# Talys(talysFilePath).plotTalys('78', '193', 'Ir', '05')
