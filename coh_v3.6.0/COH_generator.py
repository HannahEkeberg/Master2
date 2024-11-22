import os
import shutil
import itertools 
import sys
import fileinput


# targets = ['Cu-63', 'Cu-65']
# beta_rot = [0.151, -0.125]

# targets = ['Fe-54', 'Fe-56', 'Fe-57', 'Fe-58']
# beta_rot = [0,  0.117,  0.162, 0.173]

# targets = ['Ni-58', 'Ni-60', 'Ni-61', 'Ni-62', 'Ni-64']
# beta_rot = [0,  0,   0.107,  0.107, -0.094]

targets = ['Ir-191', 'Ir-193']
beta_rot = [ 0.164, 0.141]
# beta_2 From https://t2.lanl.gov/nis/molleretal/publications/ADNDT-FRDM2012.pdf




for (isotope, beta) in zip(targets, beta_rot):
	# print(isotope)
	# print(beta)
	A = isotope.split('-')[1]
	Z = isotope.split('-')[0]
	# print('A',A)
	# print('Z',Z)

	folder_name = Z+A
	print(folder_name)

	source = "./template/"
	dst = './'+Z+'/'+A+Z+'/'

	print(source)
	print(dst)

	try:
		shutil.copytree(source, dst)
	except FileExistsError:
		print('Directory ', dst, 'already exists, moving on...')


	# Update run_coh.sh
	coh_sh_path = dst+"run_coh.sh"

	# Read in the file
	with open(coh_sh_path, 'r') as file:
		filedata = file.read()

	# Replace the target string
	filedata = filedata.replace('TARGETNAME', A+Z)

	# Write the file out again
	with open(coh_sh_path, 'w') as file:
		file.write(filedata)




	# Update coh.dat
	coh_dat_path = dst+A+Z+"_coh.dat"
	try:
		os.rename(dst+"template_coh.dat", coh_dat_path)
	except:
		print('File', coh_dat_path, 'already renamed')

	# Read in the file
	with open(coh_dat_path, 'r') as file:
		filedata = file.read()

	# Replace the target string
	filedata = filedata.replace('ZZZ', Z)
	filedata = filedata.replace('AAA', A)
	filedata = filedata.replace('BETAROT', str(beta))

	# Write the file out again
	with open(coh_dat_path, 'w') as file:
		file.write(filedata)




	print('---------------------------------------------------')

