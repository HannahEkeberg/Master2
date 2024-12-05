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
cohFilePath = os.getcwd() + '/../coh_v3.6.0/'
aliceFilePath = os.getcwd() + '/../alice2020/'
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

cupper = AssembleExcitationFunctionForTarget(
crossSectionCsvPath = crossSectionCsvPath,
target = natCu,
empireFilePath = empireFilePath,
talysFilePath = talysFilePath,
cohFilePath = cohFilePath,
aliceFilePath = aliceFilePath,
exforFilePath = exforFilePath)

nickel = AssembleExcitationFunctionForTarget(
crossSectionCsvPath = crossSectionCsvPath,
target = natNi,
empireFilePath = empireFilePath,
talysFilePath = talysFilePath,
cohFilePath = cohFilePath,
aliceFilePath = aliceFilePath,
exforFilePath = exforFilePath)

saveFlag = True
showFlag = True


#INDEPENDENT

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
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {191} }}$Pt - independent', 'Ir_191Pt_i', maxCs = 850.0, show=showFlag, save=saveFlag)

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
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {189} }}$Pt - Independent', 'Ir_189Pt_i', maxCs = 600, show=showFlag, save=saveFlag)

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
    iridium.collectCrossSections("Ir_188Pt")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {188} }}$Pt - Independent', 'Ir_188Pt_i', maxCs=300, show=showFlag, save=saveFlag)

def Ir194m2Ir_independent():
    iridium.collectDataAndModels(
        reaction = 'Ir_194m2Ir', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '77',
        productA = '194',
        isomerLevel = '38', #'05', tot (tendl, talys)
        isomerState = 'm2', #m, m2 (empire, coh)
        nuclearState = 'isomer2', # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent = None
        )
    # Exfor(exforFilePath).plotExforData('Ir_194m2Ir', independent=True)
    iridium.collectCrossSections("Ir_194m2Ir_independent")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {194m2} }}$Ir - Independent', 'Ir_194m2Ir_i', maxCs = None, show=showFlag, save=saveFlag)

def Cu65Zn_independent():
    cupper.collectDataAndModels(
        reaction = 'Cu_65Zn', # 'Ir_193mPt'
        targetFoil = 'Cu',
        productZ = '30',
        productA = '65',
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
    cupper.plotCrossSectionWithLeftRightUncertainty("Cu_65Zn_independent")
    cupper.plotMonitorCrossSections("cud65znt")
    generate.plotExcitationFunction(r'$^{nat}$Cu(d,x)$^{{ {65} }}$Zn - independent', 'Cu_65Zn_i', maxCs = None, show=showFlag, save=saveFlag)

def Cu63Zn_independent():
    cupper.collectDataAndModels(
        reaction = 'Cu_63Zn', # 'Ir_193mPt'
        targetFoil = 'Cu',
        productZ = '30',
        productA = '63',
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
    cupper.plotCrossSectionWithLeftRightUncertainty("Cu_63Zn_independent")
    cupper.plotMonitorCrossSections("cud63znt")
    generate.plotExcitationFunction(r'$^{nat}$Cu(d,x)$^{{ {63} }}$Zn - independent', 'Cu_63Zn_i', maxCs = None, show=showFlag, save=saveFlag)

def Cu62Zn_independent():
    cupper.collectDataAndModels(
        reaction = 'Cu_62Zn', # 'Ir_193mPt'
        targetFoil = 'Cu',
        productZ = '30',
        productA = '62',
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
    cupper.plotCrossSectionWithLeftRightUncertainty("Cu_62Zn_independent")
    cupper.plotMonitorCrossSections("cud62znt")
    generate.plotExcitationFunction(r'$^{nat}$Cu(d,x)$^{{ {62} }}$Zn - independent', 'Cu_62Zn_i', maxCs = 45, show=showFlag, save=saveFlag)    

def Cu64Cu_independent():
    cupper.collectDataAndModels(
        reaction = 'Cu_64Cu', # 'Ir_193mPt'
        targetFoil = 'Cu',
        productZ = '29',
        productA = '64',
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
    cupper.plotCrossSectionWithLeftRightUncertainty("Cu_64Cu_independent")
    generate.plotExcitationFunction(r'$^{nat}$Cu(d,x)$^{{ {64} }}$Cu - independent', 'Cu_64Cu_i', maxCs = 450, show=showFlag, save=saveFlag)    

def Cu65Ni_independent():
    cupper.collectDataAndModels(
        reaction = 'Cu_65Ni', # 'Ir_193mPt'
        targetFoil = 'Cu',
        productZ = '28',
        productA = '65',
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
    # Coh has generated 65Ni as ground state and ismoer
    cupper.plotCrossSectionWithLeftRightUncertainty("Cu_65Ni_independent")
    generate.plotExcitationFunction(r'$^{nat}$Cu(d,x)$^{{ {65} }}$Ni - independent', 'Cu_65Ni_i', maxCs = 7, show=showFlag, save=saveFlag)    

def Fe56Co_independent():
    iron.collectDataAndModels(
        reaction = 'Fe_56Co', # 'Ir_193mPt'
        targetFoil = 'Fe',
        productZ = '27',
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
        independent = True
        )
    iron.plotMonitorCrossSections("fed56cot")
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_56Co_independent")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {56} }}$Co - independent', 'Fe_56Co_i', maxCs = None, show=showFlag, save=saveFlag)

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
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_57Co_independent")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {57} }}$Co - independent', 'Fe_57Co_i', maxCs = None, show=showFlag, save=saveFlag)

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
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_55Co_independent")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {55} }}$Co - independent', 'Fe_55Co_i', maxCs = None, show=showFlag, save=saveFlag)

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
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_59Fe_independent")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {59} }}$Fe - independent', 'Fe_59Fe_i', maxCs = None, show=showFlag, save=saveFlag)

def Fe54Mn_independent():
    iron.collectDataAndModels(
        reaction = 'Fe_54Mn', # 'Ir_193mPt'
        targetFoil = 'Fe',
        productZ = '25',
        productA = '54',
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
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_54Mn_independent")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {54} }}$Mn - independent', 'Fe_54Mn_i', maxCs = None, show=showFlag, save=saveFlag)


def Ni64Cu_independent():
    nickel.collectDataAndModels(
        reaction = 'Ni_64Cu', # 'Ir_193mPt'
        targetFoil = 'Ni',
        productZ = '29',
        productA = '64',
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
    nickel.plotCrossSectionWithLeftRightUncertainty("Ni_64Cu_independent")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {64} }}$Cu - independent', 'Ni_64Cu_i', maxCs = None, show=showFlag, save=saveFlag)

def Ni61Cu_independent():
    nickel.collectDataAndModels(
        reaction = 'Ni_61Cu', # 'Ir_193mPt'
        targetFoil = 'Ni',
        productZ = '29',
        productA = '61',
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
    # nickel.collectCrossSections("Ni_61Cu")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {61} }}$Cu - independent', 'Ni_61Cu_i', maxCs = None, show=showFlag, save=saveFlag)

def Ni60Cu_independent():
    nickel.collectDataAndModels(
        reaction = 'Ni_60Cu', # 'Ir_193mPt'
        targetFoil = 'Ni',
        productZ = '29',
        productA = '60',
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
    nickel.collectCrossSections("Ni_60Cu")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {60} }}$Cu - independent', 'Ni_60Cu_i', maxCs = None, show=showFlag, save=saveFlag)

def Ni65Ni_independent():
    nickel.collectDataAndModels(
        reaction = 'Ni_65Ni', # 'Ir_193mPt'
        targetFoil = 'Ni',
        productZ = '28',
        productA = '65',
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
    nickel.collectCrossSections("Ni_65Ni")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {65} }}$Ni - independent', 'Ni_65Ni_i', maxCs = None, show=showFlag, save=saveFlag)

def Ni54Mn_independent():
    nickel.collectDataAndModels(
        reaction = 'Ni_54Mn', # 'Ir_193mPt'
        targetFoil = 'Ni',
        productZ = '25',
        productA = '54',
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
    # nickel.plotCrossSectionWithLeftRightUncertainty("Ni_61Cu_independent")
    nickel.collectCrossSections("Ni_54Mn")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {54} }}$Mn - independent', 'Ni_54Mn_i', maxCs = None, show=showFlag, save=saveFlag)


# ONE STEP FEEDING:

def Ir189Ir_cumulative():
    # Coh is for short lived isomer and ground state + betaFeeding,  manual plot:
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '189', 'Ir_189Ir', isomerState='g', betaPlusDecayChain={"189Pt": ['78', 1.0, None, 'Ir_189Pt']}, betaMinusDecayChain=None, isomerDecayChain={"189mIr": [1.0, 'm', 'Ir_189mIr']})
    Empire(natIr, empireFilePath).plotdataWithMultipleFeeding('77', '189', 'Ir_189Ir', isomerState=None, betaPlusDecayChain={"189Pt": ['78', 1.0, None, 'Ir_189Pt']}, betaMinusDecayChain=None, isomerDecayChain=None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='189', targetFoil='Ir', nuclearState = None, betaPlusDecayChain={"189Pt": ['78', 1.0, None]}, betaMinusDecayChain=None, isomerDecayChain=None)
    Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '189', isomerLevel = None, betaPlusDecayChain = {"189Pt": ['78', 1.0, None]}, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='77', productA = '189', targetFoil = 'Ir', isomerLevel = None, betaPlusDecayChain = {"189Pt": ['78', 1.0, None]}, betaMinusDecayChain = None, isomerDecayChain = None)
    Exfor(exforFilePath).plotExforData('Ir_189Ir', independent=False)
    iridium.plotComparableCrossSection('Ir_189Pt', label=r'$^{189}$Pt ($\epsilon: 100\%$)', color='darkgreen')
    iridium.plotComparableCrossSection('Ir_189Ir', label=r'$^{189}$Ir (cumulative)', color='darkred')
    # iridium.collectCrossSections("Ir_189Ir")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {189} }}$Ir - Cumulative', 'Ir_189Ir_c', maxCs = 517.0, show=showFlag, save=saveFlag)

def Ir189Ir_independent(): # TODO negative values
    iridium.collectDataAndModels(
        reaction = 'Ir_189Ir', # 'Ir_193mPt'
        targetFoil = 'Ir',
        productZ = '77',
        productA = '189',
        isomerLevel = None, #'05', tot (tendl, talys)
        isomerState = None, #g, m, m2 (empire, coh)
        nuclearState = None, # groundState, isomer1, isomer2 (alice)
        feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
        branchingRatio = None, #1, 0.5 (empire, coh, alice)
        parentIsomerLevel = None,
        parentNuclearState = None,
        parentIsomerState = None,
        reactionParent =None,
        independent = True
        )
    # Coh is for short lived isomer and ground state + betaFeeding,  manual plot:
    Coh(natIr, cohFilePath).plotCoh('77', '189', 'Ir_189gIr', 'g')
    #Coh(natIr, cohFilePath).dataWithMultipleFeeding('77', '189', 'Ir_189Ir', isomerState='g', betaPlusDecayChain={"189Pt": ['78', 1.0, None, 'Ir_189Pt']}, betaMinusDecayChain=None, isomerDecayChain={"189mIr": [1.0, 'm', 'Ir_189mIr']})
    # iridium.collectCrossSections("Ir_189Ir_independent")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {189} }}$Ir - Independent', 'Ir_189Ir_c', show=showFlag, save=saveFlag)

def Ir188Ir_cumulative():
    br = 0.99999974
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '188', 'Ir_188Ir', isomerState=None, betaPlusDecayChain={"188Pt": ['78', br, None, 'Ir_188Pt']}, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(natIr, empireFilePath).plotdataWithMultipleFeeding('77', '188', 'Ir_188Ir', isomerState=None, betaPlusDecayChain={"188Pt": ['78', br, None, 'Ir_188Pt']}, betaMinusDecayChain=None, isomerDecayChain=None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='188', targetFoil='Ir', nuclearState = None, betaPlusDecayChain={"188Pt": ['78', br, None]}, betaMinusDecayChain=None, isomerDecayChain=None)
    Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '188', isomerLevel = None, betaPlusDecayChain = {"188Pt": ['78', br, None]}, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='77', productA = '188', targetFoil = 'Ir', isomerLevel = None, betaPlusDecayChain = {"188Pt": ['78', br, None]}, betaMinusDecayChain = None, isomerDecayChain = None)
    Exfor(exforFilePath).plotExforData('Ir_188Ir', independent=False)
    iridium.collectCrossSections("Ir_188Ir")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {188} }}$Ir - Cumulative', 'Ir_188Ir_c', maxCs = 12, show=showFlag, save=saveFlag)

def Ir188Ir_independent():
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '188', 'Ir_188Ir', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(natIr, empireFilePath).plotdataWithMultipleFeeding('77', '188', 'Ir_188Ir', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='188', targetFoil='Ir', nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '188', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='77', productA = '188', targetFoil = 'Ir', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    iridium.plotComparableCrossSection('Ir_188Ir', label='Cumulative', color='darkgreen')
    iridium.plotComparableCrossSection('Ir_188Ir_independent', label='Independent', color='darkred')
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {188} }}$Ir -independent', 'Ir_188Ir_i', maxCs=6, show=showFlag, save=saveFlag)

def Ir188Ir_independentAndCumulative():
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '188', 'Ir_188Ir', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(natIr, empireFilePath).plotdataWithMultipleFeeding('77', '188', 'Ir_188Ir', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='188', targetFoil='Ir', nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '188', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='77', productA = '188', targetFoil = 'Ir', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    iridium.plotComparableCrossSection('Ir_188Ir', label='Cumulative', color='darkred')
    iridium.plotComparableCrossSection('Ir_188Ir_independent', label='Independent', color='darkgreen')
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {188} }}$Ir -independent', 'Ir_189Ir_ic', maxCs=50, show=showFlag, save=saveFlag)

def Ir194Ir_cumulative(): # Must figure out what is m1+g and m2.... 
    # Only isomer feeding from m1.
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '194', 'Ir_194Ir', isomerState='g', betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain={'194mIr': [1.0, 'm', 'Ir_194mIr']})
    # TODO no isomer for empire. Does it plot m1+g or only g?
    Empire(natIr, empireFilePath).plotdataWithMultipleFeeding('77', '194', 'Ir_194Ir', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='194', targetFoil='Ir', nuclearState = 'groundState', betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain={'194mIr': [1.0, 'isomer1']})
    # Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '194', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '194', isomerLevel = '00', betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = {'194mIr': [1.0, '38']})
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='77', productA = '194', targetFoil = 'Ir', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Exfor(exforFilePath).plotExforData('Ir_194Ir', independent=False)
    iridium.collectCrossSections("Ir_194Ir")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {194} }}$Ir - Cumulative', 'Ir_194Ir_c', maxCs = 470.0, show=showFlag, save=saveFlag)

def Ir194m2Ir_independent(): # Must figure out what is m1+g and m2.... 
    # Only isomer feeding from m1.
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '194', 'Ir_194m2Ir', isomerState='m2', betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    # No isomer for empire
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='194', targetFoil='Ir', nuclearState = 'isomer2', betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    # No isomer2 for tendl?
    # No talys.. 
    Exfor(exforFilePath).plotExforData('Ir_194m2Ir', independent=True)
    iridium.collectCrossSections("Ir_194m2Ir")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {194m2} }}$Ir - independent', 'Ir_194m2Ir_i', maxCs = 3.0, show=showFlag, save=saveFlag)

def Ir192Ir_cumulative():
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '192', 'Ir_192Ir', isomerState='g', betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain={'192m2Ir': [1.0, 'm2', 'Ir_192m2Ir'], '192m1Ir': [0.999825, 'm', 'Ir_192mIr']})
    Empire(natIr, empireFilePath).plotdataWithMultipleFeeding('77', '192', 'Ir_192Ir', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    # Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '192', isomerLevel = '00', betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = {'192mIr': [1.0, '03'], '192m2Ir': [1.0, '15']})
    Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '192', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='77', productA = '192', targetFoil = 'Ir', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='192', targetFoil='Ir', nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    iridium.collectCrossSections("Ir_192Ir")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {192} }}$Ir - Cumulative', 'Ir_192Ir_c', maxCs = 470.0, show=showFlag, save=saveFlag)

def Ir190Ir_cumulative(): # m1 + m2 + g
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '190', 'Ir_190Ir', isomerState='g', betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain={'190m2Ir': [0.086, 'm2', 'Ir_190m2Ir'], '192m1Ir': [1.0, 'm', 'Ir_190mIr']})
    Empire(natIr, empireFilePath).plotdataWithMultipleFeeding('77', '190', 'Ir_190Ir', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '190', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='77', productA = '190', targetFoil = 'Ir', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='190', targetFoil='Ir', nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Exfor(exforFilePath).plotExforData('Ir_190Ir', independent=False)
    iridium.collectCrossSections("Ir_190Ir")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {190} }}$Ir - Cumulative', 'Ir_190Ir_c', maxCs = 230.0, show=showFlag, save=saveFlag)

def Ir190m1gIr_cumulative(): # g + m1
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '190', 'Ir_190Ir', isomerState='g', betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain={'190m1Ir': [1.0, 'm', 'Ir_190mIr']})
    Empire(natIr, empireFilePath).plotdataWithMultipleFeeding('77', '190', 'Ir_190Ir', isomerState='g', betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain={'190m1Ir': [1.0, 'm']})
    Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '190', isomerLevel = '00', betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = {'190m1Ir': [1.0, '02']})
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='77', productA = '190', targetFoil = 'Ir', isomerLevel = '00', betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = {'190m1Ir': [1.0, '02']})
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='190', targetFoil='Ir', nuclearState = 'groundState', betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain={'190m1Ir': [1.0, 'isomer1']})
    # Exfor(exforFilePath).plotExforData('Ir_190Ir', independent=False)
    iridium.plotComparableCrossSection('Ir_190Ir', label=r'$^{190}$Ir (g+m1+m2)', color='darkgreen')
    iridium.plotComparableCrossSection('Ir_190Ir_independent', label=r'$^{190m1+g}$Ir', color='darkred')
    # iridium.collectCrossSections("Ir_190Ir")
    # iridium.collectCrossSections("Ir_190Ir_independent")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {190m1+g} }}$Ir - Cumulative', 'Ir_190m1+gIr_c', maxCs = 230.0, show=showFlag, save=saveFlag)

def Ir190m2Ir_independent(): # m2
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '190', 'Ir_190Ir', isomerState='m2', betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(natIr, empireFilePath).plotdataWithMultipleFeeding('77', '190', 'Ir_190Ir', isomerState='m2', betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '190', isomerLevel = '37', betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='77', productA = '190', targetFoil = 'Ir', isomerLevel = '37', betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='190', targetFoil='Ir', nuclearState = 'isomer2', betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Exfor(exforFilePath).plotExforData('Ir_190m2Ir', independent=True)
    iridium.collectCrossSections("Ir_190m2Ir")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {190m2} }}$Ir - Independent', 'Ir_190m2Ir_i', maxCs = 15.0, show=showFlag, save=saveFlag)