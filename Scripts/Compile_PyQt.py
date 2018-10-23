# To use:
# Place this script in the home directory
# and execute:
# python Compile_PyQt_4.py


import os


os.chdir('/home/admin1/scvid/epon_sims/sim_mgr/')

print 'Attempting plotnameform.ui ...'
os.system('pyuic4 -o plotnameform.py plotnameform.ui -x')

print 'Attempting siminitform.ui ...'
os.system('pyuic4 -o siminitform.py siminitform.ui -x')

print 'Attempting simmgrform.ui ...'
os.system('pyuic4 -o simmgrform.py simmgrform.ui -x')

print 'Attempting simviewform.ui ...'
os.system('pyuic4 -o simviewform.py simviewform.ui -x')

print 'Attempting waitform.ui ...'
os.system('pyuic4 -o waitform.py waitform.ui -x')

print 'PyQt4 files updated.'
