
import os 
import numpy as np 
import matplotlib.pyplot as plt


#from jan20_CrossSections import CrossSections 
from foil_info import * 

path = os.getcwd() 



class SimCrossSectionData:

	def __init__(self, reaction):
		# reaction = Ir_193mPt for instance 

		self.reaction = reaction
		self.path = os.getcwd() 
		#self.ziegler_file = self.path +'/cleaned_zieglerfiles/ziegler_B_+2_D_+4,25_fluxes.csv'
		#print(self.ziegler_file)

	def data(self, react_func, foil, filename, n, reaction, BC_csv_filename='B_+2_D_+4,25.csv'): 
		#CS_class = CrossSections(self.ziegler_file)
		#E, dE, CS, dCS = CS_class.make_CS(react_func, foil, filename, n ,reaction, BC_csv_filename)
		#print(E)
		pass
		
		#pass

		#class = CrossSections(func, Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu', csv_filename)
		#class.


	def ALICE(self, foil, A, Z):
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
					print(Z, A)
					print(content[lines])


			f.close()

		print("E: ",E_new)
		print("CS: ", CS_new)


		
		plt.plot(E_new, CS_new, label='ALICE')
		plt.legend()
		plt.show()
		
		return E_new, CS_new

	def TALYS(self,foil, Z, A):
		# Z = 0XX, A=0XX

		filename = self.path + '/../Talys/' +foil+ '/rp'+Z+A+'.tot'
		#filename = self.path + '/../Talys/' +foil+ '/rp'+Z+A+'.L02'
		E  = np.genfromtxt(filename, delimiter=' ', usecols=[0],skip_header=5)
		CS = np.genfromtxt(filename, delimiter=' ', usecols=[1],skip_header=5)


		#print(CS)
		#print(E)

		#plt.plot(E,CS)
		#plt.show()
		return E, CS
		

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

			print("Ir 193 file: ",f_193Ir)
			print("Ir 191 file: ",f_191Ir)
			if os.path.isfile(f_191Ir): 
				#print("Ir 191 file: ",f_191Ir)
				CS_191Ir = np.genfromtxt(f_191Ir, delimiter=' ', usecols=[1],skip_header=5)
				E_191Ir = np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)
			else: 
				print("Ir 191 file does not exist")
				CS_191Ir = 0
				E_191Ir =  0 #np.genfromtxt(f_191Ir, delimiter=' ', usecols=[0],skip_header=5)

			if os.path.isfile(f_193Ir):
				CS_193Ir = np.genfromtxt(f_193Ir, delimiter=' ', usecols=[1],skip_header=5)
				E_193Ir = np.genfromtxt(f_193Ir, delimiter=' ', usecols=[0],skip_header=5)
				
			else: 
				print("Ir 193 file does not exist")
				CS_193Ir = 0
				E_193Ir = 0#np.genfromtxt(f_193Ir, delimiter=' ', usecols=[0],skip_header=5)
			
			E = E_191Ir*abund_191Ir + E_193Ir*abund_193Ir
			CS = CS_191Ir*abund_191Ir + CS_193Ir*abund_193Ir

			#plt.plot(E, CS, label='tendl')

			

				
			#plt.plot(E_191Ir,CS_191Ir, label='191Ir')
			#plt.plot(E_193Ir,CS_193Ir, label='193Ir')
			#plt.plot(E, CS, label='tot')
			#plt.legend()
			#plt.show()
			return E, CS
			
			#except:
				#print("files not exist or file ending is wrong. ") 
				

			#plt.legend()
			#plt.show()

			#E = E_191Ir*abund_191Ir + E_193Ir*abund_193Ir
			#CS = CS_191Ir*abund_191Ir + CS_193Ir*abund_193Ir
			
		elif foil == 'Ni':
			abund_58Ni = 0.68077; abund_60Ni = 0.26233; abund_61Ni = 0.011399; abund_62Ni = 0.036346; abund_64Ni = 0.009255;


			f_58Ni = self.path + '/../Tendl/' + foil + '/rp028058_' + Z + A + file_ending + '.txt'
			f_60Ni = self.path + '/../Tendl/' + foil + '/rp028060_' + Z + A + file_ending + '.txt'
			f_61Ni = self.path + '/../Tendl/' + foil + '/rp028061_' + Z + A + file_ending + '.txt'
			f_62Ni = self.path + '/../Tendl/' + foil + '/rp028062_' + Z + A + file_ending + '.txt'
			f_64Ni = self.path + '/../Tendl/' + foil + '/rp028064_' + Z + A + file_ending + '.txt'
			
			#print(f_60Ni)
			#print(f_61Ni)
			#print(f_62Ni)
			#print(f_64Ni)
			#E = []; CS = []

			# try:
			# 	CS_58Ni = np.genfromtxt(f_58Ni, delimiter=' ', usecols=[1],skip_header=5)
			# 	E_58Ni = np.genfromtxt(f_58Ni, delimiter=' ', usecols=[0],skip_header=5)
			# 	E.append(E_58Ni*abund_58Ni)
			# 	CS.append(CS_58Ni*abund_58Ni)
			# 	plt.plot(E_58Ni,CS_58Ni, label='58Ni', linewidth=0.5)
			# except: 
			# 	print("58Ni does not exist")
				
			# try: 
			# 	CS_60Ni = np.genfromtxt(f_60Ni, delimiter=' ', usecols=[1],skip_header=5)
			# 	E_60Ni = np.genfromtxt(f_60Ni, delimiter=' ', usecols=[0],skip_header=5)
			# 	plt.plot(E_60Ni,CS_60Ni, label='60Ni', linewidth=0.5)
			# 	E.append(E_60Ni)
			# 	CS.append(CS_60Ni)
			# except:
			# 	print("60Ni does not exist")

			CS_58Ni = np.genfromtxt(f_58Ni, delimiter=' ', usecols=[1],skip_header=5)
			E_58Ni = np.genfromtxt(f_58Ni, delimiter=' ', usecols=[0],skip_header=5)
			CS_60Ni = np.genfromtxt(f_60Ni, delimiter=' ', usecols=[1],skip_header=5)
			E_60Ni = np.genfromtxt(f_60Ni, delimiter=' ', usecols=[0],skip_header=5)

			CS_61Ni = np.genfromtxt(f_61Ni, delimiter=' ', usecols=[1],skip_header=5)
			E_61Ni = np.genfromtxt(f_61Ni, delimiter=' ', usecols=[0],skip_header=5)
			CS_62Ni = np.genfromtxt(f_62Ni, delimiter=' ', usecols=[1],skip_header=5)
			E_62Ni = np.genfromtxt(f_62Ni, delimiter=' ', usecols=[0],skip_header=5)
			CS_64Ni = np.genfromtxt(f_64Ni, delimiter=' ', usecols=[1],skip_header=5)
			E_64Ni = np.genfromtxt(f_64Ni, delimiter=' ', usecols=[0],skip_header=5)
			#print(E_64Ni)

			#print(E_58Ni)
			#CS_193Ir = np.genfromtxt(f_193Ir, delimiter=' ', usecols=[1],skip_header=5)
			#E_193Ir = np.genfromtxt(f_193Ir, delimiter=' ', usecols=[0],skip_header=5)
			
			E = E_58Ni*abund_58Ni + E_60Ni*abund_60Ni + E_61Ni*abund_61Ni + E_62Ni*abund_62Ni + E_64Ni*abund_64Ni
			CS = CS_58Ni*abund_58Ni + CS_60Ni*abund_60Ni + CS_61Ni*abund_61Ni + CS_62Ni*abund_62Ni + CS_64Ni*abund_64Ni
			#CS = CS_191Ir*abund_191Ir + CS_193Ir*abund_193Ir
			
			#plt.plot(E_60Ni,CS_60Ni, label='60Ni', linewidth=0.5)
			#plt.plot(E_61Ni,CS_61Ni, label='61Ni', linewidth=0.5)
			#plt.plot(E_62Ni,CS_62Ni, label='62Ni', linewidth=0.5)
			#plt.plot(E_64Ni,CS_64Ni, label='64Ni', linewidth=0.5)
			#plt.plot(E, CS, label='tot')
		
			#except:

				#print("files not exist or file ending is wrong. ") 
				#pass

			#plt.legend()
			#plt.show()

		return E, CS 

	def EMPIRE(self):
		pass 

	def COH(self):
		pass 

	"""
	def EXFOR(self, reaction):
		filename = self.path + '/../EXFOR/' + reaction + '.txt'
		print(filename)
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

			#str1 = content[0]

			#x = str1.lstrip()
			#print(x.split())
			E = []; dE=[]; CS = []; dCS=[]; author=[]

			for ind in range(len(content)):
				string= content[ind]
				string = (string.lstrip()).split()
				E.append(float(string[0]))
				dE.append(float(string[1]))
				CS.append(float(string[2])*1e3) # in mb
				dCS.append(float(string[3])*1e3) # in mb
				author.append(string[5]) #index 4 is equal to #
		
		print(author)
		print("**")
		equal=0
		non_equal=0
		for i in range(len(author)-1):
			if author[i]==author[i+1]:
				equal += 1
				#print(equal)

				#print(equal)
				print("equal")
				print(author[i], author[i+1])
				#print(i)
			else:
				non_equal += 1
				#print(non_equal)
				print("not equal")
				print(author[i], author[i+1])
		
		print(equal)
		print(non_equal)
		print(len(author))

		author.sort()
		print(author)








		#print(indices)
		#print(indices)
		#for i in indices:
		#	print(i)
		#x = indices.sort(key=author.__getitem__)
		#print("x; ",type(x))
		#print(author)
		#print(E)
		#f.close()
		#print(author[i], author[i+1])print(author)
		#equal=0
		#non_equal=0

		#indices = range(len(author))
		#indices.sort(key=author.__getitem__)
		#print(indices)
		#print(author)
		#print(author)

		#author.sort()
		#print(author)


		#plt.errorbar(E, CS, marker='P', linewidth=0.0001, xerr=dE, yerr=dCS, elinewidth=1.0, capthick=1.0, capsize=3.0, label='this data')
		#plt.show()
		
		return E, dE, CS, dCS, author

	"""
	def EXFOR(self, reaction):
		try:
			print("function EXFOR in sim class" )
			filename = self.path + '/../EXFOR/' + reaction + '.txt'
			print(filename)
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

				#str1 = content[0]

				#x = str1.lstrip()
				#print(x.split())
				E = []; dE=[]; CS = []; dCS=[]; author=[]

				for ind in range(len(content)):
					string= content[ind]
					string = (string.lstrip()).split()
					E.append(float(string[0]))
					dE.append(float(string[1]))
					CS.append(float(string[2])*1e3) # in mb
					dCS.append(float(string[3])*1e3) # in mb
					author.append(string[5]) #index 4 is equal to #
			return E, dE, CS, dCS, author
			#print(author)
			#print("**")
			
			# for i in range(len(author)):
			# 	if author[i]==author[i+1]:
			# 		equal += 1
			# 		#print(equal)

			# 		#print(equal)
			# 		#print("equal")
			# 		#print(author[i], author[i+1])
			# 		#print(i)
			# 	else:
			# 		non_equal += 1
					#print(non_equal)
					#print("not equal")
					#print(author[i], author[i+1])
			


			#indices = range(len(E))
			#indices.sort(key=E.__getitem__)
			#print(indices)
			#print(indices)
			#for i in indices:
			#	print(i)
			#x = indices.sort(key=author.__getitem__)
			#print("x; ",type(x))
			#print(author)
			#print(E)
			#f.close()
			#print(author[i], author[i+1])print(author)
			#equal=0
			#non_equal=0

			#indices = range(len(author))
			#indices.sort(key=author.__getitem__)
			#print(indices)
			#print(author)
			#print(author)

			#author.sort()
			#print(author)

	
			#plt.errorbar(E, CS, marker='P', linewidth=0.0001, xerr=dE, yerr=dCS, elinewidth=1.0, capthick=1.0, capsize=3.0, label='this data')
			#plt.show()
			
			return E, dE, CS, dCS, author

			#for i in author:
		except:
			print("exfor file does not exist for {}".format(reaction))
			return 0, 0, 0, 0, '0'



		#for i in range(len(E)):
		#for i in 
		#plt.errorbar(E[i], CS[i], marker='.', linewidth=0.001, xerr=dE[i], yerr=dCS[i], elinewidth=0.5, capthick=0.5, capsize=3.0, label=author[i] )
		#plt.legend()
		#plt.show()
		#print(type(E[0]))

	def multiple_reactions(self):
		E_193Pt, CS_193Pt = self.Tendl('Ir', '193', '078', file_ending='.L05')
		E_191Pt, CS_191Pt = self.Tendl('Ir', '191', '078', file_ending='.tot')
		E_189Pt, CS_189Pt = self.Tendl('Ir', '189', '078', file_ending='.tot')
		E_188Pt, CS_188Pt = self.Tendl('Ir', '188', '078', file_ending='.tot')

		plt.plot(E_188Pt, CS_188Pt, label=r'$^{188}$Pt')
		plt.plot(E_189Pt, CS_189Pt, label=r'$^{189}$Pt')
		plt.plot(E_191Pt, CS_191Pt, label=r'$^{191}$Pt')
		plt.plot(E_193Pt, CS_193Pt, label=r'$^{193m}$Pt')

		plt.title('Tendl cross sections for deuterions on natural iridium')
		plt.xlabel('Energy, MeV')
		plt.ylabel('Cross section, mb')
		plt.legend()
		plt.savefig('reactionchannels_pt.png', dpi=300)
		plt.show()


	def Cumulative_CS(self):
		pass 

		


#print(path)


SimCS = SimCrossSectionData('Ir_194Pt')
#SimCS.multiple_reactions()
SimCS.Tendl('Ir', '193', '078', file_ending='.L05')
#SimCS.Tendl('Ir', '191', '078', file_ending='.tot')
#SimCS.Tendl('Ni', '052', '025')
#SimCS.Tendl('Ni', '060', '027')



#E_193Ir = np.genfromtxt(f_193Ir, delimiter=' ', usecols=[0],skip_header=5)
#SimCS.TALYS('Ir', '078', '193')

#E, dE, CS, dCS, author = SimCS.EXFOR('Ni_64Cu')
#print(E)
#SimCS.TALYS('Cu', '27', '058')
#SimCS.ALICE('Ni', '54', '25')
#SimCS.TALYS('Ni', '027', '056')
#SimCS.ALICE('Ni', '64', '29')
#SimCS.data(Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu', 'B_+2_D_+4,25.csv')
	
if __name__=='__main__':
	print(__name__)
else:
	print("simulated_CrossSectionData.py")



