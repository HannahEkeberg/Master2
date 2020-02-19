import os
import numpy as np
import csv
#import matplotlib.pyplot as plt


path = os.getcwd() +'/cleaned_zieglerfiles/'
files = []

#def ziegler():
names = []
files = []
with open(path + 'cleaned_files.txt', 'r') as fh:
    for line in fh.readlines():
        files.append(line[:-1])
        fh.close()

for f in files[:10]:
    ind_B = f.find('B')   #index where B info starts
    ind_D = f.find('f')-1   #index where D info ends
    #print(ind_B)
    #print(ind_D)
    name = f[ind_B:ind_D]
    #print("filename: ", f)
    #print("name: ", name)
    files.append(f)
    names.append(name)

print(names)
