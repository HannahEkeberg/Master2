
from generateExcitationFunction import *

crossSectionCsvPath = os.getcwd() + '/CrossSections/CrossSections_csv/'
empireFilePath = os.getcwd() + '/../EMPIRE/'
talysFilePath = os.getcwd() + '/../talys_v2.04/'
cohFilePath = os.getcwd() + '/../coh_v3.6.0/'
aliceFilePath = os.getcwd() + '/../alice2020/'
exforFilePath = os.getcwd() + '/../exfor2024/'
dirUpdatedFigures = 'CrossSections/updatedExcitationFunctions'

natIr = {"Ir191": 0.373, "Ir193": 0.627}
natNi = {"Ni58": 0.680769, "Ni60": 0.262231, "Ni61": 0.011399, "Ni62": 0.036345, "Ni64": 0.009256}


# #190Ir
# isomer2Feeding = ParentFeeding('isomer2', 0.086, '37', 'isomer2', 'm2', 'Ir_190m2Ir')
# isomer1Feeding = ParentFeeding('isomer1', 1.0, '02', 'isomer1', 'm1', 'Ir_190m1Ir')

# #56Co
# betaFeeding56Ni56Co = ParentFeeding('beta+', 1.0, None, None, None, None)

iridium = AssembleExcitationFunctionForTarget(
crossSectionCsvPath = crossSectionCsvPath,
target = natIr,
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

# iridium.collectDataAndModels(
#     'Ir_190mIr', # 'Ir_193mPt'
#     'Ir', # 'Ir'
#     '77',
#     '190',
#     isomerLevel = None, #'05', tot (tendl, talys)
#     isomerState = None, #m, m2 (empire, coh)
#     nuclearState = None, # groundState, isomer1, isomer2 (alice)    
#     feeding = [isomer2Feeding, isomer1Feeding],
#     independent = False # For exfor. If None --> independent == True
# )

# iridium.collectDataAndModels(
#     'Ir_190m1Ir', # 'Ir_193mPt'
#     'Ir', # 'Ir'
#     '77',
#     '190',
#     isomerLevel = '02', #'05', tot (tendl, talys)
#     isomerState = None, #m, m2 (empire, coh)
#     nuclearState = None, # groundState, isomer1, isomer2 (alice)    
#     feeding = [isomer2Feeding],
#     independent = False # For exfor. If None --> independent == True
# )

# iridium.collectDataAndModels(
#     'Ir_190m2Ir', # 'Ir_193mPt'
#     'Ir', # 'Ir'
#     '77',
#     '190',
#     isomerLevel = '35', #'05', tot (tendl, talys)
#     isomerState = None, #m, m2 (empire, coh)
#     nuclearState = None, # groundState, isomer1, isomer2 (alice)    
#     feeding = None,
#     independent = False # For exfor. If None --> independent == True
# )

nickel.collectDataAndModels(
    'Ni_56Co',
    'Ni',
    '27',
    '56',
    isomerLevel = None, #'05', tot (tendl, talys)
    isomerState = None, #m, m2 (empire, coh)
    nuclearState = None, # groundState, isomer1, isomer2 (alice)
    feeding = None,
    #feeding = [betaFeeding56Ni56Co],
    independent=False
)

# iridium.collectCrossSections('Ir_190Ir')
# iridium.collectCrossSections('Ir_190m2Ir')

nickel.collectCrossSections('Ni_56Co')
generate = GenerateExcitationFunction()
generate.plotExcitationFunction(show=True)