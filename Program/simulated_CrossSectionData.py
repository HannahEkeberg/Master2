
import os 
import numpy as np 
import matplotlib.pyplot as plt


from jan20_CrossSections import CrossSections 
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

	def TALYS(self):
		pass 

	def Tendl(self):
		pass 

	def EMPIRE(self):
		pass 

	def COH(self):
		pass 

	#def plot(self):



SimCS = SimCrossSectionData('Ir_194Pt')
SimCS.ALICE('Ni', '58', '27')
#SimCS.data(Cu_64Cu(), 'Cu', 'Cu_64Cu.csv', 10, 'Cu_64Cu', 'B_+2_D_+4,25.csv')

