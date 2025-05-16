from Tendl import *
import matplotlib.pyplot as plt

Ir191 = {"Ir191": 0.373}
Ir193 = {"Ir193": 0.627}


# Tendl(natIr).plotTendl23('78', '189', isomerLevel = None)
Tendl(Ir191).plotTendl23Unique(productZ='78', productA = '189', isomerLevel = None, color='forestgreen', lineStyle='-.', label='Radiocontaminant')
# Tendl(Ir193).plotTendl23Unique(productZ='78', productA = '191', isomerLevel = None, color='royalblue', lineStyle=':', label='Radiocontaminant')
Tendl(Ir191).plotTendl23Unique(productZ='77', productA = '192', isomerLevel = None, color='royalblue', lineStyle=':', label='Radiocontaminant')
Tendl(Ir193).plotTendl23Unique(productZ='78', productA = '193', isomerLevel = '05', color='hotpink', lineStyle='-', label='Desired radionuclide')
plt.xlabel("Energy (MeV)")
plt.gca().set_xlim(left=0, right=40)
plt.ylabel("Cross section (mb)")
plt.title("Excitation functions (TENDL23)")
plt.legend()
# plt.show()
plt.savefig('excitationFunctionExample.png', dpi=300)