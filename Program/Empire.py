import os
import numpy as np
import matplotlib.pyplot as plt
from tools import *

class Empire:

    def __init__(self, target, empireFilePath):
        # target = {"Ir191": 0.373, "Ir193": 0.627}
        self.target = target
        self.empireFilePath = empireFilePath

    def empireData(self, productZ, productA, reaction, isomerState = None):
        #reaction = 'Fe_51Cr'
        targetFoil = list(self.target.keys())[0][0:2]
        filePath = self.empireFilePath + targetFoil + '/'
        E = []; Cs = []
        if isomerState:
            productA = productA + self.empireIsomerState(isomerState)
        for t in self.target.keys():
            data = self.retrieveDataFromEmpireFile(filePath, t, productZ, productA, reaction)
            E.append(data[0])
            Cs.append(data[1])
        CsSummed = sum(Cs)
        E = next(item for item in E if item is not None) # Use first not None energy for reaction files
        E, Cs = Tools().interpolate(E, CsSummed)
        return E, Cs

    def plotEmpire(
        self,
        productZ,
        productA,
        reaction,
        isomerState = None,
        independent = True,
        feeding = None,
        parentIsomerState = None,
        branchingRatio = None,
        reactionParent = None
        ):
        E, Cs = self.empireData(productZ, productA, reaction, isomerState)
        if feeding:
            Cs_parent = self.correctForFeeding(feeding, productZ, productA, parentIsomerState, reactionParent, branchingRatio)[1]
            Cs = Cs + Cs_parent
        plt.plot(E, Cs, label='EMPIRE-3.2.3', linestyle='--', color='red', linewidth=0.7)

    def correctForFeeding(self, feeding, productZ, productA, parentIsomerState, reactionParent, branchingRatio):
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

    def retrieveDataFromEmpireFile(self, filepath, target, productZ, productA, reaction):
        targetIsotopeNumber = target[2:]; targetFoil = target[:2]
        product = self.getProductFromReaction(reaction) # feks Co, Pt, V
        empireFile = (filepath + targetIsotopeNumber + targetFoil + '/'
            + productZ + '-' + product + '-' + productA + '_empire.txt')
        if os.path.isfile(empireFile):
            Cs = np.genfromtxt(empireFile, delimiter='\t', usecols=[1])
            E = np.genfromtxt(empireFile, delimiter='\t', usecols=[0])
        else:
            print("No empire file for:" + target + ' --> ' + reaction)
            print(empireFile)
            Cs = 0; E = None
        abundance = self.target[target]
        return E, Cs*abundance

    def empireIsomerState(self, isomerState):
        if isomerState == 'm':
            isomerState =  'M'
        if isomerState == 'm2':
            isomerState =  'M2'
        elif isomerState == 'g':
            isomerState = 'G'
        elif isomerState == 'm1+g':
            isomerState = ''
        return isomerState

    def getProductFromReaction(self, reaction):
        product = reaction[-2:] # If product is two letters
        for i in range(1,9):
            if reaction[-2]==i:
                # If product is single letter.
                # For instance 48V --> reaction[-2:] = 8V instead of just V
                product = reaction[-1]
        return product


# empireFilePath = os.getcwd() + '/../EMPIRE/'
# empire = Empire({"Ir191": 0.373, "Ir193": 0.627}, empireFilePath)
# empire.plotEmpire('77', '188', 'Ir_188Ir', isomerState = 'm1+g',
# independent = False,
# feeding = 'beta+',
# branchingRatio = 1.0,
# reactionParent = 'Ir_188Pt',
# parentIsomerState = None)

# empire.plotEmpire('78', '193', 'Ir_193Pt', isomerState = None,
# independent = False,
# feeding = 'isomer',
# branchingRatio = 1.0,
# reactionParent = 'Ir_193mPt',
# parentIsomerState = 'm')

# empire.plotEmpire('78', '193', 'Ir_193mPt', isomerState = 'm',
# independent = True,
# feeding = None,
# branchingRatio = None,
# reactionParent = None,
# parentIsomerState = None)
# plt.show()
