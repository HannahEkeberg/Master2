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
from Exfor import *

"""
    *  isomerLevel - TENDL, TALYS:
        examples: None (becomes '.tot') '00' - groundstate '05' - isomerstate 5. Check tendl what level isomer is at
        If None, '.tot' is used, which is the cumulative cross section for isomer + ground state
   
    *  isomerState - EMPIRE, CoH:
        examples: g, m, m2. None is total cross section. For coh: g->G, m->M1, m2->M2.
        For empire: g->'', m->M, m2->M2
        To get a total cross section, all isomers must be listed with branching ratio.
        As well as beta feeding with branching ratio

    *   nuclearState - ALICE 
        Represents which column to look at in Alice file.
        None or 'total' - total cross section column 3,
        'groundstate' - column 5, 'isomer1' - column 7, 'isomer2' - column 9

    *   betafeeding - {parentIsomer}

    *  independent - implies whether experimental exfor data is independent or cumulative
"""

class AssembleExcitationFunctionForTarget:

    def __init__(self, crossSectionCsvPath, target, empireFilePath, talysFilePath, cohFilePath, aliceFilePath, exforFilePath):
        self.crossSectionCsvPath = crossSectionCsvPath
        self.target = target
        self.empireFilePath = empireFilePath
        self.talysFilePath = talysFilePath
        self.aliceFilePath = aliceFilePath
        self.cohFilePath = cohFilePath
        self.crossSectionData = CrossSection(crossSectionCsvPath)
        self.coh = Coh(target, cohFilePath)
        self.tendl = Tendl(target)
        self.empire = Empire(target, empireFilePath)
        self.talys = Talys(talysFilePath)
        self.alice = Alice(aliceFilePath)
        self.exfor = Exfor(exforFilePath)

    def collectCrossSections(self, reaction, label=None):
        self.crossSectionData.plotCrossSection(reaction, label)
    
    def plotCrossSectionWithLeftRightUncertainty(self, reaction, label=None, color=None):
        self.crossSectionData.plotCrossSectionWithLeftRightUncertainty(reaction, label, color)

    def plotComparableCrossSection(self, reaction, label, color):
        self.crossSectionData.plotComparableCrossSection(reaction, label, color)

    def plotMonitorCrossSections(self, reactionDir, label = None):
        self.crossSectionData.plotMonitorCrossSection(reactionDir, label)

    def collectDataAndModels(
        self,
        reaction, # 'Ir_193mPt'
        targetFoil, # 'Ir'
        productZ,
        productA,
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None,
        branchingRatio = None,
        parentIsomerLevel = None,
        parentIsomerState = None,
        parentNuclearState = None,
        reactionParent = None,
        independent = None # For exfor. If None --> independent == True
        ):
        self.tendl.plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
        self.empire.plotEmpire(productZ, productA, reaction, isomerState)# , feeding, parentIsomerState, branchingRatio, reactionParent)
        self.talys.plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
        self.coh.plotCoh(productZ, productA, reaction, isomerState)
        self.alice.plotAlice(productZ, productA, targetFoil, nuclearState)#, feeding, branchingRatio, parentNuclearState)
        self.exfor.plotExforData(reaction, independent)

    # def collectDataAndModelsWithFeeding(
    #     self,
    #     reaction, # 'Ir_193mPt'
    #     targetFoil, # 'Ir'
    #     productZ,
    #     productA,
    #     isomerLevel = None, #'05', tot (tendl, talys)
    #     isomerState = None, #m, m2 (empire, coh)
    #     nuclearState = None, # groundState, isomer1, isomer2 (alice)
    #     betaPlusDecayChain=None,
    #     betaMinusDecayChain=None,
    #     isomerDecayChain=None
    # ):
    #     self.empire.plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    #     self.coh.plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)

class GenerateExcitationFunction:

    def __init__(self, directoryFigs = None):
        self.directoryFigs = directoryFigs

    def plotExcitationFunction(self, title=None, reaction=None, maxCs=None, show=False, save=False):
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
            if reaction != None:
                plt.savefig(self.figPath(reaction), dpi=300)
            else: 
                raise Exception("In order to save the excitation function, a reaction must be present (e.g. Ni_60Cu)")
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

"""
Beta decay chain:
give the highest Z to desired isotope (which we already have).
If beta +, proton -1. If beta -

Give list of branching ratios. 
Find reaction modelling code per ... 


Can do the same with isomers... 
"""
