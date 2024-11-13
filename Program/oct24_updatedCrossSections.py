import numpy as np
import matplotlib.pyplot as plt
import os
import requests
from scipy.interpolate import splev, splrep
from collections import OrderedDict

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
dirUpdatedFigures = 'CrossSections/updatedExcitationFunctions'

natIr = {"Ir191": 0.373, "Ir193": 0.627}
natCu = {"Ir191": 0.373, "Ir193": 0.627}
natFe = {"Ir191": 0.373, "Ir193": 0.627}
natNi = {"Ir191": 0.373, "Ir193": 0.627}


generate = GenerateExcitationFunction(directoryFigs = dirUpdatedFigures)

iridium = AssembleExcitationFunctionForTarget(
crossSectionCsvPath = crossSectionCsvPath,
target = natIr,
empireFilePath = empireFilePath,
talysFilePath = talysFilePath,
cohFilePath = cohFilePath,
aliceFilePath = aliceFilePath)


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
        reactionParent = None
        )
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {193m} }}$Pt - Independent', 'Ir_193mPt_i', show=True, save=True)

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
        reactionParent = None
        )
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {189} }}$Pt - Independent', 'Ir_189Pt_i', show=True, save=True)

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
        reactionParent = 'Ir_188Pt'
        )
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {188} }}$Ir - Independent', 'Ir_188Ir_i', show=True, save=True)

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
        reactionParent = None
        )
    generate.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {188} }}$Pt - Independent', 'Ir_188Pt_i', show=False, save=True)

Ir188Pt_independent()
# excitationFunction = GenerateExcitationFunction(dirUpdatedFigures)
# crossSectionData = CrossSection(crossSectionCsvPath)
# tendl_natIr = Tendl(natIr)
# empire_natIr = Empire(natIr, empireFilePath)
# talys = Talys(talysFilePath)
# alice = Alice(alicePath)

# crossSectionData.plotCrossSection('Ir_189Pt')
# tendl_natIr.plotTendl23(productZ='78', productA='189', isomerLevel=None)
# empire_natIr.plotEmpire(productZ='78', productA='189', reaction = 'Ir_189Pt', isomerState=None)
# talys.plotTalys(productZ='78', productA='189', targetFoil='Ir', isomerLevel=None)
# plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {189} }}$Pt - Independent', "Ir_189Pt")

# crossSectionData.plotCrossSection('Ir_193mPt')
# tendl_natIr.plotTendl23(productZ='78', productA='193', isomerLevel='05')
# empire_natIr.plotEmpire(productZ='78', productA='193', reaction = 'Ir_193mPt', isomerState='m')
# talys.plotTalys(productZ='78', productA='193', targetFoil='Ir', isomerLevel='05')
# # coh_natIr.plotCoh(productZ = '78', productA='193', reaction='Ir_193mPt', isomerState = 'm')
# alice.plotAlice(productZ='78', productA='193', targetFoil='Ir', nuclearState='isomer1', betaFeeding = None, branchingRatio = None, parentNuclearState = None)
# excitationFunction.plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {193m} }}$Pt - Independent', "Ir_193mPt", show=True)
