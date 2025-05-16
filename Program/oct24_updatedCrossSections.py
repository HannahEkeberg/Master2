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


# MONITOR REACTIONS:

def Fe_56Co_mon():
    productZ='27'; productA='56'; isomerLevel=None; reaction='Fe_56Co'; isomerState=None; targetFoil='Fe'; nuclearState=None
    independent=True; threshold=6; foilDict=natFe
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=6)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    iron.plotMonitorCrossSections("fed56cot")
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_56Co_independent")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {56} }}$Co - independent', 'Fe_56Co_i', maxCs = 600, show=showFlag, save=saveFlag)

def Ni_56Co_mon():
    productZ='27'; productA='56'; isomerLevel= None; reaction='Ni_56Co'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=False; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    nickel.plotMonitorCrossSections("nid56cot")
    nickel.collectCrossSections("Ni_56Co")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {56} }}$Co - cumulative', 'Ni_56Co_c', maxCs = None, show=showFlag, save=saveFlag)

def Ni_58Co_mon():
    productZ='27'; productA='58'; isomerLevel= None; reaction='Ni_58Co'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=False; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    nickel.plotMonitorCrossSections("nid58cot")
    nickel.collectCrossSections("Ni_58Co_cumulative")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {58} }}$Co - cumulative', 'Ni_58Co_c', maxCs = 500, show=showFlag, save=saveFlag)

def Ni_61Cu_mon():
    productZ='29'; productA='61'; isomerLevel=None; reaction='Ni_61Cu'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=True; threshold=3
    Tendl(natNi).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(natNi, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(natNi, cohFilePath).plotCoh(productZ, productA, reaction, isomerState)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    nickel.plotMonitorCrossSections("nid61cut")
    nickel.plotCrossSectionWithLeftRightUncertainty("Ni_61Cu_independent.csv")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {61} }}$Cu - independent', 'Ni_61Cu_i', maxCs = None, show=showFlag, save=saveFlag)

def Cu_62Zn_mon():
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

def Cu65Zn_mon():
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

def Cu63Zn_mon():
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
    productZ='78'; productA='189'; isomerLevel=None; reaction='Ir_189Pt'; isomerState=None; targetFoil='Ir'; nuclearState=None
    independent=True; threshold=19
    Tendl(natIr).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(natIr, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(natIr, cohFilePath).plotCoh(productZ, productA, reaction, isomerState)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    iridium.collectCrossSections("Ir_189Pt")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {189} }}$Pt - Independent', 'Ir_189Pt_i', maxCs = 600, show=showFlag, save=saveFlag)

def Ir188Pt_independent():
    productZ='78'; productA='188'; isomerLevel=None; reaction='Ir_188Pt'; isomerState=None; targetFoil='Ir'; nuclearState=None
    independent=True; threshold=26
    Tendl(natIr).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(natIr, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(natIr, cohFilePath).plotCoh(productZ, productA, reaction, isomerState)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
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
    productZ='29'; productA='64'; isomerLevel=None; reaction='Cu_64Cu'; isomerState=None; targetFoil='Cu'; nuclearState=None
    independent=True; threshold=3; foilDict=natCu
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    cupper.plotCrossSectionWithLeftRightUncertainty("Cu_64Cu_independent")
    generate.plotExcitationFunction(r'$^{nat}$Cu(d,x)$^{{ {64} }}$Cu - independent', 'Cu_64Cu_i', maxCs = 450, show=showFlag, save=saveFlag)    

def Cu65Ni_independent():
    # cupper.collectDataAndModels(
    #     reaction = 'Cu_65Ni', # 'Ir_193mPt'
    #     targetFoil = 'Cu',
    #     productZ = '28',
    #     productA = '65',
    #     isomerLevel = None, #'05', tot (tendl, talys)
    #     isomerState = None, #m, m2 (empire, coh)
    #     nuclearState = None, # groundState, isomer1, isomer2 (alice)
    #     feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
    #     branchingRatio = None, #1, 0.5 (empire, coh, alice)
    #     parentIsomerLevel = None,
    #     parentNuclearState = None,
    #     parentIsomerState = None,
    #     reactionParent = None,
    #     independent = True
    #     )
    # Coh has generated 65Ni as ground state and ismoer
    productZ='28'; productA='65'; isomerLevel=None; reaction='Cu_65Ni'; isomerState=None; targetFoil='Cu'; nuclearState=None
    independent=True; threshold=10; foilDict=natCu
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    cupper.plotCrossSectionWithLeftRightUncertainty("Cu_65Ni_independent")
    generate.plotExcitationFunction(r'$^{nat}$Cu(d,x)$^{{ {65} }}$Ni - independent', 'Cu_65Ni_i', maxCs = 7, show=showFlag, save=saveFlag)    

def Fe56Co_independent():
    # iron.collectDataAndModels(
    #     reaction = 'Fe_56Co', # 'Ir_193mPt'
    #     targetFoil = 'Fe',
    #     productZ = '27',
    #     productA = '56',
    #     isomerLevel = None, #'05', tot (tendl, talys)
    #     isomerState = None, #m, m2 (empire, coh)
    #     nuclearState = None, # groundState, isomer1, isomer2 (alice)
    #     feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
    #     branchingRatio = None, #1, 0.5 (empire, coh, alice)
    #     parentIsomerLevel = None,
    #     parentNuclearState = None,
    #     parentIsomerState = None,
    #     reactionParent = None,
    #     independent = True
    #     )
    productZ='27'; productA='56'; isomerLevel=None; reaction='Fe_56Co'; isomerState=None; targetFoil='Fe'; nuclearState=None
    independent=True; threshold=6; foilDict=natFe
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=6)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    iron.plotMonitorCrossSections("fed56cot")
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_56Co_independent")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {56} }}$Co - independent', 'Fe_56Co_i', maxCs = None, show=showFlag, save=saveFlag)

def Fe57Co_independent():
    # iron.collectDataAndModels(
    #     reaction = 'Fe_57Co', # 'Ir_193mPt'
    #     targetFoil = 'Fe',
    #     productZ = '27',
    #     productA = '57',
    #     isomerLevel = None, #'05', tot (tendl, talys)
    #     isomerState = None, #m, m2 (empire, coh)
    #     nuclearState = None, # groundState, isomer1, isomer2 (alice)
    #     feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
    #     branchingRatio = None, #1, 0.5 (empire, coh, alice)
    #     parentIsomerLevel = None,
    #     parentNuclearState = None,
    #     parentIsomerState = None,
    #     reactionParent = None,
    #     independent = True
    #     )
    productZ='27'; productA='57'; isomerLevel=None; reaction='Fe_57Co'; isomerState=None; targetFoil='Fe'; nuclearState=None
    independent=True; threshold=3; foilDict=natFe
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_57Co_independent")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {57} }}$Co - independent', 'Fe_57Co_i', maxCs = None, show=showFlag, save=saveFlag)

def Fe55Co_independent():
    # iron.collectDataAndModels(
    #     reaction = 'Fe_55Co', # 'Ir_193mPt'
    #     targetFoil = 'Fe',
    #     productZ = '27',
    #     productA = '55',
    #     isomerLevel = None, #'05', tot (tendl, talys)
    #     isomerState = None, #m, m2 (empire, coh)
    #     nuclearState = None, # groundState, isomer1, isomer2 (alice)
    #     feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
    #     branchingRatio = None, #1, 0.5 (empire, coh, alice)
    #     parentIsomerLevel = None,
    #     parentNuclearState = None,
    #     parentIsomerState = None,
    #     reactionParent = None,
    #     independent = True
    #     )
    productZ='27'; productA='55'; isomerLevel=None; reaction='Fe_55Co'; isomerState=None; targetFoil='Fe'; nuclearState=None
    independent=True; threshold=3; foilDict=natFe
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_55Co_independent")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {55} }}$Co - independent', 'Fe_55Co_i', maxCs = None, show=showFlag, save=saveFlag)

def Fe59Fe_independent():
    productZ='26'; productA='59'; isomerLevel=None; reaction='Fe_59Fe'; isomerState=None; targetFoil='Fe'; nuclearState=None
    independent=True; threshold=3; foilDict=natFe
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_59Fe_independent")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {59} }}$Fe - independent', 'Fe_59Fe_i', maxCs = None, show=showFlag, save=saveFlag)

def Fe54Mn_independent():
    # iron.collectDataAndModels(
    #     reaction = 'Fe_54Mn', # 'Ir_193mPt'
    #     targetFoil = 'Fe',
    #     productZ = '25',
    #     productA = '54',
    #     isomerLevel = None, #'05', tot (tendl, talys)
    #     isomerState = None, #m, m2 (empire, coh)
    #     nuclearState = None, # groundState, isomer1, isomer2 (alice)
    #     feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
    #     branchingRatio = None, #1, 0.5 (empire, coh, alice)
    #     parentIsomerLevel = None,
    #     parentNuclearState = None,
    #     parentIsomerState = None,
    #     reactionParent = None,
    #     independent = True
    #     )
    productZ='25'; productA='54'; isomerLevel=None; reaction='Fe_54Mn'; isomerState=None; targetFoil='Fe'; nuclearState=None
    independent=True; threshold=3; foilDict=natFe
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
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

def Ni61Cu_independent(): ### There are no measured cross sections for Ni_61Cu. Why?
    productZ='29'; productA='61'; isomerLevel=None; reaction='Ni_61Cu'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=True; threshold=3
    # Tendl(natNi).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(natNi, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(natNi, cohFilePath).plotCoh(productZ, productA, reaction, isomerState)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    # nickel.collectCrossSections("Ni_61Cu")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {61} }}$Cu - independent', 'Ni_61Cu_i', maxCs = None, show=showFlag, save=saveFlag)

def Ni60Cu_independent():
    # nickel.collectDataAndModels(
    #     reaction = 'Ni_60Cu', # 'Ir_193mPt'
    #     targetFoil = 'Ni',
    #     productZ = '29',
    #     productA = '60',
    #     isomerLevel = None, #'05', tot (tendl, talys)
    #     isomerState = None, #m, m2 (empire, coh)
    #     nuclearState = None, # groundState, isomer1, isomer2 (alice)
    #     feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
    #     branchingRatio = None, #1, 0.5 (empire, coh, alice)
    #     parentIsomerLevel = None,
    #     parentNuclearState = None,
    #     parentIsomerState = None,
    #     reactionParent = None,
    #     independent = True
    #     )
    productZ='29'; productA='60'; isomerLevel=None; reaction='Ni_60Cu'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=True; threshold=8; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    nickel.collectCrossSections("Ni_60Cu")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {60} }}$Cu - independent', 'Ni_60Cu_i', maxCs = None, show=showFlag, save=saveFlag)

def Ni65Ni_independent():
    # nickel.collectDataAndModels(
    #     reaction = 'Ni_65Ni', # 'Ir_193mPt'
    #     targetFoil = 'Ni',
    #     productZ = '28',
    #     productA = '65',
    #     isomerLevel = None, #'05', tot (tendl, talys)
    #     isomerState = None, #m, m2 (empire, coh)
    #     nuclearState = None, # groundState, isomer1, isomer2 (alice)
    #     feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
    #     branchingRatio = None, #1, 0.5 (empire, coh, alice)
    #     parentIsomerLevel = None,
    #     parentNuclearState = None,
    #     parentIsomerState = None,
    #     reactionParent = None,
    #     independent = True
    #     )
    productZ='28'; productA='65'; isomerLevel=None; reaction='Ni_65Ni'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=True; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    nickel.collectCrossSections("Ni_65Ni")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {65} }}$Ni - independent', 'Ni_65Ni_i', maxCs = None, show=showFlag, save=saveFlag)

def Ni54Mn_independent():
    # nickel.collectDataAndModels(
    #     reaction = 'Ni_54Mn', # 'Ir_193mPt'
    #     targetFoil = 'Ni',
    #     productZ = '25',
    #     productA = '54',
    #     isomerLevel = None, #'05', tot (tendl, talys)
    #     isomerState = None, #m, m2 (empire, coh)
    #     nuclearState = None, # groundState, isomer1, isomer2 (alice)
    #     feeding = None, #beta+, beta-, isomer (empire only) (empire, coh, alice))
    #     branchingRatio = None, #1, 0.5 (empire, coh, alice)
    #     parentIsomerLevel = None,
    #     parentNuclearState = None,
    #     parentIsomerState = None,
    #     reactionParent = None,
    #     independent = True
    #     )
    productZ='25'; productA='54'; isomerLevel=None; reaction='Ni_54Mn'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=True; threshold=11; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    # nickel.plotCrossSectionWithLeftRightUncertainty("Ni_61Cu_independent")
    nickel.collectCrossSections("Ni_54Mn")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {54} }}$Mn - independent', 'Ni_54Mn_i', maxCs = None, show=showFlag, save=saveFlag)

def Ni58mCo_independent():
    productZ='27'; productA='58'; isomerLevel= '01'; reaction='Ni_58mCo'; isomerState='m'; targetFoil='Ni'; nuclearState='isomer1'
    independent=True; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    nickel.plotCrossSectionWithLeftRightUncertainty("Ni_58mCo_independent")
    # nickel.plotCrossSectionWithLeftRightUncertainty("Ni_58Co_independent")
    # nickel.collectCrossSections("Ni_58Co_cumulative")
    # nickel.collectCrossSections("Ni_58mCo_independent")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {58m} }}$Co - independent', 'Ni_58mCo_i', maxCs = None, show=showFlag, save=saveFlag)

def Ni58Co_independent():
    productZ='27'; productA='58'; isomerLevel= '00'; reaction='Ni_58Co'; isomerState='g'; targetFoil='Ni'; nuclearState='groundState'
    independent=True; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    nickel.plotCrossSectionWithLeftRightUncertainty("Ni_58Co_independent")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {58} }}$Co - independent', 'Ni_58Co_i', maxCs = None, show=showFlag, save=saveFlag)

def Ni58Co_cumulative():
    productZ='27'; productA='58'; isomerLevel= None; reaction='Ni_58Co'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=False; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_58Co_independent", label='groundstate', color='deeppink')
    nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_58mCo_independent", label=r'isomer ($IT: 99.9988\%$)', color='forestgreen')
    nickel.collectCrossSections("Ni_58Co_cumulative", label='total')
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {58} }}$Co - cumulative', 'Ni_58Co_c', maxCs = None, show=showFlag, save=saveFlag)

def Ni57Co_independent():
    productZ='27'; productA='57'; isomerLevel= None; reaction='Ni_57Co'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=True; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    nickel.plotCrossSectionWithLeftRightUncertainty("Ni_57Co_cumulative", label='Cumulative', color='deeppink')
    nickel.plotComparableCrossSection('Ni_57Ni', label=r'$^{57}$Ni ($\epsilon: 100\%$)', color='darkgreen')
    nickel.collectCrossSections("Ni_57Co_independent", label=r'Subtracted feeding $^{57}$Ni')
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {57} }}$Co - independent', 'Ni_57Co_i', maxCs = None, show=showFlag, save=saveFlag)

def Ni57Co_cumulative():
    productZ='27'; productA='57'; isomerLevel= None; reaction='Ni_57Co'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=False; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    # nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_57Co_independent", label='Independent', color='deeppink')
    # nickel.collectCrossSections("Ni_57Co_independent", label='Independent')
    # nickel.plotComparableCrossSection('Ni_57Ni', label=r'$^{57}$Ni ($\epsilon: 100\%$)', color='darkgreen')
    nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_57Co_cumulative", label='Cumulative')#, color='deeppink')
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {57} }}$Co - cumulative', 'Ni_57Co_c', maxCs = None, show=showFlag, save=saveFlag)

def Ni56Co_independent():
    productZ='27'; productA='56'; isomerLevel= None; reaction='Ni_56Co'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=True; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    nickel.plotComparableCrossSection("Ni_56Co", label='Cumulative', color='deeppink')
    nickel.plotComparableCrossSection('Ni_56Ni', label=r'$^{56}$Ni ($\epsilon: 100\%$)', color='darkgreen')
    nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_56Co_independent", label=r'Subtracted feeding $^{56}$Ni')#, color='deeppink')
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {56} }}$Co - independent', 'Ni_56Co_i', maxCs = None, show=showFlag, save=saveFlag)

def Ni56Co_cumulative():
    productZ='27'; productA='56'; isomerLevel= None; reaction='Ni_56Co'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=False; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    # nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_57Co_independent", label='Independent', color='deeppink')
    nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_56Co_independent", label='independent', color='deeppink')
    nickel.plotComparableCrossSection('Ni_56Ni', label=r'$^{56}$Ni ($\epsilon: 100\%$)', color='darkgreen')
    nickel.collectCrossSections("Ni_56Co", label='Cumulative')
    # nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_56Co_cumulative", label='Cumulative', color='deeppink')
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {56} }}$Co - cumulative', 'Ni_56Co_c', maxCs = None, show=showFlag, save=saveFlag)

def Ni55Co_cumulative():
    productZ='27'; productA='55'; isomerLevel= None; reaction='Ni_55Co'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=False; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_55Co_cumulative")#, label='Cumulative', color='deeppink')
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {55} }}$Co - cumulative', 'Ni_56Co_c', maxCs = None, show=showFlag, save=saveFlag)

def Ni59Fe_cumulative():
    productZ='26'; productA='59'; isomerLevel= None; reaction='Ni_59Fe'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=False; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_59Fe_cumulative")#, label='Cumulative', color='deeppink')
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {59} }}$Fe - cumulative', 'Ni_59Fe_c', maxCs = None, show=showFlag, save=saveFlag)

def Ni56Mn_cumulative():
    productZ='25'; productA='55'; isomerLevel= None; reaction='Ni_56Mn'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=False; threshold=3; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    # nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_56Mn_independent", label='Independent', color='deeppink')
    nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_56Mn_cumulative") #, label='Cumulative', color='darkred')
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {56} }}$Mn - cumulative', 'Ni_56Mn_c', maxCs = None, show=showFlag, save=saveFlag)

def Ni52Mn_cumulative():
    productZ='25'; productA='52'; isomerLevel= None; reaction='Ni_52Mn'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=False; threshold=None; foilDict=natNi
    Tendl(foilDict).plotTendl23(productZ, productA, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Empire(foilDict, empireFilePath).plotEmpire(productZ, productA, reaction, isomerState, threshold)# , feeding, parentIsomerState, branchingRatio, reactionParent)
    Talys(talysFilePath).plotTalys(productZ, productA, targetFoil, isomerLevel)#, feeding, branchingRatio, parentIsomerLevel)
    Coh(foilDict, cohFilePath).plotCoh(productZ, productA, reaction, isomerState, threshold=None)
    Alice(aliceFilePath).plotAlice(productZ, productA, targetFoil, nuclearState, threshold)#, feeding, branchingRatio, parentNuclearState)
    Exfor(exforFilePath).plotExforData(reaction, independent)
    # nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_56Mn_independent", label='Independent', color='deeppink')
    nickel.plotCrossSectionWithLeftRightUncertainty(reaction="Ni_52Mn_cumulative") #, label='Cumulative', color='darkred')
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {52} }}$Mn - cumulative', 'Ni_52Mn_c', maxCs = None, show=showFlag, save=saveFlag)

### Multiple feeding


def Ir189Ir_cumulative():
    # Coh is for short lived isomer and ground state + betaFeeding,  manual plot:
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '189', 'Ir_189Ir', isomerState='g', betaPlusDecayChain={"189Pt": ['78', 1.0, None, 'Ir_189Pt']}, betaMinusDecayChain=None, isomerDecayChain={"189mIr": [1.0, 'm', 'Ir_189mIr']})
    Empire(natIr, empireFilePath).plotdataWithMultipleFeeding('77', '189', 'Ir_189Ir', isomerState=None, betaPlusDecayChain={"189Pt": ['78', 1.0, None, 'Ir_189Pt']}, betaMinusDecayChain=None, isomerDecayChain=None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='189', targetFoil='Ir', nuclearState = None, betaPlusDecayChain={"189Pt": ['78', 1.0, None]}, betaMinusDecayChain=None, isomerDecayChain=None, threshold=None)
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
    threshold = 28
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '188', 'Ir_188Ir', isomerState=None, betaPlusDecayChain={"188Pt": ['78', br, None, 'Ir_188Pt']}, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(natIr, empireFilePath).plotdataWithMultipleFeeding('77', '188', 'Ir_188Ir', isomerState=None, betaPlusDecayChain={"188Pt": ['78', br, None, 'Ir_188Pt']}, betaMinusDecayChain=None, isomerDecayChain=None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='188', targetFoil='Ir', nuclearState = None, betaPlusDecayChain={"188Pt": ['78', br, None]}, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '188', isomerLevel = None, betaPlusDecayChain = {"188Pt": ['78', br, None]}, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='77', productA = '188', targetFoil = 'Ir', isomerLevel = None, betaPlusDecayChain = {"188Pt": ['78', br, None]}, betaMinusDecayChain = None, isomerDecayChain = None)
    Exfor(exforFilePath).plotExforData('Ir_188Ir', independent=False)
    iridium.collectCrossSections("Ir_188Ir")
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {188} }}$Ir - Cumulative', 'Ir_188Ir_c', maxCs = 12, show=showFlag, save=saveFlag)

def Ir188Ir_independent():
    Coh(natIr, cohFilePath).plotdataWithMultipleFeeding('77', '188', 'Ir_188Ir', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(natIr, empireFilePath).plotdataWithMultipleFeeding('77', '188', 'Ir_188Ir', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='77', productA='188', targetFoil='Ir', nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=25)
    Tendl(natIr).plotdataWithMultipleFeeding(productZ='77', productA = '188', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='77', productA = '188', targetFoil = 'Ir', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    iridium.plotComparableCrossSection('Ir_188Ir', label='Cumulative', color='darkgreen')
    iridium.plotComparableCrossSection('Ir_188Ir_independent', label='Independent', color='darkred')
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {188} }}$Ir - independent', 'Ir_188Ir_i', maxCs=6, show=showFlag, save=saveFlag)

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
    Exfor(exforFilePath).plotExforData('Ir_192Ir', independent=False)
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

def Ni64Cu_independent(): 
    Coh(natNi, cohFilePath).plotdataWithMultipleFeeding('29', '64', 'Ni_64Cu', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(natNi, empireFilePath).plotdataWithMultipleFeeding('29', '64', 'Ni_64Cu', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Tendl(natNi).plotdataWithMultipleFeeding(productZ='29', productA = '64', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='29', productA = '64', targetFoil = 'Ni', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='29', productA='64', targetFoil='Ni', nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Exfor(exforFilePath).plotExforData('Ni_64Cu', independent=True)
    nickel.collectCrossSections("Ni_64Cu")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {64} }}$Cu - Independent', 'Ni_64Cu_i', maxCs = None, show=showFlag, save=saveFlag)


def Fe58Co_cumulative():
    productZ='27'; productA='58'; isomerLevel=None; reaction='Fe_58Co'; isomerState=None; targetFoil='Fe'; nuclearState=None
    independent=False; threshold=3; foilDict=natFe
    Coh(foilDict, cohFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(foilDict, empireFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Tendl(foilDict).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, targetFoil = targetFoil, isomerLevel = isomerLevel, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ=productZ, productA=productA, targetFoil=targetFoil, nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Exfor(exforFilePath).plotExforData('Fe_58Co', independent=False)
    iron.collectCrossSections("Fe_58Co")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {58} }}$Co - Cumulative', 'Fe_58Co_c', maxCs = None, show=showFlag, save=saveFlag)

def Fe56Mn_cumulative():
    productZ='25'; productA='56'; isomerLevel=None; reaction='Fe_56Mn'; isomerState=None; targetFoil='Fe'; nuclearState=None
    independent=False; threshold=None; foilDict=natFe
    # betaMinusDecayChain= {'56Cr': []} 
    Coh(foilDict, cohFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(foilDict, empireFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Tendl(foilDict).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, targetFoil = targetFoil, isomerLevel = isomerLevel, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ=productZ, productA=productA, targetFoil=targetFoil, nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Exfor(exforFilePath).plotExforData('Fe_56Mn', independent=False)
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_56Mn_cumulative")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {56} }}$Mn - Cumulative', 'Fe_56Mn_c', maxCs = None, show=showFlag, save=saveFlag)

def Fe52Mn_cumulative():
    productZ='25'; productA='52'; isomerLevel=None; reaction='Fe_52Mn'; isomerState=None; targetFoil='Fe'; nuclearState=None
    independent=False; threshold=3; foilDict=natFe
    # betaplusDecayChain_alice = {'52Co': ['27', 1.0, None], '52Fe': {'26', 1.0, None}} # Z, BR, nuclearState
    betaPlusDecayChain_tendlys = {'52Co': ['27', 1.0, None], '52Fe': ['26', 1.0, None]} # Z, BR, isomerState
    betaPlusDecayChain_coh = {'52Co': ['27', 1.0, None, 'Fe_52Co'], '52Fe': ['26', 1.0, None, 'Fe_52Fe']}  # Z, BR, isomerState (G, M etc), reaction
    isomerDecayChain_coh = {0.0178, 'm', 'Fe_52mMn'} # BR, isomerState, reaction 
    # betaPlusDecayChain_empire = {'52Co': ['27', 1.0, None], '52Fe': ['26', 1.0, None]} # Z, BR, state

    Coh(foilDict, cohFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState='g', betaPlusDecayChain=betaPlusDecayChain_coh, betaMinusDecayChain=None, isomerDecayChain=isomerDecayChain_coh)
    Empire(foilDict, empireFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Tendl(foilDict).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, isomerLevel = None, betaPlusDecayChain = betaPlusDecayChain_tendlys, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, targetFoil = targetFoil, isomerLevel = isomerLevel, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ=productZ, productA=productA, targetFoil=targetFoil, nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Exfor(exforFilePath).plotExforData('Fe_52Mn', independent=False)
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_52Mn_cumulative")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {52} }}$Mn - Cumulative', 'Fe_52Mn_c', maxCs = None, show=showFlag, save=saveFlag)

def Fe51Cr_cumulative():
    productZ='24'; productA='51'; isomerLevel=None; reaction='Fe_51Cr'; isomerState=None; targetFoil='Fe'; nuclearState=None
    independent=False; threshold=3; foilDict=natFe
    # betaplusDecayChain_alice = {'52Co': ['27', 1.0, None], '52Fe': {'26', 1.0, None}} # Z, BR, nuclearState
    # betaPlusDecayChain_tendlys = {'51Co': ['27', 1.0, None], '51Fe': ['26', 1.0, None], '51Mn': ['25', 1.0, None]} # Z, BR, isomerState
    betaPlusDecayChain_coh = {'52Co': ['27', 1.0, None, 'Fe_52Co'], '52Fe': ['26', 1.0, None, 'Fe_52Fe']}  # Z, BR, isomerState (G, M etc), reaction
    isomerDecayChain_coh = {0.0178, 'm', 'Fe_52mMn'} # BR, isomerState, reaction 
    # betaPlusDecayChain_empire = {'52Co': ['27', 1.0, None], '52Fe': ['26', 1.0, None]} # Z, BR, state

    Coh(foilDict, cohFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(foilDict, empireFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Tendl(foilDict).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, targetFoil = targetFoil, isomerLevel = isomerLevel, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ=productZ, productA=productA, targetFoil=targetFoil, nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Exfor(exforFilePath).plotExforData('Fe_51Cr', independent=False)
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_51Cr_cumulative")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {51} }}$Cr - Cumulative', 'Fe_52Cr_c', maxCs = 25, show=showFlag, save=saveFlag)

def Fe48V_cumulative():
    productZ='23'; productA='48'; isomerLevel=None; reaction='Fe_48V'; isomerState=None; targetFoil='Fe'; nuclearState=None
    independent=False; threshold=3; foilDict=natFe

    Coh(foilDict, cohFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(foilDict, empireFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Tendl(foilDict).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, targetFoil = targetFoil, isomerLevel = isomerLevel, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ=productZ, productA=productA, targetFoil=targetFoil, nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Exfor(exforFilePath).plotExforData('Fe_48V', independent=False)
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_48V_cumulative")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {48} }}$V - Cumulative', 'Fe_48V_c', maxCs = None, show=showFlag, save=saveFlag)

def Fe53Fe_cumulative():
    productZ='26'; productA='53'; isomerLevel=None; reaction='Fe_53Fe'; isomerState=None; targetFoil='Fe'; nuclearState=None
    independent=False; threshold=3; foilDict=natFe

    Coh(foilDict, cohFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(foilDict, empireFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Tendl(foilDict).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, targetFoil = targetFoil, isomerLevel = isomerLevel, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ=productZ, productA=productA, targetFoil=targetFoil, nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Exfor(exforFilePath).plotExforData('Fe_53Fe', independent=False)
    iron.plotCrossSectionWithLeftRightUncertainty("Fe_53Fe_cumulative")
    generate.plotExcitationFunction(r'$^{nat}$Fe(d,x)$^{{ {53} }}$Fe - Cumulative', 'Fe_53Fe_c', maxCs = None, show=showFlag, save=saveFlag)


def Ni57Ni_cumulative():
    productZ='28'; productA='57'; isomerLevel=None; reaction='Ni_57Ni'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=False; threshold=10; foilDict=natNi
    betaplusDecayChain_alice = {'57Cu': ['29', 1.0, None]} # Z, BR, nuclearState
    betaPlusDecayChain_tendlys = {'57Cu': ['29', 1.0, None]} # Z, BR, isomerState
    betaPlusDecayChain_coh = {'57Cu': ['29', 1.0, None, 'Ni_57Cu']} # Z, BR, isomerState (G, M etc), reaction
    betaPlusDecayChain_empire = {'57Cu': ['29', 1.0, None]} # Z, BR, state

    Coh(foilDict, cohFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=betaPlusDecayChain_coh, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(foilDict, empireFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Tendl(foilDict).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, isomerLevel = None, betaPlusDecayChain = betaPlusDecayChain_tendlys, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, targetFoil = targetFoil, isomerLevel = isomerLevel, betaPlusDecayChain = betaPlusDecayChain_tendlys, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ=productZ, productA=productA, targetFoil=targetFoil, nuclearState = None, betaPlusDecayChain=betaplusDecayChain_alice, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Exfor(exforFilePath).plotExforData('Ni_57Ni', independent=False)
    nickel.plotCrossSectionWithLeftRightUncertainty("Ni_57Ni_cumulative")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {57} }}$Ni - Cumulative', 'Ni_57Ni_c', maxCs = None, show=showFlag, save=saveFlag)

def Ni56Ni_cumulative():
    productZ='28'; productA='56'; isomerLevel=None; reaction='Ni_56Ni'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=False; threshold=None; foilDict=natNi
    betaplusDecayChain_alice =  None #{'56Cu': ['29', 1.0, None]} # Z, BR, nuclearState
    betaPlusDecayChain_tendlys = None #{'56Cu': ['29', 1.0, None]} # Z, BR, isomerState
    betaPlusDecayChain_coh = None # {'56Cu': ['29', 1.0, None, 'Ni_56Cu']} # Z, BR, isomerState (G, M etc), reaction
    betaPlusDecayChain_empire = None # {'56Cu': ['29', 1.0, None]} # Z, BR, state
    Coh(foilDict, cohFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=betaPlusDecayChain_coh, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(foilDict, empireFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Tendl(foilDict).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, isomerLevel = None, betaPlusDecayChain = betaPlusDecayChain_tendlys, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, targetFoil = targetFoil, isomerLevel = isomerLevel, betaPlusDecayChain = betaPlusDecayChain_tendlys, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ=productZ, productA=productA, targetFoil=targetFoil, nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Exfor(exforFilePath).plotExforData('Ni_56Ni', independent=False)
    nickel.plotCrossSectionWithLeftRightUncertainty("Ni_56Ni_cumulative")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {56} }}$Ni - Cumulative', 'Ni_56Ni_c', maxCs = 4, show=showFlag, save=saveFlag)

def Ni60Co_cumulative():
    productZ='27'; productA='60'; isomerLevel=None; reaction='Ni_60Co'; isomerState=None; targetFoil='Ni'; nuclearState=None
    independent=False; threshold=3; foilDict=natNi
    betaplusDecayChain_alice =  None #{'56Cu': ['29', 1.0, None]} # Z, BR, nuclearState
    betaPlusDecayChain_tendlys = None #{'56Cu': ['29', 1.0, None]} # Z, BR, isomerState
    betaPlusDecayChain_coh = None # {'56Cu': ['29', 1.0, None, 'Ni_56Cu']} # Z, BR, isomerState (G, M etc), reaction
    betaPlusDecayChain_empire = None # {'56Cu': ['29', 1.0, None]} # Z, BR, state
    Coh(foilDict, cohFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=betaPlusDecayChain_coh, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(foilDict, empireFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Tendl(foilDict).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, isomerLevel = None, betaPlusDecayChain = betaPlusDecayChain_tendlys, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, targetFoil = targetFoil, isomerLevel = isomerLevel, betaPlusDecayChain = betaPlusDecayChain_tendlys, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ=productZ, productA=productA, targetFoil=targetFoil, nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None, threshold=threshold)
    Exfor(exforFilePath).plotExforData('Ni_60Co', independent=False)
    nickel.plotCrossSectionWithLeftRightUncertainty("Ni_60Co_cumulative")
    generate.plotExcitationFunction(r'$^{nat}$Ni(d,x)$^{{ {60} }}$Co - Cumulative', 'Ni_60Co_c', maxCs = 40, show=showFlag, save=saveFlag)

#MULTIPLE STEP FEEDING:
def Cu61Cu_cumulative():
    # betaPlus = {"189Pt": ['78', 1.0, None, 'Ir_189Pt']}
    # {"61Zn": ['30', 1.0, None, 'Cu_61Zu']}
    Coh(natCu, cohFilePath).plotdataWithMultipleFeeding('29', '61', 'Cu_61Cu', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(natCu, empireFilePath).plotdataWithMultipleFeeding('29', '61', 'Cu_61Cu', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Tendl(natCu).plotdataWithMultipleFeeding(productZ='29', productA = '61', isomerLevel = None, betaPlusDecayChain = {"61Zn": ['30', 1.0, None]}, betaMinusDecayChain = None, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='29', productA = '61', targetFoil = 'Cu', isomerLevel = None, betaPlusDecayChain = {"61Zn": ['30', 1.0, None]}, betaMinusDecayChain = None, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='29', productA='61', targetFoil='Cu', nuclearState = None, betaPlusDecayChain={"61Zn": ['30', 1.0, None]}, betaMinusDecayChain=None, isomerDecayChain=None, threshold=20)
    Exfor(exforFilePath).plotExforData('Cu_61Cu', independent=False)
    cupper.collectCrossSections("Cu_61Cu")
    generate.plotExcitationFunction(r'$^{nat}$Cu(d,x)$^{{ {61} }}$Cu - Cumulative', 'Cu_61Cu_c', maxCs = None, show=showFlag, save=saveFlag)

def Cu61Co_cumulative(): # Removed beta minus decay chain from alice.
    #betaMinusDecayChain: # Z, branching, isomerState, nuclear state,
    betaMinusDecayChain = {'61Fe': ['26', 1.0, None]}
    # Coh(natCu, cohFilePath).plotdataWithMultipleFeeding('27', '61', 'Cu_61Co', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain={'61Fe': ['26', 1.0, None, 'Cu_61Fe']}, isomerDecayChain=None)
    Coh(natCu, cohFilePath).plotdataWithMultipleFeeding('27', '61', 'Cu_61Co', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(natCu, empireFilePath).plotdataWithMultipleFeeding('27', '61', 'Cu_61Co', isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain={'61Fe': ['26', 1.0, None, 'Cu_61Fe']}, isomerDecayChain=None)
    Tendl(natCu).plotdataWithMultipleFeeding(productZ='27', productA = '61', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = betaMinusDecayChain, isomerDecayChain = None)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ='27', productA = '61', targetFoil = 'Cu', isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = betaMinusDecayChain, isomerDecayChain = None)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ='27', productA='61', targetFoil='Cu', nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Exfor(exforFilePath).plotExforData('Cu_61Co', independent=False)
    cupper.collectCrossSections("Cu_61Co")
    generate.plotExcitationFunction(r'$^{nat}$Cu(d,x)$^{{ {61} }}$Co - Cumulative', 'Cu_61Co_c', maxCs = None, show=showFlag, save=saveFlag)

def Cu60Co_cumulative(): # only feeding from isomer
    #isomer decay chain: {isotope: [branchingRatio isomerLevel]} #isomer talys, tendl
    isomerDecayChain = {'60mCo': [0.9975, '01']}
    # {isotope: [branchingRatio, nuclearState]} isomer # alice
    # isomerDecayChainAlice = {'60mCo': [0.9975, '01']}
    productZ='27'; productA='60'; isomerLevel='00'; reaction='Cu_60Co'; isomerState=None; targetFoil='Cu'; nuclearState=None
    independent=False; threshold=2; foilDict=natCu
    
    Coh(natCu, cohFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Empire(natCu, empireFilePath).plotdataWithMultipleFeeding(productZ, productA, reaction, isomerState=None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Tendl(natCu).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, isomerLevel = None, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = isomerDecayChain)
    Talys(talysFilePath).plotdataWithMultipleFeeding(productZ=productZ, productA = productA, targetFoil = targetFoil, isomerLevel = isomerLevel, betaPlusDecayChain = None, betaMinusDecayChain = None, isomerDecayChain = isomerDecayChain)
    Alice(aliceFilePath).plotAliceWithFeeding(productZ=productZ, productA=productA, targetFoil=targetFoil, nuclearState = None, betaPlusDecayChain=None, betaMinusDecayChain=None, isomerDecayChain=None)
    Exfor(exforFilePath).plotExforData('Cu_60Co', independent=False)
    cupper.collectCrossSections("Cu_60Co")
    generate.plotExcitationFunction(r'$^{nat}$Cu(d,x)$^{{ {60} }}$Co - Cumulative', 'Cu_60Co_c', maxCs = None, show=showFlag, save=saveFlag)