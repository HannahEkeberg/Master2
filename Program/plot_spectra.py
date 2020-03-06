import numpy as np, matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit, minimize_scalar
#from scipy import optimize
from scipy import asarray as ar,exp
from scipy.stats import norm

#filename = 'data_spectra.csv'
#channels = np.linspace(0,3000,8191)
#a = 5.312952e1; b=3.102316e-1; c=7.348633e-6 #energy calibration parameters, keV


path = '../Spectra_experiment/room131/text_Spe/'
Ir08_03182019 = path + 'CF03202019_Ir08_10cm_room131.Spe'
Cu04_02272019 = path + 'BN02272019_Cu04_5cm_room131.Spe'

def extract(Spe_file):
	with open(Spe_file) as f:
		spec = (f.readlines()[12:-24])   # actual array 
		begin = '$DATA:' # +1 extra line
		end = '$ROI:'

		#begin =   'Ebeam  Z   A   Total    grnd st  isomer1 isomer2  isomer1  isomer2  didl nolevs'
		#end   =   'Ebeam =  '
		#content_full = f.readlines()
		#ind_begin = [line for line in range(len(content_full)) if begin in content_full[line]][0]+1  # only one element but want it as integer
		#ind_end   = [line for line in range(len(content_full)) if end   in content_full[line]][0]  # list of different, only want the first element
		#content = content_full[ind_begin:ind_end]
		#print(content)
		
		counts = []
		for i in spec: 
			i.strip()
			counts.append(float(i))


		a=4.607848E-002; b= 1.881157E-001;  c=6.431981E-009  # keV  energy calibration in maestro 
		channels = len(counts)
		channels = np.linspace(0,len(counts),len(counts))
		

		energy = np.zeros(len(channels))
		for i,e in enumerate(channels):
		   energy[i] = a + b*i + c*i**2  #making energy array
		#print(energy)

		return energy, counts


def plot_spectrum(foil, filename, zoom=[0,0], log=False):
	if foil=='Ir':
		gammas = {'190Ir': [605.14, 569.30, 407.22, 371.24],'191Pt': 91.1,'193mPt':135.50}
		#pass 
	if foil == 'Cu':
		gammas = {'63Zn':[669.62, 962.06],'65Zn': [1115, 1481]}



	E, C  = extract(filename)    #energy and counts 
	E = list(E)
	list_of_markers = ['v', '^', 'o', 's', 'D', '8']
	colors = ['mediumpurple', 'cyan', 'palevioletred', 'darkorange', 'forestgreen', 'orchid', 'dodgerblue', 'lime', 'crimson', 'indianred']

	g = list(gammas.values())
	key = list(gammas.keys())
	print(type(g[1]))

	if log==True:
		marker_on_yaxis = 14
	else: 
		marker_on_yaxis = 4e5

	for i,e in enumerate(g):
		if isinstance(e, list):
			for j in range(len(e)):
				### Label only for the first element of this loop. 
				plt.axvline(e[j],linewidth=0.5, linestyle='--', color=colors[i])#, marker=list_of_markers[0]))
				plt.plot(e[j], marker_on_yaxis, marker=list_of_markers[i], color=colors[i], label=(key[i] if j==0 else ""))
				
			
		else:
			plt.axvline(e,linewidth=0.5, linestyle='--', color=colors[i])#, marker=list_of_markers[0])
			#marker_on_yaxis = C[i]	
			#print(ind)

			plt.plot(e, marker_on_yaxis, marker=list_of_markers[i], color=colors[i], label=key[i])
			
	print(E)

	#ind = E.index(135)
	#print(ind)
	

	"""
	for i,e in enumerate(g):
		if type(e)=='list': 
			for j in e:
				plt.axvline(j, label=key[i],linewidth=0.5, linestyle='--', color=colors[i])#, marker=list_of_markers[0]))
		else:
			plt.axvline(e, label=key[i], linewidth=0.5, linestyle='--', color=colors[i])#, marker=list_of_markers[0])
	"""

	if zoom!= [0,0]:
		print("dif")
		plt.xlim(zoom[0], zoom[1])

	if log: 
		plt.plot(E, np.log(C), color='slategrey', linewidth=0.8)
	else: 
		plt.plot(E, C, color='slategrey', linewidth=0.8)
	plt.xlabel('Energy keV')
	plt.ylabel('Counts')
	plt.legend(fontsize="x-small")

	plt.show()



plot_spectrum('Ir', Ir08_03182019, zoom=[0,2000], log=True)
plot_spectrum('Cu', Cu04_02272019, zoom=[0,0], log=True)


