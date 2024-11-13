import os

class Exfor:

    def __init__(self, exforFilePath):
        self.exforFilePath = exforFilePath

    def retrieveExforData(self, reaction, independent=True):
        if independent == True:
            filename = self.exforFilePath + reaction + '_ind.txt'
        elif independent == False:
            filename = self.exforFilePath + reaction + '_cum.txt'

        self.fileHandle(filename)

    def fileHandle(self, filename):
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
                    author.append(string[5]) #index 4 is equal to #
                except:
                    print(string[5], "not included in exfor data")
                    pass

        author_new  = []
        for auth in author:
            if '+' in auth:
                author_new.append(auth.replace('+', ''))
                return E, dE, CS, dCS, author_new
            else:
                return 0, 0, 0, 0, '0'


Exfor(os.getcwd() + '/../EXFOR/').retrieveExforData('Ir_189Pt')
