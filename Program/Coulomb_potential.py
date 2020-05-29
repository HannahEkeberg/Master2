
##### INCLUDE IN THEORY!!!!!!!

from scipy.constants import e, epsilon_0
import numpy as np
#print(e)
def coulomb_barrier(Z_a, Z_b, A_a, A_b):
	r0 = 1.25#1.25 #fm,   ca. constant, for nuclear rad

	if Z_a ==1 and A_a==1:
		R_a = 0.877 #fm
	if Z_a ==2 and A_a ==4:
		R_a = 0.923 #fm
	else:	
		R_a = r0*A_a**(1/3)# *1e-15 #m
	R_b = r0*A_b**(1/3)# *1e-15 #m
	#print("particle radius: ", R_a, A_a)
	#print("nuclear radius: ", R_b, A_b)

	#print(R_a)
	#print(r0)
	#K = (4*np.pi*epsilon_0)**(-1)
	K = 1.44 #  constant: ke^2 = MeV/fm
	#epsilon_0 = F/m = e**2/(J*m) = e**2/(6.24*1e18 eV)*m 
	#conversion_unit =  e**2/ (6.24*1e15) # C/(MeV*m ) 

	#Coulomb constant: eV aangstroem per c^2 ---- > MeV fm /c^2:
	#K = 14.3996 *1e3 * 1e-5


	#print(K)
 
	#return e**2/ (4*np.pi*epsilon_0*conversion_unit)   * ( (Z_a*Z_b)/(R_a+R_b)) 
	return K* ( (Z_a*Z_b)/(R_a+R_b)) 
	#return 1


def tunneling_prob(Z_p, Z_t, A_p, A_t, E_beam):
	V = coulomb_barrier(Z_p, Z_t, A_p, A_t)
	constant = 1.505 # eC nm^2  = 2me_/hˆ2
	kappa = 2*np.pi *np.sqrt(V-E_beam)
	L=1e-15 # width of barrier? 1 fm
	T =  (16*E_beam * (V-E_beam) / V**2) * np.exp(-2*kappa*L)

	return T


#t = tunneling_prob(2, 20, 4, 60, 10)	
#print(t)


b1_a = coulomb_barrier(2, 27, 4, 56)
b2_a = coulomb_barrier(2, 27, 4, 58)
b3_a = coulomb_barrier(2, 27, 4, 59)
b4_a = coulomb_barrier(2, 27, 4, 60)
b1_p = coulomb_barrier(1, 27, 1, 56)
b2_p = coulomb_barrier(1, 27, 1, 58)
b3_p = coulomb_barrier(1, 27, 1, 59)
b4_p = coulomb_barrier(1, 27, 1, 60)
print(b1_a, b2_a,b3_a, b4_a)
print(b1_p, b2_p,b3_p, b4_p)

#b = coulomb_barrier(0, 29, 1, 60)
#print(r"Neutron barrier height for $^{60*}$Cu: ", b)

b1 = coulomb_barrier(2, 29, 4, 58)
b2 = coulomb_barrier(2, 29, 4, 60)
b3 = coulomb_barrier(2, 29, 4, 61)
b4 = coulomb_barrier(2, 29, 4, 62)
b5 = coulomb_barrier(2, 29, 4, 64)

print(b1)
print(b2)
print(b3)
print(b4)
print(b5)

b5 = coulomb_barrier(2, 79, 4, 193)
print("***", b5)

#print(r"alpha barrier height for $^{60*}$Cu: ", b)



#b = coulomb_barrier(2, 29, 3, 60)
#print(r"$^{3}$He barrier height for $^{60*}$Cu: ", b)

#b = coulomb_barrier(1, 29, 3, 60)
#print(r"triton barrier height for $^{60*}$Cu: ", b)

#b = coulomb_barrier(1, 29, 2, 60)
#print(r"deuteron barrier height for $^{60*}$Cu: ", b)




#proton, 193Ir
b1 = coulomb_barrier(1, 78, 1, 193)
b2 = coulomb_barrier(1, 78, 1, 195)
b3 = coulomb_barrier(2, 78, 4, 195)
print("mean:", np.mean((b1, b2)))
print("Coulomb barrier for compound nucleus 193Pt: ", b1, "MeV")  
print("Coulomb barrier for compound nucleus 195t: ", b2, "MeV") 
print(b3)
print("***")
b1 = coulomb_barrier(1, 29, 1, 60)
b2 = coulomb_barrier(1, 29, 1, 62)
b3 = coulomb_barrier(1, 29, 1, 63)
b4 = coulomb_barrier(1, 29, 1, 64)
b5 = coulomb_barrier(1, 29, 1, 66)
b6 = coulomb_barrier(2, 20, 4, 62)
print("mean:", np.mean((b1, b2, b3, b4)))
print("Coulomb barrier for compound nucleus 60Cu: ", b1, "MeV")  
print("Coulomb barrier for compound nucleus 62Cu: ", b2, "MeV")  
print("Coulomb barrier for compound nucleus 63Cu: ", b3, "MeV")  
print("Coulomb barrier for compound nucleus 64Cu: ", b4, "MeV")  
print("Coulomb barrier for compound nucleus 66Cu: ", b5, "MeV")  
print(b6)
print("***")
b1 = coulomb_barrier(1, 30, 1, 65)
b2 = coulomb_barrier(1, 30, 1, 67)
print("mean:", np.mean((b1, b2)))
print("Coulomb barrier for compound nucleus 65Zn: ", b1, "MeV")  
print("Coulomb barrier for compound nucleus 67Zn: ", b2, "MeV")  
print("***")
b1 = coulomb_barrier(1, 27, 1, 56)
b2 = coulomb_barrier(1, 27, 1, 58)
b3 = coulomb_barrier(1, 27, 1, 59)
b4 = coulomb_barrier(1, 27, 1, 60)
print("mean:", np.mean((b1, b2, b3, b4)))
print("Coulomb barrier for compound nucleus 56Co: ", b1, "MeV")  
print("Coulomb barrier for compound nucleus 58Co: ", b2, "MeV")  
print("Coulomb barrier for compound nucleus 59Co: ", b3, "MeV")  
print("Coulomb barrier for compound nucleus 60Co: ", b4, "MeV")  

