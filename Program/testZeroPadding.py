from Alice import *
import matplotlib.pyplot as plt

aliceFilePath = os.getcwd() + '/../alice2020/'
E, Cs = Alice(aliceFilePath).aliceData(productZ = '29', productA = '61', targetFoil = 'Ni', nuclearState = 'total', threshold=3)

