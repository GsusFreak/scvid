# To use:
# Place this script in the home directory
# and execute:
# python Compile_PyQt_4.py


import os


os.chdir('/home/admin1/epon_sims/sim_mgr/')

print '1'
os.system('pyuic4 -o plotnameform.py plotnameform_v4.ui')
print '2'
os.system('pyuic4 -o siminitform.py siminitform_v4.ui')
print '3'
os.system('pyuic4 -o simmgrform.py simmgrform_v4.ui')
print '4'
os.system('pyuic4 -o simviewform.py simviewform_v4.ui')
print '5'
os.system('pyuic4 -o waitform.py waitform_v4.ui')

print 'PyQt4 files updated.'
