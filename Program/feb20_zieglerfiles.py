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

#with open('ziegler_FilesNames.csv', 'w', newline='') as file:
#    writer = csv.writer(file)#
#    writer.writerow(['File', 'Name'])
#files = files[:10]
#csv_save_array= np.zeros((len(files), 2))
files_=[]
names_=[]


for f in files:
    #print(f)
    #print(csv_save_array[])
    ind = files.index(f)  # row of f in files

    ind_B = f.find('B')   #index where B info starts
    ind_D = f.find('f')-1   #index where D info ends
    #print(ind_B)
    #print(ind_D)
    n = f[ind_B:ind_D]

    #csv_save_array[ind,:] = np.array((str(f), str(n)), dtype='|S6')
    #files_[f] = f
    #names_[f] = n
    files_.append(f)
    names_.append(n)
    #csv_save_array[f,0]= 1



csv_save = np.vstack((files_, names_)).T
print(type(csv_save))


    #csv_save_array = np.array((files, names))
#print(csv_save_array)
    #print(csv_save_array)
    #print(f)
np.savetxt('ziegler_FilesNames.csv', csv_save, delimiter='|', header='Filename, Name', fmt="%s"  )#, %.6f, %.6f")
    #print(n)

    #print(name)

    #writer.writerow(['0','1'])
    #print("filename: ", f)
    #print("name: ", name)
    #files.append(f)
    #names.append(name)

#print(names)
