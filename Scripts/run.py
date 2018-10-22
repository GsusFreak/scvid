
import os
import sys
import shutil

# print sys.argv
# print type(sys.argv)

if len(sys.argv) is 1 or '-c' in sys.argv:
	os.chdir('eponsim')
	os.system('make eponsim')
	os.chdir('..')

if len(sys.argv) is 1 or '-r' in sys.argv:
	os.chdir('epon_sims/sim_mgr')
	os.system('python sim_mgr.py')
