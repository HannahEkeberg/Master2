

from scipy.constants import m_e, e, epsilon_0, pi, hbar
import numpy as np 

class Calculations:

	def __init__(self, particle, A, Z):
		self.particle = particle   # eg alpha, proton
		self.A = A                 # eg Compound 193Pt or 195Pt
		self.Z = Z                 # eg Z number of Pt = 78

		self.E = np.linspace(0,33, 100)
		if self.particle == 'alpha': # 2p 2n
			self.Z_p = 2; self.A_p = 2; self.mass = 3727.3794066 #MeV
		elif self.particle == 'p':   # 1p 0n
			self.Z_p = 1; self.A_p = 1; self.mass = 1
		elif self.particle == 'n':	 # 0p 1n
			self.Z_p = 0; self.A_p = 1; self.mass = 1
		elif self.particle == 'd':	 # 1p 1n	
			self.Z_p = 1; self.A_p = 2; self.mass = 1
		elif self.particle == '3He': # 2p 1n
			self.Z_p = 2; self.A_p = 3; self.mass = 1
		elif self.particle == 't':   # 1p 2n
			self.Z_p = 1; self.A_p = 3; self.mass = 1


	def Coulomb_barrier(self):
		K = (4*pi*epsilon_0)**(-1)
		#print(type(K))
		#print(type(self.Z))

		U = K* (self.Z * self.Z_p * e** 2) / (self.A**(1/3) + self.A_p**(1/3))
		
		print(U)

		return U


		


	def Centrifugal_barrier(self):
		pas

	def tunneling_prob(self, Coulomb=False, Centrifugal=False, Total=False):
		if Coulomb:
			U = self.Coulomb_barrier()
		if Centrifugal:
			U = self.Centrifugal_barrier()
		if Total:
			U = self.Coulomb_barrier() + self.Centrifugal_barrier()

		alpha = np.sqrt(2* self.mass * self.E / hbar**2)
		L = self.A**(1/3)     # L is the width of the square potential


		T = (1+ 0.25*(U**2 / (self.E*(U-self.E))))#*np.sinh(alpha*L)**2)**(-1) 
		print(T)
		



					


Calculations('alpha', 195, 78).Coulomb_barrier()
Calculations('p', 195, 78).Coulomb_barrier()
Calculations('n', 195, 78).Coulomb_barrier()
Calculations('t', 195, 78).Coulomb_barrier()
Calculations('3He', 195, 78).Coulomb_barrier()
#Calculations('alpha', 64, 29).tunneling_prob(Coulomb=True)
