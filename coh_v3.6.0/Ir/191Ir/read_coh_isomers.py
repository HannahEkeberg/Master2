import matplotlib.pylab as plt
import os

path = os.getcwd()
if not os.path.exists('plots'):
    os.makedirs('plots')

# A list of all isotopes you want extracted for plotting
products= ['078-188Pt', '078-189Pt', '078-191Pt', '077-188Ir', '077-189Ir', '077-190Ir','077-192Ir',
           '077-194Ir' 
           # etc etc
           ]

# Target isotope - needed if you have multiple sub-directories for each target isotope in an element
target = '191Ir'

# Run 'cat out_coh_*_MeV.dat > out_coh_merged.dat' in the ./output directory to unify files for parsing
with open('./'+target+'/output/out_coh_merged.dat','r') as f:

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
                if cross_sections[isotope] is None:
                    cross_sections[isotope] = {'G':[], 'M':[]}
                ex = float(line.split()[2])
                if ex > 0:
                    key = 'M'
                else:
                    key = 'G'
                while len(cross_sections[isotope][key])<len(energies)-1:
                    cross_sections[isotope][key].append(0.0)

                cross_sections[isotope][key].append(float(line.split()[5]))

for isotope in products:
    for key in ['M','G']:
        if cross_sections[isotope][key] is None:
            print('nothing for ', isotope)
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
            plt.savefig('./'+target+'/plots/'+isotope+key+"_coh.png")
            plt.close()
        except ValueError:
            continue
        # with open('files/'+isotope+key+"_coh.txt",'w') as f:
        with open('./'+target+'/plots/'+isotope+key+"_coh.txt",'w') as f:

            for i in range(len(energies)):
                f.write(str(energies[i])+"\t"+str(cross_sections[isotope][key][i])+"\n")