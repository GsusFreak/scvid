# To use:
# Place this script in the home directory
# and execute:
# python Compile_PyQt_4.py


import os


os.chdir('/home/admin1/scvid/epon_sims/sim_mgr/')

print '1'
os.system('pyuic4 -o plotnameform.py plotnameform.ui')
print '2'
os.system('pyuic4 -o siminitform.py siminitform.ui')
print '3'
os.system('pyuic4 -o simmgrform.py simmgrform.ui')
print '4'
os.system('pyuic4 -o simviewform.py simviewform.ui')
print '5'
os.system('pyuic4 -o waitform.py waitform.ui')

print 'PyQt4 files updated.'
