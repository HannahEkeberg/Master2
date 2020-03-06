
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
		

	def Tendl(self):
		pass 

	def EMPIRE(self):
		pass 

	def COH(self):
		pass 

	def EXFOR(self, reaction):
		try:
			filename = self.path + '/../EXFOR/' + reaction + '.txt'

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
		
			f.close()
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


		



#SimCS = SimCrossSectionData('Ir_194Pt')
#SimCS.TALYS('Ir', '078', '193')
#SimCS.EXFOR('Cu_65Ni')
#SimCS.TALYS('Cu', '27', '058')
#SimCS.ALICE('Ni', '54', '25')
#SimCS.TALYS('Ni', '027', '056')
#SimCS.ALICE('Ni', '64', '29')
#SimCS.data(Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu', 'B_+2_D_+4,25.csv')
	
if __name__=='__main__':
	print(__name__)
else:
	print("simulated_CrossSectionData.py")



