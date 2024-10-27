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
        for t in self.target.keys():
            data = self.retrieveDataFromEmpireFile(filePath, t, productZ, productA, reaction)
            E.append(data[0])
            Cs.append(data[1])
        CsSummed = sum(Cs)
        E = next(item for item in E if item is not None) # Use first not None energy for reaction
        E, Cs = Tools().interpolate(E, CsSummed)
        return E, Cs

    def plotEmpire(self, productZ, productA, reaction, isomerState = None):
        if isomerState:
            productA = productA + self.empireIsomerState(isomerState)
        E, Cs = self.empireData(productZ, productA, reaction)
        plt.plot(E, Cs, label='EMPIRE-3.2.3', linestyle='--', color='red', linewidth=0.7)

    def retrieveDataFromEmpireFile(self, filepath, target, productZ, productA, reaction):
        targetIsotopeNumber = target[2:]; targetFoil = target[:2]
        product = self.getProductFromReaction(reaction) # feks Co, Pt, V
        empireFile = (filepath + targetIsotopeNumber + targetFoil + '/'
            + productZ + '-' + product + '-' + productA + '_empire.txt')
        if os.path.isfile(empireFile):
            Cs = np.genfromtxt(empireFile, delimiter='\t', usecols=[1])
            E = np.genfromtxt(empireFile, delimiter='\t', usecols=[0])
        else:
            print("No empire file for:" + reaction)
            Cs = 0; E = None
        abundance = self.target[target]
        return E, Cs*abundance

    def empireIsomerState(self, isomerState):
        if isomerState == 'm':
            isomerState =  'M'
        elif isomerState == 'g':
            isomerState = 'G'
        elif isomerState == 'm1+g':
            isomerState = None
        return isomerState


    def getProductFromReaction(self, reaction):
        product = reaction[-2:] # If product is two letters
        for i in range(1,9):
            if reaction[-2]==i:
                product = reaction[-1] # If product is single letter
        return product

# natIr = {"Ir191": 0.373, "Ir193": 0.627}
#
# empireFilePath = os.getcwd() + '/../EMPIRE/'
# empire_Fe = Empire({"Fe54": 0.5845, "Fe56": 0.91754, "Fe57": 0.2119, "Fe58": 0.282}, empireFilePath)
# empire_Ir = Empire(natIr, empireFilePath)
# empire_Ir.plotEmpire("78", "193", 'Ir_193mPt', isomerState='m')
