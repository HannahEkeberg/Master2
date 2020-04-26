import numpy as np, matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit, minimize_scalar
#from scipy import optimize
from scipy import asarray as ar,exp
from scipy.stats import norm
from scipy import interpolate
import os

#filename = 'data_spectra.csv'
#channels = np.linspace(0,3000,8191)
#a = 5.312952e1; b=3.102316e-1; c=7.348633e-6 #energy calibration parameters, keV




def interpolation(x,y):	
	print(y)
	tck = interpolate.splrep(x, y, s=0)
	#print(type(tck))
	#print(tck[0])
	#print(tck[1])
	#x_new = np.linspace(1, 40, 1000)
	x_new = np.linspace(0,np.max(x), len(x))
	y_new = interpolate.splev(x_new, tck, der=0)
	return x_new, y_new

def reportfiles_plot(filename, foil):
	path = os.getcwd() + '/../matlab/fitz_reports3/'
	fname = path + filename 
	print(fname)

	
	with open(fname) as f:
		lines = f.readlines()
		begin = 'Energy  Channel  (KeV)  Signif  of Fit    Area   Uncert.  per sec.   Uncert. Background'
		end = 'indicates the Iterative Peak Width fitting reached a limiting value.'

		#print(begin)
		#print(lines[35])
		footer=len(lines)-4
		print(footer)
		header=36

		E = []; counts = []
		for l in range(len(lines)):
			#lines[l].rstrip()
			
			if lines[l].rstrip() == begin:
				header=l+2
			if lines[l].rstrip() == end:
				footer=l-2
			if "Live:" in lines[l]:
				line = lines[l].strip().split()
				livetime = line[-1]

			#print(header, footer)
			if l >= header and l<=footer:# and l<= footer:
				#print(l)
				lins=lines[l].strip().split()
				E.append(lins[0]); counts.append(lins[5])

		#plt.plot(E, (counts/livetime))
		#plt.show()

			#new_lines.append(lines[l].strip())
		#print(lines)

			#print(lines)
		#print(new_lines)
			

		#counts = np.genfromtxt(fname, delimiter=' ', usecols=[1], skip_header=header, skip_footer=footer) #hours since e.o.b
		#print(counts)
		#	if lines[l] == begin: 
		#		header = l+2
		#	print(lines[l])
		#print(header)
		#for i in lines:
		#	i.strip()
		#counts = np.genfromtxt(fname, delimiter='\n,', usecols=[0], skip_header=36) #hours since e.o.b
		#print(counts)

#filename = 'CA03032019_32cm_Ir06_HPGE1.txt' 
# reportfiles_plot(filename, 'Ir06')

def extract(Spe_file):     # for plotting single spectra
	with open(Spe_file) as f:
		#spec=f.readlines()

		spec = f.readlines()   # actual array 
		begin = '$DATA:' # +2 extra lines
		end = '$ROI:'    # correct numb of lines
		energy_cal = '$SHAPE_CAL:'    # - 1 numb of lines
		#print(enD)
		#spec[:] = [i for i in spec if i != '\n'].
		#print(spec)
		
		#lines.write('\n'.join(spec))

		for l in range(len(spec)):
			if spec[l].rstrip() == end:
				footer = len(spec)-l
			if spec[l].rstrip() == begin:
				header = l+2 
			if spec[l].rstrip() == energy_cal:
				cal_line = spec[l-1].split()
				a=float(cal_line[0]); b=float(cal_line[1]); c=float(cal_line[2])


		counts = np.genfromtxt(Spe_file, delimiter='\n,', usecols=[0], skip_header=header, skip_footer=footer) #hours since e.o.b

		channels = len(counts)
		channels = np.linspace(0,len(counts),len(counts))
		

		energy = np.zeros(len(channels))
		for i,e in enumerate(channels):
		   energy[i] = a + b*i + c*i**2  #making energy array
		e_new, c_new = interpolation(energy, counts)   
		#return energy, counts
		
		#print(e_new[:50], c_new[:50])
		return e_new, c_new


def plot_multiple_spectra(list_of_filenames, list_of_labels, log=True, zoom=[0,0,0,0]):
	for i in range(len(list_of_filenames)):
		E, C = extract(list_of_filenames[i])
		if log: 
			plt.plot(E,np.log(C), label=list_of_labels[i], linewidth=0.5)
		else:
			plt.plot(E,C, label=list_of_labels[i], linewidth=0.5)

	if zoom!= [0,0,0,0]:
		plt.xlim(zoom[0], zoom[1])	
		plt.ylim(zoom[2], zoom[3])	
	plt.legend()
	plt.show()



def plot_spectrum(foil, filename, title, zoom=[0,0,0,0], log=False):
	if foil=='Ir':
		gammas = {'188Ir': [1209.80, 1715.67,2059.65], '189Ir': [95.23, 216.7, 233.5, 245.1], '190Ir': [605.14, 569.30, 407.22, 371.24],
		'192m2Ir': [361.2, 502.5, 616.5 ], '192Ir': [295.95650, 468.06885, 612.46215], '194Ir': [298.541], '194m2Ir': [338.8, 482.6, 562.4, 687.8],    
		'188Pt': [195.05, 381.43], '189Pt': [94.34, 2243.50, 721.28], '191Pt': 91.1,'193mPt':[66.831,135.50]}
		#gammas = {'193mPt':[66.831,135.50]}
		#pass 
	if foil == 'Cu':
		gammas = {'63Zn':[669.62, 962.06],'65Zn': [1115, 1481]}



	E, C  = extract(filename)    #energy and counts 
	E = list(E)
	#list_of_markers = ['v', '^', 'o', 's', 'D', '8', '.', '.', '.', '*', '*']
	list_of_markers = ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*']
	colors = ['mediumpurple', 'cyan', 'palevioletred', 'darkorange', 'forestgreen', 'orchid', 'dodgerblue', 'lime', 'crimson', 'indianred', 'black']

	g = list(gammas.values())
	key = list(gammas.keys())
	#print(type(g[1]))
	#print(g[0][0])
	#for i in range(len(E)):
		#if np.abs(g[0][0]-E[i]) < 1:
			#print(i)
			#print(E[i])
		#if (np.abs(np.where(g[0][0])-E[i])< 0.5) == True:
			#print(i)
			#print(E[i])
			#print(g[0][0])


	if log==True:
		C = np.log(C)
		plt.plot(E, C, color='slategrey', linewidth=0.8)
		#marker_on_yaxis = 14
	#else: 
		#marker_on_yaxis = 4e5
	else: 
		plt.plot(E, C, color='slategrey', linewidth=0.8)

	
	for i,e in enumerate(g):
		if isinstance(e, list):
			for j in range(len(e)):
				### Label only for the first element of this loop. 
				list_of_inds = []
				for k in range(len(E)):
					if np.abs(e[j]-E[k])<1:
						list_of_inds.append(k)
				mean_k = int(np.mean(list_of_inds))
				label_placement = C[mean_k]*1.05
				plt.plot(e[j], label_placement, color=colors[i], marker=list_of_markers[i], label=(key[i] if j==0 else ""))
				#plt.axvline(e[j],linewidth=0.5, linestyle='--', color=colors[i])#, marker=list_of_markers[0]))
				#plt.plot(e[j], marker_on_yaxis, marker=list_of_markers[i], color=colors[i], label=(key[i] if j==0 else ""))
				
			
		else:
			
			#plt.axvline(e,linewidth=0.5, linestyle='--', color=colors[i])#, marker=list_of_markers[0])
			#marker_on_yaxis = C[i]	
			#print(ind)
			list_of_inds = []
			for k in range(len(E)):
				if np.abs(e-E[k])<1:
					list_of_inds.append(k)
			mean_k = int(np.mean(list_of_inds))
			#print(mean_k)
			
			label_placement = C[mean_k]*1.05
			plt.plot(e, label_placement, color=colors[i], marker=list_of_markers[i], label=key[i])


			
					

			#plt.plot(e, marker_on_yaxis, marker=list_of_markers[i], color=colors[i], label=key[i])
		
		
	if zoom!= [0,0,0,0]:
		print("dif")
		plt.xlim(zoom[0], zoom[1])
		plt.ylim(zoom[2], zoom[3])


	plt.xlabel('Energy keV')
	if log==True:
		plt.ylabel('Counts (log-scale)')
	else:
		plt.ylabel('Counts')
	plt.title(title)
	plt.legend(fontsize="x-small")

	plt.show()



path = '../Spectra_experiment/room131/text_Spe/'
path_idm1 = '../Spectra_experiment/IDM1/text_Spe/'
#Ir08_03182019 = path + 'CF03202019_Ir08_10cm_room131.Spe'
Cu04_02272019 = path + 'BN02272019_Cu04_5cm_room131.Spe'
Ni06_02272019 = path + 'BR02272019_Ni06_5cm_room131.Spe'


Ir05_030619 = path_idm1 + 'BK030619_53cm_Ir05_IDM1.Spe'

Ir10_02262019 = path + 'AI02262019_Ir10_10cm_room131.Spe'
Ir09_02262019 = path + 'AH02262019_Ir09_18cm_room131.Spe'
Ir08_02262019 = path + 'AC02262019_Ir08_22cm_room131.Spe'
Ir07_02262019 = path + 'AG02262019_Ir07_18cm_room131.Spe'
Ir06_02262019 = path + 'AF02262019_Ir06_18cm_room131.Spe'
Ir05_02262019 = path + 'AE02262019_Ir05_18cm_room131.Spe'
Ir04_02262019 = path + 'AB02262019_Ir04_18cm_room131.Spe'
Ir03_02262019 = path + 'AJ02262019_Ir03_40cm_room131.Spe'
Ir02_02262019 = path + 'AD02262019_Ir02_40cm_room131.Spe'
Ir01_02262019 = path + 'AA02262019_Ir01_50cm_room131.Spe'

#f_names = [Ir01_02262019, Ir02_02262019, Ir03_02262019, Ir04_02262019, Ir05_02262019, Ir06_02262019, Ir07_02262019, Ir08_02262019, Ir09_02262019, Ir10_02262019]
#labels=['Ir01', 'Ir02', 'Ir03', 'Ir04','Ir05', 'Ir06', 'Ir07', 'Ir08', 'Ir09', 'Ir10',]
#plot_multiple_spectra(f_names, labels, log=True, zoom=[0,250,5,12])

#plot_spectrum('Ir', Ir08_03182019, zoom=[0,250], log=False)
#plot_spectrum('Cu', Cu04_02272019, zoom=[0,0], log=True)


plot_spectrum('Ir', Ir05_030619, title='Gammaray spectrum for Ir05 (ca. 35 hours after EOB)', zoom=[0,2000,0,13], log=True)
#plot_spectrum('Ir', Ir05_030619, title='Gammaray spectrum for Ir05 (ca. 35 hours after EOB)', zoom=[0,0,0,0], log=False)


