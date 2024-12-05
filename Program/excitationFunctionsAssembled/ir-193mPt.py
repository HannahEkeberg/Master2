import os
import sys

sys.path.append('../')

from oct24_updatedCrossSections import *

"""
Independent. Not subject to beta feeding
"""

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