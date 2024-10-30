import numpy as np
import matplotlib.pyplot as plt
import os
import requests
from scipy.interpolate import splev, splrep
from collections import OrderedDict

from Tendl import *
from CrossSectionData import *
from Empire import *
from Talys import *
from Coh import *


crossSectionCsvPath = os.getcwd() + '/CrossSections/CrossSections_csv/'
empireFilePath = os.getcwd() + '/../EMPIRE/'
talysFilePath = os.getcwd() + '/../talys_v2.04/'
cohFilePath = os.getcwd() + '/../coh_v3.6.0/'
dirUpdatedFigures = 'CrossSections/updatedExcitationFunctions'
if not os.path.exists(dirUpdatedFigures):
    os.mkdir(dirUpdatedFigures)

def plotExcitationFunction(title, reaction, maxCs=None, show=False):
    pathToFigs = os.getcwd() + '/' + dirUpdatedFigures + '/'
    plt.xlabel('Deuteron Energy (MeV)')
    plt.ylabel('Cross Section (mb)')
    plt.title(title)
    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = OrderedDict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys(),fontsize='small', loc='best')
    plt.gca().set_xlim(left=0, right=40)
    if maxCs==None:
        plt.gca().set_ylim(bottom=0)
    else:
        plt.gca().set_ylim(bottom=0, top=maxCs)
    plt.savefig(pathToFigs + reaction + '.png', dpi=300)
    if show:
        plt.show()

natIr = {"Ir191": 0.373, "Ir193": 0.627}


crossSectionData = CrossSection(crossSectionCsvPath)
tendl_natIr = Tendl(natIr)
empire_natIr = Empire(natIr, empireFilePath)
talys = Talys(talysFilePath)
coh_natIr = Coh(natIr, cohFilePath)

# crossSectionData.plotCrossSection('Ir_189Pt')
# tendl_natIr.plotTendl23(productZ='78', productA='189', isomerLevel=None)
# empire_natIr.plotEmpire(productZ='78', productA='189', reaction = 'Ir_189Pt', isomerState=None)
# talys.plotTalys(productZ='78', productA='189', targetFoil='Ir', isomerLevel=None)
# plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {189} }}$Pt - Independent', "Ir_189Pt")

crossSectionData.plotCrossSection('Ir_193mPt')
tendl_natIr.plotTendl23(productZ='78', productA='193', isomerLevel='05')
empire_natIr.plotEmpire(productZ='78', productA='193', reaction = 'Ir_193mPt', isomerState='m')
talys.plotTalys(productZ='78', productA='193', targetFoil='Ir', isomerLevel='05')
coh_natIr.plotCoh(productZ = '78', productA='193', reaction='Ir_193mPt', isomerState = 'm')
plotExcitationFunction(r'$^{nat}$Ir(d,x)$^{{ {193m} }}$Pt - Independent', "Ir_193mPt", show=True)
