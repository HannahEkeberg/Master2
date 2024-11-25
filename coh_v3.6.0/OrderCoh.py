import matplotlib.pylab as plt
import os 

class OrderCoh:
    """
    * createFolder must be run for each target

    * unify files for parsing must be run for each target, unless this is done manually by running 
    'cat out_coh_*_MeV.dat > out_coh_merged.dat' in the ./output directory to unify files for parsing

    * readCoh is used for all isotopes with no isomers present. Will generate plot and txt-datafile without G, 

    * readCohIsomers is used 

    """

    def __init__(self, target, foil):
        self.target = target
        self.foil = foil

    def createFolder(self):
        path = self.foil + '/' + self.target +'/plots'
        if not os.path.exists(path):
            os.makedirs(path)

    def unifyFilesForParsing(self):
        os.chdir(self.foil + '/' + self.target +'/output')
        command = 'cat out_coh_*_MeV.dat > out_coh_merged.dat'
        os.system(command)
        os.chdir('../../../')

    def readCoh(self, products):
                # Run 'cat out_coh_*_MeV.dat > out_coh_merged.dat' in the ./output directory to unify files for parsing
        pathToTarget = self.foil + '/' + self.target
        with open(pathToTarget + '/output/out_coh_merged.dat','r') as f:
            energies = []
            cross_sections = dict.fromkeys(products)
            print(cross_sections)
            reading = False

            for line in f:
                if 'sum' in line:
                    reading = False
                elif 'INDIVIDUAL GROUND STATE PRODUCTION' in line:
                    reading = True
                elif '#..................................' in line:
                    current_energy = float(line.split()[-1])
                    if len(energies) == 0 or current_energy != energies[-1]:
                        energies.append(current_energy)
                elif reading:
                    isotope = line.split()[1]
                    if isotope in cross_sections.keys():
                        # print(cross_sections[isotope])
                        if cross_sections[isotope] is None:
                            cross_sections[isotope] = []
                        # print('length of len(cross_sections[isotope]): ', len(cross_sections[isotope]))
                        # print('length of energies: ', len(energies))
                        while len(cross_sections[isotope])<len(energies)-1:
                        # while len(cross_sections[isotope])<len(energies):
                            cross_sections[isotope].append(0.0)
                            # print('Appending 0 for isotope '+isotope+ ' at energy ' + str(current_energy))
                        if len(cross_sections[isotope]) == len(energies):
                            # print(line.split()[2])
                            cross_sections[isotope][-1]+=float(line.split()[2])
                        else:
                            cross_sections[isotope].append(float(line.split()[2]))


        # print(cross_sections)
        # print(energies)

        for isotope in products:
            if cross_sections[isotope] is None:
                print('nothing for ', isotope)
                continue
            #print('plotting ', isotope)
            try:
                # Pad 0.0 to all runs with missing channel data
                while len(cross_sections[isotope])<len(energies):
                    cross_sections[isotope].append(0.0)
                # print('plotting ', isotope)
                # print('energies : ', energies)
                # print('XS : ', cross_sections[isotope])
                # print('./'+target+'/plots/'+isotope+"_coh.png")
                # print('./'+target+'/plots/'+isotope+"_coh.txt")
                # print(len(energies))
                # print(len(cross_sections[isotope]))
                plt.plot(energies,cross_sections[isotope])
                plt.xlabel('Proton Energy (MeV)')
                plt.ylabel('Cross Section (mb)')
                plt.title(isotope)
                plt.savefig(pathToTarget + '/plots/'+isotope+"_coh.png")
                plt.close()
            except ValueError:
                print('ValueError!')
                continue
            with open(pathToTarget + '/plots/'+isotope+"_coh.txt",'w') as f:
            # with open('files/'+isotope+"_coh.txt",'w') as f:
                for i in range(len(energies)):
                    f.write(str(energies[i])+"\t"+str(cross_sections[isotope][i])+"\n")

    def readCohIsomers(self, products):
        # Run 'cat out_coh_*_MeV.dat > out_coh_merged.dat' in the ./output directory to unify files for parsing
        pathToTarget = self.foil + '/' + self.target
        with open(pathToTarget + '/output/out_coh_merged.dat','r') as f:

            energies = []
            cross_sections = dict.fromkeys(products)
            reading = False

            for line in f:
                if 'sum' in line:
                    reading = False
                elif 'STABLE AND LONG-LIVED STATE PRODUCTIONS' in line:
                    reading = True
                elif '#..................................' in line:
                    current_energy = float(line.split()[-1])
                    if len(energies) == 0 or current_energy != energies[-1]:
                        energies.append(current_energy)
                elif reading:
                    isotope = line.split()[1]
                    if isotope in cross_sections.keys():
                        # print(len(line.split()))
                        if cross_sections[isotope] is None:
                            cross_sections[isotope] = {'G':[], 'M1':[], 'M2':[]}
                        ex = float(line.split()[2])
                        # print(isotope)
                        # print(len(cross_sections[isotope]))
                        # print(type(line.split()))
                        if len(line.split()) == 6:
                            if ex > 0:
                                key = 'M1'
                            else:
                                key = 'G'
                            while len(cross_sections[isotope][key])<len(energies)-1:
                                cross_sections[isotope][key].append(0.0)
                            cross_sections[isotope][key].append(float(line.split()[5]))
                        elif len(line.split()) == 7:
                            meta = int(line.split()[6])
                            if (ex > 0) and (meta == 1):
                                key = 'M1'
                            elif (ex > 0) and (meta == 2):
                                key = 'M2' 
                            else:
                                key = 'G'
                            # print(cross_sections[isotope][key])
                            while len(cross_sections[isotope][key])<len(energies)-1:
                                cross_sections[isotope][key].append(0.0)

                            cross_sections[isotope][key].append(float(line.split()[5]))
        for isotope in products:
            if cross_sections[isotope] is None:
                print('nothing for ', isotope)
                continue
            for key in ['M2','M1','G']:
                print(cross_sections[isotope])
                if len(cross_sections[isotope][key]) == 0:
                    print('nothing for ', isotope, ', with key ', key)
                    continue
                #print('plotting ', isotope)
                try:
                    # Pad 0.0 to all runs with missing channel data
                    while len(cross_sections[isotope][key])<len(energies):
                        cross_sections[isotope][key].append(0.0)
                    plt.plot(energies,cross_sections[isotope][key])
                    plt.xlabel('Proton Energy (MeV)')
                    plt.ylabel('Cross Section (mb)')
                    plt.title(isotope+' '+key)
                    # plt.savefig(isotope+key+"_coh.png")
                    plt.savefig(pathToTarget + '/plots/'+isotope+key+"_coh.png")
                    plt.close()
                except ValueError:
                    continue
                # with open('files/'+isotope+key+"_coh.txt",'w') as f:
                with open(pathToTarget + '/plots/'+isotope+key+"_coh.txt",'w') as f:

                    for i in range(len(energies)):
                        f.write(str(energies[i])+"\t"+str(cross_sections[isotope][key][i])+"\n")
