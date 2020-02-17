from npat import Ziegler, Isotope

if __name__=='__main__':

	######## Ziegler Tests #############

	## Compound must be specified, and enough info to determine areal density
	## Units:
	## thickness: mm
	## mass: g
	## area: cm^2
	## ad (areal density): mg/cm^2
	## density: g/cm^3
	import numpy as np
	#names = ['-10', '-5', '0', '+5', '+10' ]
	#names = ['-4', '-3,5', '-3', '-2,5', '-2', '-1,5', '-1', '-0,5', '+0,5', '+1', '+1,5', '+2', '+2.5', '+3', '+3,5', '+4']
	#scaling_parameter = [0.96, 0.975, 0.97, 0.985, 0.99, 0.995, 1.005, 1.05, 1.055, 1.01, 1.015, 1.02, 1.025, 1.03, 1.035, 1.04]
	#scaling_parameter = [0.9, 0.95, 1.0, 1.05, 1.1]




	#scaling_parameter = [0.875, 0.85, 0.835, 0.80, 0.775, 0.75]
	#names = ['-12,5', '-15', '-17,5', '-20', '-22,5', '-25']

	#scaling_parameter = [0.75, 0.775, 0.80, 0.825, 0.85, 0.875, 0.90, 0.925, 0.95, 0.96,
	#0.965, 0.97, 0.975, 0.98, 0.985, 0.99, 0.995, 1.0, 1.005, 1.01, 1.015, 1.02, 1.025,
	#1.03, 1.035, 1.04, 1.05, 1.075, 1.1, 1.125, 1.15]

	#names  = ['D_-25', 'D_-22,5', 'D_-20', 'D_-17,5', 'D_-15', 'D_-12,5', 'D_-10', 'D_-7,5',
	#'D_-5', 'D_-4', 'D_-3,5', 'D_-3', 'D_-2,5', 'D_-2', 'D_-1,5' 'D_-1','D_-0,5', 'D_0',
	#'D_+0,5', 'D_+1', 'D_+1,5', 'D_+2', 'D_+2,5',
	#'D_+3', 'D_+3,5', 'D_+4', 'D_+5', 'D_+7,5', 'D_+10', 'D_+15']


	scaling_parameter = [0.95, 0.9525, 0.955, 0.9575, 0.96, 0.9625, 0.965, 0.9675, 0.97, 0.9725, 0.975, 0.9775, 0.98, 0.9825, 0.985,
	0.9875, 0.99, 0.9925, 0.995, 0.9975, 1.0, 1.0025, 1.005, 1.0075, 1.01, 1.0125, 1.015, 1.0175, 1.02, 1.0225,
	1.025, 1.0275, 1.03, 1.0325, 1.035, 1.0375, 1.04, 1.0425, 1.045, 1.0475, 1.05]
	#scaling_parameter_beam = [0.875, 0.85, 0.835, 0.80, 0.775, 0.75]
	#names_beam = ['B_-12,5', 'B_-15', 'B_-17,5', 'B_-20', 'B_-22,5', 'B_-25']
	names = ['D_-5', 'D_-4,75', 'D_-4,5', 'D_-4,25', 'D_-4', 'D_-3,75', 'D_-3,5', 'D_-3,25', 'D_-3','D_-2,75', 'D_-2,5', 'D_-2,25', 'D_-2',
		'D_-1,75', 'D_-1,5', 'D_-1,25', 'D_-1', 'D_-0,75', 'D_-0,5', 'D_-0,25', 'D_0', 'D_+0,25', 'D_+0,5', 'D_+0,75', 'D_+1','D_+1,25', 'D_+1,5',
		'D_+1,75', 'D_+2','D_+2,25', 'D_+2,5', 'D_+2,75', 'D_+3', 'D_+3,25', 'D_+3,5', 'D_+3,75', 'D_+4','D_+4,25', 'D_+4,5', 'D_+4,75', 'D_+5']
	scaling_parameter_beam = [0.95, 0.9525, 0.955, 0.9575, 0.96, 0.9625, 0.965, 0.9675, 0.97, 0.9725, 0.975, 0.9775, 0.98, 0.9825, 0.985,
	0.9875, 0.99, 0.9925, 0.995, 0.9975, 1.0, 1.0025, 1.005, 1.0075, 1.01, 1.0125, 1.015, 1.0175, 1.02, 1.0225,
	1.025, 1.0275, 1.03, 1.0325, 1.035, 1.0375, 1.04, 1.0425, 1.045, 1.0475, 1.05]
	#names_beam = ['B_-10', 'B_-7,5', 'B_-5', 'B_-2,5', 'B_0', 'B_+2,5', 'B_+5', 'B_+7,5', 'B_+10']
	names_beam = ['B_-5', 'B_-4,75', 'B_-4,5', 'B_-4,25', 'B_-4', 'B_-3,75', 'B_-3,5', 'B_-3,25', 'B_-3','B_-2,75', 'B_-2,5', 'B_-2,25', 'B_-2',
	'B_-1,75', 'B_-1,5', 'B_-1,25', 'B_-1', 'B_-0,75', 'B_-0,5', 'B_-0,25', 'B_0', 'B_+0,25', 'B_+0,5', 'B_+0,75', 'B_+1','B_+1,25', 'B_+1,5',
	'B_+1,75', 'B_+2', 'B_+2,25', 'B_+2,5', 'B_+2,75', 'B_+3', 'B_+3,25', 'B_+3,5', 'B_+3,75', 'B_+4','B_+4,25', 'B_+4,5', 'B_+4,75', 'B_+5']
	#np.flip(scaling_parameter_beam)
	#np.flip(names_beam)

	#SS_316 stainless steel
	for i in range(len(scaling_parameter)):
		for j in range(len(scaling_parameter_beam)):
			#save_filename = 'E_foils_Fe_{}.csv'.format(names[i])
			#save_filename = 'E_foils_SS_{}.csv'.format(names[i])
			save_filename = 'ziegler_{}_{}.csv'.format(names_beam[j], names[i])
			stack = [{'compound':'SS_316', 'name':'SS01', 'ad':102.0},

					{'compound':'Ni', 'name':'Ni01', 'ad':22.772},
					{'compound':'Ir', 'name':'Ir01', 'ad':55.174},
					{'compound':'Cu', 'name':'Cu01', 'ad':22.338},

					{'compound':'Fe', 'name':'Fe01', 'ad':20.030},


					{'compound':'Ni', 'name':'Ni02', 'ad':23.118},
					{'compound':'Ir', 'name':'Ir02', 'ad':55.601},
					{'compound':'Cu', 'name':'Cu02', 'ad':22.325},

					{'compound':'Fe', 'name':'Fe02', 'ad':20.017},


					{'compound':'Ni', 'name':'Ni03', 'ad':22.338},
					{'compound':'Ir', 'name':'Ir03', 'ad':55.643},
					{'compound':'Cu', 'name':'Cu03', 'ad':22.313},

					{'compound':'Fe', 'name':'Fe03', 'ad':19.948},

					{'compound':'Ni', 'name':'Ni04', 'ad':20.704},
					{'compound':'Ir', 'name':'Ir04', 'ad':56.000},
					{'compound':'Cu', 'name':'Cu04', 'ad':22.284},


					{'compound':'Ni', 'name':'Ni05', 'ad':21.768},
					{'compound':'Ir', 'name':'Ir05', 'ad':55.161},
					{'compound':'Cu', 'name':'Cu05', 'ad':22.443},


					{'compound':'Ni', 'name':'Ni06', 'ad':22.861},
					{'compound':'Ir', 'name':'Ir06', 'ad':55.731},
					{'compound':'Cu', 'name':'Cu06', 'ad':22.396},


					{'compound':'Ni', 'name':'Ni07', 'ad':23.092},
					{'compound':'Ir', 'name':'Ir07', 'ad':56.685},
					{'compound':'Cu', 'name':'Cu07', 'ad':22.320},


					{'compound':'Ni', 'name':'Ni08', 'ad':22.409},
					{'compound':'Ir', 'name':'Ir08', 'ad':58.030},
					{'compound':'Cu', 'name':'Cu08', 'ad':22.401},


					{'compound':'Ni', 'name':'Ni09', 'ad':21.741},
					{'compound':'Ir', 'name':'Ir09', 'ad':56.669},
					{'compound':'Cu', 'name':'Cu09', 'ad':22.425},


					{'compound':'Ni', 'name':'Ni10', 'ad':23.093},
					{'compound':'Ir', 'name':'Ir10', 'ad':55.065},
					{'compound':'Cu', 'name':'Cu10', 'ad':22.314},

					{'compound':'SS_316', 'name':'SS02', 'ad':102.0} ]

			## must specify stack and beam...
			## stack is list of dicts, which specify composition of each
			## element of the stack
			##
			## beam is dict, specifying the isotope and incident energy
			## of the incoming beam.  dE0 (1-sigma width) and N (number of particles)
			## can optionally be included
			zg = Ziegler(stack=stack)
			#beam_istp='2H', E0=33.0, dE0=0.5, N=1E6, max_steps=100, 'dp'=scaling_parameter[i])
			zg.meta = {'istp':'2H', 'E0':33.0*scaling_parameter_beam[j], 'dE0':0.5, 'N':1E6, 'max_steps':100,'dp':scaling_parameter[i] }
			## name from stack is used for plotting - either incl_no_names=True must
			## be set, or name must be specified
			## if zg.plot() is called, all foils in stack are plotted that have a name.
			## optionally the first argument to plot is a list of samples that will be
			## regex matched to the names in the stack

			#zg.plot(['Ir'])#,'Ni','Ti'])

			## summarize either prints out the mean and 1-sigma energies of each
			## foil in the stack (with a name), or saves this info to a .csv using
			## the saveas argument.
			#zg.summarize(['Ir'])

			#zg.saveas('E_foils_test3.csv')


			#zg.saveas('E_foils_Fe_{}.csv'.format(names[i]))
			zg.saveas(save_filename)

	## The results of the stack calculation can be found in the zg.stack
	## variable, which is a list of Sample objects which store the energy,
	## flux, and other info about each sample in the stack calculation.
	#print(zg.stack[2].meta)
	#print(zg.stack[1].energy)
	#print(zg.stack[1].flux)


	####### Isotope Tests ############

	# ISTP = Isotope('133BA')
	# print ISTP.name
	# print ISTP.element
	# print ISTP.A
	# print ISTP.isomer
	# print ISTP.isotope
	# print ISTP.E_level
	# print ISTP.TeX
	# print ISTP.mass
	# print ISTP.half_life(ISTP.optimum_units(),unc=True),ISTP.optimum_units()
	# print ISTP.gammas()
	# print ISTP.electrons()
	# print ISTP.beta_minus()
	# print ISTP.beta_plus()
	# print ISTP.alphas()
