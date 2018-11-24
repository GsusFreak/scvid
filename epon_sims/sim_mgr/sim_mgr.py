#
# Simulation Manager
#
# Author: Michael McGarry
# Date: 12/14/04
#
# $Log: sim_mgr.py,v $
# Revision 1.7  2007/02/01 21:06:48  mmcgarry
# Added support for EAF and EAAF schedulers.
# Added support for fixed propagation delay.
#
# Revision 1.6  2006/03/14 20:27:46  mmcgarry
# Added DBA Type options (i.e., grant sizing)
#
# Revision 1.5  2005/12/20 19:30:47  mmcgarry
# Using pickle instead of marshal for storing data (pickle is more portable).
# Added simulation params for getting distribution tails.
#
# Revision 1.4  2005/11/02 15:44:37  mmcgarry
# Changed some sim parameter defaults.
# Added support for plots vs. ONU.
#
# Revision 1.3  2005/10/09 23:31:20  mmcgarry
# Added support for LFJ-LPT.
# Added support for script in different directory than sim data.
# Added waitform to vault.
#
# Revision 1.2  2005/10/09 22:39:33  mmcgarry
# Many enhancements
#
# Revision 1.1.1.1  2004/12/28 22:19:18  mmcgarry
# Initial version of Simulation Manager
#
#


# Import necessary modules

import pexpect
import tkFileDialog
import re
import subprocess, shutil

import shutil
import signal

import sys
import os
import copy
import time
import string
import pickle
import stat
#from qt import *  		#Qt3

from PyQt4.QtGui import * 	#Qt4
from PyQt4.QtCore import *	#Qt4
from PyQt4 import QtGui	#Qt4

from simmgrform import Ui_SimMgr
from siminitform import Ui_SimInitForm
from simviewform import Ui_SimViewForm
from waitform import Ui_WaitForm
from plotnameform import Ui_plotNameForm

#
# To port this code, modify these variables
# and create a form to input your simulation Parameters (siminitform.ui)
#

# Set up the working directories
print 'used directories:'
dir_sim_mgr = os.getcwd()
print dir_sim_mgr
dir_epon_sims = os.path.dirname(dir_sim_mgr)
print dir_epon_sims
dir_projectRoot = os.path.dirname(dir_epon_sims)
print dir_projectRoot
dir_eponsim = os.path.join(dir_projectRoot, 'eponsim')
print dir_eponsim
print 'end section -- used directories\n'


#dirRoot = '/home/admin1/scvid'

dirLauncher = os.path.join(dir_eponsim, 'eponsim')

st = os.stat(dirLauncher)
os.chmod(dirLauncher, st.st_mode | stat.S_IEXEC | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
# print st.st_mode

#path, empty = os.path.split(os.getcwd())
#path_2, directory = os.path.split(path)
#home, Username = os.path.split(path_2)

simusername = 'admin1'
simpassword = ''
simhomedir = str(dir_epon_sims)
#simhomedir_2 = str(directory)
#simcommand = 'eponsim/eponsim'
simhostname = 'localhost'
simParamsList = []	# a list
simParams = {}		# a dictionary

setupSimParamsList = []	# a list of lists
setupSimParams = [] # a list of dictionaries
queueSimParamsList = [] # a list of lists
queueSimParams = [] # a list of dictionaries
queueIndex = 0
queueIndexMax = 0
maxNumOfRunningSims = 1
finished_pids = []

# David's Funcitons:
def add_simParamsList():
	new_list = list(setupSimParamsList[-1])
	setupSimParamsList.append(new_list)

def add_simParams():
	new_dict = dict(setupSimParams[-1])
	setupSimParams.append(new_dict)
	
def store_parameters(self):
	global queueIndex
	global maxNumOfRunningSims
	if self.ui.svOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['SCALABLE_VIDEO_TRAFFIC'] = 'SCALABLE_VIDEO_OFF'
	if self.ui.svOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['SCALABLE_VIDEO_TRAFFIC'] = 'SCALABLE_VIDEO_ON'
	if self.ui.svDropNone.isChecked() == 1:
		setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] = 'SCALABLE_VIDEO_DROPPING_OFF'
	if self.ui.svDropThreshold.isChecked() == 1:
		setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] = 'SCALABLE_VIDEO_DROPPING_THRESHOLD'
	if self.ui.svDropDynamic.isChecked() == 1:
		setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] = 'SCALABLE_VIDEO_DROPPING_DYNAMIC'
	if self.ui.svDropStepThreshold.isChecked() == 1:
		setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] = 'SCALABLE_VIDEO_DROPPING_STEP_THRESHOLD'
	if self.ui.ipactpsfBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_IPACT_PSF'
	if self.ui.nascBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_NASC'
	if self.ui.ipactBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_IPACT'
	if self.ui.leastAssignedBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LEAST_ASSIGNED'
	if self.ui.apsBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_APS'
	if self.ui.lfjBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LFJ'
	if self.ui.lfjlptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LFJ_LPT'
	if self.ui.lfjsptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LFJ_SPT'
	if self.ui.lfjlnfBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LFJ_LNF'
	if self.ui.eafBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_EAF'
	if self.ui.eaafBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_EAAF'
	if self.ui.spdBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_SPD'
	if self.ui.lpdBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LPD'
	if self.ui.spdLptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_SPD_LPT'
	if self.ui.intvlLfjlptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_LFJ_LPT'
	if self.ui.intvlLfjsptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_LFJ_SPT'
	if self.ui.intvlLfjlnfBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_LFJ_LNF'
	if self.ui.intvlEafBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_EAF'
	if self.ui.intvlEaafBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_EAAF'
	if self.ui.jitLfjlptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_LFJ_LPT'
	if self.ui.jitLfjsptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_LFJ_SPT'
	if self.ui.jitLfjlnfBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_LFJ_LNF'
	if self.ui.jitEafBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_EAF'
	if self.ui.jitEaafBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_EAAF'
	if self.ui.jitSpdBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_SPD'
	if self.ui.jitLpdBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_LPD'
	if self.ui.jitTestBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_TEST'
	if self.ui.dbaGatedBtn.isChecked() == 1:
		setupSimParams[queueIndex]['DBA_TYPE'] = 'DBA_GATED'
	if self.ui.dbaFixedBtn.isChecked() == 1:
		setupSimParams[queueIndex]['DBA_TYPE'] = 'DBA_FIXED'
	if self.ui.dbaLimitedBtn.isChecked() == 1:
		setupSimParams[queueIndex]['DBA_TYPE'] = 'DBA_LIMITED_GATE'
	if self.ui.dbaExcessBtn.isChecked() == 1:
		setupSimParams[queueIndex]['DBA_TYPE'] = 'DBA_EXCESS'
	if self.ui.pnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['TRAFFIC_TYPE'] = 'TRAFFIC_POISSON'
	if self.ui.ssBtn.isChecked() == 1:
		setupSimParams[queueIndex]['TRAFFIC_TYPE'] = 'TRAFFIC_SELF_SIMILAR'
	if self.ui.tunableBtn.isChecked() == 1:
		setupSimParams[queueIndex]['WDM_TYPE'] = 'WDM_TUNABLE'
	if self.ui.fixedBtn.isChecked() == 1:
		setupSimParams[queueIndex]['WDM_TYPE'] = 'WDM_FIXED'
	if self.ui.fpdOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['FIXED_PROP_DELAY'] = 'FIXED_PROP_DELAY_ON'
	if self.ui.fpdOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['FIXED_PROP_DELAY'] = 'FIXED_PROP_DELAY_OFF'
	if self.ui.gtOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['GET_TAIL'] = 'GET_TAIL_ON'
	if self.ui.gtOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['GET_TAIL'] = 'GET_TAIL_OFF'
	if self.ui.ttOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['SIM_TRACE'] = 'SIM_TRACE_ON'
	if self.ui.ttOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['SIM_TRACE'] = 'SIM_TRACE_OFF'
	if self.ui.vtOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_TRAFFIC'] = 'VIDEO_TRAFFIC_ON'
		if setupSimParamsList[queueIndex].count('FRAME_RATE') == 0:
			setupSimParamsList[queueIndex].append('FRAME_RATE')
		setupSimParams[queueIndex]['FRAME_RATE'] = self.ui.frameRateEdit.text()
		if setupSimParamsList[queueIndex].count('VIDEO_TRACE_FILE') == 0:
			setupSimParamsList[queueIndex].append('VIDEO_TRACE_FILE')
		setupSimParams[queueIndex]['VIDEO_TRACE_FILE'] = self.ui.videoTraceEdit.text()
		if setupSimParamsList[queueIndex].count('VIDEO_PREDICTION') == 0:
			setupSimParamsList[queueIndex].append('VIDEO_PREDICTION')
		if self.ui.pvtOnBtn.isChecked() == 1 and setupSimParamsList[queueIndex].count('PREDICTION_TYPE') == 0:
			setupSimParamsList[queueIndex].append('PREDICTION_TYPE')
		if setupSimParamsList[queueIndex].count('TIME_SHIFT') == 0:
			setupSimParamsList[queueIndex].append('TIME_SHIFT')
		if setupSimParamsList[queueIndex].count('VIDEO_DBA_TYPE') == 0:
			setupSimParamsList[queueIndex].append('VIDEO_DBA_TYPE')
	if self.ui.pvtOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_PREDICTION'] = 'VIDEO_PREDICTION_ON'
		setupSimParams[queueIndex]['PREDICTION_TYPE'] = self.ui.PredTypeEdit.text()
	else:
		setupSimParams[queueIndex]['VIDEO_PREDICTION'] = 'VIDEO_PREDICTION_OFF'
	if self.ui.vsOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_RANDOM_START'] = 'VIDEO_RANDOM_START_ON'
		setupSimParams[queueIndex]['TIME_SHIFT'] = self.ui.timeShiftEdit.text()
	#else:
		#setupSimParams[queueIndex]['TIME_SHIFT'] = '0.0'
	if self.ui.vsOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_RANDOM_START'] = 'VIDEO_RANDOM_START_OFF'
	if self.ui.dbaGatedVideoBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] = 'VIDEO_DBA_GATED'
	if self.ui.dbaFixedVideoBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] = 'VIDEO_DBA_FIXED'
	if self.ui.dbaLimitedVideoBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] = 'VIDEO_DBA_LIMITED_GATE'
	if self.ui.vtOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_TRAFFIC'] = 'VIDEO_TRAFFIC_OFF'
	if self.ui.grtOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['GRANT_TRACE'] = 'GRANT_TRACE_ON'
	if self.ui.grtOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['GRANT_TRACE'] = 'GRANT_TRACE_OFF'
	if self.ui.schedulerMaxWinChkBox.isChecked() == 1:
		setupSimParams[queueIndex]['SCHEDULER_MAX_WINDOW'] = '1'
	else:
		setupSimParams[queueIndex]['SCHEDULER_MAX_WINDOW'] = '0'
	setupSimParams[queueIndex]['GUARD_TIME'] = self.ui.grdTimeEdit.text()
	setupSimParams[queueIndex]['TUNING_TIME'] = self.ui.tuningTimeEdit.text()
	setupSimParams[queueIndex]['FIXED_PROP_DELAY_VALUE'] = self.ui.fpdValueEdit.text()
	setupSimParams[queueIndex]['MAX_PROP_DELAY'] = self.ui.maxPropDelayEdit.text()
	setupSimParams[queueIndex]['NUM_RUNS'] = self.ui.runsEdit.text()
	setupSimParams[queueIndex]['NUM_ONU'] = self.ui.numONUEdit.text()
	setupSimParams[queueIndex]['NUM_HEAVY_ONU'] = self.ui.numHvyONUEdit.text()
	setupSimParams[queueIndex]['HEAVY_LOAD'] = self.ui.heavyLoadEdit.text()
	setupSimParams[queueIndex]['NUM_WDM_ONU'] = self.ui.numWdmONUEdit.text()
	setupSimParams[queueIndex]['NUM_UH_WDM_ONU'] = self.ui.numUhWdmONUEdit.text()
	setupSimParams[queueIndex]['NUM_LH_WDM_ONU'] = self.ui.numLhWdmONUEdit.text()
	setupSimParams[queueIndex]['LINK_SPEED'] = self.ui.linkSpdEdit.text()
	setupSimParams[queueIndex]['START_LOAD'] = self.ui.startLoadEdit.text()
	setupSimParams[queueIndex]['END_LOAD'] = self.ui.endLoadEdit.text()
	setupSimParams[queueIndex]['LOAD_INCR'] = self.ui.loadIncrEdit.text()
	setupSimParams[queueIndex]['START_LAMBDA'] = self.ui.startLambdaEdit.text()
	setupSimParams[queueIndex]['END_LAMBDA'] = self.ui.endLambdaEdit.text()
	setupSimParams[queueIndex]['SS_HURST_PARAM'] = self.ui.hurstParamEdit.text()
	setupSimParams[queueIndex]['NUM_SS_STREAMS'] = self.ui.numStrmsEdit.text()
	setupSimParams[queueIndex]['FIXED_GRANT_SIZE'] = self.ui.fixedGrantSizeEdit.text()
	setupSimParams[queueIndex]['MAX_GRANT_SIZE'] = self.ui.maxGrantSizeEdit.text()
	setupSimParams[queueIndex]['SCHEDULER_NUM_SLOT'] = self.ui.schedulerNumSlotEdit.text()
	setupSimParams[queueIndex]['SCHEDULER_SLOT_SIZE'] = self.ui.schedulerSlotSizeEdit.text()
	setupSimParams[queueIndex]['STARVE_THRESH'] = self.ui.starveThreshEdit.text()
	setupSimParams[queueIndex]['AVAIL_COST_WEIGHT'] = self.ui.acwEdit.text()
	setupSimParams[queueIndex]['NUM_PREFERRED_ONU'] = self.ui.npoEdit.text()
	setupSimParams[queueIndex]['SIM_TIME'] = self.ui.simTimeEdit.text()
	setupSimParams[queueIndex]['simID'] = self.ui.simIdEdit.text()
	setupSimParams[queueIndex]['SV_DROP_LAYER_THRESHOLD'] = self.ui.svDropThresholdEdit.text()
	setupSimParams[queueIndex]['SV_DROP_SENSITIVITY'] = self.ui.svDropSensitivity.text()
	setupSimParams[queueIndex]['SV_MIN_BOUND'] = self.ui.svDropStepMinBound.text()
	setupSimParams[queueIndex]['SV_MAX_BOUND'] = self.ui.svDropStepMaxBound.text()
	setupSimParams[queueIndex]['SV_NUM_MA_VALUES'] = self.ui.svDropStep_NumMAValues.text()
	maxNumOfRunningSims = int(self.ui.parallelSimsEdit.text())

	
def restore_parameters(self):
	global queueIndex
	global maxNumOfRunningSims
	if setupSimParams[queueIndex]['SCALABLE_VIDEO_TRAFFIC'] == 'SCALABLE_VIDEO_OFF':
		self.ui.svOffBtn.setChecked(1)
	if setupSimParams[queueIndex]['SCALABLE_VIDEO_TRAFFIC'] == 'SCALABLE_VIDEO_ON':
		self.ui.svOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_OFF':
		self.ui.svDropNone.setChecked(1)
	if setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_THRESHOLD':
		self.ui.svDropThreshold.setChecked(1)
	if setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_DYNAMIC':
		self.ui.svDropDynamic.setChecked(1)
	if setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_STEP_THRESHOLD':
		self.ui.svDropStepThreshold.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_IPACT_PSF':
		self.ui.ipactpsfBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_NASC':
		self.ui.nascBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_IPACT':
		self.ui.ipactBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LEAST_ASSIGNED':
		self.ui.leastAssignedBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_APS':
		self.ui.apsBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LFJ':
		self.ui.lfjBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LFJ_LPT':
		self.ui.lfjlptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LFJ_SPT':
		self.ui.lfjsptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LFJ_LNF':
		self.ui.lfjlnfBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_EAF':
		self.ui.eafBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_EAAF':
		self.ui.eaafBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_SPD':
		self.ui.spdBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LPD':
		self.ui.lpdBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_SPD_LPT':
		self.ui.spdLptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_LFJ_LPT':
		self.ui.intvlLfjlptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_LFJ_SPT':
		self.ui.intvlLfjsptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_LFJ_LNF':
		self.ui.intvlLfjlnfBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_EAF':
		self.ui.intvlEafBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_EAAF':
		self.ui.intvlEaafBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_LFJ_LPT':
		self.ui.jitLfjlptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_LFJ_SPT':
		self.ui.jitLfjsptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_LFJ_LNF':
		self.ui.jitLfjlnfBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_EAF':
		self.ui.jitEafBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_EAAF':
		self.ui.jitEaafBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_SPD':
		self.ui.jitSpdBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_LPD':
		self.ui.jitLpdBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_TEST':
		self.ui.jitTestBtn.setChecked(1)
	if setupSimParams[queueIndex]['DBA_TYPE'] == 'DBA_GATED':
		self.ui.dbaGatedBtn.setChecked(1)
	if setupSimParams[queueIndex]['DBA_TYPE'] == 'DBA_FIXED':
		self.ui.dbaFixedBtn.setChecked(1)
	if setupSimParams[queueIndex]['DBA_TYPE'] == 'DBA_LIMITED_GATE':
		self.ui.dbaLimitedBtn.setChecked(1)
	if setupSimParams[queueIndex]['DBA_TYPE'] == 'DBA_EXCESS':
		self.ui.dbaExcessBtn.setChecked(1)
	if setupSimParams[queueIndex]['TRAFFIC_TYPE'] == 'TRAFFIC_POISSON':
		self.ui.pnBtn.setChecked(1)
	if setupSimParams[queueIndex]['TRAFFIC_TYPE'] == 'TRAFFIC_SELF_SIMILAR':
		self.ui.ssBtn.setChecked(1)
	if setupSimParams[queueIndex]['WDM_TYPE'] == 'WDM_FIXED':
		self.ui.fixedBtn.setChecked(1)
	if setupSimParams[queueIndex]['WDM_TYPE'] == 'WDM_TUNABLE':
		self.ui.tunableBtn.setChecked(1)
	if setupSimParams[queueIndex]['FIXED_PROP_DELAY'] == 'FIXED_PROP_DELAY_ON':
		self.ui.fpdOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['FIXED_PROP_DELAY'] == 'FIXED_PROP_DELAY_OFF':
		self.ui.fpdOffBtn.setChecked(1)
	if setupSimParams[queueIndex]['GET_TAIL'] == 'GET_TAIL_ON':
		self.ui.gtOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['GET_TAIL'] == 'GET_TAIL_OFF':
		self.ui.gtOffBtn.setChecked(1)
	if setupSimParams[queueIndex]['SIM_TRACE'] == 'SIM_TRACE_ON':
		self.ui.ttOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['SIM_TRACE'] == 'SIM_TRACE_OFF': 
		self.ui.ttOffBtn.setChecked(1) 
	if setupSimParams[queueIndex]['VIDEO_TRAFFIC'] == 'VIDEO_TRAFFIC_ON':
		self.ui.vtOnBtn.setChecked(1)
		self.ui.videoTraceEdit.setText(setupSimParams[queueIndex]['VIDEO_TRACE_FILE'])
	if setupSimParams[queueIndex]['VIDEO_PREDICTION'] == 'VIDEO_PREDICTION_ON':
		self.ui.pvtOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_PREDICTION'] == 'VIDEO_PREDICTION_OFF':
		self.ui.pvtOffBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] == 'VIDEO_DBA_GATED':
		self.ui.dbaGatedVideoBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] == 'VIDEO_DBA_FIXED':
		self.ui.dbaFixedVideoBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] == 'VIDEO_DBA_LIMITED_GATE':
		self.ui.dbaLimitedVideoBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_RANDOM_START'] == 'VIDEO_RANDOM_START_ON':
		self.ui.vsOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_RANDOM_START'] == 'VIDEO_RANDOM_START_OFF':
		self.ui.vsOffBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_TRAFFIC'] == 'VIDEO_TRAFFIC_OFF':
		self.ui.vtOffBtn.setChecked(1)
		try:
			for param in setupSimParamsList[queueIndex]:
				setupSimParamsList[queueIndex].remove('FRAME_RATE')
		except:
			pass
		try:
			for param in setupSimParamsList[queueIndex]:
				setupSimParamsList[queueIndex].remove('VIDEO_TRACE_FILE')
		except:
			pass
		try:
			for param in setupSimParamsList[queueIndex]:
				setupSimParamsList[queueIndex].remove('VIDEO_PREDICTION')
		except:
			pass
		try:
			for param in setupSimParamsList[queueIndex]:
				setupSimParamsList[queueIndex].remove('PREDICTION_TYPE')
		except:
			pass
		try:
			for param in setupSimParamsList[queueIndex]:
				setupSimParamsList[queueIndex].remove('TIME_SHIFT')
		except:
			pass
		try:
			for param in setupSimParamsList[queueIndex]:
				setupSimParamsList[queueIndex].remove('VIDEO_DBA_TYPE')
		except:
			pass
	if setupSimParams[queueIndex]['GRANT_TRACE'] == 'GRANT_TRACE_ON':
		self.ui.grtOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['GRANT_TRACE'] == 'GRANT_TRACE_OFF':
		self.ui.grtOffBtn.setChecked(1)
	if setupSimParams[queueIndex]['SCHEDULER_MAX_WINDOW'] == '1':
		self.ui.schedulerMaxWinChkBox.setChecked(1)
	else:
		self.ui.schedulerMaxWinChkBox.setChecked(0)
	self.ui.hostEdit.setText(simhostname)
	self.ui.grdTimeEdit.setText(setupSimParams[queueIndex]['GUARD_TIME'])
	self.ui.tuningTimeEdit.setText(setupSimParams[queueIndex]['TUNING_TIME'])
	self.ui.fpdValueEdit.setText(setupSimParams[queueIndex]['FIXED_PROP_DELAY_VALUE'])
	self.ui.maxPropDelayEdit.setText(setupSimParams[queueIndex]['MAX_PROP_DELAY'])
	self.ui.runsEdit.setText(setupSimParams[queueIndex]['NUM_RUNS'])
	self.ui.numONUEdit.setText(setupSimParams[queueIndex]['NUM_ONU'])
	self.ui.numHvyONUEdit.setText(setupSimParams[queueIndex]['NUM_HEAVY_ONU'])
	self.ui.heavyLoadEdit.setText(setupSimParams[queueIndex]['HEAVY_LOAD'])
	self.ui.numWdmONUEdit.setText(setupSimParams[queueIndex]['NUM_WDM_ONU'])
	self.ui.numUhWdmONUEdit.setText(setupSimParams[queueIndex]['NUM_UH_WDM_ONU'])
	self.ui.numLhWdmONUEdit.setText(setupSimParams[queueIndex]['NUM_LH_WDM_ONU'])
	self.ui.linkSpdEdit.setText(setupSimParams[queueIndex]['LINK_SPEED'])
	self.ui.startLoadEdit.setText(setupSimParams[queueIndex]['START_LOAD'])
	self.ui.endLoadEdit.setText(setupSimParams[queueIndex]['END_LOAD'])
	self.ui.loadIncrEdit.setText(setupSimParams[queueIndex]['LOAD_INCR'])
	self.ui.startLambdaEdit.setText(setupSimParams[queueIndex]['START_LAMBDA'])
	self.ui.endLambdaEdit.setText(setupSimParams[queueIndex]['END_LAMBDA'])
	self.ui.hurstParamEdit.setText(setupSimParams[queueIndex]['SS_HURST_PARAM'])
	self.ui.numStrmsEdit.setText(setupSimParams[queueIndex]['NUM_SS_STREAMS'])
	self.ui.fixedGrantSizeEdit.setText(setupSimParams[queueIndex]['FIXED_GRANT_SIZE'])
	self.ui.frameRateEdit.setText(setupSimParams[queueIndex]['FRAME_RATE'])
	self.ui.maxGrantSizeEdit.setText(setupSimParams[queueIndex]['MAX_GRANT_SIZE'])
	self.ui.schedulerNumSlotEdit.setText(setupSimParams[queueIndex]['SCHEDULER_NUM_SLOT'])
	self.ui.schedulerSlotSizeEdit.setText(setupSimParams[queueIndex]['SCHEDULER_SLOT_SIZE'])
	self.ui.starveThreshEdit.setText(setupSimParams[queueIndex]['STARVE_THRESH'])
	self.ui.acwEdit.setText(setupSimParams[queueIndex]['AVAIL_COST_WEIGHT'])
	self.ui.npoEdit.setText(setupSimParams[queueIndex]['NUM_PREFERRED_ONU'])
	self.ui.PredTypeEdit.setText(setupSimParams[queueIndex]['PREDICTION_TYPE'])
	self.ui.simTimeEdit.setText(setupSimParams[queueIndex]['SIM_TIME'])
	self.ui.timeShiftEdit.setText(setupSimParams[queueIndex]['TIME_SHIFT'])
	self.ui.queueIndexSlotEdit.setText(str(queueIndex + 1))
	self.ui.simIdEdit.setText(setupSimParams[queueIndex]['simID'])
	self.ui.parallelSimsEdit.setText(str(maxNumOfRunningSims))
	self.ui.svDropThresholdEdit.setText(str(setupSimParams[queueIndex]['SV_DROP_LAYER_THRESHOLD']))
	self.ui.svDropSensitivity.setText(str(setupSimParams[queueIndex]['SV_DROP_SENSITIVITY']))
	self.ui.svDropStepMinBound.setText(str(setupSimParams[queueIndex]['SV_MIN_BOUND']))
	self.ui.svDropStepMaxBound.setText(str(setupSimParams[queueIndex]['SV_MAX_BOUND']))
	self.ui.svDropStep_NumMAValues.setText(str(setupSimParams[queueIndex]['SV_NUM_MA_VALUES']))
	#if self.ui.svOnBtn.isChecked():
		#self.ui.svButtonGroup.setEnabled(True)
	#else:
		#self.ui.svButtonGroup.setEnabled(False)
	if self.ui.vtOnBtn.isChecked():
		self.ui.videoTraceEdit.setEnabled(True)
		self.ui.changeTraceBtn.setEnabled(True)
		#self.ui.VideoDBABtnGroup.setEnabled(True)
		# Replacement:
		
		
		self.ui.dbaGatedVideoBtn.setEnabled(True)
		self.ui.dbaFixedVideoBtn.setEnabled(True)
		self.ui.dbaLimitedVideoBtn.setEnabled(True)
		#self.ui.predictTrafficBox.setEnabled(True)
		self.ui.FRateLbl.setEnabled(True)
		self.ui.frameRateEdit.setEnabled(True)
		#self.ui.videoStartBox.setEnabled(True)
		self.ui.ipactpsfBtn.setEnabled(True)
		#self.ui.scalableVideoBox.setEnabled(True)
		self.ui.svDropThresholdEdit.setEnabled(True)
		self.ui.svDropSensitivity.setEnabled(True)
		self.ui.svDropStepMinBound.setEnabled(True)
		self.ui.svDropStepMaxBound.setEnabled(True)
		self.ui.svDropStep_NumMAValues.setEnabled(True)
		self.ui.svDropMinBoundLabel.setEnabled(True)
		self.ui.svDropMaxBoundLabel.setEnabled(True)
	else:
		self.ui.videoTraceEdit.clear()
		self.ui.videoTraceEdit.setEnabled(False)
		self.ui.changeTraceBtn.setEnabled(False)
		#self.ui.VideoDBABtnGroup.setEnabled(False)
		self.ui.dbaGatedVideoBtn.setEnabled(False)
		self.ui.dbaFixedVideoBtn.setEnabled(False)
		self.ui.dbaLimitedVideoBtn.setEnabled(False)
		#self.ui.predictTrafficBox.setEnabled(False)
		self.ui.FRateLbl.setEnabled(False)
		self.ui.frameRateEdit.setEnabled(False)
		#self.ui.videoStartBox.setEnabled(False)
		#if self.ui.ipactpsfBtn.isChecked() == 1:
			#self.ui.nascBtn.setChecked(1)
		self.ui.ipactpsfBtn.setEnabled(False)
		#self.ui.scalableVideoBox.setEnabled(False)
		self.ui.svDropThresholdEdit.setEnabled(False)
		self.ui.svDropSensitivity.setEnabled(False)
		self.ui.svDropStepMinBound.setEnabled(False)
		self.ui.svDropStepMaxBound.setEnabled(False)
		self.ui.svDropStep_NumMAValues.setEnabled(False)
		self.ui.svDropMinBoundLabel.setEnabled(False)
		self.ui.svDropMaxBoundLabel.setEnabled(False)
	if self.ui.pvtOnBtn.isChecked():
		self.ui.PredTypeLbl.setEnabled(True)
		self.ui.PredTypeEdit.setEnabled(True)
	else:
		self.ui.PredTypeLbl.setEnabled(False)
		self.ui.PredTypeEdit.setEnabled(False)
	if self.ui.vsOffBtn.isChecked():
		self.ui.timeShiftLbl.setEnabled(False)
		self.ui.timeShiftEdit.setEnabled(False)
	else:
		self.ui.timeShiftLbl.setEnabled(True)
		self.ui.timeShiftEdit.setEnabled(True)
	# app.processEvents(0)


def saveSettingsBtn_pressed2(self):
	global plotSettings
	plotSettings['pointsCBox1'] = self.ui.pointsCBox1.currentIndex()
	plotSettings['pointsCBox2'] = self.ui.pointsCBox2.currentIndex()
	plotSettings['pointsCBox3'] = self.ui.pointsCBox3.currentIndex()
	plotSettings['pointsCBox4'] = self.ui.pointsCBox4.currentIndex()
	plotSettings['pointsCBox5'] = self.ui.pointsCBox5.currentIndex()
	plotSettings['pointsCBox6'] = self.ui.pointsCBox6.currentIndex()
	plotSettings['pointsCBox7'] = self.ui.pointsCBox7.currentIndex()
	plotSettings['pointsCBox8'] = self.ui.pointsCBox8.currentIndex()
	
	plotSettings['file1Edit'] = self.ui.file1Edit.text()
	plotSettings['file2Edit'] = self.ui.file2Edit.text()
	plotSettings['file3Edit'] = self.ui.file3Edit.text()
	plotSettings['file4Edit'] = self.ui.file4Edit.text()
	plotSettings['file5Edit'] = self.ui.file5Edit.text()
	plotSettings['file6Edit'] = self.ui.file6Edit.text()
	plotSettings['file7Edit'] = self.ui.file7Edit.text()
	plotSettings['file8Edit'] = self.ui.file8Edit.text()
	
	plotSettings['pointSizeCBox1'] = self.ui.pointSizeCBox1.currentIndex()
	plotSettings['pointSizeCBox2'] = self.ui.pointSizeCBox2.currentIndex()
	plotSettings['pointSizeCBox3'] = self.ui.pointSizeCBox3.currentIndex()
	plotSettings['pointSizeCBox4'] = self.ui.pointSizeCBox4.currentIndex()
	plotSettings['pointSizeCBox5'] = self.ui.pointSizeCBox5.currentIndex()
	plotSettings['pointSizeCBox6'] = self.ui.pointSizeCBox6.currentIndex()
	plotSettings['pointSizeCBox7'] = self.ui.pointSizeCBox7.currentIndex()
	plotSettings['pointSizeCBox8'] = self.ui.pointSizeCBox8.currentIndex()
	
	plotSettings['lineWidthCBox1'] = self.ui.lineWidthCBox1.currentIndex()
	plotSettings['lineWidthCBox2'] = self.ui.lineWidthCBox2.currentIndex()
	plotSettings['lineWidthCBox3'] = self.ui.lineWidthCBox3.currentIndex()
	plotSettings['lineWidthCBox4'] = self.ui.lineWidthCBox4.currentIndex()
	plotSettings['lineWidthCBox5'] = self.ui.lineWidthCBox5.currentIndex()
	plotSettings['lineWidthCBox6'] = self.ui.lineWidthCBox6.currentIndex()
	plotSettings['lineWidthCBox7'] = self.ui.lineWidthCBox7.currentIndex()
	plotSettings['lineWidthCBox8'] = self.ui.lineWidthCBox8.currentIndex()
	
	plotSettings['lineColorCBox1'] = self.ui.lineColorCBox1.currentIndex()
	plotSettings['lineColorCBox2'] = self.ui.lineColorCBox2.currentIndex()
	plotSettings['lineColorCBox3'] = self.ui.lineColorCBox3.currentIndex()
	plotSettings['lineColorCBox4'] = self.ui.lineColorCBox4.currentIndex()
	plotSettings['lineColorCBox5'] = self.ui.lineColorCBox5.currentIndex()
	plotSettings['lineColorCBox6'] = self.ui.lineColorCBox6.currentIndex()
	plotSettings['lineColorCBox7'] = self.ui.lineColorCBox7.currentIndex()
	plotSettings['lineColorCBox8'] = self.ui.lineColorCBox8.currentIndex()


def restoreSettingsBtn_pressed2(self):
	global plotSettings
	self.ui.pointsCBox1.setCurrentIndex(plotSettings['pointsCBox1'])
	self.ui.pointsCBox2.setCurrentIndex(plotSettings['pointsCBox2'])
	self.ui.pointsCBox3.setCurrentIndex(plotSettings['pointsCBox3'])
	self.ui.pointsCBox4.setCurrentIndex(plotSettings['pointsCBox4'])
	self.ui.pointsCBox5.setCurrentIndex(plotSettings['pointsCBox5'])
	self.ui.pointsCBox6.setCurrentIndex(plotSettings['pointsCBox6'])
	self.ui.pointsCBox7.setCurrentIndex(plotSettings['pointsCBox7'])
	self.ui.pointsCBox8.setCurrentIndex(plotSettings['pointsCBox8'])
	
	self.ui.file1Edit.setText(plotSettings['file1Edit'])
	self.ui.file2Edit.setText(plotSettings['file2Edit'])
	self.ui.file3Edit.setText(plotSettings['file3Edit'])
	self.ui.file4Edit.setText(plotSettings['file4Edit'])
	self.ui.file5Edit.setText(plotSettings['file5Edit'])
	self.ui.file6Edit.setText(plotSettings['file6Edit'])
	self.ui.file7Edit.setText(plotSettings['file7Edit'])
	self.ui.file8Edit.setText(plotSettings['file8Edit'])
	
	self.ui.pointSizeCBox1.setCurrentIndex(plotSettings['pointSizeCBox1'])
	self.ui.pointSizeCBox2.setCurrentIndex(plotSettings['pointSizeCBox2'])
	self.ui.pointSizeCBox3.setCurrentIndex(plotSettings['pointSizeCBox3'])
	self.ui.pointSizeCBox4.setCurrentIndex(plotSettings['pointSizeCBox4'])
	self.ui.pointSizeCBox5.setCurrentIndex(plotSettings['pointSizeCBox5'])
	self.ui.pointSizeCBox6.setCurrentIndex(plotSettings['pointSizeCBox6'])
	self.ui.pointSizeCBox7.setCurrentIndex(plotSettings['pointSizeCBox7'])
	self.ui.pointSizeCBox8.setCurrentIndex(plotSettings['pointSizeCBox8'])
	
	self.ui.lineWidthCBox1.setCurrentIndex(plotSettings['lineWidthCBox1'])
	self.ui.lineWidthCBox2.setCurrentIndex(plotSettings['lineWidthCBox2'])
	self.ui.lineWidthCBox3.setCurrentIndex(plotSettings['lineWidthCBox3'])
	self.ui.lineWidthCBox4.setCurrentIndex(plotSettings['lineWidthCBox4'])
	self.ui.lineWidthCBox5.setCurrentIndex(plotSettings['lineWidthCBox5'])
	self.ui.lineWidthCBox6.setCurrentIndex(plotSettings['lineWidthCBox6'])
	self.ui.lineWidthCBox7.setCurrentIndex(plotSettings['lineWidthCBox7'])
	self.ui.lineWidthCBox8.setCurrentIndex(plotSettings['lineWidthCBox8'])
	
	self.ui.lineColorCBox1.setCurrentIndex(plotSettings['lineColorCBox1'])
	self.ui.lineColorCBox2.setCurrentIndex(plotSettings['lineColorCBox2'])
	self.ui.lineColorCBox3.setCurrentIndex(plotSettings['lineColorCBox3'])
	self.ui.lineColorCBox4.setCurrentIndex(plotSettings['lineColorCBox4'])
	self.ui.lineColorCBox5.setCurrentIndex(plotSettings['lineColorCBox5'])
	self.ui.lineColorCBox6.setCurrentIndex(plotSettings['lineColorCBox6'])
	self.ui.lineColorCBox7.setCurrentIndex(plotSettings['lineColorCBox7'])
	self.ui.lineColorCBox8.setCurrentIndex(plotSettings['lineColorCBox8'])
	
# END David's Functions


# global simulation data
sims = {}
simData = {}
plotSettings = {}

fileList = []

plotType = 0

setupSimParamsList.append(simParamsList)
setupSimParams.append(simParams)


simParamsList.append('OLT_TYPE')
simParamsList.append('DBA_TYPE')
simParamsList.append('TRAFFIC_TYPE')

simParamsList.append('VIDEO_TRAFFIC')

simParamsList.append('SCALABLE_VIDEO_TRAFFIC')
simParamsList.append('SCALABLE_VIDEO_DROPPING_ALGORITHM')
simParamsList.append('SV_DROP_LAYER_THRESHOLD')
simParamsList.append('SV_DROP_SENSITIVITY')
simParamsList.append('SV_MIN_BOUND')
simParamsList.append('SV_MAX_BOUND')
simParamsList.append('SV_NUM_MA_VALUES')

simParamsList.append('WDM_TYPE')
simParamsList.append('GUARD_TIME')
simParamsList.append('TUNING_TIME')
simParamsList.append('NUM_RUNS')
simParamsList.append('NUM_ONU')
simParamsList.append('NUM_HEAVY_ONU')
simParamsList.append('HEAVY_LOAD')
simParamsList.append('LINK_SPEED')

simParamsList.append('NUM_WDM_ONU')
simParamsList.append('NUM_UH_WDM_ONU')
simParamsList.append('NUM_LH_WDM_ONU')

simParamsList.append('SS_HURST_PARAM')
simParamsList.append('NUM_SS_STREAMS')

simParamsList.append('START_LOAD')
simParamsList.append('END_LOAD')
simParamsList.append('LOAD_INCR')

simParamsList.append('START_LAMBDA')
simParamsList.append('END_LAMBDA')

simParamsList.append('FIXED_GRANT_SIZE')
simParamsList.append('MAX_GRANT_SIZE')

simParamsList.append('SCHEDULER_MAX_WINDOW')
simParamsList.append('SCHEDULER_NUM_SLOT')
simParamsList.append('SCHEDULER_SLOT_SIZE')
simParamsList.append('STARVE_THRESH')
simParamsList.append('AVAIL_COST_WEIGHT')
simParamsList.append('NUM_PREFERRED_ONU')

simParamsList.append('SIM_TIME')

simParamsList.append('GET_TAIL')
simParamsList.append('SIM_TRACE')
simParamsList.append('GRANT_TRACE')

simParamsList.append('FIXED_PROP_DELAY')
simParamsList.append('FIXED_PROP_DELAY_VALUE')
simParamsList.append('MAX_PROP_DELAY')

simParams['OLT_TYPE']   	= 'OLT_ONLINE_NASC'
simParams['DBA_TYPE']   	= 'DBA_LIMITED'
simParams['TRAFFIC_TYPE']   = 'TRAFFIC_POISSON' # Traffic Type
simParams['WDM_TYPE']   	= 'WDM_FIXED' # WDM Type
simParams['GUARD_TIME'] 	= '1e-6'
simParams['TUNING_TIME']	= '5e-3'
simParams['NUM_RUNS']   	= '1'   # Number of independent runs
simParams['NUM_ONU']		= '32'  # Number of ONUs on PON
simParams['NUM_HEAVY_ONU'] 	= '0'   # Number of heavily loaded ONUs
simParams['HEAVY_LOAD'] 	= '2'   # heavily loaded ONU multiple
simParams['LINK_SPEED'] 	= '1e9' # link speed in bps

simParams['SCALABLE_VIDEO_TRAFFIC']				= 'SCALABLE_VIDEO_OFF'
simParams['SCALABLE_VIDEO_DROPPING_ALGORITHM']	= 'SCALABLE_VIDEO_DROPPING_OFF'
simParams['SV_DROP_LAYER_THRESHOLD']			= '4'
simParams['SV_DROP_SENSITIVITY']				= '1.0'
simParams['SV_MIN_BOUND']				= '0.0005'
simParams['SV_MAX_BOUND']				= '0.005'
simParams['SV_NUM_MA_VALUES']				= '5'

simParams['NUM_WDM_ONU']		= '0'   # Number of WDM ONUs
simParams['NUM_UH_WDM_ONU'] 	= '0'   # Number of WDM ONUs
simParams['NUM_LH_WDM_ONU'] 	= '0'   # Number of WDM ONUs

simParams['SS_HURST_PARAM'] 	= '0.75'# Self Similar Traffic Source Hurst Parameter
simParams['NUM_SS_STREAMS'] 	= '32'  # Number of Self Similar Traffic Streams

simParams['START_LOAD'] 	= '0.1'
simParams['END_LOAD']   	= '0.9'
simParams['LOAD_INCR']  	= '0.1'

simParams['START_LAMBDA']   	= '1'
simParams['END_LAMBDA'] 	= '1'

#simParams['FIXED_GRANT_SIZE']   = '1534'
#simParams['MAX_GRANT_SIZE'] 	= '7188'

simParams['FIXED_GRANT_SIZE']   = '156876'
simParams['MAX_GRANT_SIZE'] 	= '156876'

simParams['SCHEDULER_MAX_WINDOW'] 	= '0'
simParams['SCHEDULER_NUM_SLOT'] 	= '180'
simParams['SCHEDULER_SLOT_SIZE']	= '64'
simParams['STARVE_THRESH']  		= '64'
simParams['AVAIL_COST_WEIGHT']  	= '1.0'
simParams['NUM_PREFERRED_ONU']  	= '0'

simParams['SIM_TIME']   		= '300'

simParams['GET_TAIL']   		= 'GET_TAIL_OFF'
simParams['SIM_TRACE']  		= 'SIM_TRACE_OFF'
simParams['GRANT_TRACE']		= 'GRANT_TRACE_OFF'
simParams['FIXED_PROP_DELAY']   	= 'FIXED_PROP_DELAY_OFF'
simParams['FIXED_PROP_DELAY_VALUE'] 	= '50e-6'
simParams['MAX_PROP_DELAY'] 		= '50e-6'
simParams['GRANT_TRACE'] 			= 'GRANT_TRACE_OFF'

simParams['VIDEO_TRAFFIC']			= 'VIDEO_TRAFFIC_OFF'
simParams['VIDEO_PREDICTION']		= 'VIDEO_PREDICTION_OFF'
simParams['VIDEO_TRACE_FILE']		= ''
simParams['VIDEO_RANDOM_START']		= 'VIDEO_RANDOM_START_OFF'
simParams['TIME_SHIFT'] 			= '0.0'
simParams['VIDEO_DBA_TYPE'] 		= 'VIDEO_DBA_LIMITED'
simParams['SCHEDULER_MAX_WINDOW'] 	= 'NULL'
simParams['simID']					= ''
simParams['FRAME_RATE']				= '30.0'
simParams['PREDICTION_TYPE']		= 'FFBI'


def initialize_data_structure():
	pass
	
	


def load_sim_data():
	simList = []
	global sims
	os.chdir(dir_epon_sims)
	if os.path.exists('sim_mgr_data'):
		simpicklefile = open('sim_mgr_data', 'r')
		unpickler = pickle.Unpickler(simpicklefile)
		sims = unpickler.load()
		simpicklefile.close()
		simList = sims.keys()
		simList.sort()
		for loopIdx in range(len(simList)):
			sim_mgr_win.ui.simListBox.addItem(simList[loopIdx])


def load_plot_settings():
	global plotSettings
	os.chdir(dir_epon_sims)
	if os.path.exists('plot_settings_data'):
		plotSettingsPicklefile = open('plot_settings_data', 'r')
		unpickler = pickle.Unpickler(plotSettingsPicklefile)
		plotSettings = unpickler.load()
		plotSettingsPicklefile.close()
		restoreSettingsBtn_pressed2(plot_name_win)
	else:
		saveSettingsBtn_pressed2(plot_name_win)


def load_test_num():
	global testNum
	os.chdir(dir_epon_sims)
	if os.path.exists('test_num'):
		testNumPickleFile = open('test_num', 'r')
		unpickler = pickle.Unpickler(testNumPickleFile)
		testNum = unpickler.load()
		testNumPickleFile.close()
	else:
		testNum = 1


def write_sim_param_file():
	sim_cfg = open('sim_cfg','w')
	for loopIdx in range(len(simParamsList)):
		sim_cfg.write(queueSimParamsList[0][loopIdx] + '\t' + queueSimParams[0][simParamsList[loopIdx]] + '\n')
	sim_cfg.close()

    
def generate_file_list(file_list,list_box):
	for loopIdx in range(list_box.count()):
		if list_box.isSelected(loopIdx) == 1:
			file_list.append(list_box.item(loopIdx).text())

def check_pids(currentlyRunning):
	global finished_pids
	finished_pids = []
	for iaa in range(len(currentlyRunning)):
		pid, simID = currentlyRunning[iaa]
		try:
			os.kill(pid, 0)
		except:
			finished_pids.append(pid)
	#print 'finished_pids: {}'.format(finished_pids)
	
def conclude_simulation(pid, currentlyRunning):
	#print 'conclude_simulation has been run'
	#print 'currentlyRunning: {}'.format(currentlyRunning)
	for simPidTmp, simIDTmp in currentlyRunning:
		if simPidTmp == pid:
			simPid = simPidTmp
			simID = simIDTmp
			break
		else:
			return
			
	simListBoxItem = sim_mgr_win.ui.startedListBox.findItem(simID)
	sim_mgr_win.ui.startedListBox.takeItem(simListBoxItem)
	sim_mgr_win.ui.simListBox.insertItem(simID)
	print simID + ' has concluded.'
	#print '(pid, simID): ({}, {})'.format(simPid, simID)
	currentlyRunning.remove((simPid, simID))
	#print 'currentlyRunning: {}'.format(currentlyRunning)
	return
	
def launch_additional_sim(currentlyRunning, simpassword):
	global queueSimParamsList
	global queueSimParams
	global simusername
	global simhomedir
	global simhomedir_2
	global simcommand
	global simhostname
	
	#print 'launch_additional_sim has been run'
	
	simID = queueSimParams[0]['simID']
	os.chdir(dir_epon_sims)
	if os.path.exists(simID) != 1:
		os.mkdir(simID)
	os.chdir(simID)
	
	pid_file = open('pid','w')
	pid_file.close()
	
	# Write Sim Parameter File
	write_sim_param_file()
	# Find a prime host for simulation
	# upTimeStr = os.popen('ssh -f -lmcgarrym '+currHost+' uptime').read()
	# load = float(upTimeStr[upTimeStr.find('load average:'):].split(':')[1].split(',')[0])
	# simhostname = ???
	# Launch simulation on host
	
	
	#ExecutePath = os.path.join(os.path.join('/home',str(simusername)), str(simhomedir_2))
	ExecutePath = dir_epon_sims
	SimPath = os.join(dir_epon_sims, simID)
	#os.chdir(os.path.join('/home',str(simusername)))
	os.chdir(dir_project)
	#simcommandfinal = 'valgrind --leak-check=yes --log-file=valgrind_output ' + os.path.join(os.path.join('/home',str(simusername)), str(simcommand))
	#cmd = 'ssh -f -l'+simusername+' '+simhostname+' \'cd '+ExecutePath+'/'+simID+'; '+simcommandfinal+' > sim_log &\''
	#simcommandfinal = os.path.join(os.path.join('/home',str(simusername)), str(simcommand))
	cmd = 'ssh -f -l' + simusername + ' ' + simhostname + ' \'cd ' + SimPath + '; ' + dirLauncher + ' > sim_log &\''
	child = pexpect.spawn(cmd)
	# expect ssh to prompt for a user password
	child.expect('Password:')
	print str(simusername) + '@' + str(simhostname) + '\'s' + ' password:'
	# send the password
	child.sendline(str(simpassword))
	child.read()
	
	if child.isalive() == False:
		print 'Simulation Launched Successfully'

		ResultPath = os.path.join(SimPath, 'pid')
		
#		retVal = os.system('ssh -f -l'+simusername+' '+simhostname+' \'cd '+simhomedir+'/'+simID+'; '+simcommandfinal+' >sim_log &\'')
#		if retVal == 0:
		# Get it's process ID
		
#			while not os.path.exists(ResultPath):
#				time.sleep(1) # wait 1 second, then check again
		
		pidFile = open(ResultPath,'r')
		pidStr = pidFile.readline()
		pidFile.close()
		while pidStr == "":
			time.sleep(0.1)
			pidFile = open(ResultPath,'r')
			pidStr = pidFile.readline()
			pidFile.close()
		
		
		if ((pidStr == 'done\n') or (pidStr == 'Failed\n')):
			simpid = 0
		else:
			simpid = int(pidStr)
			currentlyRunning.append((simpid,simID))
		if pidStr == 'Failed\n':
			os.system('mv sim_core ..')
			time.sleep(1)
			os.system('rm *')
			time.sleep(5)
			os.chdir('..')
			os.system('rm -rf ' + simID)
			print "Launch Failed!!!!"
		else:
			# Record simulation data and place an entry in simulation list box
			simData['host'] = simhostname
			simData['pid'] = simpid
			simData['params'] = copy.deepcopy(queueSimParams[0])
			sims[simID] = copy.deepcopy(simData)
			#simListBoxItem = sim_mgr_win.simListBox.findItem(simID + '_(Not_Started)')
			#indexOfItem = sim_mgr_win.simListBox.index(simListBoxItem)
			#sim_mgr_win.ui.simListBox.changeItem(simID + '_(Started)', indexOfItem)
			simListBoxItem = sim_mgr_win.ui.notStartedListBox.findItem(simID)
			sim_mgr_win.ui.notStartedListBox.takeItem(simListBoxItem)
			sim_mgr_win.ui.startedListBox.insertItem(simID)
			#sim_mgr_win.ui.simListBox.setCurrentItem(simID)
			#sim_mgr_win.ui.simListBox.currentItem().setTextColor(qColor.fromRgb(255,0,0,255))
			os.chdir('..')
			print 'Sim ID: ' + simID + '   Sim Host: ' + simhostname + '   Simulation ID: ' + str(simpid)
	else:	
		os.system('rm *')
		time.sleep(5)
		os.chdir('..')
		os.system('rm -rf ' + simID)
		print "Launch Failed!!!!"
		
	queueSimParamsList.remove(queueSimParamsList[0])
	queueSimParams.remove(queueSimParams[0])
	
def add_items_to_list():
	newList = []
#	for iaa in range(len(queueSimParamsList)):
#		newList[iaa] = queueSimParamsList[iaa]['simID']
#	for simID in newList:
	for simID in [queueSimParams[iaa]['simID'] for iaa in range(len(queueSimParams))]:
		sim_mgr_win.ui.notStartedListBox.insertItem(simID)
		#qIndex = sim_mgr_win.simListBox.findItem(simID + ' (Not Started)')
		#sim_mgr_win.simListBox.changeitem(simID + ' (Started)', qIndex)
		#lineObject = sim_mgr_win.simListBox.row(rowIndex)
		#lineObject.setTextColor(qColor.fromRgb(0,0,255,255))
		

def launch_sim(simpassword):
	global queueSimParamsList
	global queueSimParams
	global maxNumOfRunningSims
	global finished_pids
	print maxNumOfRunningSims
	queueSimParamsList = copy.deepcopy(setupSimParamsList)
	queueSimParams = copy.deepcopy(setupSimParams)
	currentlyRunning = []
	queueStatus = 'NotDone'
	add_items_to_list()
	#counter = 0
	while queueStatus is 'NotDone':
		check_pids(currentlyRunning)
		for pid in finished_pids:
			conclude_simulation(pid, currentlyRunning)
		if len(currentlyRunning) < maxNumOfRunningSims and len(queueSimParamsList) > 0:
			launch_additional_sim(currentlyRunning, simpassword)
		if (len(currentlyRunning) == 0) and (len(queueSimParamsList) == 0):
			print 'Sims have concluded.'
			queueStatus = 'Done'
		app.processEvents(0)
		#counter += 1
		#if counter == 150:
			#print 'queueStatus is: {}'.format(queueStatus)
			#print 'currentlyRunning: {}'.format(currentlyRunning)
			#print 'queue: {}'.format(len(queueSimParamsList))
			#print 'finished_pids: {}'.format(finished_pids)
			#counter = 0
		time.sleep(0.1)


class PlotNameWin (QtGui.QWidget):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.ui = Ui_plotNameForm()
		self.ui.setupUi(self)


	
	def saveSettingsBtn_pressed(self):
		saveSettingsBtn_pressed2(self)
		
	def restoreSettingsBtn_pressed(self):
		restoreSettingsBtn_pressed2(self)
		
	def pointsCBoxChangeAll_activated(self, pointsCBoxIndex):
		self.ui.pointsCBox1.setCurrentItem(pointsCBoxIndex)
		self.ui.pointsCBox2.setCurrentItem(pointsCBoxIndex)
		self.ui.pointsCBox3.setCurrentItem(pointsCBoxIndex)
		self.ui.pointsCBox4.setCurrentItem(pointsCBoxIndex)
		self.ui.pointsCBox5.setCurrentItem(pointsCBoxIndex)
		self.ui.pointsCBox6.setCurrentItem(pointsCBoxIndex)
		self.ui.pointsCBox7.setCurrentItem(pointsCBoxIndex)
		self.ui.pointsCBox8.setCurrentItem(pointsCBoxIndex)
		
	def pointSizeCBoxChangeAll_activated(self, pointSizeCBoxIndex):
		self.ui.pointSizeCBox1.setCurrentItem(pointSizeCBoxIndex)
		self.ui.pointSizeCBox2.setCurrentItem(pointSizeCBoxIndex)
		self.ui.pointSizeCBox3.setCurrentItem(pointSizeCBoxIndex)
		self.ui.pointSizeCBox4.setCurrentItem(pointSizeCBoxIndex)
		self.ui.pointSizeCBox5.setCurrentItem(pointSizeCBoxIndex)
		self.ui.pointSizeCBox6.setCurrentItem(pointSizeCBoxIndex)
		self.ui.pointSizeCBox7.setCurrentItem(pointSizeCBoxIndex)
		self.ui.pointSizeCBox8.setCurrentItem(pointSizeCBoxIndex)
		
	def lineWidthCBoxChangeAll_activated(self, lineWidthCBoxIndex):
		self.ui.lineWidthCBox1.setCurrentItem(lineWidthCBoxIndex)
		self.ui.lineWidthCBox2.setCurrentItem(lineWidthCBoxIndex)
		self.ui.lineWidthCBox3.setCurrentItem(lineWidthCBoxIndex)
		self.ui.lineWidthCBox4.setCurrentItem(lineWidthCBoxIndex)
		self.ui.lineWidthCBox5.setCurrentItem(lineWidthCBoxIndex)
		self.ui.lineWidthCBox6.setCurrentItem(lineWidthCBoxIndex)
		self.ui.lineWidthCBox7.setCurrentItem(lineWidthCBoxIndex)
		self.ui.lineWidthCBox8.setCurrentItem(lineWidthCBoxIndex)
		
	def lineColorCBoxChangeAll_activated(self, lineColorCBoxIndex):
		self.ui.lineColorCBox1.setCurrentItem(lineColorCBoxIndex)
		self.ui.lineColorCBox2.setCurrentItem(lineColorCBoxIndex)
		self.ui.lineColorCBox3.setCurrentItem(lineColorCBoxIndex)
		self.ui.lineColorCBox4.setCurrentItem(lineColorCBoxIndex)
		self.ui.lineColorCBox5.setCurrentItem(lineColorCBoxIndex)
		self.ui.lineColorCBox6.setCurrentItem(lineColorCBoxIndex)
		self.ui.lineColorCBox7.setCurrentItem(lineColorCBoxIndex)
		self.ui.lineColorCBox8.setCurrentItem(lineColorCBoxIndex)
	
	def SaveTimeButton_pressed(self):
		global fileList
		
		if len(fileList) > 0:
			pieces = fileList[0].split('_')
			newLegend1 = pieces[4] + ' ' + pieces[5]
			self.ui.file1Edit.setText(newLegend1)
	
		if len(fileList) > 1:
			pieces = fileList[1].split('_')
			newLegend2 = pieces[4] + ' ' + pieces[5]
			self.ui.file2Edit.setText(newLegend2)
		
		if len(fileList) > 2:
			pieces = fileList[2].split('_')
			newLegend3 = pieces[4] + ' ' + pieces[5]
			self.ui.file3Edit.setText(newLegend3)
		
		if len(fileList) > 3:
			pieces = fileList[3].split('_')
			newLegend4 = pieces[4] + ' ' + pieces[5]
			self.ui.file4Edit.setText(newLegend4)
		
		if len(fileList) > 4:
			pieces = fileList[4].split('_')
			newLegend5 = pieces[4] + ' ' + pieces[5]
			self.ui.file5Edit.setText(newLegend5)
		
		if len(fileList) > 5:
			pieces = fileList[5].split('_')
			newLegend6 = pieces[4] + ' ' + pieces[5]
			self.ui.file6Edit.setText(newLegend6)
		
		if len(fileList) > 6:
			pieces = fileList[6].split('_')
			newLegend7 = pieces[4] + ' ' + pieces[5]
			self.ui.file7Edit.setText(newLegend7)
		
		if len(fileList) > 7:
			pieces = fileList[7].split('_')
			newLegend8 = pieces[4] + ' ' + pieces[5]
			self.ui.file8Edit.setText(newLegend8)
		
	def LegendPosition_selected(self):
		if self.ui.legendCBox.currentText() == 'Customized Position':
			self.ui.x_axisPositionLbl.setEnabled(True)
			self.ui.y_axisPositionLbl.setEnabled(True)
			self.ui.x_axisEdit.setEnabled(True)
			self.ui.y_axisEdit.setEnabled(True)
		else:
			self.ui.x_axisPositionLbl.setEnabled(False)
			self.ui.y_axisPositionLbl.setEnabled(False)
			self.ui.x_axisEdit.setEnabled(False)
			self.ui.y_axisEdit.setEnabled(False)			
		
	def doneBtn_pressed(self):
		global fileList
		global plotType
		simID = sim_view_win.ui.simIDEdit.text()
		os.chdir(simID)
		# Set files to be plotted, in proper order
		newFileList = []
		newFileListText = []
		newPointTypeList = []
		newPointSizeList = []
		newLineWidthList = []
		newLineColorList = []
		for loopIdx in range(8):
			newFileList.append('temp')
			newFileListText.append('temp')
			newPointTypeList.append('temp')
			newPointSizeList.append('temp')
			newLineWidthList.append('temp')
			newLineColorList.append('temp')
			
		for loopIdx in range(len(fileList)):
			if loopIdx == 0:
				plotIdx = int(self.ui.plotOrder1.text())-1
				newFileList[plotIdx] = fileList[0]
				newFileListText[plotIdx] = self.ui.file1Edit.text()
				newPointTypeList[plotIdx] = self.ui.pointsCBox1.currentItem()
				newPointSizeList[plotIdx] = self.ui.pointSizeCBox1.currentText()
				newLineWidthList[plotIdx] = self.ui.lineWidthCBox1.currentText()
				newLineColorList[plotIdx] = self.ui.lineColorCBox1.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1
				
			elif loopIdx == 1:
				plotIdx = int(self.ui.plotOrder2.text())-1
				newFileList[plotIdx] = fileList[1]
				newFileListText[plotIdx] = self.ui.file2Edit.text()
				newPointTypeList[plotIdx] = self.ui.pointsCBox2.currentItem()
				newPointSizeList[plotIdx] = self.ui.pointSizeCBox2.currentText()
				newLineWidthList[plotIdx] = self.ui.lineWidthCBox2.currentText()
				newLineColorList[plotIdx] = self.ui.lineColorCBox2.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1								
			elif loopIdx == 2:
				plotIdx = int(self.ui.plotOrder3.text())-1
				newFileList[plotIdx] = fileList[2]
				newFileListText[plotIdx] = self.ui.file3Edit.text()
				newPointTypeList[plotIdx] = self.ui.pointsCBox3.currentItem()
				newPointSizeList[plotIdx] = self.ui.pointSizeCBox3.currentText()
				newLineWidthList[plotIdx] = self.ui.lineWidthCBox3.currentText()
				newLineColorList[plotIdx] = self.ui.lineColorCBox3.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1			
			elif loopIdx == 3:
				plotIdx = int(self.ui.plotOrder4.text())-1
				newFileList[plotIdx] = fileList[3]
				newFileListText[plotIdx] = self.ui.file4Edit.text()
				newPointTypeList[plotIdx] = self.ui.pointsCBox4.currentItem()
				newPointSizeList[plotIdx] = self.ui.pointSizeCBox4.currentText()
				newLineWidthList[plotIdx] = self.ui.lineWidthCBox4.currentText()
				newLineColorList[plotIdx] = self.ui.lineColorCBox4.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1			
			elif loopIdx == 4:
				plotIdx = int(self.ui.plotOrder5.text())-1
				newFileList[plotIdx] = fileList[4]
				newFileListText[plotIdx] = self.ui.file5Edit.text()
				newPointTypeList[plotIdx] = self.ui.pointsCBox5.currentItem()
				newPointSizeList[plotIdx] = self.ui.pointSizeCBox5.currentText()
				newLineWidthList[plotIdx] = self.ui.lineWidthCBox5.currentText()
				newLineColorList[plotIdx] = self.ui.lineColorCBox5.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1			
			elif loopIdx == 5:
				plotIdx = int(self.ui.plotOrder6.text())-1
				newFileList[plotIdx] = fileList[5]
				newFileListText[plotIdx] = self.ui.file6Edit.text()
				newPointTypeList[plotIdx] = self.ui.pointsCBox6.currentItem()
				newPointSizeList[plotIdx] = self.ui.pointSizeCBox6.currentText()
				newLineWidthList[plotIdx] = self.ui.lineWidthCBox6.currentText()
				newLineColorList[plotIdx] = self.ui.lineColorCBox6.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1
			elif loopIdx == 6:
				plotIdx = int(self.ui.plotOrder7.text())-1
				newFileList[plotIdx] = fileList[6]
				newFileListText[plotIdx] = self.ui.file7Edit.text()
				newPointTypeList[plotIdx] = self.ui.pointsCBox7.currentItem()
				newPointSizeList[plotIdx] = self.ui.pointSizeCBox7.currentText()
				newLineWidthList[plotIdx] = self.ui.lineWidthCBox7.currentText()
				newLineColorList[plotIdx] = self.ui.lineColorCBox7.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1
			elif loopIdx == 7:
				plotIdx = int(self.ui.plotOrder8.text())-1
				newFileList[plotIdx] = fileList[7]
				newFileListText[plotIdx] = self.ui.file8Edit.text()
				newPointTypeList[plotIdx] = self.ui.pointsCBox8.currentItem()
				newPointSizeList[plotIdx] = self.ui.pointSizeCBox8.currentText()
				newLineWidthList[plotIdx] = self.ui.lineWidthCBox8.currentText()
				newLineColorList[plotIdx] = self.ui.lineColorCBox8.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1
		#
		# Setup gnuplot script
		#
		if sim_view_win.ui.plotNameEdit.text() == '':
			sim_view_win.ui.plotNameEdit.setText('selected_plot')
		gplot_file = open(sim_view_win.ui.plotNameEdit.text()+'.gp','w')
		if sim_view_win.ui.histBtn.isChecked() == 1 or sim_view_win.ui.timeHistBtn.isChecked() == 1 or sim_view_win.ui.byteHistBtn.isChecked() == 1:
			gplot_file.write('set style data hist\n')
			gplot_file.write('set key right top Right\n')
		else:
			if self.ui.legendCBox.currentText() == 'Customized Position':		
					gplot_file.write('set key ' + self.ui.x_axisEdit.text() + ',' + self.ui.y_axisEdit.text() + '\n')
			elif self.legendCBox.currentText() == 'Remove Legend':
					gplot_file.write('unset key\n')
			else:
				gplot_file.write('set key left top Left\n')
				
			if sim_view_win.ui.confIntvlChkBox.isChecked() == 1:
				gplot_file.write('set style data yerrorlines\n')
			else:
				for loopIdx in range(len(fileList)):
					pointtype = newPointTypeList[loopIdx]
					pointsize = newPointSizeList[loopIdx]
					linewidth = newLineWidthList[loopIdx]
					linecolor = newLineColorList[loopIdx]
					
					gplot_file.write('set style line ' + str(loopIdx+1) + ' pt ' + str(pointtype) + ' ps ' + str(pointsize) + ' lw ' + str(linewidth) + ' lc ' + str(linecolor) + ' \n')
				
		if sim_view_win.ui.delayVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'delay (in seconds)\'\n') #{/Symbol m}
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
#   		gplot_file.write('set xtics 0.0,0.2\n')
			gplot_file.write('set format y \"%.1se%S\"\n')
		if sim_view_win.ui.jitterVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'jitter (in seconds squared)\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
#   		gplot_file.write('set xtics 0.0,0.2\n')
			gplot_file.write('set format y \"%.1se%S\"\n') #%csec^2
		if sim_view_win.ui.delayVsTimeBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'delay (in seconds)\'\n')
			gplot_file.write('set xlabel \'simulation time (in 1 second intervals)\'\n')
#   		gplot_file.write('set xtics 0.0,1\n')
			gplot_file.write('set format y \"%.1s %csec\"\n')
		if sim_view_win.ui.ui.delayVsONUBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'delay (in seconds)\'\n')
			gplot_file.write('set xlabel \'# of ONUs\'\n')
			gplot_file.write('set format y \"%.1s %csec\"\n')
		if sim_view_win.ui.utilVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'utilization\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
		if sim_view_win.ui.cyclelenVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'cycle length (in seconds)\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
			gplot_file.write('set format y \"%.1se%S\"\n')
		if sim_view_win.ui.cyclelenVsONUBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'cycle length (in seconds)\'\n')
			gplot_file.write('set xlabel \'# of ONUs\'\n')
			gplot_file.write('set format y \"%.1s %csec\"\n')
		if sim_view_win.ui.grantsizeVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Grant Size (in bytes)\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
			gplot_file.write('set format y \"%.1f\"\n')
		if sim_view_win.ui.reportsizeVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Report Size (in bytes)\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
			gplot_file.write('set format y \"%.1f\"\n')
		if sim_view_win.ui.grantsizePVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Grant Size (in packets)\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
		if sim_view_win.ui.granttimeVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Grant Time (in seconds)\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
			gplot_file.write('set format y \"%.1s %csec\"\n')
		if sim_view_win.ui.histBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Probability\'\n')
		if sim_view_win.ui.timeHistBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Probability\'\n')
			gplot_file.write('set xlabel \'(in seconds)\'\n')
			gplot_file.write('set format x \"%.1s%cs\"\n')
		if sim_view_win.ui.byteHistBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Probability\'\n')
			gplot_file.write('set xlabel \'(in bytes)\'\n')
			gplot_file.write('set format x \"%.1s%cB\"\n')
		if ((sim_view_win.ui.maxYEdit.text() != '') and (sim_view_win.ui.minYEdit.text() != '')):
			gplot_file.write('set yrange ['+sim_view_win.ui.minYEdit.text()+':'+sim_view_win.ui.maxYEdit.text()+']\n')
		if ((sim_view_win.ui.maxYEdit.text() != '') and (sim_view_win.ui.minYEdit.text() == '')):
			gplot_file.write('set yrange [:'+sim_view_win.ui.maxYEdit.text()+']\n')
		if ((sim_view_win.ui.maxYEdit.text() == '') and (sim_view_win.ui.minYEdit.text() != '')):
			gplot_file.write('set yrange ['+sim_view_win.ui.minYEdit.text()+':]\n')
		if ((sim_view_win.ui.maxXEdit.text() != '') and (sim_view_win.ui.minXEdit.text() != '')):
			gplot_file.write('set xrange ['+sim_view_win.ui.minXEdit.text()+':'+sim_view_win.ui.maxXEdit.text()+']\n')
		if ((sim_view_win.ui.maxXEdit.text() != '') and (sim_view_win.ui.minXEdit.text() == '')):
			gplot_file.write('set xrange [:'+sim_view_win.ui.maxXEdit.text()+']\n')
		if ((sim_view_win.ui.maxXEdit.text() == '') and (sim_view_win.ui.minXEdit.text() != '')):
			gplot_file.write('set xrange ['+sim_view_win.ui.minXEdit.text()+':]\n')
		gplot_file.write('set grid\n')
		if plotType == 0:
			gplot_file.write('set terminal x11 font \"times,14\" enhanced \n')
		else:
			gplot_file.write('set terminal fig fontsize 12 \n')
			gplot_file.write('set output "'+sim_view_win.ui.plotNameEdit.text()+'.fig"\n')
		plotStr = 'plot '
		count = 1
		
		if sim_view_win.ui.confIntvlChkBox.isChecked() == 1:
			for loopIdx in range(len(fileList)):
				if loopIdx > 0:
					plotStr = plotStr + ','
				plotStr = plotStr + '"' + newFileList[loopIdx] + '"'
				plotStr = plotStr + ' title \'' + newFileListText[loopIdx] + '\''
		else:
			for loopIdx in range(len(fileList)):
				if loopIdx > 0:
					plotStr = plotStr + ','
				plotStr = plotStr + '"' + newFileList[loopIdx] + '"'
				plotStr = plotStr + ' title \'' + newFileListText[loopIdx] + '\'' + ' with linespoints linestyle ' + str(loopIdx+1)
			
		plotStr = plotStr + '\n'
		gplot_file.write(plotStr)
		#
		# Setup plot refresh loop file
		
		if sim_view_win.ui.plotRefreshChkBox.isChecked() == 1:
			gplot_file.write('load "loop.gp"')
			loop_file = open('loop.gp','w')
			loop_file.write('pause 15\n')
			loop_file.write('replot\n')
			loop_file.write('reread\n')
			loop_file.close()
		gplot_file.close()
		if plotType == 0:
			os.system('gnuplot -persist '+sim_view_win.ui.plotNameEdit.text()+'.gp')
		else:
			os.system('gnuplot '+sim_view_win.ui.plotNameEdit.text()+'.gp')
			os.system('fig2dev -L pdf '+sim_view_win.ui.plotNameEdit.text()+'.fig '+sim_view_win.ui.plotNameEdit.text()+'.pdf')
			os.system('fig2dev -L eps '+sim_view_win.ui.plotNameEdit.text()+'.fig '+sim_view_win.ui.plotNameEdit.text()+'.eps')
			tex_file = open(sim_view_win.ui.plotNameEdit.text()+'.tex','w')
			tex_file.write('\\begin{figure}[tb]\n')
			tex_file.write('\\includegraphics[scale=0.75,angle=270]{'+sim_view_win.ui.plotNameEdit.text()+'.pdf}\n')
			tex_file.write('\\caption{'+sim_view_win.ui.plotCaptionEdit.text()+'}\n')
			tex_file.write('\\label{fig:'+sim_view_win.ui.plotNameEdit.text()+'}\n')
			tex_file.write('\\end{figure}\n')
			tex_file.close()
		
		cwdDir = os.getcwd()
		resultsDir = cwdDir + '/A_Results'
		pdfDir = resultsDir + '/pdf_files'
		if not os.path.isdir(resultsDir):
			os.mkdir('A_Results')
		if not os.path.isdir(pdfDir):
			os.mkdir('A_Results/pdf_files')
		os.rename(cwdDir + '/' + sim_view_win.ui.plotNameEdit.text() + '.gp', resultsDir + '/' + sim_view_win.ui.plotNameEdit.text() + '.gp')
		os.rename(cwdDir + '/' + sim_view_win.ui.plotNameEdit.text() + '.fig', resultsDir + '/' + sim_view_win.ui.plotNameEdit.text() + '.fig')
		os.rename(cwdDir + '/' + sim_view_win.ui.plotNameEdit.text() + '.pdf', resultsDir + '/' + sim_view_win.ui.plotNameEdit.text() + '.pdf')
		os.rename(cwdDir + '/' + sim_view_win.ui.plotNameEdit.text() + '.eps', resultsDir + '/' + sim_view_win.ui.plotNameEdit.text() + '.eps')
		os.rename(cwdDir + '/' + sim_view_win.ui.plotNameEdit.text() + '.tex', resultsDir + '/' + sim_view_win.ui.plotNameEdit.text() + '.tex')

		shutil.copy2(resultsDir + '/' + sim_view_win.ui.plotNameEdit.text() + '.pdf', pdfDir + '/' + sim_view_win.ui.plotNameEdit.text() + '.pdf')
		
		os.chdir('..')
		self.hide()

class WaitWin (QtGui.QWidget):	
	def __init__(self):
		super(self.__class__, self).__init__()
		self.ui = Ui_WaitForm()
		self.ui.setupUi(self)

class SimViewWin (QtGui.QWidget):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.ui = Ui_SimViewForm()
		self.ui.setupUi(self)
	
	def pushButtonAutoName_pressed(self):
		global fileList
		del fileList
		fileList = []
		generate_file_list(fileList, self.simOutputListBox)
		if fileList[0] != '':
			plot_name_win.file1Lbl.setText(fileList[0])
		if len(fileList) > 1:
			if fileList[1] != '':
				plot_name_win.file2Lbl.setText(fileList[1])
		if len(fileList) > 2:
			if fileList[2] != '':
				plot_name_win.file3Lbl.setText(fileList[2])
		if len(fileList) > 3:
			if fileList[3] != '':
				plot_name_win.file4Lbl.setText(fileList[3])
		if len(fileList) > 4:
			if fileList[4] != '':
				plot_name_win.file5Lbl.setText(fileList[4])
		if len(fileList) > 5:
			if fileList[5] != '':
				plot_name_win.file6Lbl.setText(fileList[5])
		if len(fileList) > 6:
			if fileList[6] != '':
				plot_name_win.file7Lbl.setText(fileList[6])
		if len(fileList) > 7:
			if fileList[7] != '':
				plot_name_win.file8Lbl.setText(fileList[7])
		pieces = fileList[0].split('_')
		piecesLast = fileList[len(fileList)-1].split('_')
		if 'od' == pieces[0]:
			self.delayVsLoadBtn.setChecked(True)
		elif 'vod' == pieces[0]:
			self.delayVsLoadBtn.setChecked(True)
		elif 'vods' == pieces[0]:
			self.jitterVsLoadBtn.setChecked(True)
#		if 'Q20' in pieces[4]:
#			newLegend = pieces[0]+'_'+pieces[3]+'_Q20-Q30'
#		elif 'Q35' in pieces[4]:
#			newLegend = pieces[0]+'_'+pieces[3]+'_Q35-Q45'
#		else:
#			newLegend = pieces[0]+'_'+pieces[3]
		newLegend = pieces[0]+'_'+pieces[3]+'_'+pieces[4]+'-'+piecesLast[4]
		self.plotNameEdit.setText(newLegend)
		
	
	def exitBtn_pressed(self):
		self.exitBtn.setDown(0)
		sim_view_win.hide()
		sim_mgr_win.show()
	def viewOutputBtn_pressed(self):
		plot_name_win.show()
		self.viewOutputBtn.setDown(0)
		global fileList
		global plotType
		del fileList
		fileList = []
		generate_file_list(fileList,self.simOutputListBox)
		if fileList[0] != '':
			plot_name_win.file1Lbl.setText(fileList[0])
		if len(fileList) > 1:
			if fileList[1] != '':
				plot_name_win.file2Lbl.setText(fileList[1])
		if len(fileList) > 2:
			if fileList[2] != '':
				plot_name_win.file3Lbl.setText(fileList[2])
		if len(fileList) > 3:
			if fileList[3] != '':
				plot_name_win.file4Lbl.setText(fileList[3])
		if len(fileList) > 4:
			if fileList[4] != '':
				plot_name_win.file5Lbl.setText(fileList[4])
		if len(fileList) > 5:
			if fileList[5] != '':
				plot_name_win.file6Lbl.setText(fileList[5])
		if len(fileList) > 6:
			if fileList[6] != '':
				plot_name_win.file7Lbl.setText(fileList[6])
		if len(fileList) > 7:
			if fileList[7] != '':
				plot_name_win.file8Lbl.setText(fileList[7])
		plotType = 0
		# restoreSettingsBtn_pressed2(plot_name_win)
	def exportOutputBtn_pressed(self):
		plot_name_win.show()
		self.exportOutputBtn.setDown(0)
		global fileList
		global plotType
		del fileList
		fileList = []
		generate_file_list(fileList,self.simOutputListBox)
		if fileList[0] != '':
			plot_name_win.file1Lbl.setText(fileList[0])
		if len(fileList) > 1:
			if fileList[1] != '':
				plot_name_win.file2Lbl.setText(fileList[1])
		if len(fileList) > 2:
			if fileList[2] != '':
				plot_name_win.file3Lbl.setText(fileList[2])
		if len(fileList) > 3:
			if fileList[3] != '':
				plot_name_win.file4Lbl.setText(fileList[3])
		if len(fileList) > 4:
			if fileList[4] != '':
				plot_name_win.file5Lbl.setText(fileList[4])
		if len(fileList) > 5:
			if fileList[5] != '':
				plot_name_win.file6Lbl.setText(fileList[5])
		if len(fileList) > 6:
			if fileList[6] != '':
				plot_name_win.file7Lbl.setText(fileList[6])
		if len(fileList) > 7:
			if fileList[7] != '':
				plot_name_win.file8Lbl.setText(fileList[7])
		plotType = 1
		# restoreSettingsBtn_pressed2(plot_name_win)

	def stopSimBtn_pressed(self):
		sim_ctrl_file = open('sim_ctrl','w')
		sim_ctrl_file.write('stop')
		sim_ctrl_file.close()
		
	#Redefining the close even to give a message box to confirm	
	def closeEvent(self, event):
		self.exitBtn.setDown(0)
		sim_view_win.hide()
		sim_mgr_win.show()


class SimInitWin (QtGui.QWidget):
	#def __init__(self, parent = None, name = "Simulation Init Form", modal = 0, fl = 0):
		#Ui_SimInitForm.__init__(self)
	def __init__(self):
		super(self.__class__, self).__init__()
		self.ui = Ui_SimInitForm()
		self.ui.setupUi(self)
		
		global simhostname
		restore_parameters(self)
		
	def cancelBtn_pressed(self):
		store_parameters(self)
		self.ui.cancelBtn.setDown(0)
		sim_init_win.hide()
		sim_mgr_win.show()
		
	def launchBtn_pressed(self):
		self.ui.launchBtn.setDown(0)
		global simhostname
		store_parameters(self)
		simpassword = self.ui.passwordEdit.text()
		sim_init_win.hide()
		sim_mgr_win.show()
		launch_sim(simpassword)
		
	def indexIncreaseButton_pressed(self):
		global queueIndexMax
		global queueIndex
		if queueIndex < queueIndexMax:
			store_parameters(self)
			queueIndex += 1
			restore_parameters(self)
	
	def indexDecreaseButton_pressed(self):
		global queueIndexMax
		global queueIndex
		if queueIndex > 0:
			store_parameters(self)
			queueIndex -= 1
			restore_parameters(self)
	
	def indexMaxIncreaseButton_pressed(self):
		global queueIndexMax
		global queueIndex
		global testNum
		if queueIndexMax < 100:
			store_parameters(self)
			restore_parameters(self)
			add_simParams()
			add_simParamsList()
			if queueIndex == queueIndexMax:
				queueIndexMax += 1
				self.indexIncreaseButton_pressed()
				# Increment the Sim ID test number
				testNum += 1
				self.ui.simIdEdit.setText('test_' + "%04d" % (testNum,))
			else:
				queueIndexMax += 1
	
	def indexMaxDecreaseButton_pressed(self):
		global queueIndexMax
		global queueIndex
		if queueIndexMax > 0:
			if queueIndex == queueIndexMax:
				self.indexDecreaseButton_pressed()
			setupSimParams.pop()
			setupSimParamsList.pop()
			queueIndexMax -= 1
			restore_parameters(self)
	
	def loginBtn_pressed(self):
		self.ui.loginBtn.setDown(0)
		simusername = self.ui.usernameEdit.text()
		simpassword = self.ui.passwordEdit.text()
		if False:
		#if os.path.isdir(os.path.join('/home', str(simusername))) == False:
			print 'Not a Valid Username, please Try again.' 
			self.ui.usernameEdit.clear()
			self.ui.passwordEdit.clear()
		else:
			ExecutePath = dir_projectRoot
			os.chdir(ExecutePath)
			#simcommandfinal = os.path.join(ExecutePath, 'ls')
			simcommandfinal = 'ls'

			cmd = 'ssh -f -l ' + str(simusername) + ' ' + str(simhostname) + ' \'cd ' + ExecutePath + '; ' + simcommandfinal + ' > sim_log &\''
			child = pexpect.spawn(cmd)

			# expect ssh to prompt for a user password
			child.expect('Password:')
			print str(simusername) + '@' + str(simhostname) + '\'s' + ' password:'
			# send the password
			child.sendline(str(simpassword))
			child.read()
			if child.isalive() == False:
				self.ui.passwordEdit.setEnabled(False)
				self.ui.logoutBtn.setEnabled(True)
				self.ui.loginBtn.setEnabled(False)
				print 'Logged In Successfully'
				self.ui.launchBtn.setEnabled(True)
			else:
				print 'Logged In Failed'
				self.ui.usernameEdit.clear()
				self.ui.passwordEdit.clear()
				
	def logoutBtn_pressed(self):
		self.ui.logoutBtn.setDown(0)
		simpassword = ''
		self.ui.passwordEdit.clear()
		self.ui.passwordEdit.setEnabled(True)
		self.ui.loginBtn.setEnabled(True)
		self.ui.logoutBtn.setEnabled(False)
		self.ui.launchBtn.setEnabled(False)
		
	def svOnBtn_checked(self):
		#self.ui.svButtonGroup.setEnabled(True)
		self.ui.svDropNone.setEnabled(True)
		self.ui.svDropThreshold.setEnabled(True)
		self.ui.svDropDynamic.setEnabled(True)
		self.ui.svDropStepThreshold.setEnabled(True)
		self.ui.svDropThresholdEdit.setEnabled(True)
		self.ui.svDropSensitivity.setEnabled(True)
		self.ui.svDropStepMinBound.setEnabled(True)
		self.ui.svDropStepMaxBound.setEnabled(True)
		self.ui.svDropStep_NumMAValues.setEnabled(True)
		self.ui.svDropMinBoundLabel.setEnabled(True)
		self.ui.svDropMaxBoundLabel.setEnabled(True)
		
		
	def svOffBtn_checked(self):
		#self.ui.svButtonGroup.setEnabled(False)
		self.ui.svDropNone.setEnabled(False)
		self.ui.svDropThreshold.setEnabled(False)
		self.ui.svDropDynamic.setEnabled(False)
		self.ui.svDropStepThreshold.setEnabled(False)
		self.ui.svDropThresholdEdit.setEnabled(False)
		self.ui.svDropSensitivity.setEnabled(False)
		self.ui.svDropStepMinBound.setEnabled(False)
		self.ui.svDropStepMaxBound.setEnabled(False)
		self.ui.svDropStep_NumMAValues.setEnabled(False)
		self.ui.svDropMinBoundLabel.setEnabled(False)
		self.ui.svDropMaxBoundLabel.setEnabled(False)

		
	def vtOnBtn_checked(self):
		global filename
		self.ui.videoTraceEdit.setEnabled(True)
		self.ui.changeTraceBtn.setEnabled(True)
		
		#self.ui.VideoDBABtnGroup.setEnabled(True)
		self.ui.dbaGatedVideoBtn.setEnabled(True)
		self.ui.dbaFixedVideoBtn.setEnabled(True)
		self.ui.dbaLimitedVideoBtn.setEnabled(True)
		
		#self.ui.predictTrafficBox.setEnabled(True)
		self.ui.pvtOffBtn.setEnabled(True)
		self.ui.pvtOnBtn.setEnabled(True)
		
		self.ui.FRateLbl.setEnabled(True)
		self.ui.frameRateEdit.setEnabled(True)
		#self.ui.videoStartBox.setEnabled(True)		#I don't plan on replacing this line
		self.ui.ipactpsfBtn.setEnabled(True)
		
		#self.ui.scalableVideoBox.setEnabled(True)
		self.ui.svOffBtn.setEnabled(True)
		self.ui.svOnBtn.setEnabled(True)
				
		
		sim_init_win.hide()
		filename = "()"
		while str(filename) == "()":
			filename = tkFileDialog.askopenfilename(title = "Select a Video Trace File to be Used", initialdir = dir_epon_sims)
		if str(filename) != "()":
			self.ui.videoTraceEdit.setText(filename)
		sim_init_win.show()
		
		self.ui.vtOnBtn.setChecked(1)		#For whatever reason, it doesn't seem to do this by default.
		
	def vtOffBtn_checked(self):
		self.ui.videoTraceEdit.clear()
		self.ui.videoTraceEdit.setEnabled(False)
		self.ui.changeTraceBtn.setEnabled(False)
		
		#self.ui.VideoDBABtnGroup.setEnabled(False)
		self.ui.dbaGatedVideoBtn.setEnabled(False)
		self.ui.dbaFixedVideoBtn.setEnabled(False)
		self.ui.dbaLimitedVideoBtn.setEnabled(False)
		
		#self.ui.predictTrafficBox.setEnabled(False)
		self.ui.pvtOffBtn.setEnabled(False)
		self.ui.pvtOnBtn.setEnabled(False)
		self.ui.PredTypeEdit.setEnabled(False)
		
		self.ui.FRateLbl.setEnabled(False)
		self.ui.frameRateEdit.setEnabled(False)
		#self.ui.videoStartBox.setEnabled(False)
		if self.ui.ipactpsfBtn.isChecked() == 1:
			self.ui.nascBtn.setChecked(1)
		self.ui.ipactpsfBtn.setEnabled(False)
		
		#self.ui.scalableVideoBox.setEnabled(False)
		self.ui.svOffBtn.setEnabled(False)
		self.ui.svOnBtn.setEnabled(False)
		
		self.ui.svDropThresholdEdit.setEnabled(False)
		self.ui.svDropSensitivity.setEnabled(False)
		self.ui.svDropStepMinBound.setEnabled(False)
		self.ui.svDropStepMaxBound.setEnabled(False)
		self.ui.svDropStep_NumMAValues.setEnabled(False)
		self.ui.svDropMinBoundLabel.setEnabled(False)
		self.ui.svDropMaxBoundLabel.setEnabled(False)
	
		
	def pvtOnBtn_checked(self):
		self.ui.PredTypeLbl.setEnabled(True)
		self.ui.PredTypeEdit.setEnabled(True)
	
	def pvtOffBtn_checked(self):
		self.ui.PredTypeLbl.setEnabled(False)
		self.ui.PredTypeEdit.setEnabled(False)
		
	def vsOffBtn_checked(self):
		self.ui.timeShiftLbl.setEnabled(False)
		self.ui.timeShiftEdit.setEnabled(False)
		
	def vsOnBtn_checked(self):
		self.ui.timeShiftLbl.setEnabled(True)
		self.ui.timeShiftEdit.setEnabled(True)
		
	def changeTraceBtn_pressed(self):
		sim_init_win.hide()
		newfilename = "()"
		newfilename = tkFileDialog.askopenfilename()
		if str(newfilename) == "()":
			newfilename = filename
		self.ui.videoTraceEdit.setText(newfilename)
		sim_init_win.show()
		
	#Redefining the close even to give a message box to confirm	
	def closeEvent(self, event):
		self.ui.cancelBtn.setDown(0)
		sim_init_win.hide()
		sim_mgr_win.show()		

	

class MainSimMgrWin (QtGui.QWidget):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.ui = Ui_SimMgr()
		self.ui.setupUi(self)
		self.ui.simListBox.setSelectionMode(3)

	def languageChange(self):
		Ui_SimMgr.ui.languageChange(self)
		self.ui.simListBox.clear()
		self.ui.notStartedListBox.clear()
		self.ui.startedListBox.clear()
		
	def quitButton_pressed(self):
		os.chdir(dir_epon_sims)
		simpicklefile = open('sim_mgr_data','w')
		pickler = pickle.Pickler(simpicklefile)
		pickler.dump(sims)
		simpicklefile.close()
		
		plotSettingsPicklefile = open('plot_settings_data','w')
		pickler = pickle.Pickler(plotSettingsPicklefile)
		pickler.dump(plotSettings)
		plotSettingsPicklefile.close()
		
		global testNum
		testNum += 1
		testNumPickleFile = open('test_num','w')
		pickler = pickle.Pickler(testNumPickleFile)
		pickler.dump(testNum)
		testNumPickleFile.close()
		
		sys.exit()
		
	def newSimButton_pressed(self):
		self.ui.newSimButton.setDown(0)
		global simhostname
		global testNum
		sim_mgr_win.hide()
		restore_parameters(sim_init_win);
		sim_init_win.ui.usernameEdit.setText('admin1')
		sim_init_win.ui.usernameEdit.setEnabled(False)
		sim_init_win.ui.simIdEdit.setText('test_' + "%04d" % (testNum, ))
		sim_init_win.show()
		
	def viewSimButton_pressed(self):
		# wait_win.ui.waitProgressBar.setPercentageVisible(1)
		wait_win.ui.waitProgressBar.setMaximum(5)
		wait_win.ui.waitProgressBar.setValue(0)
		wait_win.show()
		self.hide()
		self.ui.viewSimButton.setDown(0)
		Selection = False
		for loopIdx in range(self.ui.simListBox.count()):
			if self.ui.simListBox.isSelected(loopIdx) == 1:
				simIdx = loopIdx
				Selection = True
		if Selection:
			simID = self.ui.simListBox.item(simIdx).text()
			# Clear list box
			sim_view_win.ui.simOutputListBox.clear()
		
			os.chdir(dir_epon_sims)
			if os.path.exists(simID) == 1:
				os.chdir(simID)
			wait_win.waitProgressBar.setProgress(1)
			# Check process ID file
			if os.path.exists('pid') == 1:
				pidFile = open('pid','r')
				pidStr = pidFile.readline()
				if pidStr == 'done\n':
					sim_view_win.ui.simStatusLbl.setText('Completed')
				else:
					if pidStr == 'Failed\n':
						sim_view_win.ui.simStatusLbl.setText('Failed')
					else:
						sim_view_win.ui.simStatusLbl.setText('Running: ' + pidStr)
			simData = sims[simID]
			sim_view_win.ui.simIDEdit.setText(simID)
			sim_view_win.ui.hostEdit.setText(simData['host'])
			wait_win.ui.waitProgressBar.setProgress(3)
			# Fill list box with output files
			#
			filedir = os.popen('ls','r')
			filename = filedir.readline()
			while filename:
				filename = string.rstrip(filename)
				if ((filename != 'pid') and (filename != 'sim_cfg') and (filename != 'sim_log') 
				and (filename != 'sim_core')
				and (string.find(filename,'.fig') == -1) 
				and (string.find(filename,'.gp') == -1)):
					sim_view_win.ui.simOutputListBox.insertItem(filename)
				filename = filedir.readline()
			os.chdir('..')
			wait_win.ui.waitProgressBar.setValue(5)
			wait_win.hide()
			sim_view_win.show()
		else:
			wait_win.ui.waitProgressBar.setValue(5)
			wait_win.hide()
			sim_mgr_win.show()
			print "No valid Selection for a Simulation ID to be viewed, Please Try again."
			
	def consolidateBtn_pressed(self):
		wait_win.show()
		self.ui.consolidateBtn.setDown(0)
		global simParams
		simList = self.ui.simListBox.selectedItems()
		#for loopIdx in range(self.ui.simListBox.count()):
			#if self.ui.simListBox.isSelected(loopIdx) == 1:
				## Add simulation to list
				#simList.append(self.simListBox.item(loopIdx).text())
		
		#for entry in self.ui.simListBox.selectedItems()
			## Add simulation to list
			#simList.append(self.ui.simListBox.item(loopIdx).text())
		
		# Create a consolidated pseudo-simulation
		if str(self.ui.consolidateNameEdit.text()) == '':
			self.ui.consolidateNameEdit.setText('consolidated')
		consolidatedNameQSTRING = self.ui.consolidateNameEdit.text()
		consolidatedName = str(consolidatedNameQSTRING)
		if sims.has_key(consolidatedName) == 1:
			del sims[consolidatedName]
		simData['host'] = 'null'
		simData['pid'] = 0
		simData['params'] = copy.deepcopy(simParams)
		simID = consolidatedName
		sims[simID] = copy.deepcopy(simData)
		if os.path.exists(consolidatedName) == 1:
			os.system('rm -rf ' + consolidatedName)
		os.mkdir(consolidatedName)
		# copy files to consolidated directory
		for item in simList:
			# dirStr = simList[loopIdx]
			os.system('cp ' + str(dirStr) + '/* ' + consolidatedName)
		self.ui.simListBox.addItem(consolidatedNameQSTRING)
		wait_win.hide()
	
	def addSimButton_pressed(self):
		wait_win.show()
		self.ui.addSimButton.setDown(0)
		global simParams
		simList = []
		os.chdir(dir_epon_sims)

		# Add the simulation directory
		if str(self.ui.consolidateNameEdit.text()) == '':
			self.ui.consolidateNameEdit.setText('new_sim')
		addSimName = str(self.ui.consolidateNameEdit.text())
		
		if os.path.exists(addSimName) == 0:
			os.mkdir(addSimName)
		
		if sims.has_key(addSimName) == 1:
			del sims[addSimName]
		simData['host'] = 'null'
		simData['pid'] = 0
		simData['params'] = copy.deepcopy(simParams)
		simID = addSimName
		sims[simID] = copy.deepcopy(simData)
		self.ui.simListBox.addItem(addSimName)
		wait_win.hide()
	
	def removeSimButton_pressed(self):
		wait_win.show() 
		#app.processEvents(0)
		self.ui.removeSimButton.setDown(0)
		#os.chdir('epon_sims')
		for itemSelected in self.ui.simListBox.selectedItems():
			# Remove selected simulation
			selectedSimID = str(itemSelected.text())
			print sims.keys()
			#self.ui.simListBox.removeItemWidget(itemSelected)
			self.ui.simListBox.takeItem(self.ui.simListBox.row(itemSelected))
			os.chdir(dir_epon_sims)
			if self.ui.removeDirCheckBox.isChecked() == 1:
				if os.path.exists(selectedSimID) == 1:
					os.chdir(selectedSimID)
					
					if os.path.exists('pid') == 1:
						pidFile = open('pid','r')
						pidStr = pidFile.readline()
						pidFile.close()
						
						if pidStr == 'done\n':
							shutil.rmtree(os.getcwd())
							print selectedSimID + ' was Deleted'
						elif pidStr == 'Failed\n':
							shutil.rmtree(os.getcwd())
							print selectedSimID + ' was Deleted'
						else:
							try:
								os.kill(int(pidStr), signal.SIG_IGN)
							except:
								pass
							shutil.rmtree(os.getcwd())
							print selectedSimID + ' was Stopped and Deleted'
							#simData = sims[selectedSimID]
							#cmd = 'ssh ' + simData['host'] + ' kill ' + str(int(pidStr)) + ' &\''
							#child = pexpect.spawn(cmd)
							## expect ssh to prompt for a user password
							#child.expect('Password:')
							#print str(simusername)+'@'+str(simData['host'])+'\'s' + ' password:'
							## send the password
							#child.sendline(sim_init_win.passwordEdit.text().ascii())
							#child.read()
							#child.kill(0)
							#shutil.rmtree(os.getcwd())
							#print selectedSimID + ' was Stopped and Deleted'
					else:
						os.system('rm -rf ' + selectedSimID)
			
			listofRowsToRemove = []
			# Please note that it doesn't include -1
			for iaa in range(self.ui.simListBox.count() - 1, -1, -1):
				if str(self.ui.simListBox.item(iaa).text()) == selectedSimID:
					#listofRowsToRemove.append(iaa)
					self.ui.simListBox.takeItem(iaa)
					
			#for iaa in listofRowsToRemove.reverse():
				#self.ui.simListBox.takeItem(iaa)
			del sims[selectedSimID]
		self.ui.removeDirCheckBox.setChecked(0)
		time.sleep(0.05)
		wait_win.hide()
	
	def haltSimBtn_pressed(self):
		#self.haltSimBtn.setDown(0)
		os.chdir('epon_sims')
		for loopIdx in range(self.startedListBox.count()):
			if self.ui.startedListBox.isSelected(loopIdx) == 1:
				# Halt selected simulation
				selectedSimID = self.ui.startedListBox.item(loopIdx).text()
				os.chdir(dir_epon_sims)
				if os.path.exists(selectedSimID) == 1:
					os.chdir(selectedSimID)
					
					if os.path.exists('pid') == 1:
						pidFile = open('pid','r')
						pidStr = pidFile.readline()
						pidFile.close()
						
						if (not (pidStr == 'done\n')) and (not (pidStr == 'Failed\n')):
							try:
								os.kill(int(pidStr), signal.SIG_IGN)
							except:
								pass
							pidFile = open('pid', 'w')
							pidFile.write('Failed\n')
							pidFile.close()
							print selectedSimID + ' was Stopped'
	
	def openSimButton_pressed(self):
		listSelected = self.ui.simListBox.findItems()
		os.chdir('epon_sims')
		for listItem in listSelected:
		#for loopIdx in range(self.ui.simListBox.count())[::-1]:
			#if self.ui.simListBox.isSelected(loopIdx) == 1:
			selectedSimID = str(listItem)
			os.chdir(dir_epon_sims)
			if os.path.exists(selectedSimID) == 1:
				os.chdir(selectedSimID)
				os.system('xdg-open ' + os.getcwd())
				
	def simListBox_doubleClicked(self, selectedItem):
		selectedSimID = str(selectedItem.text())
		print selectedSimID




# app = QApplication(sys.argv)
app = QtGui.QApplication(sys.argv)

sim_mgr_win = MainSimMgrWin()
sim_init_win = SimInitWin()
sim_view_win = SimViewWin()
wait_win = WaitWin()
plot_name_win = PlotNameWin()

sim_mgr_win.show()
load_sim_data()
load_plot_settings()
sim_mgr_win.show()
load_test_num()
sys.exit(app.exec_())
