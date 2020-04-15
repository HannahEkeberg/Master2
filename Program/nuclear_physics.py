

from scipy.constants import m_e, e, epsilon_0, pi, hbar
import numpy as np 
import matplotlib.pyplot as plt

class Calculations:

	def __init__(self, particle, A, Z):
		self.particle = particle   # eg alpha, proton
		self.A = A                 # eg Compound 193Pt or 195Pt
		self.Z = Z                 # eg Z number of Pt = 78

		#if self.Z == 26:

		#if isinstance(self.A, list):
		#	print("yes")
		#else:
		#		print("no")



		self.E = np.linspace(0,33, 100)
		if self.particle == 'alpha': # 2p 2n
			self.Z_p = 2; self.A_p = 2; self.l=0.0; self.mass = 3727.379 #MeV
		elif self.particle == 'p':   # 1p 0n
			self.Z_p = 1; self.A_p = 1; self.l = 0.5; self.mass = 938.28
		elif self.particle == 'n':	 # 0p 1n
			self.Z_p = 0; self.A_p = 1; self.l = 0.5; self.mass = 939.57
		elif self.particle == 'd':	 # 1p 1n	
			self.Z_p = 1; self.A_p = 2; self.l = 1; self.mass = 1875.6 
		elif self.particle == '3He': # 2p 1n
			self.Z_p = 2; self.A_p = 3; self.l= 0.5; self.mass=3.0160293*931.5 # from u to MeV, multiply by 931.5 MeV
		elif self.particle == 't':   # 1p 2n
			self.Z_p = 1; self.A_p = 3; self.l = 0.5; self.mass = 2808.921


	def Coulomb_barrier(self):

		print("Coulomb barrier for {}".format(self.particle))
		e = 1.44 #MeV fm
		conversion_to_MeV =6.24150913*1e12
		K = 1.2 #fm
		if isinstance(self.A, list):
			U0 = []
			for i in self.A:
				U = K* (self.Z * self.Z_p * e ** 2) / (i**(1/3) + self.A_p**(1/3))
				#print(U)
				#U = K* (self.Z * self.Z_p * e** 2) / (i**(1/3) + self.A_p**(1/3))
				U0.append(U)
			print("For Z={} and A={}, Coulomb barrier is: ".format(self.Z, self.A), U0)
			print("Mean value Coulomb barrier: ", np.mean(U0))
			#l = len(self.A)
			#U0 = np.sum
			U0 = np.mean(U0)
		else:
			U0 = K* (self.Z * self.Z_p * e** 2) / (self.A**(1/3) + self.A_p**(1/3))
			print("For Z={} and A={}, Coulomb barrier is: ".format(self.Z, self.A), U0)

		#U0 = K* (self.Z * self.Z_p * e** 2) / (self.A**(1/3) + self.A_p**(1/3))
		
		print("--------------------------------------------------------------")
		return U0




		


	def Centrifugal_barrier(self):
		if isinstance(self.A, list):
			U0 = []
			for i in self.A:
				U = self.l*(self.l+1)/(i**(1/3)+self.A_p**(1/3))
				
				#U = K* (self.Z * self.Z_p * e** 2) / (i**(1/3) + self.A_p**(1/3))
				U0.append(U)
				print("For Z={} and A={}, Centrifugal barrier is: ".format(self.Z, self.A), U0)
			#print("Mean value Coulomb barrier: ", np.mean(U0))
			#l = len(self.A)
			#U0 = np.sum
			U0 = np.mean(U0)
		else:
			U0 = self.l*(self.l+1)/(self.A**(1/3)+self.A_p**(1/3))
		print(U0)
		return U0

		#U = self.l*(self.l+1)/(self.A**(1/3)+self.A_p**(1/3))


	def tunneling_prob(self, Coulomb=False, Centrifugal=False, Total=False, label=None, style=None):
		if Coulomb:
			U = self.Coulomb_barrier()
			
		if Centrifugal:
			U = self.Centrifugal_barrier()
		if Total:
			U_c = self.Coulomb_barrier()
			U_s = self.Centrifugal_barrier()
			U = U_c+ U_s

		alpha = np.sqrt(2* self.mass * self.E / hbar**2)
		if isinstance(self.A, list):
			L=self.A[0]**(1/3)
		else:
			L = self.A**(1/3)     # L is the width of the square potential


		T = (1+ 0.25*(U**2 / (self.E*(U-self.E))))#*np.sinh(alpha*L)**2)**(-1) 
		

		if label is not None:
			plt.plot(self.E, T, label=label, linestyle=style, linewidth=1.5)

		else:
			plt.plot(self.E, T)
		


class Q_val_calc:
	def __init__(self, Q, Z_targ, A_targ, Z_prod, A_prod, decay_channel):
		self.Q = Q 
		self.d_mass = 1875.6 #MeV /c^2
		self.p_mass = 938.28 #MeV/ c^2
		self.n_mass = 939.57 #MeV / c^2

		self.M_targ = Z_targ*self.p_mass + (A_targ-Z_targ)*self.n_mass
		self.M_prod = Z_prod*self.p_mass + (A_prod-Z_prod)*self.n_mass

		self.decay_channel = decay_channel
		if isinstance(self.decay_channel,list):
			m_outgoing = 0
			for i in self.decay_channel:
				if i == 'p':
					m_outgoing+= self.p_mass
				elif i == 'n':
					m_outgoing+= self.n_mass
			self.m_outgoing = m_outgoing

		else:
			if self.decay_channel == 'p':
				self.m_outgoing= self.p_mass
			elif self.decay_channel == 'n':
				self.m_outgoing = self.n_mass

		
		E = -Q* (self.m_outgoing + self.M_prod)/ (self.m_outgoing + self.M_prod- self.M_targ)
		print(E*1e3)
		#	return E

			


Q_ = Q_val_calc(-10.251, 77, 191, 77, 190, ['p', 'n', 'n'])







		
#A= [193, 195]; Z=78
#A = [58+2, 60+2, 61+2, 62+2, 64+2]; Z=29
#A = [63, 65]; Z=30
#A = [54, 56, 57, 58; Z=27
#p = Calculations('p', A, Z)
#a = Calculations('alpha', A, Z)
#n = Calculations('n', A, Z)
#t = Calculations('t', A, Z)
#d = Calculations('d', A, Z)
#h = Calculations('3He', A, Z)



"""
a.tunneling_prob(Coulomb=True)

plt.axis([0,35,0,100])
plt.legend()
plt.xlabel('Deuteron energy (MeV)')
plt.ylabel('Transmission probability')
plt.show()
"""




#Calculations('p', [193,195], 78).Centrifugal_barrier()
#Calculations('p', [193,195], 78).tunneling_prob(Total=True, label=r'p', style='--')
#Calculations('n', [193,195], 78).tunneling_prob(Total=True, label=r'p', style='--')

"""
Calculations('p', [193,195], 78).tunneling_prob(Coulomb=True, label=r'p', style='--')
Calculations('alpha', [193,195], 78).tunneling_prob(Coulomb=True, label=r'$\alpha$', style=':')
Calculations('t', [193,195], 78).tunneling_prob(Coulomb=True, label=r't', style='-.')
Calculations('d', [193,195], 78).tunneling_prob(Coulomb=True, label=r'd', style='--')
Calculations('3He', [193,195], 78).tunneling_prob(Coulomb=True, label=r'$^3$He', style='-.')
plt.title(r'Emission probability $^{193*}$Pt and $^{195*}$Pt')
"""
"""
Calculations('p', [58, 60, 61, 62, 64], 29).tunneling_prob(Coulomb=True, label=r'p', style='--')
Calculations('alpha', [58, 60, 61, 62, 64], 29).tunneling_prob(Coulomb=True, label=r'$\alpha$', style=':')
Calculations('t', [58, 60, 61, 62, 64], 29).tunneling_prob(Coulomb=True, label=r't', style='-.')
Calculations('d', [58, 60, 61, 62, 64], 29).tunneling_prob(Coulomb=True, label=r'd', style='--')
Calculations('3He', [58, 60, 61, 62, 64], 29).tunneling_prob(Coulomb=True, label=r'$^3$He', style='-.')
plt.title(r'Emission probability $^{58,60,61,62,64*}$Cu')
"""

"""
Calculations('p', [58, 60, 61, 62, 64], 29).tunneling_prob(Coulomb=True, label=r'p', style='--')
Calculations('alpha', [58, 60, 61, 62, 64], 29).tunneling_prob(Coulomb=True, label=r'$\alpha$', style=':')
Calculations('t', [58, 60, 61, 62, 64], 29).tunneling_prob(Coulomb=True, label=r't', style='-.')
Calculations('d', [58, 60, 61, 62, 64], 29).tunneling_prob(Coulomb=True, label=r'd', style='--')
Calculations('3He', [58, 60, 61, 62, 64], 29).tunneling_prob(Coulomb=True, label=r'$^3$He', style='-.')
plt.title(r'Emission probability $^{58,60,61,62,64*}$Cu')
"""

"""
Calculations('p', [63,65], 30).tunneling_prob(Coulomb=True, label=r'p', style='--')
Calculations('alpha', [63,65], 30).tunneling_prob(Coulomb=True, label=r'$\alpha$', style=':')
Calculations('t', [63,65], 30).tunneling_prob(Coulomb=True, label=r't', style='-.')
Calculations('d', [63,65], 30).tunneling_prob(Coulomb=True, label=r'd', style='--')
Calculations('3He', [63,65], 30).tunneling_prob(Coulomb=True, label=r'$^3$He', style='-.')
plt.title(r'Emission probability $^{63,65*}$Cu')
"""

"""
Calculations('p', [54,56, 57, 58], 27).tunneling_prob(Coulomb=True, label=r'p', style='--')
Calculations('alpha', [63,65], 30).tunneling_prob(Coulomb=True, label=r'$\alpha$', style=':')
Calculations('t', [63,65], 30).tunneling_prob(Coulomb=True, label=r't', style='-.')
Calculations('d', [63,65], 30).tunneling_prob(Coulomb=True, label=r'd', style='--')
Calculations('3He', [63,65], 30).tunneling_prob(Coulomb=True, label=r'$^3$He', style='-.')
plt.title(r'Emission probability $^{54,56, 57, 58*}$Co')
"""




