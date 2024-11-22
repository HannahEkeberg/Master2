import numpy as np
import matplotlib.pyplot as plt
import os
import requests
from scipy.interpolate import splev, splrep
from collections import OrderedDict

from tools import *
from Tendl import *
from CrossSectionData import *
from Empire import *
from Talys import *
from Coh import *
from Alice import *
from generateExcitationFunction import *

crossSectionCsvPath = os.getcwd() + '/CrossSections/CrossSections_csv/'
empireFilePath = os.getcwd() + '/../EMPIRE/'
talysFilePath = os.getcwd() + '/../talys_v2.04/'
# cohFilePath = os.getcwd() + '/../coh_v3.6.0/' #Remember to update to the correct label once new coh works
cohFilePath = os.getcwd() + '/../CoH/' #OLD CoH
aliceFilePath = os.getcwd() + '/../alice2020/'
# exforFilePath = os.getcwd() + '/../EXFOR/'
exforFilePath = os.getcwd() + '/../exfor2024/'
dirUpdatedFigures = 'CrossSections/updatedExcitationFunctions'

natIr = {"Ir191": 0.373, "Ir193": 0.627}
natCu = {"Cu63": 0.6915, "Cu65": 0.3085}
natFe = {"Fe54": 0.05845, "Fe56": 0.91754, "Fe57": 0.02119, "Fe58": 0.00282}
natNi = {"Ni58": 0.680769, "Ni60": 0.262231, "Ni61": 0.011399, "Ni62": 0.036345, "Ni64": 0.009256}


colors = Tools().colors()

generate = GenerateExcitationFunction(directoryFigs = dirUpdatedFigures)

iridium = AssembleExcitationFunctionForTarget(
crossSectionCsvPath = crossSectionCsvPath,
target = natIr,
empireFilePath = empireFilePath,
talysFilePath = talysFilePath,
cohFilePath = cohFilePath,
aliceFilePath = aliceFilePath,
exforFilePath = exforFilePath)

iron = AssembleExcitationFunctionForTarget(
crossSectionCsvPath = crossSectionCsvPath,
target = natFe,
empireFilePath = empireFilePath,
talysFilePath = talysFilePath,
cohFilePath = cohFilePath,
aliceFilePath = aliceFilePath,
exforFilePath = exforFilePath)

saveFlag = True
showFlag = True


#IRIDIUM

def Ir188Ir_independent():
    iridium.collectDataAndModels(
        reaction = 'Ir_188Ir', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '77',
        productA = '188',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = 'beta+', #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = 1.0, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = 'Ir_188Pt',
        independent = True
        )
    iridium.collectCrossSections("Ir_188Ir_independent")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {188} }}$Ir - Independent', 'Ir_188Ir_i', maxCs=2.9, show=showFlag, save=saveFlag)

def Ir188Ir_cumulative():
    iridium.collectDataAndModels(
        reaction = 'Ir_188Ir', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '77',
        productA = '188',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = False
        )
    iridium.collectCrossSections("Ir_188Ir")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {188} }}$Ir - cumulative', 'Ir_188Ir_c', maxCs=30.0, show=showFlag, save=saveFlag)

def Ir188Ir_independentWithSubtraction():
    iridium.plotComparableCrossSection("Ir_188Ir", r'$^{188}$Ir Cumulative ($\epsilon=100\%$)', 'maroon')
    iridium.plotComparableCrossSection("Ir_188Ir_independent", r'$^{188}$Ir Independent', 'mediumvioletred')
    # iridium.plotComparableCrossSection("Ir_188Pt", "188Pt - feeding 100%", colors[6])
    # iridium.collectCrossSections("Ir_188Ir_independent", "188Ir independent")
    iridium.collectDataAndModels(
        reaction = 'Ir_188Ir', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '77',
        productA = '188',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = 'beta+', #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = 1.0, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = "Ir_188Pt",
        independent = True
        )
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {188} }}$Ir - Independent', 'Ir_188Pt_i_subtracted', maxCs=1.75, show=showFlag, save=saveFlag)

def Ir188Pt_independent():
    iridium.collectDataAndModels(
        reaction = 'Ir_188Pt', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '78',
        productA = '188',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = True
        )
    iridium.collectCrossSections("Ir_188t")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {188} }}$Pt - Independent', 'Ir_188Pt_i', maxCs=2.0, show=showFlag, save=saveFlag)

def Ir189Ir_independent(): # DOES NOT WORK DUE TO 
    iridium.plotComparableCrossSection("Ir_189Ir", "189Ir Cumulative", colors[-1])
    iridium.plotComparableCrossSection("Ir_189Pt", "189Pt - feeding 100%", colors[-5])
    # iridium.collectCrossSections("Ir_189Ir_independent", "189Ir independent")
    iridium.collectDataAndModels(
        reaction = 'Ir_189Ir', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '77',
        productA = '189',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = 'beta+', #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = 1.0, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = "Ir_189Pt",
        independent = True
        )
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {189} }}$Ir - Independent', 'Ir_189Pt_i_subtracted', maxCs=550, show=showFlag, save=saveFlag)

def Ir189Ir_cumulative():
    iridium.collectCrossSections("Ir_189Ir")
    # iridium.collectCrossSections("Ir_189Ir_independent", "189Ir independent")
    iridium.collectDataAndModels(
        reaction = 'Ir_189Ir', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '77',
        productA = '189',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = False
        )
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {189} }}$Ir - Cumulative', 'Ir_189Ir_c', maxCs=370, show=showFlag, save=saveFlag)

def Ir189Pt_independent():
    iridium.collectDataAndModels(
        reaction = 'Ir_189Pt', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '78',
        productA = '189',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = True
        )
    iridium.collectCrossSections("Ir_189Pt")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {189} }}$Pt - Independent', 'Ir_189Pt_i', show=showFlag, save=saveFlag)

def Ir190m2Ir_independent():
    iridium.collectDataAndModels(
        reaction = 'Ir_190m2Ir', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '77',
        productA = '190',
        isomerLevel = '02', #'05', tot (tendl, talys)
        isomerState = 'm2', #m, m2 (empire, coh)
        nuclearState = 'isomer2', # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = True
        )
    iridium.collectCrossSections("Ir_190m2Ir")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {190m2} }}$Ir - Independent', 'Ir_190m2Ir_i', maxCs = 14.0, show=showFlag, save=saveFlag)

def Ir190Ir_cumulative():
    iridium.collectDataAndModels(
        reaction = 'Ir_190Ir', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '77',
        productA = '190',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = False
        )
    # iridium.collectCrossSections("Ir_190Ir")
    iridium.plotComparableCrossSection("Ir_190m2Ir", r'$^{190m2}$Ir (IT: $100\%$)', colors[-5])
    iridium.plotComparableCrossSection("Ir_190Ir_independent", r'$^{190m1+g}$ Independent', 'limegreen')
    iridium.plotComparableCrossSection("Ir_190Ir", r'$^{190}$Ir Cumulative', 'darkred')
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {190} }}$Ir - cumulative', 'Ir_190Ir_c', maxCs = 100.0, show=showFlag, save=saveFlag)

def Ir190Ir_cumulative_subtractedm2(): # TODO how to make reaction models model m1+g state?
    iridium.collectDataAndModels(
        reaction = 'Ir_190Ir', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '77',
        productA = '190',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = False
        )
    # iridium.collectCrossSections("Ir_190Ir")
    iridium.plotComparableCrossSection("Ir_190m2Ir", r'$^{190m2}$Ir (IT: $100\%$)', colors[-5])
    iridium.plotComparableCrossSection("Ir_190Ir_independent", r'$^{190m1+g}$ Independent', 'limegreen')
    iridium.plotComparableCrossSection("Ir_190Ir", r'$^{190}$Ir Cumulative', 'darkred')
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {190} }}$Ir - cumulative', 'Ir_190Ir_c', maxCs = 100.0, show=showFlag, save=saveFlag)

def Ir191Pt_independent(): # independent
    iridium.collectDataAndModels(
        reaction = 'Ir_191Pt', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '78',
        productA = '191',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = True
        )
    iridium.collectCrossSections("Ir_191Pt")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {191} }}$Pt - independent', 'Ir_191Pt_i', maxCs = 730.0, show=showFlag, save=saveFlag)

def Ir192Ir_cumulative(): # Cumulative with isomer feedings. Not detected, hence total cross section 
    iridium.collectDataAndModels(
        reaction = 'Ir_192Ir', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '77',
        productA = '192',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = False
        )
    iridium.collectCrossSections("Ir_192Ir")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {192} }}$Ir - cumulative', 'Ir_192Ir_c', maxCs = 250.0, show=showFlag, save=saveFlag)

def Ir193mPt_independent():
    iridium.collectDataAndModels(
        reaction = 'Ir_193mPt', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '78',
        productA = '193',
        isomerLevel = '05', #'05', tot (tendl, talys)
        isomerState = 'm', #m, m2 (empire, coh)
        nuclearState = 'isomer1', # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = True
        )
    iridium.collectCrossSections("Ir_193mPt")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {193m} }}$Pt - Independent', 'Ir_193mPt_i', maxCs = 530.0, show=showFlag, save=saveFlag)

def Ir194m2Ir_independent(): # TODO any point in including this?
    # iridium.collectDataAndModels(
    #     reaction = 'Ir_194m2Ir', # 'Ir_193mPt'
    #     targetFoil = 'Ir',
    #     productZ = '77',
    #     productA = '194',
    #     isomerLevel = '38', #'05', tot (tendl, talys)
    #     isomerState = 'm2', #m, m2 (empire, coh)
    #     nuclearState = 'isomer2', # groundState, isomer1, isomer2 (alice)
    #     feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
    #     branchingRatio = None, #1, 0.5 (empire, coh, alice)
    #     parentIsomerLevel = None,
    #     parentNuclearState = None,
    #     parentIsomerState = None,
    #     reactionParent = None
    #     )
    Exfor(exforFilePath).plotExforData('Ir_194m2Ir', independent=True)
    iridium.collectCrossSections("Ir_194m2Ir_independent")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {194m2} }}$Ir - Independent', 'Ir_194m2Ir_i', maxCs = 2.5, show=showFlag, save=saveFlag)

def Ir194Ir_cumulative():
    iridium.collectDataAndModels(
        reaction = 'Ir_194Ir', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '77',
        productA = '194',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = False
        )
    iridium.collectCrossSections("Ir_194Ir")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {194m2} }}$Ir - Cumulative', 'Ir_194Ir_c', maxCs = 160, show=showFlag, save=saveFlag)

#IRON

def Fe58Co_cumulative(): #isomer + groundstate...
    iron.collectDataAndModels(
        reaction = 'Fe_58Co', # 'Ir_193mPt'
        targetFoil = 'Fe',
        productZ = '27',
        productA = '58',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = False
        )
    iron.collectCrossSections("Fe_58Co")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {58} }}$Co - cumulative', 'Fe_58Co_c', maxCs = 10.0, show=showFlag, save=saveFlag)

def Fe57Co_independent(): 
    iron.collectDataAndModels(
        reaction = 'Fe_57Co', # 'Ir_193mPt'
        targetFoil = 'Fe',
        productZ = '27',
        productA = '57',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = True
        )
    iron.collectCrossSections("Fe_57Co")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {57} }}$Co - independent', 'Fe_57Co_i', maxCs = 370.0, show=showFlag, save=saveFlag)

def Fe55Co_independent():
    iron.collectDataAndModels(
        reaction = 'Fe_55Co', # 'Ir_193mPt'
        targetFoil = 'Fe',
        productZ = '27',
        productA = '55',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = True
        )
    iron.collectCrossSections("Fe_55Co")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {55} }}$Co - independent', 'Fe_55Co_i', maxCs = 50.0, show=showFlag, save=saveFlag)

def Fe59Fe_independent():
    iron.collectDataAndModels(
        reaction = 'Fe_59Fe', # 'Ir_193mPt'
        targetFoil = 'Fe',
        productZ = '26',
        productA = '59',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = True
        )
    iron.collectCrossSections("Fe_59Fe")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {59} }}$Fe - independent', 'Fe_59Fe_i', maxCs = 1.0, show=showFlag, save=saveFlag)

def Fe56Mn_cumulative(): # Can be subject to beta- feeding from 56Cr.  Missing cross section csv file... 
    iron.collectDataAndModels(
        reaction = 'Fe_56Mn', # 'Ir_193mPt'
        targetFoil = 'Fe',
        productZ = '25',
        productA = '56',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None,
        independent = False
        )
    iron.collectCrossSections("Fe_56Mn_cumulative")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {56} }}$Mn - cumulative', 'Fe_56Mn_c', maxCs = 30.0, show=showFlag, save=saveFlag)

Ir191Pt_independent()