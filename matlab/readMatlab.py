import scipy.io
import os
import pandas as pd
# import nuclearanalysistools as nat
# from nuclearanalysistools import findGammas
from nuclearanalysistools.findGammas import AnalyzeGammas
import numpy as np


mat_data = scipy.io.loadmat('fe_mat.mat')
fe_mat = mat_data['fe_mat']
pathToFiles = os.getcwd() + '/fitz_reports3/' 
file_glines = 'fe_glines.mat'
file_key_energies = 'fe_key_energies.mat'
fe_glines = scipy.io.loadmat(pathToFiles + file_glines)['fe_glines']
fe_key_energies = scipy.io.loadmat(pathToFiles + file_key_energies)['fe_key_energies']

ni_glines = scipy.io.loadmat(pathToFiles + 'ni_glines.mat')['ni_glines']
ni_key_energies = scipy.io.loadmat(pathToFiles + 'ni_key_energies.mat')['ni_key_energies']

cu_glines = scipy.io.loadmat(pathToFiles + 'cu_glines.mat')['cu_glines']
cu_key_energies = scipy.io.loadmat(pathToFiles + 'cu_key_energies.mat')['cu_key_energies']

ir_glines = scipy.io.loadmat(pathToFiles + 'ir_glines.mat')['ir_glines']
ir_key_energies = scipy.io.loadmat(pathToFiles + 'ir_key_energies.mat')['ir_key_energies']


def createDataframe(matrix, columnNames = None):
    rows = []
    for row in matrix:
        rows.append(row)
    data = pd.DataFrame(
                rows, columns=columnNames)
    return data

def saveCsv(dataframe, filename, directory=None):
    if directory==None:
        filename = os.getcwd() + '/' + filename + '.csv'
    else:
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = os.getcwd() + '/' + directory + '/' + filename + '.csv'
    dataframe.to_csv(filename, index=False)





listOfPossibleProductsNatFe= ['55CO', '56CO', '57CO', 'CO-58m', 'CO-58g', '60CO',
                            '61CO', '55FE', '59FE', 'FE-53m', 'FE-53g', '52FE',
                            '56MN', '54MN', '53MN', 'MN-52m', 'MN-52g', '51MN',
                            '56CR', '55CR', '51CR', '49CR', '48CR', '52V', '49V', '48V', '47V'
                            ]
listOfPossibleProductsNatNi = ['64CU', '62CU', '61CU', '60CU',
                            '65NI', '63NI', '59NI', '57NI', '56NI', 
                            '61CO', 'CO-60g', 'CO-60m', 'CO-58m', 'CO-58g', '57CO', '56CO', '55CO',
                            '61FE', '59FE', '55FE', 'FE-53m', 'FE-53g', '52FE',
                            '56MN', '54MN', '53MN', 'MN-52m', 'MN-52g', '51MN',
                            '56CR', '55CR', '51CR', '49CR', '48CR', '52V', '49V', '48V', '47V'
                            ]

listOfPossibleProductsNatCu = ['65ZN', '63ZN', '62ZN',
                            '66CU', '64CU', '62CU', '61CU', '60CU', 
                            '65NI', '63NI', '57NI', '56NI',
                            '61CO', 'CO-60m', 'CO-60g', 'CO-58m', 'CO-58g', '57CO', '56CO', '55CO',
                            '61FE', '59FE', '55FE', 'FE-53m', 'FE-53g', '52FE'
                            ]


listOfPossibleProductsNatIr = ['188IR', '189IR', 'IR-190m2', 'IR-190m1', 'IR-190g', '192IR', 'IR-194m2', 'IR-194g',
                            '188PT', '189PT', '191PT', 'PT-193m'
                            ]

fe = AnalyzeGammas(listOfPossibleProductsNatFe).findAllGammas()
ir = AnalyzeGammas(listOfPossibleProductsNatIr).findAllGammas()
# print(fe)

# saveCsv(data2, 'fe_glines', 'csv_2025')
# saveCsv(data3, 'fe_key_energies', 'csv_2025')
# fe = AnalyzeGammas(listOfPossibleProductsNatFe).findAllGammas()
# saveCsv(fe, 'fedata', 'csv_2025')


# ni_glines_df = createDataframe(ni_glines, columnNames = ['half life (s)', 'I (%)', 'dI'])
# saveCsv(ni_glines_df, 'ni_glines', 'csv_2025')
# ni = AnalyzeGammas(listOfPossibleProductsNatNi).findAllGammas()
# saveCsv(ni, 'nidata', 'csv_2025')



cu_glines_df = createDataframe(cu_glines, columnNames = ['half life (s)', 'I (%)', 'dI'])
# saveCsv(cu_glines_df, 'cu_glines', 'csv_2025')
# cu = AnalyzeGammas(listOfPossibleProductsNatCu).findAllGammas()
# saveCsv(cu, 'cudata', 'csv_2025')

ir_glines_df = createDataframe(ir_glines, columnNames = ['half life (s)', 'I (%)', 'dI'])
# saveCsv(ir_glines_df, 'ir_glines', 'csv_2025')
ir = AnalyzeGammas(listOfPossibleProductsNatIr).findAllGammas()
# saveCsv(ir, 'irdata', 'csv_2025')


def getIsotopeAndIntesities(gammas, glines):
    for i in range(len(gammas)):
        for j in range(len(glines)):
            if gammas['Half life (s)'][i] == glines['half life (s)'][j]:
                print(gammas['Isotope'][i], glines['I (%)'][j], glines['dI'][j])

getIsotopeAndIntesities(ir, ir_glines_df)


# print(AnalyzeGammas({}).findGammasSpecificIsotope('PT-193m'))




# keyEnergies = createDataframe(fe_key_energies, columnNames = ['E (keV)'])['E (keV)'].to_numpy()
# intensity = createDataframe(fe_glines, columnNames = ['half life (s)', 'I (%)', 'dI'])['I (%)'].to_numpy()
# dintensity = createDataframe(fe_glines, columnNames = ['half life (s)', 'I (%)', 'dI'])['dI'].to_numpy()
# halflives = createDataframe(fe_glines, columnNames = ['half life (s)', 'I (%)', 'dI'])['half life (s)'].to_numpy()

# row = []
# for i in range(len(E)):
#     if E[i] in keyEnergies:
#         print(E[i])


# rows = []
# for indx in range(len(ir)):
#     row = []
#     # print(ir['Isotope'][indx])
#     if ir['Energy'][indx] in ir_key_energies:
#         print(ir['Isotope'][indx], ir['Energy'][indx])



    # for i,e in enumerate(intensity):
    #     if fe['Half life (s)'][indx] in halflives:
    #         print(intensity[i], dintensity[i])
    #         fe['Isotope'][indx]


# print(AnalyzeGammas(listOfPossibleProductsNatFe).findGammasSpecificIsotope('48V'))
    #     print(fe['Half life (s)'][i], fe['Intensity'][i])
    #     I = fe['Intensity'][i]
    

    
    # print(halfLife[i])
    # fe['Half life (s)'][i]
    # index_glines = 
    # nndcDataRow = fe.loc[i, ['Isotope', 'Energy', 'Intensity', 'Half life (s)']].to_dict()


    # if 
    # if fe['Half life (s)'][i] in halflives:
    #     halflife = fe['Half life (s)'][i]
    #     isotope = fe['Isotope'][i]
    #     if fe['Energy'][i] in keyEnergies:
    #         keyEnergy = fe['Energy'][i]
    #     if fe['Intensity'][i] in intensity:
    #         index = np.where(intensity == fe['Intensity'][i])[0][0]
    #         keyIntensity = intensity[index]; dKeyIntensity = dintensity[index]
    #         thalf = halflives[index]
    #     rows.append([isotope,halflife,  thalf, keyEnergy, keyIntensity, dKeyIntensity])

# 48V 1312.106
# 1.16 0.09


# a = createDataframe(rows, [ 'E','Isotope', 'Half life (s)', 'I', 'dI'])
# saveCsv(a, 'matchedIntensityEnergy', 'csv_2025')
        





# saveCsv(data1, 'fe_mat', 'csv_2025')
# saveCsv(data2, 'fe_glines', 'csv_2025')
# saveCsv(data3, 'fe_key_energies', 'csv_2025')



