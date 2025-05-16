import os
import matplotlib.pyplot as plt
from collections import OrderedDict
from generateExcitationFunction import *

class Exfor:

    def __init__(self, exforFilePath):
        self.exforFilePath = exforFilePath

    def retrieveExforData(self, reaction, independent):
        if independent == True:
            filename = self.exforFilePath + reaction + '_ind.txt'
        elif independent == False:
            filename = self.exforFilePath + reaction + '_cum.txt'
        if os.path.isfile(filename):
            return self.retrieveDataFromFile(filename)
        else:
            print(self.exforFilePath + reaction )
            raise Exception("EXFOR file does not exist: " + filename)
        
    def plotExforData(self, reaction, independent=None):
        if independent==None:
            independent=True
        try:
            E, dE, CS, dCS, authors =  self.retrieveExforData(reaction, independent)
            unique_authors = []
            for auth in authors:
                if auth not in unique_authors:
                    unique_authors.append(auth)
            colors = self.colors()
            for i in range(len(E)):
                for j in range(len(unique_authors)):
                    if authors[i] == unique_authors[j]:
                        plt.errorbar(E[i], CS[i], marker='.', color=colors[j], markersize=1, linewidth=0.0001, xerr=dE[i], yerr=dCS[i], elinewidth=0.25, capthick=0.25, capsize=3.0, label=unique_authors[j])
        except:
            typ = "independent" if independent==True else "cumulative"
            print("No exfor file found reaction " + reaction + " - " + typ )
            pass

    def retrieveDataFromFile(self, filename):
        with open(filename) as f:
            beginMark =   'EXFOR-ID'
            endMark   =   '//'
            content_full = f.readlines()
            ind_begin = [line for line in range(len(content_full)) if beginMark in content_full[line]][0]+1  # only one element but want it as integer
            ind_end   = [line for line in range(len(content_full)) if endMark in content_full[line]][0]  # list of different, only want the first element
            content = content_full[ind_begin:ind_end]
            E = []; dE=[]; CS = []; dCS=[]; author=[]
            for ind in range(len(content)):
                string= content[ind]
                string = (string.lstrip()).split()
                E.append(float(string[0]))
                dE.append(float(string[1]))
                CS.append(float(string[2])*1e3) # in mb
                dCS.append(float(string[3])*1e3) # in mb
                try:
                    author.append(string[5]) #index 4 is equal to
                except:
                    print(string[5], "not included in exfor data")
                    pass
        authors  = []
        for auth in author:
            if '+' in auth:
                authors.append(auth.replace('+', ''))
        if len(authors)!= 0:
            return E, dE, CS, dCS, authors
        else:
            return 0, 0, 0, 0, '0'

    def colors(self):
        # return ['mediumpurple', 'cyan', 'palevioletred', 'darkorange', 'forestgreen', 'orchid', 'dodgerblue', 'lime', 'crimson', 'indianred']
        return [ 'crimson','cyan', 'forestgreen', 'palevioletred', 'darkorange', 'indianred', 'orchid', 'dodgerblue', 'lime','mediumpurple']
