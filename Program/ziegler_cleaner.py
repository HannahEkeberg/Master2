import os
import numpy as np
import matplotlib.pyplot as plt

### Change path to ziegler filesself.
### All files should be listed in a .txt file
path = os.getcwd() +'/new_ziegler/'

### Creating a new folder for the cleaned
### files so the old will not be overwritten
dir_files = 'cleaned_zieglerfiles'
if not os.path.exists(dir_files):
    os.mkdir(dir_files)


files = []
with open(path + 'fnames.txt', 'r') as fh:
    for line in fh.readlines():
        files.append(line[:-1])
        fh.close()
for f in files:
    ziegler_foil = np.loadtxt(path + f, dtype="str", delimiter=",", usecols=[0], skiprows=1)
    foil = np.genfromtxt(path+f, dtype="str", delimiter=',', usecols=[0], skip_header=1)
    ziegler_E = np.genfromtxt(path + f, delimiter=',', usecols=[1], skip_header=1)
    ziegler_flux = np.genfromtxt(path + f, delimiter=',', usecols=[2], skip_header=1)

    print("filename", f)

    max_F = np.max(ziegler_flux)

    ### Separating the peaks by selecting upon lower and upper indices
    lower_index_edges = [0]
    upper_index_edges = []
    for i,e in enumerate(range(len(ziegler_E)-1)):
        if ziegler_E[i+1] < ziegler_E[i]:
            #print(i)
            lower_index_edges.append(i+1)
            upper_index_edges.append(i)

    upper_index_edges.append(i+1)  #adding last element of SS02

    E_csv = []; F_csv = []; name_csv = []

    ### Going through each peak
    for k in range(len(lower_index_edges)):
        ind1 = lower_index_edges[k]
        ind2 = upper_index_edges[k]+1

        numb_of_points = np.abs(ind1-ind2)

        foil_name = foil[ind1:ind2]
        F = ziegler_flux[ind1:ind2]
        E = ziegler_E[ind1:ind2]
        ind_maxF = np.argmax(F)


        for i in range(len(E)-2):

            #print(ind_maxF)
            if ind_maxF==0:
                ind_maxF=20

            ### Setting values in the lower energy range that is higher than the [i+1] peak to zero
            if F[i]>F[i+1]:
                if F[i]>F[i+2]:  # need to make sure that it does not delete something that should not be deleted
                    if i < ind_maxF:
                        #print("if testing: bad index=", i)
                        #print(i)
                        #print(F[i], F[i+1])
                        #print(E[i], E[i+1])
                        #print(F[i]-F[i+1])
                        print("Changing ", F[i])
                        F[i] = 0.0
                        print("Changed ", F[i] )

        E_csv.append(E); F_csv.append(F); name_csv.append(foil_name)
    E_csv = [item for sublist in E_csv for item in sublist]
    F_csv = [item for sublist in F_csv for item in sublist]
    name_csv = [item for sublist in name_csv for item in sublist]

    E_csv=np.array(E_csv);F_csv=np.array(F_csv);name_csv=np.array(name_csv);

    csv_save_array = np.array((name_csv, E_csv, F_csv)).T

    ### Writing out new ziegler csv files with the same name to a new folder
    np.savetxt('cleaned_zieglerfiles/{}'.format(f), csv_save_array, delimiter=',', header='name, energy, flux', fmt="%s"  )#, %.6f, %.6f")



import time
start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))
