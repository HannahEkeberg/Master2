import matplotlib.pylab as plt

# A list of all isotopes you want extracted for plotting
products= ['078-188Pt', '078-189Pt', '078-191Pt', '077-188Ir', '077-189Ir', '077-190Ir','077-192Ir',
           '077-194Ir' 
           # etc etc
           ]

# Target isotope - needed if you have multiple sub-directories for each target isotope in an element
target = '191Ir'

# Run 'cat out_coh_*_MeV.dat > out_coh_merged.dat' in the ./output directory to unify files for parsing
with open('./' + target + '/output/out_coh_merged.dat','r') as f:
    energies = []
    cross_sections = dict.fromkeys(products)
    # print(cross_sections)
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
        plt.savefig('./'+target+'/plots/'+isotope+"_coh.png")
        plt.close()
    except ValueError:
        print('ValueError!')
        continue
    with open('./'+target+'/plots/'+isotope+"_coh.txt",'w') as f:
    # with open('files/'+isotope+"_coh.txt",'w') as f:
        for i in range(len(energies)):
            f.write(str(energies[i])+"\t"+str(cross_sections[isotope][i])+"\n")