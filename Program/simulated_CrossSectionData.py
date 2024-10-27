

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


#from jan20_CrossSections import CrossSections
from foil_info import *
path = os.getcwd()



class SimCrossSectionData:

	def __init__(self):
		# reaction = Ir_193mPt for instance
		self.path = os.getcwd()
		#self.ziegler_file = self.path +'/cleaned_zieglerfiles/ziegler_B_+2_D_+4,25_fluxes.csv'
		#print(self.ziegler_file)

	def extract_from_alicefiles(self, filename, A, Z, CS_colonne):
		with open(filename) as f:
			content = f.readlines()
			for s in content:
				#line = ' '.join(s).split()
				line = " ".join(s.split())
				#print(line)

			#print(content)
			E_all = np.genfromtxt(filename, delimiter=' ', usecols=[0])#, skip_header=2)
			CS_all = np.genfromtxt(filename, delimiter=' ', usecols=[CS_colonne])#, skip_header=2)
			Z_ = np.genfromtxt(filename, delimiter=' ', usecols=[2])#, skip_header=2)
			A_ = np.genfromtxt(filename, delimiter=' ', usecols=[3])#, skip_header=2)

			E = []; CS = []
			#print(A, Z)
			Z = ' ' + Z + ' ' # must change to this so that it doesnt get mixed up by other line
			A = ' ' + A + ' '
			for lines in range(len(content)):
				if (A in content[lines]) and (Z in content[lines]):
					#print(content[lines])
					#print("line: ", lines)
					#print("A: ", A_[lines])
					#print("Z: ", Z_[lines])

					E.append(E_all[lines])
					CS.append(CS_all[lines])
				#else:
				#	print("nothing")
				#print("**")
			#n=20
			n=40
			E_typ = np.linspace(0,39, n)  # this we want to return, but want to add CS=0 to these values
			CS_typ = np.zeros((n))
			for i in range(len(E_typ)):
				for j in range(len(E)):
					if E_typ[i]==E[j]:
						CS_typ[i]=CS[j]
					#else:
						#CS_typ[i]=CS_typ[i-1]

			"""
			Andrew, how to deal with energies which lacks where the cs!=0,
			how to solve this? because it is not zero....
			"""

			#rom math import isnan
			#for i in range(len(CS_typ)):

				#if CS_typ[i]==0:
			#CS_typ[CS_typ == 0] = 'nan'
					#CS_typ[i]=isnan(CS_typ[i])



			#print("old:")
			#print("E: ", E)
			#print("CS: ", CS)
			#print("new:")
			#print("E: ", E_typ)
			#print("CS: ", CS_typ)

			#print(E_typ)
			#print(CS_typ)
			#print(len(E_typ), len(CS_typ))
			#print("**")



			#print(E_)
			#print("new")
			#print(E_typ, CS_typ)
			#print("old")
			#print(E, CS)
			return E_typ, CS_typ




		"""

		with open(filename) as f:

			#begin =   'Ebeam  Z   A   Total    grnd st  isomer1 isomer2  isomer1  isomer2  didl nolevs'
			begin = '(MeV)           cs.      cs.      cs.     cs.     to total to total'
			end   =   'Ebeam =  '
			content_full = f.readlines()
			ind_begin = [line for line in range(len(content_full)) if begin in content_full[line]][0]+2  # only one element but want it as integer
			ind_end   = [line for line in range(len(content_full)) if end   in content_full[line]][0]-1  # list of different, only want the first element
			content = content_full[ind_begin:ind_end]
			print(content)

			#print("ind_begin: ", ind_begin)
			#print("ind_end: ", ind_end)

			E  = np.genfromtxt(filename, delimiter=' ', usecols=[0],skip_header=56, skip_footer=(len(content_full)-len(content)))
			#Z_  = np.genfromtxt(filename, delimiter=' ', usecols=[1], skip_header=56, skip_footer=(len(content_full)-len(content)))
			#A_  = np.genfromtxt(filename, delimiter=' ', usecols=[2], skip_header=56, skip_footer=(len(content_full)-len(content)))

			CS = np.genfromtxt(filename, delimiter=' ', usecols=[5], skip_header=56, skip_footer=(len(content_full)-len(content)))
			E_new = []; CS_new = []
			Z = ' ' + Z + ' '
			A = ' ' + A + ' '
			for lines in range(len(content)):
				#print(lines)
				if Z in content[lines] and A in content[lines]:
					#print(Z,A)
					E_new.append(E[lines])
					CS_new.append(CS[lines])
					#print(Z, A)


			f.close()
		return np.array((E_new)), np.array((CS_new))
		"""
	def interpolation(self, x,y, tendl=False):
		#print(x)

		no = []; yes = []
		for i in range(len(y)):
			if y[i-1]>y[i]:
				#print("**")
				#print(x[i])
				#print(y[i-1], y[i])
				yes.append(i)
			else:
				#print("@@")
				#print(y[i-1], y[i])
				#print(x[i])
				no.append(i)

		#if no[0]==1:
		#	print(y[no[0]])
		#	print(y[no[1]])



		### ZERO PADDING WORKS!!!!
		if tendl==False:
			if x[0]!=0:
				zero_padding = np.linspace(0,x[0]-0.5,10)
				zeros_y = np.zeros((len(zero_padding)))


				x = np.concatenate((zero_padding, x))
				y = np.concatenate((zeros_y, y))


		#print(y)


		#if x[0]!=0 and y[0]!=0:

		tck = interpolate.splrep(x, y, s=0)
		x_new = np.linspace(1, 40, 1000)
		#x_new = np.linspace(0, 40, 1000)
		#for i in range(len(x_new)):
			#y_new = interpolate.splev(x_new[i], tck, der=0)
		y_new = interpolate.splev(x_new, tck, der=0)




		#for i in range(len(y_new[:50])):
		#	if y_new[i-1]> y_new[i]:
		#		print("cross section decreases")
		#	else:
		#		print("cross section increases")
			#print(y_new[i], y_new[i-1])

		return x_new, y_new


	def ALICE(self, foil, A, Z, CS_colonne=4):

		f_Ni = self.path + '/../Alice/plot_{}'.format('natNi_20')
		f_Cu = self.path + '/../Alice/plot_{}'.format('natCu_20')
		f_Fe = self.path + '/../Alice/plot_{}'.format('natFe_20')
		f_Ir = self.path + '/../Alice/plot_{}'.format('natIr_20')


		if foil == 'Ni':
			filename=f_Ni
		elif foil == 'Cu':
			filename = f_Cu
		elif foil == 'Fe':
			filename = f_Fe
		elif foil == 'Ir':
			filename = f_Ir

		with open(filename) as f:
			content = f.readlines()
			for s in content:
				#line = ' '.join(s).split()
				line = " ".join(s.split())
				#print(line)

			#print(content)
			E_all = np.genfromtxt(filename, delimiter=' ', usecols=[0])#, skip_header=2)
			CS_all = np.genfromtxt(filename, delimiter=' ', usecols=[CS_colonne])#, skip_header=2)
			Z_ = np.genfromtxt(filename, delimiter=' ', usecols=[2])#, skip_header=2)
			A_ = np.genfromtxt(filename, delimiter=' ', usecols=[3])#, skip_header=2)

			E = []; CS = []
			#print(A, Z)
			Z = ' ' + Z + ' ' # must change to this so that it doesnt get mixed up by other line
			A = ' ' + A + ' '
			for lines in range(len(content)):
				if (A in content[lines]) and (Z in content[lines]):
					#print(content[lines])
					#print("line: ", lines)
					#print("A: ", A_[lines])
					#print("Z: ", Z_[lines])

					E.append(E_all[lines])
					CS.append(CS_all[lines])


		E_new, CS_new = self.interpolation(E, CS)
		#plt.plot(E_new, CS_new)
		#plt.show()
		return E_new, CS_new
		#return E, CS




	def ALICE_isotopic(self, foil, A, Z, CS_colonne=4):
		#print("ALICE IN SIM")
		#print(foil, A, Z, CS_colonne)
		#print("Alice")




		if foil == 'Ir':
			abund_191Ir = 0.373 ; abund_193Ir = 0.627

			f_191Ir = self.path + '/../Alice/plot_{}'.format('191Ir')
			f_193Ir = self.path + '/../Alice/plot_{}'.format('193Ir')

			E_191Ir, CS_191Ir = self.extract_from_alicefiles(f_191Ir, A, Z, CS_colonne)
			E_193Ir, CS_193Ir = self.extract_from_alicefiles(f_193Ir, A, Z, CS_colonne)

			CS = CS_191Ir*abund_191Ir + CS_193Ir*abund_193Ir
			E  = E_193Ir

			E_new, CS_new = self.interpolation(E, CS)

			#print(E_new)
			#print(CS_new)
			return E_new, CS_new
			"""
			plt.plot(E_new, CS_new, label='interpol')
			plt.plot(E_191Ir, CS_191Ir, label='191Ir')
			plt.plot(E_193Ir, CS_193Ir, label='193Ir')
			plt.plot(E, CS, label='tot')
			plt.legend()
			plt.show()
			"""
		elif foil=='Cu':
			abund_63Cu = 0.6915 ; abund_65Cu = 0.3085

			f_63Cu = self.path + '/../Alice/plot_{}'.format('63Cu')
			f_65Cu = self.path + '/../Alice/plot_{}'.format('65Cu')

			E_63Cu, CS_63Cu = self.extract_from_alicefiles(f_63Cu, A, Z, CS_colonne)
			E_65Cu, CS_65Cu = self.extract_from_alicefiles(f_65Cu, A, Z, CS_colonne)

			CS = CS_63Cu*abund_63Cu + CS_65Cu*abund_65Cu


			E  = E_65Cu
			#return E, CS

			E_new, CS_new = self.interpolation(E, CS)
			return E_new, CS_new

		elif foil=='Ni':
			#abund_63Cu = 0.6915 ; abund_65Cu = 0.3085

			#abund_54Fe=0.0545; abund_56Fe=0.91754; abund_57Fe=0.02119; abund_58Fe=0.00282

			abund_58Ni = 0.68077; abund_60Ni = 0.26233; abund_61Ni = 0.011399; abund_62Ni = 0.036346; abund_64Ni = 0.009255;


			f_58Ni = self.path + '/../Alice/plot_{}'.format('58Ni')
			f_60Ni = self.path + '/../Alice/plot_{}'.format('60Ni')
			f_61Ni = self.path + '/../Alice/plot_{}'.format('61Ni')
			f_62Ni = self.path + '/../Alice/plot_{}'.format('62Ni')
			f_64Ni = self.path + '/../Alice/plot_{}'.format('64Ni')

			E_58Ni, CS_58Ni = self.extract_from_alicefiles(f_58Ni, A, Z, CS_colonne)
			E_60Ni, CS_60Ni = self.extract_from_alicefiles(f_60Ni, A, Z, CS_colonne)
			E_61Ni, CS_61Ni = self.extract_from_alicefiles(f_61Ni, A, Z, CS_colonne)
			E_62Ni, CS_62Ni = self.extract_from_alicefiles(f_62Ni, A, Z, CS_colonne)
			E_64Ni, CS_64Ni = self.extract_from_alicefiles(f_64Ni, A, Z, CS_colonne)



			CS = CS_58Ni*abund_58Ni + CS_60Ni*abund_60Ni+ CS_61Ni*abund_61Ni + CS_62Ni*abund_62Ni+ CS_64Ni*abund_64Ni
			E  = E_64Ni

			"""
			CS_58Ni = CS_58Ni*abund_58Ni
			CS_60Ni *= abund_60Ni
			CS_61Ni *= abund_61Ni
			CS_62Ni *= abund_62Ni
			CS_64Ni *= abund_64Ni

			cs_withoutzeros_summed = []

			for i in range(len(E)):
				print("**")
				print(i)
				intermediate_sum = []
				for cs_list in [CS_58Ni, CS_60Ni, CS_61Ni, CS_62Ni, CS_64Ni]:
					if cs_list[i]!= 0:
						intermediate_sum.append(cs_list[i])
						print("nonzero:")
						print(cs_list[i])
					else:
						print("zero:")
						print(cs_list[i])

				cs.cs_withoutzeros_summed
			#CS_ = []
			#for CS_list in [CS_58Ni, CS_60Ni, CS_61Ni, CS_62Ni, CS_64Ni]:
			#	for cs in CS_list:
			#		if cs!=0:
			"""





			#return E, CS

			E_new, CS_new = self.interpolation(E, CS)
			return E_new, CS_new

		elif foil == 'Fe':
			abund_54Fe=0.0545; abund_56Fe=0.91754; abund_57Fe=0.02119; abund_58Fe=0.00282


			f_54Fe = self.path + '/../Alice/plot_{}'.format('54Fe')
			f_56Fe = self.path + '/../Alice/plot_{}'.format('56Fe')
			f_57Fe = self.path + '/../Alice/plot_{}'.format('56Fe')
			f_58Fe = self.path + '/../Alice/plot_{}'.format('58Fe')


			E_54Fe, CS_54Fe = self.extract_from_alicefiles(f_54Fe, A, Z, CS_colonne)
			E_56Fe, CS_56Fe = self.extract_from_alicefiles(f_56Fe, A, Z, CS_colonne)
			E_57Fe, CS_57Fe = self.extract_from_alicefiles(f_57Fe, A, Z, CS_colonne)
			E_58Fe, CS_58Fe = self.extract_from_alicefiles(f_58Fe, A, Z, CS_colonne)


			CS = CS_54Fe*abund_53Fe + CS_56Fe*abund_56Fe+ CS_57Fe*abund_57Fe + CS_58Fe*abund_58Fe
			E  = E_58Fe
			return E, CS

			#E_new, CS_new = self.interpolation(E, CS)
			#return E_new, CS_new


		#else:
		#	print("give a proper ALICE-foil")






			#try:
			#E_191Ir, CS_191Ir = self.extract_from_alicefiles(f_191Ir, A, Z)
			#if len(E_191Ir) > 0:
			#	E_new_191Ir, CS_new_191Ir = self.interpolation(E_191Ir, CS_191Ir)
			#	print(E_new_191Ir)
			#E_193Ir, CS_193Ir = self.extract_from_alicefiles(f_193Ir, A, Z)

			#print(E_193Ir)
			#if len(E_193Ir) > 0:
				#E_new_193Ir, CS_new_193Ir = self.interpolation(E_193Ir, CS_193Ir)
		#plt.plot(E_193Ir, CS_193Ir, label='ALICE', linestyle=':')
		#plt.legend()
		#plt.show()
		#print(E_191Ir)
		#print(E_193Ir)



		#if os.path.isfile(f_191Ir):
		#		print("f_191Ir")
		#else:
		#	print("NOT  BUT ", f_193Ir)
		#if os.path.isfile(f_193Ir):
		#	print("f_193Ir")


		"""
		filename = self.path + '/../Alice/plot_{}'.format(foil)

		with open(filename) as f:

			begin =   'Ebeam  Z   A   Total    grnd st  isomer1 isomer2  isomer1  isomer2  didl nolevs'
			end   =   'Ebeam =  '
			content_full = f.readlines()
			ind_begin = [line for line in range(len(content_full)) if begin in content_full[line]][0]+2  # only one element but want it as integer
			ind_end   = [line for line in range(len(content_full)) if end   in content_full[line]][0]-1  # list of different, only want the first element
			content = content_full[ind_begin:ind_end]

			#print("ind_begin: ", ind_begin)
			#print("ind_end: ", ind_end)


			E  = np.genfromtxt(filename, delimiter=' ', usecols=[0],skip_header=56, skip_footer=(len(content_full)-len(content)))
			#Z_  = np.genfromtxt(filename, delimiter=' ', usecols=[1], skip_header=56, skip_footer=(len(content_full)-len(content)))
			#A_  = np.genfromtxt(filename, delimiter=' ', usecols=[2], skip_header=56, skip_footer=(len(content_full)-len(content)))

			CS = np.genfromtxt(filename, delimiter=' ', usecols=[5], skip_header=56, skip_footer=(len(content_full)-len(content)))
			E_new = []; CS_new = []
			Z = ' ' + Z + ' '
			A = ' ' + A + ' '
			for lines in range(len(content)):
				if Z in content[lines] and A in content[lines]:
					#print(Z,A)
					E_new.append(E[lines])
					CS_new.append(CS[lines])
					#print(Z, A)
					#print(content[lines])


			f.close()



		#print("E: ",E_new)
		#print("CS: ", CS_new)





		return E_new, CS_new
		"""

	def TALYS(self,foil, A, Z, file_ending='.tot'):
		# Z = 0XX, A=0XX

		filename = self.path + '/../Talys/' +foil+ '/rp'+Z+A+ file_ending #'.tot'
		#filename = self.path + '/../Talys/' +foil+ '/rp'+Z+A+'.L02'
		E  = np.genfromtxt(filename, delimiter=' ', usecols=[0],skip_header=5)
		CS = np.genfromtxt(filename, delimiter=' ', usecols=[1],skip_header=5)

		#print(CS)
		#print(CS)
		#print(E)

		#plt.plot(E,CS)
		#plt.show()
		E_new, CS_new = self.interpolation(E, CS)
		return E_new, CS_new


	def Tendl(self, foil, A, Z, file_ending='.tot'):

		#print("foil: ",foil )
		#print("Z: ", Z )
		#print("A: ", A  )

		if foil == 'Ir':
			#A = ['191', '193'] # stable iridium isotopes
			abund_191Ir = 0.373 ; abund_193Ir = 0.627
			#file_ending =
			f_191Ir = self.path + '/../Tendl/' + foil + '/rp077191_' + Z+ A + file_ending + '.txt'
			f_193Ir = self.path + '/../Tendl/' + foil + '/rp077193_' + Z +A + file_ending + '.txt'

			#print("Ir 193 file: ",f_193Ir)
			#print("Ir 191 file: ",f_191Ir)
			if os.path.isfile(f_191Ir):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_191Ir exists")
				CS_191Ir = np.genfromtxt(f_191Ir, delimiter=' ', usecols=[1],skip_header=5)
				E = np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			else:
				#print("Ir 191 file does not exist")
				CS_191Ir = 0
				E_191Ir =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_193Ir):
				#print("f_193Ir exists")
				CS_193Ir = np.genfromtxt(f_193Ir, delimiter=' ', usecols=[1],skip_header=5)
				E = np.genfromtxt(f_193Ir, delimiter=' ', usecols=[0],skip_header=5)
			else:
				#print("Ir 193 file does not exist")
				CS_193Ir = 0
				E_193Ir = 0#np.genfromtxt(f_193Ir, delimiter=' ', usecols=[0],skip_header=5)

			#E = E_191Ir*abund_191Ir + E_193Ir*abund_193Ir
			#if E_191Ir != 0:
			#	E = E_191Ir
			#else:
			#	E = E_193Ir
			CS = CS_191Ir*abund_191Ir + CS_193Ir*abund_193Ir

		elif foil == 'Cu':
			abund_63Cu = 0.6915 ; abund_65Cu = 0.3085

			f_63Cu = self.path + '/../Tendl/' + foil + '/rp029063_' + Z + A + file_ending + '.txt'
			f_65Cu = self.path + '/../Tendl/' + foil + '/rp029065_' + Z + A + file_ending + '.txt'
			#print(f_63Cu)
			if os.path.isfile(f_63Cu):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_63Cu exists")
				CS_63Cu = np.genfromtxt(f_63Cu, delimiter=' ', usecols=[1],skip_header=5)
				E = np.genfromtxt(f_63Cu, delimiter=' ', usecols=[0],skip_header=5)
			else:
				print("Cu 63 file does not exist")
				CS_63Cu = 0
				E_63Cu =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_65Cu):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_65Cu exists")
				CS_65Cu = np.genfromtxt(f_65Cu, delimiter=' ', usecols=[1],skip_header=5)
				E = np.genfromtxt(f_65Cu, delimiter=' ', usecols=[0],skip_header=5)
			else:
				#print("Cu 65 file does not exist")
				CS_65Cu = 0
				E_65Cu =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)


			#E = E_63Cu*abund_63Cu + E_65Cu*abund_65Cu
			CS = CS_63Cu*abund_63Cu + CS_65Cu*abund_65Cu

			#E_new, CS_new = self.interpolation(E, CS)
			#plt.plot(E,CS)
			#plt.plot(E_new, CS_new)
			#plt.show()

		elif foil == 'Fe':
			abund_54Fe=0.0545; abund_56Fe=0.91754; abund_57Fe=0.02119; abund_58Fe=0.00282
			f_54Fe = self.path + '/../Tendl/' + foil + '/rp026054_' + Z + A + file_ending + '.txt'
			f_56Fe = self.path + '/../Tendl/' + foil + '/rp026056_' + Z + A + file_ending + '.txt'
			f_57Fe = self.path + '/../Tendl/' + foil + '/rp026057_' + Z + A + file_ending + '.txt'
			f_58Fe = self.path + '/../Tendl/' + foil + '/rp026058_' + Z + A + file_ending + '.txt'


			if os.path.isfile(f_54Fe):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_54Fe exists")
				CS_54Fe = np.genfromtxt(f_54Fe, delimiter=' ', usecols=[1],skip_header=5)
				E = np.genfromtxt(f_54Fe, delimiter=' ', usecols=[0],skip_header=5)
			else:
				#print("Fe 54 file does not exist")
				CS_54Fe = 0
				E_54Fe =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_56Fe):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_54Fe exists")
				CS_56Fe = np.genfromtxt(f_56Fe, delimiter=' ', usecols=[1],skip_header=5)
				E = np.genfromtxt(f_56Fe, delimiter=' ', usecols=[0],skip_header=5)
			else:
				#print("Fe 56 file does not exist")
				CS_56Fe = 0
				E_56Fe =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_57Fe):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_54Fe exists")
				CS_57Fe = np.genfromtxt(f_57Fe, delimiter=' ', usecols=[1],skip_header=5)
				E = np.genfromtxt(f_57Fe, delimiter=' ', usecols=[0],skip_header=5)
			else:
				#print("Fe 57 file does not exist")
				CS_57Fe = 0
				E_57Fe =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_58Fe):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_54Fe exists")
				CS_58Fe = np.genfromtxt(f_58Fe, delimiter=' ', usecols=[1],skip_header=5)
				E = np.genfromtxt(f_58Fe, delimiter=' ', usecols=[0],skip_header=5)
			else:
				#print("Fe 58 file does not exist")
				CS_58Fe = 0
				E_58Fe =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			#E = E_54Fe*abund_54Fe + E_56Fe*abund_56Fe + E_57Fe*abund_57Fe + E_58Fe*abund_58Fe
			CS = CS_54Fe*abund_54Fe + CS_56Fe*abund_56Fe + CS_57Fe*abund_57Fe + CS_58Fe*abund_58Fe
			#if E_54Fe == 0 and E_56Fe==0 and E_57Fe == 0:
				#E = E_58Fe


		elif foil == 'Ni':
			abund_58Ni = 0.68077; abund_60Ni = 0.26233; abund_61Ni = 0.011399; abund_62Ni = 0.036346; abund_64Ni = 0.009255;


			f_58Ni = self.path + '/../Tendl/' + foil + '/rp028058_' + Z + A + file_ending + '.txt'
			f_60Ni = self.path + '/../Tendl/' + foil + '/rp028060_' + Z + A + file_ending + '.txt'
			f_61Ni = self.path + '/../Tendl/' + foil + '/rp028061_' + Z + A + file_ending + '.txt'
			f_62Ni = self.path + '/../Tendl/' + foil + '/rp028062_' + Z + A + file_ending + '.txt'
			f_64Ni = self.path + '/../Tendl/' + foil + '/rp028064_' + Z + A + file_ending + '.txt'

			if os.path.isfile(f_58Ni):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_58Ni exists")
				CS_58Ni = np.genfromtxt(f_58Ni, delimiter=' ', usecols=[1],skip_header=5)
				E_58Ni = np.genfromtxt(f_58Ni, delimiter=' ', usecols=[0],skip_header=5)
				E = E_58Ni
			else:
				#print("Ni 58 file does not exist")
				CS_58Ni = 0
				E_58Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_60Ni):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_60Ni exists")
				CS_60Ni = np.genfromtxt(f_60Ni, delimiter=' ', usecols=[1],skip_header=5)
				E_60Ni = np.genfromtxt(f_60Ni, delimiter=' ', usecols=[0],skip_header=5)
				E = E_60Ni
			else:
				#print("Ni 60 file does not exist")
				CS_60Ni = 0
				E_60Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)
			if os.path.isfile(f_61Ni):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_61Ni exists")
				CS_61Ni = np.genfromtxt(f_61Ni, delimiter=' ', usecols=[1],skip_header=5)
				E_61Ni = np.genfromtxt(f_61Ni, delimiter=' ', usecols=[0],skip_header=5)
				E = E_61Ni
			else:
				#print("Ni 61 file does not exist")
				CS_61Ni = 0
				E_61Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)
			if os.path.isfile(f_62Ni):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_62Ni exists")
				CS_62Ni = np.genfromtxt(f_62Ni, delimiter=' ', usecols=[1],skip_header=5)
				E_62Ni = np.genfromtxt(f_62Ni, delimiter=' ', usecols=[0],skip_header=5)
				E = E_62Ni
			else:
				#print("Ni 62 file does not exist")
				CS_62Ni = 0
				E_62Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)
			if os.path.isfile(f_64Ni):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_64Ni exists")
				CS_64Ni = np.genfromtxt(f_64Ni, delimiter=' ', usecols=[1],skip_header=5)
				E_64Ni = np.genfromtxt(f_64Ni, delimiter=' ', usecols=[0],skip_header=5)
				E = E_64Ni
			else:
				#print("Ni 64 file does not exist")
				CS_64Ni = 0
				E_64Ni =  0



			CS = CS_58Ni*abund_58Ni + CS_60Ni*abund_60Ni + CS_61Ni*abund_61Ni + CS_62Ni*abund_62Ni + CS_64Ni*abund_64Ni
			#E = E_58Ni*abund_58Ni + E_60Ni*abund_60Ni + E_61Ni*abund_61Ni + E_62Ni*abund_62Ni + E_64Ni*abund_64Ni

		#plt.plot(E, CS)
		#plt.show()
		#print(E, CS)

		E_new, CS_new = self.interpolation(E, CS, tendl=True)
		return E_new, CS_new

	def EMPIRE(self,foil, A, Z, reaction, isomer=None):
		#print(reaction)
		#print("Hello")


		numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
		product = reaction[-2:]

		for i in numbs:
			if reaction[-2]==i:
				product = reaction[-1]
		if isomer!=None:
			A = A + isomer

		if foil == 'Ir':
			abund_191Ir = 0.373 ; abund_193Ir = 0.627
			f_191Ir = self.path + '/../EMPIRE/' + foil + '/191Ir/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			f_193Ir = self.path + '/../EMPIRE/' + foil + '/193Ir/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			#print(f_191Ir)
			#print(f_191Ir)
			#print(f_193Ir)
			#print(f_191Ir)
			if os.path.isfile(f_191Ir):
				CS_191Ir = np.genfromtxt(f_191Ir, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_191Ir, delimiter='\t', usecols=[0])
				#print(E)
			else:
				#print("Heelo")
				print("EMPIRE does not plot for 191Ir")
				CS_191Ir = 0
				E_191Ir =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_193Ir):
				#print("f_193Ir exists"
				CS_193Ir = np.genfromtxt(f_193Ir, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_193Ir, delimiter='\t', usecols=[0])
			else:
				print("EMPIRE does not plot for 193Ir")
				CS_193Ir = 0
				E_193Ir = 0#np.genfromtxt(f_193Ir, delimiter=' ', usecols=[0],skip_header=5)
			CS = CS_191Ir*abund_191Ir + CS_193Ir*abund_193Ir
			# print(CS)
			# print(E)
		elif foil == 'Ni':
			abund_58Ni = 0.68077; abund_60Ni = 0.26233; abund_61Ni = 0.011399; abund_62Ni = 0.036346; abund_64Ni = 0.009255;

			#f_191Ir = self.path + '/../EMPIRE/' + foil + '/191Ir/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			f_58Ni = self.path + '/../EMPIRE/' + foil + '/58Ni/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			f_60Ni = self.path + '/../EMPIRE/' + foil + '/60Ni/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			f_61Ni = self.path + '/../EMPIRE/' + foil + '/61Ni/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			f_62Ni = self.path + '/../EMPIRE/' + foil + '/62Ni/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			f_64Ni = self.path + '/../EMPIRE/' + foil + '/64Ni/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			#print(f_58Ni)
			if os.path.isfile(f_58Ni):
				CS_58Ni = np.genfromtxt(f_58Ni, delimiter='\t', usecols=[1])
				E_58Ni = np.genfromtxt(f_58Ni, delimiter='\t', usecols=[0])
				E = E_58Ni
			else:
				print("EMPIRE does not plot for 58Ni")
				CS_58Ni = 0
				E_58Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_60Ni):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_58Ni exists")
				CS_60Ni = np.genfromtxt(f_60Ni, delimiter='\t', usecols=[1])
				E_60Ni = np.genfromtxt(f_60Ni, delimiter='\t', usecols=[0])
				E = E_60Ni
			else:
				#print("Ni 58 file does not exist")
				print("EMPIRE does not plot for 60Ni")
				CS_60Ni = 0
				E_60Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_61Ni):
				CS_61Ni = np.genfromtxt(f_61Ni, delimiter='\t', usecols=[1])
				E_61Ni = np.genfromtxt(f_61Ni, delimiter='\t', usecols=[0])
				E = E_61Ni
			else:
				print("EMPIRE does not plot for 61Ni")
				CS_61Ni = 0
				E_61Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_62Ni):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_58Ni exists")
				CS_62Ni = np.genfromtxt(f_62Ni, delimiter='\t', usecols=[1])
				E_62Ni = np.genfromtxt(f_62Ni, delimiter='\t', usecols=[0])
				E = E_62Ni
			else:
				#print("Ni 58 file does not exist")
				print("EMPIRE does not plot for 62Ni")
				CS_62Ni = 0
				E_62Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)
			if os.path.isfile(f_64Ni):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_58Ni exists")
				CS_64Ni = np.genfromtxt(f_64Ni, delimiter='\t', usecols=[1])
				E_64Ni = np.genfromtxt(f_64Ni, delimiter='\t', usecols=[0])
				E = E_64Ni
			else:
				#print("Ni 58 file does not exist")
				print("EMPIRE does not plot for 64Ni")
				CS_64Ni = 0
				E_64Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			CS = CS_58Ni*abund_58Ni + CS_60Ni*abund_60Ni + CS_61Ni*abund_61Ni + CS_62Ni*abund_62Ni + CS_64Ni*abund_64Ni

		elif foil == 'Cu':
			abund_63Cu = 0.6915 ; abund_65Cu = 0.3085
			f_63Cu = self.path + '/../EMPIRE/' + foil + '/63Cu/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			f_65Cu = self.path + '/../EMPIRE/' + foil + '/65Cu/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			#f_63Cu = self.path + '/../Tendl/' + foil + '/rp029063_' + Z + A + file_ending + '.txt'
			#f_65Cu = self.path + '/../Tendl/' + foil + '/rp029065_' + Z + A + file_ending + '.txt'
			#print(f_63Cu)
			if os.path.isfile(f_63Cu):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_63Cu exists")
				CS_63Cu = np.genfromtxt(f_63Cu, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_63Cu, delimiter='\t', usecols=[0])
			else:
				#print("Cu 63 file does not exist")
				print("EMPIRE does not plot for 63Cu")
				CS_63Cu = 0
				E_63Cu =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_65Cu):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_65Cu exists")
				CS_65Cu = np.genfromtxt(f_65Cu, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_65Cu, delimiter='\t', usecols=[0])
			else:
				#print("Cu 65 file does not exist")
				print("EMPIRE does not plot for 65Cu")
				CS_65Cu = 0
				E_65Cu =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)


			#E = E_63Cu*abund_63Cu + E_65Cu*abund_65Cu
			CS = CS_63Cu*abund_63Cu + CS_65Cu*abund_65Cu

		elif foil == 'Fe':
			abund_54Fe=0.0545; abund_56Fe=0.91754; abund_57Fe=0.02119; abund_58Fe=0.00282
			f_54Fe = self.path + '/../EMPIRE/' + foil + '/54Fe/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			f_56Fe = self.path + '/../EMPIRE/' + foil + '/56Fe/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			f_57Fe = self.path + '/../EMPIRE/' + foil + '/57Fe/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			f_58Fe = self.path + '/../EMPIRE/' + foil + '/58Fe/' + Z  + '-' +  product + '-'  + A  + '_empire.txt'
			#f_54Fe = self.path + '/../Tendl/' + foil + '/rp026054_' + Z + A + file_ending + '.txt'
			#f_56Fe = self.path + '/../Tendl/' + foil + '/rp026056_' + Z + A + file_ending + '.txt'
			#f_57Fe = self.path + '/../Tendl/' + foil + '/rp026057_' + Z + A + file_ending + '.txt'
			#f_58Fe = self.path + '/../Tendl/' + foil + '/rp026058_' + Z + A + file_ending + '.txt'

			if os.path.isfile(f_54Fe):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_54Fe exists")
				CS_54Fe = np.genfromtxt(f_54Fe, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_54Fe, delimiter='\t', usecols=[0])
			else:
				#print("Fe 54 file does not exist")
				print("EMPIRE does not plot for 54Fe")
				CS_54Fe = 0
				E_54Fe =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_56Fe):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_54Fe exists")
				CS_56Fe = np.genfromtxt(f_56Fe, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_56Fe, delimiter='\t', usecols=[0])
			else:
				#print("Fe 56 file does not exist")
				print("EMPIRE does not plot for 56Fe")
				CS_56Fe = 0
				E_56Fe =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_57Fe):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_54Fe exists")
				CS_57Fe = np.genfromtxt(f_57Fe, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_57Fe, delimiter='\t', usecols=[0])
			else:
				#print("Fe 57 file does not exist")
				print("EMPIRE does not plot for 57Fe")
				CS_57Fe = 0
				E_57Fe =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_58Fe):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_54Fe exists")
				CS_58Fe = np.genfromtxt(f_58Fe, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_58Fe, delimiter='\t', usecols=[0])
			else:
				#print("Fe 58 file does not exist")
				print("EMPIRE does not plot for 58Fe")
				CS_58Fe = 0
				E_58Fe =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			#E = E_54Fe*abund_54Fe + E_56Fe*abund_56Fe + E_57Fe*abund_57Fe + E_58Fe*abund_58Fe
			CS = CS_54Fe*abund_54Fe + CS_56Fe*abund_56Fe + CS_57Fe*abund_57Fe + CS_58Fe*abund_58Fe


		#if E[0]==1:
		#	zero_padding = np.linspace(0,1,5)
		#	cs_zeros = np.zeros(len(zero_padding))
		#	E = np.concatenate((zero_padding, E))
		#	CS = np.concatenate((cs_zeros, CS))
		#print(E)


		E, CS = self.interpolation(E, CS)
		#plt.plot(E,CS)
		#plt.show()
		#E = np.concatenate((zero_padding, E))
		#CS = np.concatenate((zero_padding, CS))
		#plt.plot(E, CS)
		#plt.show()
		return E, CS

	def COH(self, foil, A, Z, reaction, isomer=None):
		#print(reaction)
		numbs = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
		product = reaction[-2:]
		for i in numbs:
			if reaction[-2]==i:
				product = reaction[-1]
		if isomer!=None:
			product = product + isomer
		if foil == 'Ir':
			abund_191Ir = 0.373 ; abund_193Ir = 0.627
			f_191Ir = self.path + '/../Coh/IrridiumCoH/' + foil + '/191Ir/' + Z  + '-' + A + product + '_coh.txt'
			f_193Ir = self.path + '/../Coh/IrridiumCoH/' + foil + '/193Ir/' + Z  + '-' + A + product + '_coh.txt'
			#print(f_191Ir)
			if os.path.isfile(f_191Ir):
				CS_191Ir = np.genfromtxt(f_191Ir, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_191Ir, delimiter='\t', usecols=[0])
			else:
				print("Coh file not found for 191Ir")
				CS_191Ir = 0
				E_191Ir =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_193Ir):
				#print("f_193Ir exists"
				CS_193Ir = np.genfromtxt(f_193Ir, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_193Ir, delimiter='\t', usecols=[0])
			else:
				print("Coh file not found for 193Ir")
				CS_193Ir = 0
				E_193Ir = 0#np.genfromtxt(f_193Ir, delimiter=' ', usecols=[0],skip_header=5)
			CS = CS_191Ir*abund_191Ir + CS_193Ir*abund_193Ir

		elif foil == 'Ni':
			abund_58Ni = 0.68077; abund_60Ni = 0.26233; abund_61Ni = 0.011399; abund_62Ni = 0.036346; abund_64Ni = 0.009255;


			f_58Ni = self.path + '/../Coh/IrridiumCoH/' + foil + '/58Ni/' + Z  + '-' + A + product + '_coh.txt'
			f_60Ni = self.path + '/../Coh/IrridiumCoH/' + foil + '/60Ni/' + Z  + '-' + A + product + '_coh.txt'
			f_61Ni = self.path + '/../Coh/IrridiumCoH/' + foil + '/61Ni/' + Z  + '-' + A + product + '_coh.txt'
			f_62Ni = self.path + '/../Coh/IrridiumCoH/' + foil + '/62Ni/' + Z  + '-' + A + product + '_coh.txt'
			f_64Ni = self.path + '/../Coh/IrridiumCoH/' + foil + '/64Ni/' + Z  + '-' + A + product + '_coh.txt'

			if os.path.isfile(f_58Ni):
				CS_58Ni = np.genfromtxt(f_58Ni, delimiter='\t', usecols=[1])
				E_58Ni = np.genfromtxt(f_58Ni, delimiter='\t', usecols=[0])
				E = E_58Ni
			else:
				print("Coh file not found for 58Ni")
				CS_58Ni = 0
				E_58Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_60Ni):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_58Ni exists")
				CS_60Ni = np.genfromtxt(f_60Ni, delimiter='\t', usecols=[1])
				E_60Ni = np.genfromtxt(f_60Ni, delimiter='\t', usecols=[0])
				E = E_60Ni
			else:
				#print("Ni 58 file does not exist")
				print("Coh file not found for 60Ni")
				CS_60Ni = 0
				E_60Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_61Ni):
				CS_61Ni = np.genfromtxt(f_61Ni, delimiter='\t', usecols=[1])
				E_61Ni = np.genfromtxt(f_61Ni, delimiter='\t', usecols=[0])
				E = E_61Ni
			else:
				print("Coh file not found for 61Ni")
				CS_61Ni = 0
				E_61Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_62Ni):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_58Ni exists")
				CS_62Ni = np.genfromtxt(f_62Ni, delimiter='\t', usecols=[1])
				E_62Ni = np.genfromtxt(f_62Ni, delimiter='\t', usecols=[0])
				E = E_62Ni
			else:
				#print("Ni 58 file does not exist")
				print("Coh file not found for 62Ni")
				CS_62Ni = 0
				E_62Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)
			if os.path.isfile(f_64Ni):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_58Ni exists")
				CS_64Ni = np.genfromtxt(f_64Ni, delimiter='\t', usecols=[1])
				E_64Ni = np.genfromtxt(f_64Ni, delimiter='\t', usecols=[0])
				E = E_64Ni
			else:
				#print("Ni 58 file does not exist")
				print("Coh file not found for 64Ni")
				CS_64Ni = 0
				E_64Ni =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			CS = CS_58Ni*abund_58Ni + CS_60Ni*abund_60Ni + CS_61Ni*abund_61Ni + CS_62Ni*abund_62Ni + CS_64Ni*abund_64Ni

		elif foil == 'Cu':
			abund_63Cu = 0.6915 ; abund_65Cu = 0.3085
			f_63Cu = self.path + '/../Coh/IrridiumCoH/' + foil + '/63Cu/' + Z  + '-' + A + product + '_coh.txt'
			f_65Cu = self.path + '/../Coh/IrridiumCoH/' + foil + '/65Cu/' + Z  + '-' + A + product + '_coh.txt'
			#f_63Cu = self.path + '/../Tendl/' + foil + '/rp029063_' + Z + A + file_ending + '.txt'
			#f_65Cu = self.path + '/../Tendl/' + foil + '/rp029065_' + Z + A + file_ending + '.txt'
			#print(f_63Cu)
			if os.path.isfile(f_63Cu):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_63Cu exists")
				CS_63Cu = np.genfromtxt(f_63Cu, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_63Cu, delimiter='\t', usecols=[0])
			else:
				#print("Cu 63 file does not exist")
				print("Coh file not found for 63Cu")
				CS_63Cu = 0
				E_63Cu =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_65Cu):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_65Cu exists")
				CS_65Cu = np.genfromtxt(f_65Cu, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_65Cu, delimiter='\t', usecols=[0])
			else:
				# print("Cu 65 file does not exist")
				print("Coh file not found for 65Cu")
				CS_65Cu = 0
				E_65Cu =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)


			#E = E_63Cu*abund_63Cu + E_65Cu*abund_65Cu
			CS = CS_63Cu*abund_63Cu + CS_65Cu*abund_65Cu

		elif foil == 'Fe':
			abund_54Fe=0.0545; abund_56Fe=0.91754; abund_57Fe=0.02119; abund_58Fe=0.00282
			f_54Fe = self.path + '/../Coh/IrridiumCoH/' + foil + '/54Fe/' + Z  + '-' + A + product + '_coh.txt'
			f_56Fe = self.path + '/../Coh/IrridiumCoH/' + foil + '/56Fe/' + Z  + '-' + A + product + '_coh.txt'
			f_57Fe = self.path + '/../Coh/IrridiumCoH/' + foil + '/57Fe/' + Z  + '-' + A + product + '_coh.txt'
			f_58Fe = self.path + '/../Coh/IrridiumCoH/' + foil + '/58Fe/' + Z  + '-' + A + product + '_coh.txt'
			#f_54Fe = self.path + '/../Tendl/' + foil + '/rp026054_' + Z + A + file_ending + '.txt'
			#f_56Fe = self.path + '/../Tendl/' + foil + '/rp026056_' + Z + A + file_ending + '.txt'
			#f_57Fe = self.path + '/../Tendl/' + foil + '/rp026057_' + Z + A + file_ending + '.txt'
			#f_58Fe = self.path + '/../Tendl/' + foil + '/rp026058_' + Z + A + file_ending + '.txt'

			if os.path.isfile(f_54Fe):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_54Fe exists")
				CS_54Fe = np.genfromtxt(f_54Fe, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_54Fe, delimiter='\t', usecols=[0])
			else:
				#print("Fe 54 file does not exist")
				print("Coh file not found for 54Fe")
				CS_54Fe = 0
				E_54Fe =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_56Fe):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_54Fe exists")
				CS_56Fe = np.genfromtxt(f_56Fe, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_56Fe, delimiter='\t', usecols=[0])
			else:
				#print("Fe 56 file does not exist")
				print("Coh file not found for 56Fe")
				CS_56Fe = 0
				E_56Fe =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_57Fe):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_54Fe exists")
				CS_57Fe = np.genfromtxt(f_57Fe, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_57Fe, delimiter='\t', usecols=[0])
			else:
				#print("Fe 57 file does not exist")
				print("Coh file not found for 57Fe")
				CS_57Fe = 0
				E_57Fe =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_58Fe):
				#print("Ir 191 file: ",f_191Ir)
				#print("f_54Fe exists")
				CS_58Fe = np.genfromtxt(f_58Fe, delimiter='\t', usecols=[1])
				E = np.genfromtxt(f_58Fe, delimiter='\t', usecols=[0])
			else:
				#print("Fe 58 file does not exist")
				print("Coh file not found for 58Fe")
				CS_58Fe = 0
				E_58Fe =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			#E = E_54Fe*abund_54Fe + E_56Fe*abund_56Fe + E_57Fe*abund_57Fe + E_58Fe*abund_58Fe
			CS = CS_54Fe*abund_54Fe + CS_56Fe*abund_56Fe + CS_57Fe*abund_57Fe + CS_58Fe*abund_58Fe


		#if E[0]==1:
		#	zero_padding = np.linspace(0,1,5)
		#	cs_zeros = np.zeros(len(zero_padding))
		#	E = np.concatenate((zero_padding, E))
		#	CS = np.concatenate((cs_zeros, CS))
		#print(E)


		E, CS = self.interpolation(E, CS)
		#E = np.concatenate((zero_padding, E))
		#CS = np.concatenate((zero_padding, CS))
		#plt.plot(E, CS)
		#plt.show()
		return E, CS


			#plt.plot(E, CS)
			#plt.show()



	def EXFOR(self, reaction, independent=True):

		if independent==True:
			filename = self.path + '/../EXFOR/' + reaction + '_ind.txt'
		elif independent==False:
			filename = self.path + '/../EXFOR/' + reaction + '_cum.txt'

		#print("From sim cross sections, filename is: ", filename)


		#filename = self.path + '/../EXFOR/' + reaction + '.txt'
		#print(filename)
		#print(reaction)

		#if os.
		if os.path.isfile(filename):
			#print(filename)
			#print("file exists")

			with open(filename) as f:
				begin =   'EXFOR-ID'
				end   =   '//'
				content_full = f.readlines()
				#print(content_full)
				ind_begin = [line for line in range(len(content_full)) if begin in content_full[line]][0]+1  # only one element but want it as integer
				ind_end   = [line for line in range(len(content_full)) if end   in content_full[line]][0]  # list of different, only want the first element
				#print(ind_begin)
				#print(content_full[ind_begin])
				#print(content_full[ind_end])
				#print(ind_end)
				#print(content_full[ind_end])
				content = content_full[ind_begin:ind_end]
				#print(content)
				#print(content)

				#print(content)

				#str1 = content[0]

				#x = str1.lstrip()
				#print(x.split())
				E = []; dE=[]; CS = []; dCS=[]; author=[]
				#print(len(content))
				for ind in range(len(content)):

					string= content[ind]
					#print(string)
					string = (string.lstrip()).split()
					#print(string[5])

					#if string[5]=='1995,Zhao':
					#	author.append(string[5])
					#	print("YES")
					#print(author)
					#print(ind)
					#print(string)
					E.append(float(string[0]))
					dE.append(float(string[1]))
					CS.append(float(string[2])*1e3) # in mb
					dCS.append(float(string[3])*1e3) # in mb
					#print(string[5])
					try:
						author.append(string[5]) #index 4 is equal to #
						#print("Should add ", string[5])
						#if author[ind]==string[5]:
						#	print("Success")
						#else:
							#print("Not adding")
					except:
						print(string[5], "not included in exfor data")
						pass
						#print("did not add ", string[5])
			#print("**")
			#print(author)
			#print(author)
			author_new  = []
			for auth in author:
				#print(auth)
				if '+' in auth:
					#print("in")
					author_new.append(auth.replace('+', ''))
			#print(author_new)
			return E, dE, CS, dCS, author_new
		else:
			#print("exfor file does not exist for {}".format(reaction))
			return 0, 0, 0, 0, '0'


	def multiple_reactions(self):


		colors = ['mediumpurple', 'cyan', 'palevioletred', 'darkorange', 'forestgreen', 'orchid', 'dodgerblue', 'navy', 'crimson', 'indianred', 'blue', 'black', 'yellow', 'green', 'red']

		E_194Pt, CS_194Pt = self.TALYS('Ir', '194', '078', file_ending='.tot')
		#E_193mPt, CS_193mPt = self.TALYS('Ir', '193', '078', file_ending='.L05')
		E_193Pt, CS_193Pt = self.TALYS('Ir', '193', '078', file_ending='.tot')
		E_192Pt, CS_192Pt = self.TALYS('Ir', '192', '078', file_ending='.tot')
		E_191Pt, CS_191Pt = self.Tendl('Ir', '191', '078', file_ending='.tot')
		E_190Pt, CS_190Pt = self.TALYS('Ir', '190', '078', file_ending='.tot')
		E_189Pt, CS_189Pt = self.Tendl('Ir', '189', '078', file_ending='.tot')
		E_188Pt, CS_188Pt = self.TALYS('Ir', '188', '078', file_ending='.tot')

		E_188Ir, CS_188Ir = self.TALYS('Ir', '188', '077', file_ending='.tot')
		E_189Ir, CS_189Ir = self.TALYS('Ir', '189', '077', file_ending='.tot')
		E_190Ir, CS_190Ir = self.TALYS('Ir', '190', '077', file_ending='.tot')
		E_191Ir, CS_191Ir = self.TALYS('Ir', '191', '077', file_ending='.tot')
		E_192Ir, CS_192Ir = self.TALYS('Ir', '192', '077', file_ending='.tot')
		E_193Ir, CS_193Ir = self.TALYS('Ir', '193', '077', file_ending='.tot')
		E_194Ir, CS_194Ir = self.TALYS('Ir', '194', '077', file_ending='.tot')

		#for i in colors:

		for i in range(len(E_188Ir)):
			print(CS_194Pt[i]+CS_193Pt[i]+CS_192Pt[i]+CS_191Pt[i]+CS_190Pt[i]+CS_189Pt[i]+CS_188Pt[i]+CS_194Ir[i]+CS_193Ir[i]+CS_192Ir[i]+CS_191Ir[i]+CS_190Ir[i]+CS_189Ir[i]+CS_188Ir[i])

			print((CS_194Pt[i]+CS_193Pt[i]+CS_192Pt[i]+CS_191Pt[i]+CS_190Pt[i]+CS_189Pt[i]+CS_188Pt[i]+CS_194Ir[i]+CS_193Ir[i]+CS_192Ir[i]+CS_191Ir[i]+CS_190Ir[i]+CS_189Ir[i]+CS_188Ir[i])/14)

		plt.plot(E_194Pt, CS_194Pt, label=r"$^{194}$Pt", color=colors[0])
		plt.plot(E_193Pt, CS_193Pt, label=r"$^{193m}$Pt", color=colors[1])
		plt.plot(E_193Pt, CS_193Pt, label=r"$^{193m}$Pt", color=colors[2])
		plt.plot(E_192Pt, CS_192Pt, label=r"$^{192}$Pt", color=colors[3])
		plt.plot(E_191Pt, CS_191Pt, label=r"$^{191}$Pt", color=colors[4])
		plt.plot(E_190Pt, CS_190Pt, label=r"$^{190}$Pt", color=colors[5])
		plt.plot(E_189Pt, CS_189Pt, label=r"$^{189}$Pt", color=colors[6])
		plt.plot(E_188Pt, CS_188Pt, label=r"$^{188}$Pt", color=colors[7])
		"""
		plt.plot(E_194Ir, CS_194Ir, label=r"$^{194}$Ir", color=colors[8])
		plt.plot(E_193Ir, CS_193Ir, label=r"$^{193}$Ir", color=colors[9])
		plt.plot(E_192Ir, CS_192Ir, label=r"$^{192}$Ir", color=colors[10])
		plt.plot(E_191Ir, CS_191Ir, label=r"$^{191}$Ir", color=colors[11])
		plt.plot(E_190Ir, CS_190Ir, label=r"$^{190}$Ir", color=colors[12])
		plt.plot(E_189Ir, CS_189Ir, label=r"$^{189}$Ir", color=colors[13])
		plt.plot(E_188Ir, CS_188Ir, label=r"$^{188}$Ir", color=colors[14])
		"""

		"""
		plt.text(12, 170, r'$^{193}$Ir(d,2n)$^{193m}$Pt', color='orange', fontsize=9)

		plt.text(10, 300, r'$^{191}$Ir(d,2n)$^{191}$Pt', color='red', fontsize=9)
		plt.text(25, 700, r'$^{193}$Ir(d,4n)$^{191}$Pt', color='red', fontsize=9)

		plt.text(15, 500, r'$^{193}$Ir(d,3n)$^{192}$Pt', color='green', fontsize=9)

		plt.text(9, 40, r'$^{191}$Ir(d,n)$^{192}$Pt', color='green', fontsize=9)


		plt.text(17, 310, r'$^{191}$Ir(d,3n)$^{190}$Pt', color='purple', fontsize=9)
		plt.text(30, 450, r'$^{191}$Ir(d,5n)$^{190}$Pt', color='purple', fontsize=9)

		plt.text(9, 60, r'$^{193}$Ir(d,n)$^{194}$Pt', color='blue', fontsize=9)

		plt.text(25, 400, r'$^{191}$Ir(d,4n)$^{189}$Pt', color='brown', fontsize=9)
		plt.text(33, 200, r'$^{191}$Ir(d,5n)$^{188}$Pt', color='pink', fontsize=9)
		"""

		#plt.title(r"Excitation functionsfor isotopes of Pt from $^\text{nat}$Ir(d,x) (TALYS-1.9)")
		plt.title(r'Excitation functions for isotopes of Pt from $^{nat}$Ir(d,x) (TALYS-1.9)')
		plt.xlabel('Deuteron beam energy, MeV')
		plt.ylabel('Cross section, mb')
		plt.legend()
		plt.show()



		"""
		E_193Pt, CS_193Pt = self.Tendl('Ir', '193', '078', file_ending='.L05')
		#E_193Pt, CS_193Pt = self.TALYS('Ir', '193', '078', file_ending='.L05')
		E_191Pt, CS_191Pt = self.Tendl('Ir', '191', '078', file_ending='.tot')
		#E_191Pt, CS_191Pt = self.TALYS('Ir', '191', '078', file_ending='.tot')
		E_189Pt, CS_189Pt = self.Tendl('Ir', '189', '078', file_ending='.tot')
		#E_189Pt, CS_189Pt = self.TALYS('Ir', '189', '078', file_ending='.tot')
		E_188Pt, CS_188Pt = self.Tendl('Ir', '188', '078', file_ending='.tot')
		#E_188Pt, CS_188Pt = self.TALYS('Ir', '188', '078', file_ending='.tot')

		plt.plot(E_188Pt, CS_188Pt, label=r'$^{188}$Pt')

		plt.plot(E_189Pt, CS_189Pt, label=r'$^{189}$Pt')
		plt.plot(E_191Pt, CS_191Pt, label=r'$^{191}$Pt')
		plt.plot(E_193Pt, CS_193Pt, label=r'$^{193m}$Pt')

		plt.text(10, 340, r'$^{193}$Ir(d,2n)$^{193m}$Pt', color='red', fontsize=9)
		plt.text(12, 300, r'$^{191}$Ir(d,2n)$^{191}$Pt', color='green', fontsize=9)
		plt.text(25, 700, r'$^{193}$Ir(d,4n)$^{191}$Pt', color='green', fontsize=9)
		plt.text(27, 360, r'$^{191}$Ir(d,4n)$^{189}$Pt', color='orange', fontsize=9)
		plt.text(29, 200, r'$^{191}$Ir(d,5n)$^{188}$Pt', color='blue', fontsize=9)
		#plt.plot(E_193Pt2, CS_193Pt2, label=r'$^{193m}$Pt talys')
		plt.axis((0, 40, 0, 740))
		plt.title('Tendl cross sections for deuterions on natural iridium')
		plt.xlabel('Energy, MeV')
		plt.ylabel('Cross section, mb')
		plt.legend()
		plt.savefig('reactionchannels_pt.png', dpi=300)
		plt.show()
		"""
		"""
		E_191Pt, CS_191Pt = self.Tendl('Ir', '191', '078', file_ending='.tot')

		E_189Pt, CS_189Pt = self.Tendl('Ir', '189', '078', file_ending='.tot')
		E_189Ir, CS_189Ir = self.Tendl('Ir', '189', '077', file_ending='.tot')

		E_188Pt, CS_188Pt = self.Tendl('Ir', '188', '078', file_ending='.tot')
		E_188Ir, CS_188Ir = self.Tendl('Ir', '188', '077', file_ending='.tot')

		plt.plot(E_191Pt, CS_191Pt, label='191Pt')
		plt.plot(E_189Pt, CS_189Pt, label='189Pt')
		plt.plot(E_189Ir, CS_189Ir, label='189Ir')
		plt.plot(E_188Pt, CS_188Pt, label='188Pt')
		plt.plot(E_188Ir, CS_188Ir, label='188Ir')
		plt.legend()
		plt.show()
		"""

	def Cumulative_CS(self):
		pass



# SimCS = SimCrossSectionData()
# # E, CS = SimCS.ALICE('Fe', '51', '25', 4)
# E, CS= SimCS.TALYS('Fe', '051', '025')
# # E, CS= SimCS.TALYS('Fe', '052', '026')
# plt.plot(E, CS)
# plt.show()
#SimCS.multiple_reactions()
#print(path)

"""


# E, dE, CS, dCS, author= SimCS.EXFOR(reaction='Fe_56Co', independent=True )
E, dE, CS, dCS, author= SimCS.EXFOR(reaction='Fe_57Co', independent=True )
unique_author=[]
for a in author:
	#print(a)
	if a not in unique_author:
		#print("add*")
		unique_author.append(a)
#print(unique_author)
#print(len(author))
#print(author)

#plt.plot(E, CS, '.')
#plt.show()
"""

#plt.plot(E,CS, '.')
#plt.show()
# E,CS= SimCS.EMPIRE('Ni', '58', '27', 'Ni_58Co', isomer='M')

# plt.plot(E,CS)
# plt.show()
"""
E_2, CS_2 = SimCS.ALICE('Ir', '189', '77', 4)
E_1, CS_1 = SimCS.ALICE('Ir', '189', '78', 4)

plt.plot(E_1, CS_1, label='189Pt')
plt.plot(E_2, CS_2, label='189Ir')
BR = 1.0
CS_tot = CS_2+CS_1*BR
plt.plot(E_1, CS_tot, label='cum')
plt.legend()
plt.show()
"""

#E_p, CS_p = SimCS.COH('Ni', '056', '028', 'Ni_56Ni', isomer=None)
#E, CS = SimCS.Tendl('Ni', '057', '028', file_ending='.tot')
#print(E)


"""
#E, CS = SimCS.COH('Ir', '193', '078', 'Ir_193mPt', isomer='M')
#E, CS = SimCS.COH('Cu', '064', '029', 'Cu_64Cu', isomer=None)
E, CS = SimCS.COH('Fe', '054', '025', 'Fe_54Mn', isomer=None)

E_al, CS_al = SimCS.ALICE('Fe', '54', '25', CS_colonne=5)

#print(E)

plt.plot(E,CS, label="CoH")
plt.plot(E_al, CS_al, label="ALICE")
plt.legend()
plt.show()
"""


"""
if E[0]==1:
	zero_padding = np.linspace(0,1,5)
	cs_zeros = np.zeros(len(zero_padding))
	E = np.concatenate((zero_padding, E))
	CS = np.concatenate((cs_zeros, CS))

plt.plot(E,CS, label="zeropadding")
plt.legend()
plt.show()
"""





#SimCS.COH('Ir', '191', '078', 'Ir_191Pt')
#"SimCS.COH('Ni', '054', '025', 'Ni_54Mn' )
#SimCS.ALICE('Ni', '56', '27', 5)
#SimCS.multiple_reactions()
#foil = 'Ir'; A = '190'; Z = '77' # 183Ta
#foil = 'Cu'; A = '60'; Z = '27' # 183Ta

#SimCS.ALICE(foil, A, Z, CS_colonne=4)
#A='060'; Z='027'; foil='Cu'
#SimCS.Tendl(foil, A, Z)
#foil = 'Ir'; A = '186'; Z = '075' # 186Re
#foil = 'Ir'; A = '187'; Z = '074' # 187W
#foil = 'Ir'; A = '183'; Z = '076' # 186Ta
#foil = 'Ir'; A = '194'; Z = '077' # 188Re
#foil = 'Fe'; A = '048'; Z = '023' # 188Re
#E_tendl, CS_tendl = SimCS.Tendl(foil, A, Z)

#E_talys, CS_talys= SimCS.TALYS(foil, A, Z)
#SimCS.EXFOR("Ir_194Ir")
#E, dE, CS, dCS, author=SimCS.EXFOR("Ir_190m2Ir")
#plt.plot(E, CS, '.')
#plt.show()





#plt.plot(E_tendl, CS_tendl, label='tendl')

#plt.plot(E_talys, CS_talys, label='talys')
#plt.legend()
#plt.show()


#SimCS.EXFOR('Ir_192Ir')
#SimCS.Tendl('Ir', '192', '077', file_ending='.L00')
#SimCS.ALICE('Ir', '191', '77')



#reaction = 'Ir_192Ir'

#reaction = 'Ni_52Ni'
#reaction = 'Fe_48V'

#foil = reaction[:2]


#productnumb = reaction[3:-2]
#print(productnumb)

#title = r'$^\text{nat}${}(d,x)$^{}$'


#SimCS.multiple_reactions()
#SimCS.Tendl('Ir', '193', '078', file_ending='.L05')
#SimCS.Tendl('Ir', '191', '078', file_ending='.tot')

#SimCS.Tendl('Ni', '060', '027')



#E_193Ir = np.genfromtxt(f_193Ir, delimiter=' ', usecols=[0],skip_header=5)
#SimCS.TALYS('Ir', '078', '193')

#E, dE, CS, dCS, author = SimCS.EXFOR('Ni_64Cu')
#print(E)
#SimCS.TALYS('Ir', '27', '058')
#SimCS.ALICE('Ni', '54', '25')
#SimCS.TALYS('Ir', '077', '192')
#SimCS.ALICE('Ni', '64', '29')
#SimCS.data(Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu', 'B_+2_D_+4,25.csv')

if __name__=='__main__':
	print(__name__)
else:
	print("simulated_CrossSectionData.py")
