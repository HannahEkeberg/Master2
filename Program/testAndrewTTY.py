import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
# from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               # AutoMinorLocator)

import scipy.interpolate as inter
from scipy import interpolate
from CrossSectionData import *

import curie as ci
from collections import OrderedDict
# params = {'text.usetex': True, 'mathtext.fontset': 'stix'}
# plt.rcParams["font.family"] = "Computer Modern"
# plt.rcParams.update(params)

import sys
# print(sys.version)


#  INPUT
########################################################################

el = ci.Element('Ir')     # Target material

particle='d'    # Incident beam

itp_list = ['193PTm', '191PT', '192IR', '189PT', '188PT', '194IR']    # Product isotopes, in Curie notation
i_list = ['193mPt','191Pt','192Ir', '189Pt', '188Pt', '194Ir']    # Product isotopes, for the plot legend

# Set up labels for plot legends
# prods = [r'$^{'+i[:-2]+r'}$'+i[-2:] for i in i_list]
prods = [r'$^{nat}$Ir(d,x)$^{'+i[:-2]+r'}$'+i[-2:] for i in i_list]


t_irr = 1   # irradiation length, in h  (only affects EOB thick target yield)

Z_beam = 1   # charge state of beam

show_all_plots = False   # Show all 4 yield plots, or only physical yield


# Add platinums, and all other reaction channels
result = CrossSection(os.getcwd() + '/CrossSections/CrossSections_csv/')
E_193mPt,dE_193mPt, Cs_193mPt, dCs_193mPt = result.retrieveCrossSectionData('Ir_193mPt')
E_189Pt, dE_189Pt, Cs_189Pt, dCs_189Pt = result.retrieveCrossSectionData('Ir_189Pt')
E_191Pt, dE_191Pt, Cs_191Pt, dCs_191Pt = result.retrieveCrossSectionData('Ir_191Pt')
E_192Ir, dE_192Ir, Cs_192Ir, dCs_192Ir = result.retrieveCrossSectionData('Ir_192Ir')
E_188Pt, dE_188Pt, Cs_188Pt, dCs_188Pt = result.retrieveCrossSectionData('Ir_188Pt')
E_194Ir, dE_194Ir, Cs_194Ir, dCs_194Ir = result.retrieveCrossSectionData('Ir_194Ir')

xx = [np.flip(E_193mPt), np.flip(E_191Pt), np.flip(E_192Ir), np.flip(E_189Pt), np.flip(E_188Pt), np.flip(E_194Ir)] # Energy [MeV]
crossSections = [np.flip(Cs_193mPt), np.flip(Cs_191Pt), np.flip(Cs_192Ir), np.flip(Cs_189Pt), np.flip(Cs_188Pt), np.flip(Cs_194Ir)] # [mb]
yy = []
for i in crossSections:
    yy.append(np.nan_to_num(i))

# OPTIONAL
########################################################################
line_style = ['solid','dashed','dashed','dashed','dashed','dashed','dashdot','dashed ']
# '-' or 'solid'	solid line
# '--' or 'dashed'	dashed line
# '-.' or 'dashdot'	dash-dotted line
# ':' or 'dotted'

line_weight = [2, 1, 1, 1, 1, 1, 1, 1] 

# Above are plot options for the lines 

colors = ['darkred', 'blue', 'forestgreen', 'peru', 'cyan', 'red']

# colors = ['#BB7D69', '#C8CDAF', '#D1B9AA', '#7C5953', '#426884', '#7C877C', 'pink', 'orchid']

# Pistachio, Mexico, Indie pink, Sophisticated red, True blue, Mindful green

########################################################################
# def read_exfor(fname):
# 	widths = np.array([0, 15, 28, 41, 54, 57, 82, 85, 95, 104])
# 	widths = np.diff(widths)
# 	names = ["x", "dx", "y", "dy", "#1",
#              "year, auth", "#2", "id", "com"]

# 	dtype = ""
# 	for i, w in enumerate(widths):
# 		if i < 4:
# 			dtype += f"float,"
# 		else:
# 			dtype += f"S{w},"
# 	dtype = dtype[:-1]

# 	data = np.genfromtxt(fname, delimiter=widths,
#                          skip_header=11, skip_footer=2,
#                          dtype=dtype, names=names, deletechars="",
#                          comments=None)

# 	a = [list(item) for item in data]
# 	data = pd.DataFrame(a, columns=names)
# 	data = data.drop(columns=["#1", "#2"])

# 	data["year, auth"] = data["year, auth"].str.decode('utf-8')
# 	data["com"] = data["com"].str.decode('utf-8')
# 	# data["id"] = data["id"].astype(int)
# 	return data

########################################################################
# data = read_exfor("natGe72Se_EXFOR.txt")     # Only if you wanted to overlay yield data from EXFOR, which is currently commented out




if show_all_plots:
	fig = plt.figure(figsize=(12, 9))

for n in np.arange(0,len(yy)):

	## If I was using my own experimental data instead of an EXFOR import I would have to just make sure the energy points were in increasing order
	# xx = np.concatenate((E_BNL,E_LANL))[::-1]
	# yy = np.concatenate((cs_BNL,cs_LANL))[::-1]
	# plt.plot(xx[n],yy[n])
	# plt.show()
	# print(i_list[n])


	smooth_xs = yy[n]*(1.0e-27)
	e_range = xx[n]

	MM = el.mass

	dc = ci.Isotope(itp_list[n]).decay_const('h',True)   #1/h
	# print('dc: ',dc[0])


	y = np.empty_like(e_range)
	S_pw= el.S(e_range,particle=particle, density=1E-3)*1E3   # MeV/(g/cm^2)
	# print(el.S([1e-3, 1e-2],particle=particle, density=1E-3)*1E3 )



	for i, item in enumerate(yy[n]): 
		# print(i)
		# print(e_range[0:i+1] )
		# print(np.concatenate(([], e_range[0:i+1])))

		y[i] = np.trapezoid( (np.concatenate(([0, 0], smooth_xs[0:i+1])) / (Z_beam*1.602e-19)) / (np.concatenate((el.S([1e-3, e_range[0]-0.2],particle=particle, density=1E-3)*1E3 , S_pw[0:i+1]))), x=np.concatenate(([0.1, e_range[0]-0.2], e_range[0:i+1]))   ) *(6.022e23/MM) / (1E6 * 1E6)
		#                     cm2             # particles/A      MeV/(g/cm^2)       MeV              # nuclei       MBq    uA

	# y[0]=0
	y = np.concatenate(([0], y))
	e_range = np.concatenate(([0], e_range))
	EOB_TTY = (1-np.exp(-dc[0]*t_irr))  * y
	saturation_TTY = y
	physical_TTY = dc[0] *y

	if show_all_plots:
		plt.subplot(2, 2, 1)
		plt.plot(e_range,EOB_TTY,label=prods[n], linestyle=line_style[n], linewidth=line_weight[n])
		plt.ylabel('t$_{irr}$ ('+str(t_irr)+' hr) EOB Thick Target Yield (MBq/uA)')#,labelpad=7,fontsize=22)
		plt.xlabel('Beam Energy (MeV)')#,labelpad=7,fontsize=22)
		plt.yscale('log')
		plt.xlim(left=0)
		plt.legend(loc='best')

		plt.subplot(2, 2, 2)
		plt.plot(e_range,saturation_TTY,label=prods[n], linestyle=line_style[n], linewidth=line_weight[n])
		plt.ylabel('Saturation Thick Target Yield (MBq/uA)')#,labelpad=7,fontsize=22)
		plt.xlabel('Beam Energy (MeV)')#,labelpad=7,fontsize=22)
		plt.yscale('log')
		plt.xlim(left=0)
		plt.legend(loc='best')

		plt.subplot(2, 2, 3)

	plt.plot(e_range,physical_TTY/0.0036,label=prods[n], linestyle=line_style[n], linewidth=line_weight[n], color=colors[n])
	plt.ylabel('Physical Thick Target Yield (MBq/C)', fontsize='small') #,labelpad=7,fontsize=22)
	plt.xlabel('Deuteron Energy (MeV)', fontsize='smaller') #,labelpad=7,fontsize=22)
	plt.yscale('log')
	plt.xlim(left=0, right=30.5)
	# plt.ylim(bottom=1e6)
	plt.ylim(top=1e7)
	# plt.legend(loc='best')
	# plt.title('Physical thick target yield')
	plt.legend(loc='upper left')
	plt.savefig('physicalyield', dpi=300)
	# (Preferred units)

	if show_all_plots:
		plt.subplot(2, 2, 4)
		plt.plot(e_range,physical_TTY,label=prods[n], linestyle=line_style[n], linewidth=line_weight[n])
		# plt.ylabel('Physical Thick Target Yield (MBq/uA h)') #,labelpad=7,fontsize=22)
		# plt.xlabel('Beam Energy (MeV)',labelpad=7,fontsize=22)
		plt.ylabel('Physical Thick Target Yield (MBq/C)', fontsize='small') #,labelpad=7,fontsize=22)
		plt.xlabel('Deuteron Energy (MeV)', fontsize='smaller') #,labelpad=7,fontsize=22)
		plt.yscale('log')
		plt.xlim(left=0)
		plt.gca().set_ylim(bottom=0, top=1e6)
		plt.legend(fontsize='small', loc='best')
		# plt.legend(loc='upper left', fontsize="10")
		# prop = { "size": 20 }, loc ="upper left"
		# (Only for comparison against IAEA data)
		# To convert, 1 MBq/C = 0.0036 MBq/uAh
plt.show()