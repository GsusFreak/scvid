# To use:
# Place this script in the home directory
# and execute:
# python Compile_PyQt.py


import os


os.chdir('/home/admin1/epon_sims/sim_mgr/')

os.system('pyuic -o plotnameform.py plotnameform.ui')
os.system('pyuic -o siminitform.py siminitform.ui')
os.system('pyuic -o simmgrform.py simmgrform.ui')
os.system('pyuic -o simviewform.py simviewform.ui')
os.system('pyuic -o waitform.py waitform.ui')

print 'PyQt files updated.'
