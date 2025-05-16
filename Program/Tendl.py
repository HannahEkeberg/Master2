from tools import *
import numpy as np
import requests
import matplotlib.pyplot as plt
from urllib.request import urlopen

class Tendl:

    def __init__(self, target):
        self.target = target # target = {"Ir191": 0.373, "Ir193": 0.627}

    def tendlDeuteronData(self, productZ, productA, isomerLevel = None):
        targetFoil = list(self.target.keys())[0][0:2]
        product = self.product(productZ, productA)
        fileEnding = self.tendlFileEnding(isomerLevel)
        E = []
        Cs = []
        for t in self.target.keys():
            data = self.retrieveTendlDataFromUrl(
                self.tendDeuteronlUrl(targetFoil, t, product, fileEnding), t
            )
            if isinstance(data[0], np.ndarray):
                E.append(data[0])
                Cs.append(data[1])
        if len(E)==0 or len(Cs)==0:
            "TENDL: No data found for target: " + targetFoil + " for productZ" + productZ + "and product A: " + productA
            raise Exception
        CsSummed = sum(Cs)
        E = E[0]
        E, Cs = Tools().interpolate(E, CsSummed)
        # print(Cs)
        return E, Cs

    def plotTendl23(self, productZ, productA, isomerLevel = None): #, feeding = None, branchingRatio = None, parentIsomerLevel = None):
        # try:
        E, Cs = self.tendlDeuteronData(productZ, productA, isomerLevel)
        # if feeding == 'beta+' or feeding == 'beta-':
            # CsParent = self.correctForFeeding(productZ, productA, feeding, branchingRatio, parentIsomerLevel)[1]
            # Cs = Cs + CsParent
        plt.plot(E, Cs, label='TENDL-2023', linestyle='--', color='blue')
    # except:
        # print("Unable to retrive tendl data, perhaps no internet connection?")

    def plotTendl23Unique(self, productZ, productA, isomerLevel = None, color=None, lineStyle=None, label=None):
        E, Cs = self.tendlDeuteronData(productZ, productA, isomerLevel)
        plt.plot(E, Cs, label=label, linestyle=lineStyle, color=color)
        try:
            # if color==None:
            #     color='blue'
            # if lineStyle==None:
            #     linestyle='--'
            # if label==None:
            #     label = 'TENDL-2023'
            E, Cs = self.tendlDeuteronData(productZ, productA, isomerLevel)
            plt.plot(E, Cs, label=label, linestyle=linestyle, color=color)
        except:
            print("Unable to retrive tendl data, perhaps no internet connection?")

    def plotdataWithMultipleFeeding(self, productZ, productA, isomerLevel, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None):
        # {isotope: [productZ, branchingRatio isomerLevel]} #beta+/beta-
        # {isotope: [branchingRatio isomerLevel]} #isomer
        try:
            E, Cs = self.tendlDeuteronData(productZ, productA, isomerLevel)
            Cs_betaplus = []; Cs_betaminus = []; Cs_isomer = []
            if betaPlusDecayChain:
                for i in list(betaPlusDecayChain.keys()):
                    Z = betaPlusDecayChain[i][0]
                    branchingRatio= betaPlusDecayChain[i][1]
                    isomerLevel = betaPlusDecayChain[i][2]
                    E_bp, Cs_bp = self.tendlDeuteronData(Z, productA, isomerLevel)
                    Cs_betaplus.append(Cs_bp*branchingRatio)
            if betaMinusDecayChain:
                for i in list(betaMinusDecayChain.keys()):
                    Z = betaMinusDecayChain[i][0]
                    branchingRatio= betaMinusDecayChain[i][1]
                    isomerLevel = betaMinusDecayChain[i][2]
                    E_bm, Cs_bm = self.tendlDeuteronData(Z, productA, isomerLevel)
                    Cs_betaminus.append(Cs_bm*branchingRatio)
            if isomerDecayChain:
                for i in list(isomerDecayChain.keys()):
                    branchingRatio= isomerDecayChain[i][0]
                    isomerLevel = isomerDecayChain[i][1]
                    E_i, Cs_i = self.tendlDeuteronData(productZ, productA, isomerLevel)
                    Cs_isomer.append(Cs_i*branchingRatio)
            totCs = Cs + sum(Cs_betaplus) + sum(Cs_betaminus) + sum(Cs_isomer)
            plt.plot(E, totCs, label='TENDL-2023', linestyle='--', color='blue')
        except:
            print("Unable to retrive tendl data, perhaps no internet connection?")





    # def correctForFeeding(self, productZ, productA, betaFeeding, branchingRatio, parentIsomerLevel):
    #     if (betaFeeding  == 'beta+'):
    #         parentZ = str(int(productZ)+1); parentA = productA
    #     elif (betaFeeding == 'beta-'):
    #         parentZ = str(int(productZ)-1); parentA = productA
    #     E, Cs = self.tendlDeuteronData(parentZ, parentA, parentIsomerLevel)
        # return E, Cs*branchingRatio

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

    def tendDeuteronlUrl(self, targetFoil, target, product, fileEnding):
        if len(target)<5:
            target = target[0:2] + '0' + target[2:]
        return ('https://tendl.web.psi.ch/tendl_2023/deuteron_file/'
        + targetFoil + '/' + target
        + '/tables/residual/rp'
        + product + fileEnding)

    def tendlFileEnding(self, isomerLevel=None):
        return '.tot' if isomerLevel==None else '.L' + isomerLevel

    def retrieveTendlDataFromUrl(self, url, target):
        try:
            print(url)
            tendlData = requests.get(url).text.split("\n")[27:] # skipping 27 first lines in tendl file
            tendlData = np.genfromtxt(tendlData)
            abundance = self.target[target]
            E = tendlData[:,0]
            Cs = tendlData[:,1]
            return E, Cs*abundance
        except:
            print('Unable to retrieve tendlData from url: ' + url)
            return 0,0
            # raise Exception("Unable to retrieve tendl data from url: " + url)

    def retrieveDataFromUrlWithNumpy(self, url):
        tendl_data = np.genfromtxt(urlopen("https://tendl.web.psi.ch/tendl_2023/deuteron_file/Ir/Ir193/tables/residual/rp078193.L05"), delimiter=" ")
        energy = tendl_data[:,0]
        xs = tendl_data[:,1]
        return energy, xs

    def mapFeedingObject(self, feeding):
        new = []
        for item in feeding:
            new.append(vars(item))
        print(new)
            



