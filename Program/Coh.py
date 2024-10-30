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

    def cohData(self, productZ, productA, reaction, isomerState = None):
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
        CsSummed = sum(Cs)
        E = next(item for item in E if item is not None) # Use first not None energy for reaction files
        E, Cs = Tools().interpolate(E, CsSummed, zeroPadding=True)
        return E, Cs

    def plotCoh(self, productZ, productA, reaction, isomerState = None):
        E, Cs = self.cohData(productZ, productA, reaction, isomerState)
        plt.plot(E, Cs, label='CoH-3.6.0', linestyle='-', color='dodgerblue', linewidth=0.7)

    def retrieveDataFromCohFile(self, filepath, target, productZ, productA, reaction, isomerState):
        targetIsotopeNumber = target[2:]; targetFoil = target[:2]
        product = self.getProductFromReaction(reaction, isomerState) # feks Co, PtM, ptG V
        cohFile = (filepath + targetIsotopeNumber + targetFoil + '/'
            + productZ + '-' + productA + product + '_coh.txt')
        print("*** " + cohFile)
        if os.path.isfile(cohFile):
            Cs = np.genfromtxt(cohFile, delimiter='\t', usecols=[1])
            E = np.genfromtxt(cohFile, delimiter='\t', usecols=[0])
        else:
            print("No CoH file for:" + target + ' --> ' + reaction)
            Cs = 0; E = None
        abundance = self.target[target]
        return E, Cs*abundance

    def cohIsomerState(self, isomerState):
        if isomerState == 'm':
            isomerState =  'M'
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
            # return for instance PtM for isomer of platinum.
            return product + self.cohIsomerState(isomerState)
        else:
            return product

    def formatAtomicNumber(self, number):
        if len(number) <= 2:
            return '0' + number
        else:
            return number

# cohFilepath = os.getcwd() + '/../CoH/'
# coh = Coh({"Ir191": 0.373, "Ir193": 0.627}, cohFilepath)
# coh.plotCoh('78', '193', 'Ir_193mPt', 'm')
