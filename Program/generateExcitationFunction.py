import matplotlib.pyplot as plt
import os
from collections import OrderedDict
from Tendl import *
from Alice import *
from Coh import *
from Tendl import *
from Talys import *
from Empire import *
from CrossSectionData import *


class AssembleExcitationFunctionForTarget:

    def __init__(self, crossSectionCsvPath, target, empireFilePath, talysFilePath, cohFilePath, aliceFilePath):
        self.crossSectionCsvPath = crossSectionCsvPath
        self.target = target
        self.empireFilePath = empireFilePath
        self.talysFilePath = talysFilePath
        self.aliceFilePath = aliceFilePath
        self.cohFilePath = cohFilePath
        self.crossSectionData = CrossSection(crossSectionCsvPath)
        self.tendl = Tendl(target)
        self.empire = Empire(target, empireFilePath)
        self.talys = Talys(talysFilePath)
        self.alice = Alice(aliceFilePath)

    def collectDataAndModels(
        self,
        reaction, # 'Ir_193mPt'
        targetFoil,
        productZ,
        productA,
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta- (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None
        ):
        self.crossSectionData.plotCrossSection(reaction = reaction)
        self.tendl.plotTendl23(productZ, productA, isomerLevel, feeding, branchingRatio, parentIsomerLevel)
        self.empire.plotEmpire(productZ, productA, reaction, isomerState, feeding, parentIsomerState, branchingRatio, reactionParent)
        self.talys.plotTalys(productZ, productA, targetFoil, isomerLevel, feeding, branchingRatio, parentIsomerLevel)
        # self.coh_natIr.plotCoh(productZ = '78', productA='193', reaction='Ir_193mPt', isomerState = 'm')
        self.alice.plotAlice(productZ, productA, targetFoil, nuclearState, feeding, branchingRatio, parentNuclearState)


class GenerateExcitationFunction:

    def __init__(self, directoryFigs = None):
        self.directoryFigs = directoryFigs

    def plotExcitationFunction(self, title, reaction, maxCs=None, show=False, save=False):
        # pathToFigs = os.getcwd() + '/' + dirUpdatedFigures + '/'
        plt.xlabel('Deuteron Energy (MeV)')
        plt.ylabel('Cross Section (mb)')
        plt.title(title)
        handles, labels = plt.gca().get_legend_handles_labels()
        by_label = OrderedDict(zip(labels, handles))
        plt.legend(by_label.values(), by_label.keys(),fontsize='small', loc='best')
        plt.gca().set_xlim(left=0, right=40)
        if maxCs==None:
            plt.gca().set_ylim(bottom=0)
        else:
            plt.gca().set_ylim(bottom=0, top=maxCs)
        if save:
            plt.savefig(self.figPath(reaction), dpi=300)
        if show:
            plt.show()

    def figPath(self, figName):
        if self.directoryFigs != None:
            if not os.path.exists(self.directoryFigs):
                os.mkdir(self.directoryFigs)
        if self.directoryFigs == None:
            return figName + '.png'
        else:
            return os.getcwd() + '/' + self.directoryFigs + '/' + figName + '.png'
