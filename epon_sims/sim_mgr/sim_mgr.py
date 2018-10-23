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

# Modify the dirRoot variable as necessary

dirRoot = '/home/admin1/scvid'
dirLauncher = os.path.join(dirRoot, 'eponsim/eponsim')

st = os.stat(dirLauncher)
os.chmod(dirLauncher, st.st_mode | stat.S_IEXEC | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
# print st.st_mode

path, empty = os.path.split(os.getcwd())
path_2, directory = os.path.split(path)
home, Username = os.path.split(path_2)

simusername = str(Username)
simpassword = ''
simhomedir = str(path)
simhomedir_2 = str(directory)
simcommand = 'eponsim/eponsim'
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
	if self.svOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['SCALABLE_VIDEO_TRAFFIC'] = 'SCALABLE_VIDEO_OFF'
	if self.svOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['SCALABLE_VIDEO_TRAFFIC'] = 'SCALABLE_VIDEO_ON'
	if self.svDropNone.isChecked() == 1:
		setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] = 'SCALABLE_VIDEO_DROPPING_OFF'
	if self.svDropThreshold.isChecked() == 1:
		setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] = 'SCALABLE_VIDEO_DROPPING_THRESHOLD'
	if self.svDropDynamic.isChecked() == 1:
		setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] = 'SCALABLE_VIDEO_DROPPING_DYNAMIC'
	if self.svDropStepThreshold.isChecked() == 1:
		setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] = 'SCALABLE_VIDEO_DROPPING_STEP_THRESHOLD'
	if self.ipactpsfBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_IPACT_PSF'
	if self.nascBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_NASC'
	if self.ipactBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_IPACT'
	if self.leastAssignedBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LEAST_ASSIGNED'
	if self.apsBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_APS'
	if self.lfjBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LFJ'
	if self.lfjlptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LFJ_LPT'
	if self.lfjsptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LFJ_SPT'
	if self.lfjlnfBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LFJ_LNF'
	if self.eafBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_EAF'
	if self.eaafBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_EAAF'
	if self.spdBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_SPD'
	if self.lpdBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LPD'
	if self.spdLptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_SPD_LPT'
	if self.intvlLfjlptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_LFJ_LPT'
	if self.intvlLfjsptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_LFJ_SPT'
	if self.intvlLfjlnfBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_LFJ_LNF'
	if self.intvlEafBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_EAF'
	if self.intvlEaafBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_EAAF'
	if self.jitLfjlptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_LFJ_LPT'
	if self.jitLfjsptBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_LFJ_SPT'
	if self.jitLfjlnfBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_LFJ_LNF'
	if self.jitEafBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_EAF'
	if self.jitEaafBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_EAAF'
	if self.jitSpdBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_SPD'
	if self.jitLpdBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_LPD'
	if self.jitTestBtn.isChecked() == 1:
		setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_TEST'
	if self.dbaGatedBtn.isChecked() == 1:
		setupSimParams[queueIndex]['DBA_TYPE'] = 'DBA_GATED'
	if self.dbaFixedBtn.isChecked() == 1:
		setupSimParams[queueIndex]['DBA_TYPE'] = 'DBA_FIXED'
	if self.dbaLimitedBtn.isChecked() == 1:
		setupSimParams[queueIndex]['DBA_TYPE'] = 'DBA_LIMITED_GATE'
	if self.dbaExcessBtn.isChecked() == 1:
		setupSimParams[queueIndex]['DBA_TYPE'] = 'DBA_EXCESS'
	if self.pnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['TRAFFIC_TYPE'] = 'TRAFFIC_POISSON'
	if self.ssBtn.isChecked() == 1:
		setupSimParams[queueIndex]['TRAFFIC_TYPE'] = 'TRAFFIC_SELF_SIMILAR'
	if self.tunableBtn.isChecked() == 1:
		setupSimParams[queueIndex]['WDM_TYPE'] = 'WDM_TUNABLE'
	if self.fixedBtn.isChecked() == 1:
		setupSimParams[queueIndex]['WDM_TYPE'] = 'WDM_FIXED'
	if self.fpdOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['FIXED_PROP_DELAY'] = 'FIXED_PROP_DELAY_ON'
	if self.fpdOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['FIXED_PROP_DELAY'] = 'FIXED_PROP_DELAY_OFF'
	if self.gtOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['GET_TAIL'] = 'GET_TAIL_ON'
	if self.gtOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['GET_TAIL'] = 'GET_TAIL_OFF'
	if self.ttOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['SIM_TRACE'] = 'SIM_TRACE_ON'
	if self.ttOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['SIM_TRACE'] = 'SIM_TRACE_OFF'
	if self.vtOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_TRAFFIC'] = 'VIDEO_TRAFFIC_ON'
		if setupSimParamsList[queueIndex].count('FRAME_RATE') == 0:
			setupSimParamsList[queueIndex].append('FRAME_RATE')
		setupSimParams[queueIndex]['FRAME_RATE'] = self.frameRateEdit.text().ascii()
		if setupSimParamsList[queueIndex].count('VIDEO_TRACE_FILE') == 0:
			setupSimParamsList[queueIndex].append('VIDEO_TRACE_FILE')
		setupSimParams[queueIndex]['VIDEO_TRACE_FILE'] = self.videoTraceEdit.text().ascii()
		if setupSimParamsList[queueIndex].count('VIDEO_PREDICTION') == 0:
			setupSimParamsList[queueIndex].append('VIDEO_PREDICTION')
		if self.pvtOnBtn.isChecked() == 1 and setupSimParamsList[queueIndex].count('PREDICTION_TYPE') == 0:
			setupSimParamsList[queueIndex].append('PREDICTION_TYPE')
		if setupSimParamsList[queueIndex].count('TIME_SHIFT') == 0:
			setupSimParamsList[queueIndex].append('TIME_SHIFT')
		if setupSimParamsList[queueIndex].count('VIDEO_DBA_TYPE') == 0:
			setupSimParamsList[queueIndex].append('VIDEO_DBA_TYPE')
	if self.pvtOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_PREDICTION'] = 'VIDEO_PREDICTION_ON'
		setupSimParams[queueIndex]['PREDICTION_TYPE'] = self.PredTypeEdit.text().ascii()
	else:
		setupSimParams[queueIndex]['VIDEO_PREDICTION'] = 'VIDEO_PREDICTION_OFF'
	if self.vsOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_RANDOM_START'] = 'VIDEO_RANDOM_START_ON'
		setupSimParams[queueIndex]['TIME_SHIFT'] = self.timeShiftEdit.text().ascii()
	#else:
		#setupSimParams[queueIndex]['TIME_SHIFT'] = '0.0'
	if self.vsOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_RANDOM_START'] = 'VIDEO_RANDOM_START_OFF'
	if self.dbaGatedVideoBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] = 'VIDEO_DBA_GATED'
	if self.dbaFixedVideoBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] = 'VIDEO_DBA_FIXED'
	if self.dbaLimitedVideoBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] = 'VIDEO_DBA_LIMITED_GATE'
	if self.vtOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['VIDEO_TRAFFIC'] = 'VIDEO_TRAFFIC_OFF'
	if self.grtOnBtn.isChecked() == 1:
		setupSimParams[queueIndex]['GRANT_TRACE'] = 'GRANT_TRACE_ON'
	if self.grtOffBtn.isChecked() == 1:
		setupSimParams[queueIndex]['GRANT_TRACE'] = 'GRANT_TRACE_OFF'
	if self.schedulerMaxWinChkBox.isChecked() == 1:
		setupSimParams[queueIndex]['SCHEDULER_MAX_WINDOW'] = '1'
	else:
		setupSimParams[queueIndex]['SCHEDULER_MAX_WINDOW'] = '0'
	setupSimParams[queueIndex]['GUARD_TIME'] = self.grdTimeEdit.text().ascii()
	setupSimParams[queueIndex]['TUNING_TIME'] = self.tuningTimeEdit.text().ascii()
	setupSimParams[queueIndex]['FIXED_PROP_DELAY_VALUE'] = self.fpdValueEdit.text().ascii()
	setupSimParams[queueIndex]['MAX_PROP_DELAY'] = self.maxPropDelayEdit.text().ascii()
	setupSimParams[queueIndex]['NUM_RUNS'] = self.runsEdit.text().ascii()
	setupSimParams[queueIndex]['NUM_ONU'] = self.numONUEdit.text().ascii()
	setupSimParams[queueIndex]['NUM_HEAVY_ONU'] = self.numHvyONUEdit.text().ascii()
	setupSimParams[queueIndex]['HEAVY_LOAD'] = self.heavyLoadEdit.text().ascii()
	setupSimParams[queueIndex]['NUM_WDM_ONU'] = self.numWdmONUEdit.text().ascii()
	setupSimParams[queueIndex]['NUM_UH_WDM_ONU'] = self.numUhWdmONUEdit.text().ascii()
	setupSimParams[queueIndex]['NUM_LH_WDM_ONU'] = self.numLhWdmONUEdit.text().ascii()
	setupSimParams[queueIndex]['LINK_SPEED'] = self.linkSpdEdit.text().ascii()
	setupSimParams[queueIndex]['START_LOAD'] = self.startLoadEdit.text().ascii()
	setupSimParams[queueIndex]['END_LOAD'] = self.endLoadEdit.text().ascii()
	setupSimParams[queueIndex]['LOAD_INCR'] = self.loadIncrEdit.text().ascii()
	setupSimParams[queueIndex]['START_LAMBDA'] = self.startLambdaEdit.text().ascii()
	setupSimParams[queueIndex]['END_LAMBDA'] = self.endLambdaEdit.text().ascii()
	setupSimParams[queueIndex]['SS_HURST_PARAM'] = self.hurstParamEdit.text().ascii()
	setupSimParams[queueIndex]['NUM_SS_STREAMS'] = self.numStrmsEdit.text().ascii()
	setupSimParams[queueIndex]['FIXED_GRANT_SIZE'] = self.fixedGrantSizeEdit.text().ascii()
	setupSimParams[queueIndex]['MAX_GRANT_SIZE'] = self.maxGrantSizeEdit.text().ascii()
	setupSimParams[queueIndex]['SCHEDULER_NUM_SLOT'] = self.schedulerNumSlotEdit.text().ascii()
	setupSimParams[queueIndex]['SCHEDULER_SLOT_SIZE'] = self.schedulerSlotSizeEdit.text().ascii()
	setupSimParams[queueIndex]['STARVE_THRESH'] = self.starveThreshEdit.text().ascii()
	setupSimParams[queueIndex]['AVAIL_COST_WEIGHT'] = self.acwEdit.text().ascii()
	setupSimParams[queueIndex]['NUM_PREFERRED_ONU'] = self.npoEdit.text().ascii()
	setupSimParams[queueIndex]['SIM_TIME'] = self.simTimeEdit.text().ascii()
	setupSimParams[queueIndex]['simID'] = self.simIdEdit.text().ascii()
	setupSimParams[queueIndex]['SV_DROP_LAYER_THRESHOLD'] = self.svDropThresholdEdit.text().ascii()
	setupSimParams[queueIndex]['SV_DROP_SENSITIVITY'] = self.svDropSensitivity.text().ascii()
	setupSimParams[queueIndex]['SV_MIN_BOUND'] = self.svDropStepMinBound.text().ascii()
	setupSimParams[queueIndex]['SV_MAX_BOUND'] = self.svDropStepMaxBound.text().ascii()
	setupSimParams[queueIndex]['SV_NUM_MA_VALUES'] = self.svDropStep_NumMAValues.text().ascii()
	maxNumOfRunningSims = int(self.parallelSimsEdit.text().ascii())

	
def restore_parameters(self):
	global queueIndex
	global maxNumOfRunningSims
	if setupSimParams[queueIndex]['SCALABLE_VIDEO_TRAFFIC'] == 'SCALABLE_VIDEO_OFF':
		self.svOffBtn.setChecked(1)
	if setupSimParams[queueIndex]['SCALABLE_VIDEO_TRAFFIC'] == 'SCALABLE_VIDEO_ON':
		self.svOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_OFF':
		self.svDropNone.setChecked(1)
	if setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_THRESHOLD':
		self.svDropThreshold.setChecked(1)
	if setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_DYNAMIC':
		self.svDropDynamic.setChecked(1)
	if setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_STEP_THRESHOLD':
		self.svDropStepThreshold.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_IPACT_PSF':
		self.ipactpsfBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_NASC':
		self.nascBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_IPACT':
		self.ipactBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LEAST_ASSIGNED':
		self.leastAssignedBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_APS':
		self.apsBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LFJ':
		self.lfjBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LFJ_LPT':
		self.lfjlptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LFJ_SPT':
		self.lfjsptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LFJ_LNF':
		self.lfjlnfBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_EAF':
		self.eafBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_EAAF':
		self.eaafBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_SPD':
		self.spdBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LPD':
		self.lpdBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_SPD_LPT':
		self.spdLptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_LFJ_LPT':
		self.intvlLfjlptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_LFJ_SPT':
		self.intvlLfjsptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_LFJ_LNF':
		self.intvlLfjlnfBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_EAF':
		self.intvlEafBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_EAAF':
		self.intvlEaafBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_LFJ_LPT':
		self.jitLfjlptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_LFJ_SPT':
		self.jitLfjsptBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_LFJ_LNF':
		self.jitLfjlnfBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_EAF':
		self.jitEafBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_EAAF':
		self.jitEaafBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_SPD':
		self.jitSpdBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_LPD':
		self.jitLpdBtn.setChecked(1)
	if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_TEST':
		self.jitTestBtn.setChecked(1)
	if setupSimParams[queueIndex]['DBA_TYPE'] == 'DBA_GATED':
		self.dbaGatedBtn.setChecked(1)
	if setupSimParams[queueIndex]['DBA_TYPE'] == 'DBA_FIXED':
		self.dbaFixedBtn.setChecked(1)
	if setupSimParams[queueIndex]['DBA_TYPE'] == 'DBA_LIMITED_GATE':
		self.dbaLimitedBtn.setChecked(1)
	if setupSimParams[queueIndex]['DBA_TYPE'] == 'DBA_EXCESS':
		self.dbaExcessBtn.setChecked(1)
	if setupSimParams[queueIndex]['TRAFFIC_TYPE'] == 'TRAFFIC_POISSON':
		self.pnBtn.setChecked(1)
	if setupSimParams[queueIndex]['TRAFFIC_TYPE'] == 'TRAFFIC_SELF_SIMILAR':
		self.ssBtn.setChecked(1)
	if setupSimParams[queueIndex]['WDM_TYPE'] == 'WDM_FIXED':
		self.fixedBtn.setChecked(1)
	if setupSimParams[queueIndex]['WDM_TYPE'] == 'WDM_TUNABLE':
		self.tunableBtn.setChecked(1)
	if setupSimParams[queueIndex]['FIXED_PROP_DELAY'] == 'FIXED_PROP_DELAY_ON':
		self.fpdOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['FIXED_PROP_DELAY'] == 'FIXED_PROP_DELAY_OFF':
		self.fpdOffBtn.setChecked(1)
	if setupSimParams[queueIndex]['GET_TAIL'] == 'GET_TAIL_ON':
		self.gtOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['GET_TAIL'] == 'GET_TAIL_OFF':
		self.gtOffBtn.setChecked(1)
	if setupSimParams[queueIndex]['SIM_TRACE'] == 'SIM_TRACE_ON':
		self.ttOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['SIM_TRACE'] == 'SIM_TRACE_OFF': 
		self.ttOffBtn.setChecked(1) 
	if setupSimParams[queueIndex]['VIDEO_TRAFFIC'] == 'VIDEO_TRAFFIC_ON':
		self.vtOnBtn.setChecked(1)
		self.videoTraceEdit.setText(setupSimParams[queueIndex]['VIDEO_TRACE_FILE'])
	if setupSimParams[queueIndex]['VIDEO_PREDICTION'] == 'VIDEO_PREDICTION_ON':
		self.pvtOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_PREDICTION'] == 'VIDEO_PREDICTION_OFF':
		self.pvtOffBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] == 'VIDEO_DBA_GATED':
		self.dbaGatedVideoBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] == 'VIDEO_DBA_FIXED':
		self.dbaFixedVideoBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] == 'VIDEO_DBA_LIMITED_GATE':
		self.dbaLimitedVideoBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_RANDOM_START'] == 'VIDEO_RANDOM_START_ON':
		self.vsOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_RANDOM_START'] == 'VIDEO_RANDOM_START_OFF':
		self.vsOffBtn.setChecked(1)
	if setupSimParams[queueIndex]['VIDEO_TRAFFIC'] == 'VIDEO_TRAFFIC_OFF':
		self.vtOffBtn.setChecked(1)
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
		self.grtOnBtn.setChecked(1)
	if setupSimParams[queueIndex]['GRANT_TRACE'] == 'GRANT_TRACE_OFF':
		self.grtOffBtn.setChecked(1)
	if setupSimParams[queueIndex]['SCHEDULER_MAX_WINDOW'] == '1':
		self.schedulerMaxWinChkBox.setChecked(1)
	else:
		self.schedulerMaxWinChkBox.setChecked(0)
	self.hostEdit.setText(simhostname)
	self.grdTimeEdit.setText(setupSimParams[queueIndex]['GUARD_TIME'])
	self.tuningTimeEdit.setText(setupSimParams[queueIndex]['TUNING_TIME'])
	self.fpdValueEdit.setText(setupSimParams[queueIndex]['FIXED_PROP_DELAY_VALUE'])
	self.maxPropDelayEdit.setText(setupSimParams[queueIndex]['MAX_PROP_DELAY'])
	self.runsEdit.setText(setupSimParams[queueIndex]['NUM_RUNS'])
	self.numONUEdit.setText(setupSimParams[queueIndex]['NUM_ONU'])
	self.numHvyONUEdit.setText(setupSimParams[queueIndex]['NUM_HEAVY_ONU'])
	self.heavyLoadEdit.setText(setupSimParams[queueIndex]['HEAVY_LOAD'])
	self.numWdmONUEdit.setText(setupSimParams[queueIndex]['NUM_WDM_ONU'])
	self.numUhWdmONUEdit.setText(setupSimParams[queueIndex]['NUM_UH_WDM_ONU'])
	self.numLhWdmONUEdit.setText(setupSimParams[queueIndex]['NUM_LH_WDM_ONU'])
	self.linkSpdEdit.setText(setupSimParams[queueIndex]['LINK_SPEED'])
	self.startLoadEdit.setText(setupSimParams[queueIndex]['START_LOAD'])
	self.endLoadEdit.setText(setupSimParams[queueIndex]['END_LOAD'])
	self.loadIncrEdit.setText(setupSimParams[queueIndex]['LOAD_INCR'])
	self.startLambdaEdit.setText(setupSimParams[queueIndex]['START_LAMBDA'])
	self.endLambdaEdit.setText(setupSimParams[queueIndex]['END_LAMBDA'])
	self.hurstParamEdit.setText(setupSimParams[queueIndex]['SS_HURST_PARAM'])
	self.numStrmsEdit.setText(setupSimParams[queueIndex]['NUM_SS_STREAMS'])
	self.fixedGrantSizeEdit.setText(setupSimParams[queueIndex]['FIXED_GRANT_SIZE'])
	self.frameRateEdit.setText(setupSimParams[queueIndex]['FRAME_RATE'])
	self.maxGrantSizeEdit.setText(setupSimParams[queueIndex]['MAX_GRANT_SIZE'])
	self.schedulerNumSlotEdit.setText(setupSimParams[queueIndex]['SCHEDULER_NUM_SLOT'])
	self.schedulerSlotSizeEdit.setText(setupSimParams[queueIndex]['SCHEDULER_SLOT_SIZE'])
	self.starveThreshEdit.setText(setupSimParams[queueIndex]['STARVE_THRESH'])
	self.acwEdit.setText(setupSimParams[queueIndex]['AVAIL_COST_WEIGHT'])
	self.npoEdit.setText(setupSimParams[queueIndex]['NUM_PREFERRED_ONU'])
	self.PredTypeEdit.setText(setupSimParams[queueIndex]['PREDICTION_TYPE'])
	self.simTimeEdit.setText(setupSimParams[queueIndex]['SIM_TIME'])
	self.timeShiftEdit.setText(setupSimParams[queueIndex]['TIME_SHIFT'])
	self.queueIndexSlotEdit.setText(str(queueIndex + 1))
	self.simIdEdit.setText(setupSimParams[queueIndex]['simID'])
	self.parallelSimsEdit.setText(str(maxNumOfRunningSims))
	self.svDropThresholdEdit.setText(str(setupSimParams[queueIndex]['SV_DROP_LAYER_THRESHOLD']))
	self.svDropSensitivity.setText(str(setupSimParams[queueIndex]['SV_DROP_SENSITIVITY']))
	self.svDropStepMinBound.setText(str(setupSimParams[queueIndex]['SV_MIN_BOUND']))
	self.svDropStepMaxBound.setText(str(setupSimParams[queueIndex]['SV_MAX_BOUND']))
	self.svDropStep_NumMAValues.setText(str(setupSimParams[queueIndex]['SV_NUM_MA_VALUES']))
	if self.svOnBtn.isChecked():
		self.svButtonGroup.setEnabled(True)
	else:
		self.svButtonGroup.setEnabled(False)
	if self.vtOnBtn.isChecked():
		self.videoTraceEdit.setEnabled(True)
		self.changeTraceBtn.setEnabled(True)
		self.VideoDBABtnGroup.setEnabled(True)
		self.dbaGatedVideoBtn.setEnabled(True)
		self.dbaFixedVideoBtn.setEnabled(True)
		self.dbaLimitedVideoBtn.setEnabled(True)
		self.predictTrafficBox.setEnabled(True)
		self.FRateLbl.setEnabled(True)
		self.frameRateEdit.setEnabled(True)
		self.videoStartBox.setEnabled(True)
		self.ipactpsfBtn.setEnabled(True)
		self.scalableVideoBox.setEnabled(True)
		self.svDropThresholdEdit.setEnabled(True)
		self.svDropSensitivity.setEnabled(True)
		self.svDropStepMinBound.setEnabled(True)
		self.svDropStepMaxBound.setEnabled(True)
		self.svDropStep_NumMAValues.setEnabled(True)
		self.svDropMinBoundLabel.setEnabled(True)
		self.svDropMaxBoundLabel.setEnabled(True)
	else:
		self.videoTraceEdit.clear()
		self.videoTraceEdit.setEnabled(False)
		self.changeTraceBtn.setEnabled(False)
		self.VideoDBABtnGroup.setEnabled(False)
		self.dbaGatedVideoBtn.setEnabled(False)
		self.dbaFixedVideoBtn.setEnabled(False)
		self.dbaLimitedVideoBtn.setEnabled(False)
		self.predictTrafficBox.setEnabled(False)
		self.FRateLbl.setEnabled(False)
		self.frameRateEdit.setEnabled(False)
		self.videoStartBox.setEnabled(False)
		#if self.ipactpsfBtn.isChecked() == 1:
			#self.nascBtn.setChecked(1)
		self.ipactpsfBtn.setEnabled(False)
		self.scalableVideoBox.setEnabled(False)
		self.svDropThresholdEdit.setEnabled(False)
		self.svDropSensitivity.setEnabled(False)
		self.svDropStepMinBound.setEnabled(False)
		self.svDropStepMaxBound.setEnabled(False)
		self.svDropStep_NumMAValues.setEnabled(False)
		self.svDropMinBoundLabel.setEnabled(False)
		self.svDropMaxBoundLabel.setEnabled(False)
	if self.pvtOnBtn.isChecked():
		self.PredTypeLbl.setEnabled(True)
		self.PredTypeEdit.setEnabled(True)
	else:
		self.PredTypeLbl.setEnabled(False)
		self.PredTypeEdit.setEnabled(False)
	if self.vsOffBtn.isChecked():
		self.timeShiftLbl.setEnabled(False)
		self.timeShiftEdit.setEnabled(False)
	else:
		self.timeShiftLbl.setEnabled(True)
		self.timeShiftEdit.setEnabled(True)
	# app.processEvents(0)


def saveSettingsBtn_pressed2(self):
	global plotSettings
	plotSettings['pointsCBox1'] = self.pointsCBox1.currentItem()
	plotSettings['pointsCBox2'] = self.pointsCBox2.currentItem()
	plotSettings['pointsCBox3'] = self.pointsCBox3.currentItem()
	plotSettings['pointsCBox4'] = self.pointsCBox4.currentItem()
	plotSettings['pointsCBox5'] = self.pointsCBox5.currentItem()
	plotSettings['pointsCBox6'] = self.pointsCBox6.currentItem()
	plotSettings['pointsCBox7'] = self.pointsCBox7.currentItem()
	plotSettings['pointsCBox8'] = self.pointsCBox8.currentItem()
	
	plotSettings['file1Edit'] = self.file1Edit.text().ascii()
	plotSettings['file2Edit'] = self.file2Edit.text().ascii()
	plotSettings['file3Edit'] = self.file3Edit.text().ascii()
	plotSettings['file4Edit'] = self.file4Edit.text().ascii()
	plotSettings['file5Edit'] = self.file5Edit.text().ascii()
	plotSettings['file6Edit'] = self.file6Edit.text().ascii()
	plotSettings['file7Edit'] = self.file7Edit.text().ascii()
	plotSettings['file8Edit'] = self.file8Edit.text().ascii()
	
	plotSettings['pointSizeCBox1'] = self.pointSizeCBox1.currentText().ascii()
	plotSettings['pointSizeCBox2'] = self.pointSizeCBox2.currentText().ascii()
	plotSettings['pointSizeCBox3'] = self.pointSizeCBox3.currentText().ascii()
	plotSettings['pointSizeCBox4'] = self.pointSizeCBox4.currentText().ascii()
	plotSettings['pointSizeCBox5'] = self.pointSizeCBox5.currentText().ascii()
	plotSettings['pointSizeCBox6'] = self.pointSizeCBox6.currentText().ascii()
	plotSettings['pointSizeCBox7'] = self.pointSizeCBox7.currentText().ascii()
	plotSettings['pointSizeCBox8'] = self.pointSizeCBox8.currentText().ascii()
	
	plotSettings['lineWidthCBox1'] = self.lineWidthCBox1.currentText().ascii()
	plotSettings['lineWidthCBox2'] = self.lineWidthCBox2.currentText().ascii()
	plotSettings['lineWidthCBox3'] = self.lineWidthCBox3.currentText().ascii()
	plotSettings['lineWidthCBox4'] = self.lineWidthCBox4.currentText().ascii()
	plotSettings['lineWidthCBox5'] = self.lineWidthCBox5.currentText().ascii()
	plotSettings['lineWidthCBox6'] = self.lineWidthCBox6.currentText().ascii()
	plotSettings['lineWidthCBox7'] = self.lineWidthCBox7.currentText().ascii()
	plotSettings['lineWidthCBox8'] = self.lineWidthCBox8.currentText().ascii()
	
	plotSettings['lineColorCBox1'] = self.lineColorCBox1.currentItem()
	plotSettings['lineColorCBox2'] = self.lineColorCBox2.currentItem()
	plotSettings['lineColorCBox3'] = self.lineColorCBox3.currentItem()
	plotSettings['lineColorCBox4'] = self.lineColorCBox4.currentItem()
	plotSettings['lineColorCBox5'] = self.lineColorCBox5.currentItem()
	plotSettings['lineColorCBox6'] = self.lineColorCBox6.currentItem()
	plotSettings['lineColorCBox7'] = self.lineColorCBox7.currentItem()
	plotSettings['lineColorCBox8'] = self.lineColorCBox8.currentItem()


def restoreSettingsBtn_pressed2(self):
	global plotSettings
	self.pointsCBox1.setCurrentItem(plotSettings['pointsCBox1'])
	self.pointsCBox2.setCurrentItem(plotSettings['pointsCBox2'])
	self.pointsCBox3.setCurrentItem(plotSettings['pointsCBox3'])
	self.pointsCBox4.setCurrentItem(plotSettings['pointsCBox4'])
	self.pointsCBox5.setCurrentItem(plotSettings['pointsCBox5'])
	self.pointsCBox6.setCurrentItem(plotSettings['pointsCBox6'])
	self.pointsCBox7.setCurrentItem(plotSettings['pointsCBox7'])
	self.pointsCBox8.setCurrentItem(plotSettings['pointsCBox8'])
	
	self.file1Edit.setText(plotSettings['file1Edit'])
	self.file2Edit.setText(plotSettings['file2Edit'])
	self.file3Edit.setText(plotSettings['file3Edit'])
	self.file4Edit.setText(plotSettings['file4Edit'])
	self.file5Edit.setText(plotSettings['file5Edit'])
	self.file6Edit.setText(plotSettings['file6Edit'])
	self.file7Edit.setText(plotSettings['file7Edit'])
	self.file8Edit.setText(plotSettings['file8Edit'])
	
	self.pointSizeCBox1.setCurrentText(plotSettings['pointSizeCBox1'])
	self.pointSizeCBox2.setCurrentText(plotSettings['pointSizeCBox2'])
	self.pointSizeCBox3.setCurrentText(plotSettings['pointSizeCBox3'])
	self.pointSizeCBox4.setCurrentText(plotSettings['pointSizeCBox4'])
	self.pointSizeCBox5.setCurrentText(plotSettings['pointSizeCBox5'])
	self.pointSizeCBox6.setCurrentText(plotSettings['pointSizeCBox6'])
	self.pointSizeCBox7.setCurrentText(plotSettings['pointSizeCBox7'])
	self.pointSizeCBox8.setCurrentText(plotSettings['pointSizeCBox8'])
	
	self.lineWidthCBox1.setCurrentText(plotSettings['lineWidthCBox1'])
	self.lineWidthCBox2.setCurrentText(plotSettings['lineWidthCBox2'])
	self.lineWidthCBox3.setCurrentText(plotSettings['lineWidthCBox3'])
	self.lineWidthCBox4.setCurrentText(plotSettings['lineWidthCBox4'])
	self.lineWidthCBox5.setCurrentText(plotSettings['lineWidthCBox5'])
	self.lineWidthCBox6.setCurrentText(plotSettings['lineWidthCBox6'])
	self.lineWidthCBox7.setCurrentText(plotSettings['lineWidthCBox7'])
	self.lineWidthCBox8.setCurrentText(plotSettings['lineWidthCBox8'])
	
	self.lineColorCBox1.setCurrentItem(plotSettings['lineColorCBox1'])
	self.lineColorCBox2.setCurrentItem(plotSettings['lineColorCBox2'])
	self.lineColorCBox3.setCurrentItem(plotSettings['lineColorCBox3'])
	self.lineColorCBox4.setCurrentItem(plotSettings['lineColorCBox4'])
	self.lineColorCBox5.setCurrentItem(plotSettings['lineColorCBox5'])
	self.lineColorCBox6.setCurrentItem(plotSettings['lineColorCBox6'])
	self.lineColorCBox7.setCurrentItem(plotSettings['lineColorCBox7'])
	self.lineColorCBox8.setCurrentItem(plotSettings['lineColorCBox8'])
	
# END David's Funcitons


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
	# Initialize data structures
	#simParamsList.append('OLT_TYPE')
	#simParamsList.append('DBA_TYPE')
	#simParamsList.append('TRAFFIC_TYPE')

	#simParamsList.append('VIDEO_TRAFFIC')

	#simParamsList.append('SCALABLE_VIDEO_TRAFFIC')
	#simParamsList.append('SCALABLE_VIDEO_DROPPING_ALGORITHM')

	#simParamsList.append('WDM_TYPE')
	#simParamsList.append('GUARD_TIME')
	#simParamsList.append('TUNING_TIME')
	#simParamsList.append('NUM_RUNS')
	#simParamsList.append('NUM_ONU')
	#simParamsList.append('NUM_HEAVY_ONU')
	#simParamsList.append('HEAVY_LOAD')
	#simParamsList.append('LINK_SPEED')

	#simParamsList.append('NUM_WDM_ONU')
	#simParamsList.append('NUM_UH_WDM_ONU')
	#simParamsList.append('NUM_LH_WDM_ONU')

	#simParamsList.append('SS_HURST_PARAM')
	#simParamsList.append('NUM_SS_STREAMS')

	#simParamsList.append('START_LOAD')
	#simParamsList.append('END_LOAD')
	#simParamsList.append('LOAD_INCR')

	#simParamsList.append('START_LAMBDA')
	#simParamsList.append('END_LAMBDA')

	#simParamsList.append('FIXED_GRANT_SIZE')
	#simParamsList.append('MAX_GRANT_SIZE')

	#simParamsList.append('SCHEDULER_MAX_WINDOW')
	#simParamsList.append('SCHEDULER_NUM_SLOT')
	#simParamsList.append('SCHEDULER_SLOT_SIZE')
	#simParamsList.append('STARVE_THRESH')
	#simParamsList.append('AVAIL_COST_WEIGHT')
	#simParamsList.append('NUM_PREFERRED_ONU')

	#simParamsList.append('SIM_TIME')

	#simParamsList.append('GET_TAIL')
	#simParamsList.append('SIM_TRACE')
	#simParamsList.append('GRANT_TRACE')

	#simParamsList.append('FIXED_PROP_DELAY')
	#simParamsList.append('FIXED_PROP_DELAY_VALUE')
	#simParamsList.append('MAX_PROP_DELAY')

	#simParams['OLT_TYPE']   	= 'OLT_ONLINE_NASC'
	#simParams['DBA_TYPE']   	= 'DBA_GATED'
	#simParams['TRAFFIC_TYPE']   	= 'TRAFFIC_SELF_SIMILAR' # Traffic Type
	#simParams['WDM_TYPE']   	= 'WDM_FIXED' # WDM Type
	#simParams['GUARD_TIME'] 	= '1e-6'

	#simParams['SCALABLE_VIDEO_TRAFFIC']				= 'SCALABLE_VIDEO_OFF'
	#simParams['SCALABLE_VIDEO_DROPPING_ALGORITHM']	= 'SCALABLE_VIDEO_DROPPING_OFF'

	#simParams['TUNING_TIME']	= '5e-3'
	#simParams['NUM_RUNS']   	= '1'   # Number of independent runs
	#simParams['NUM_ONU']		= '32'  # Number of ONUs on PON
	#simParams['NUM_HEAVY_ONU'] 	= '0'   # Number of heavily loaded ONUs
	#simParams['HEAVY_LOAD'] 	= '2'   # heavily loaded ONU multiple
	#simParams['LINK_SPEED'] 	= '1e9' # link speed in bps
		                                
	#simParams['NUM_WDM_ONU']	= '0'   # Number of WDM ONUs
	#simParams['NUM_UH_WDM_ONU'] 	= '0'   # Number of WDM ONUs
	#simParams['NUM_LH_WDM_ONU'] 	= '0'   # Number of WDM ONUs

	#simParams['SS_HURST_PARAM'] 	= '0.75'# Self Similar Traffic Source Hurst Parameter
	#simParams['NUM_SS_STREAMS'] 	= '32'  # Number of Self Similar Traffic Streams

	#simParams['START_LOAD'] 	= '0.1'
	#simParams['END_LOAD']   	= '0.9'
	#simParams['LOAD_INCR']  	= '0.1'

	#simParams['START_LAMBDA']   	= '1'
	#simParams['END_LAMBDA'] 	= '1'

	##simParams['FIXED_GRANT_SIZE']   = '1534'
	##simParams['MAX_GRANT_SIZE'] 	= '7188'

	#simParams['FIXED_GRANT_SIZE']   = '156876'
	#simParams['MAX_GRANT_SIZE'] 	= '156876'

	#simParams['SCHEDULER_MAX_WINDOW'] 	= '0'
	#simParams['SCHEDULER_NUM_SLOT'] 	= '180'
	#simParams['SCHEDULER_SLOT_SIZE']	= '64'
	#simParams['STARVE_THRESH']  		= '64'
	#simParams['AVAIL_COST_WEIGHT']  	= '1.0'
	#simParams['NUM_PREFERRED_ONU']  	= '0'

	#simParams['SIM_TIME']   		= '300'

	#simParams['GET_TAIL']   		= 'GET_TAIL_OFF'
	#simParams['SIM_TRACE']  		= 'SIM_TRACE_OFF'
	#simParams['GRANT_TRACE']		= 'GRANT_TRACE_OFF'
	#simParams['FIXED_PROP_DELAY']   	= 'FIXED_PROP_DELAY_OFF'
	#simParams['FIXED_PROP_DELAY_VALUE'] 	= '50e-6'
	#simParams['MAX_PROP_DELAY'] 		= '50e-6'
	
	


def load_sim_data():
	simList = []
	global sims
	os.chdir(simhomedir)
	if os.path.exists('sim_mgr_data'):
		simpicklefile = open('sim_mgr_data','r')
		unpickler = pickle.Unpickler(simpicklefile)
		sims = unpickler.load()
		simpicklefile.close()
		simList = sims.keys()
		simList.sort()
		for loopIdx in range(len(simList)):
			sim_mgr_win.simListBox.insertItem(simList[loopIdx])


def load_plot_settings():
	global plotSettings
	os.chdir(simhomedir)
	if os.path.exists('plot_settings_data'):
		plotSettingsPicklefile = open('plot_settings_data','r')
		unpickler = pickle.Unpickler(plotSettingsPicklefile)
		plotSettings = unpickler.load()
		plotSettingsPicklefile.close()
		restoreSettingsBtn_pressed2(plot_name_win)
	else:
		saveSettingsBtn_pressed2(plot_name_win)
		


def write_sim_param_file():
	sim_cfg = open('sim_cfg','w')
	for loopIdx in range(len(simParamsList)):
		sim_cfg.write(queueSimParamsList[0][loopIdx]+'\t'+queueSimParams[0][simParamsList[loopIdx]]+'\n')
	sim_cfg.close()
    
def generate_file_list(file_list,list_box):
	for loopIdx in range(list_box.count()):
		if list_box.isSelected(loopIdx) == 1:
			file_list.append(list_box.item(loopIdx).text().ascii())

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
			
	simListBoxItem = sim_mgr_win.startedListBox.findItem(simID)
	sim_mgr_win.startedListBox.takeItem(simListBoxItem)
	sim_mgr_win.simListBox.insertItem(simID)
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
	os.chdir(os.path.join(os.path.join('/home',str(simusername)), str(simhomedir_2)))
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
	
	
	ExecutePath = os.path.join(os.path.join('/home',str(simusername)), str(simhomedir_2))
	os.chdir(os.path.join('/home',str(simusername)))
	#simcommandfinal = 'valgrind --leak-check=yes --log-file=valgrind_output ' + os.path.join(os.path.join('/home',str(simusername)), str(simcommand))
	#cmd = 'ssh -f -l'+simusername+' '+simhostname+' \'cd '+ExecutePath+'/'+simID+'; '+simcommandfinal+' > sim_log &\''
	simcommandfinal = os.path.join(os.path.join('/home',str(simusername)), str(simcommand))
	cmd = 'ssh -f -l'+simusername+' '+simhostname+' \'cd '+ExecutePath+'/'+simID+'; '+simcommandfinal+' > sim_log &\''
	child = pexpect.spawn(cmd)
	# expect ssh to prompt for a user password
	child.expect(str(simusername)+'@'+str(simhostname)+'\'s' + ' password:')
	print str(simusername)+'@'+str(simhostname)+'\'s' + ' password:'
	# send the password
	child.sendline(str(simpassword))
	child.read()
	
	if child.isalive() == False:
		print 'Simulation Launched Successfully'

		ResultPath = os.path.join(os.path.join(os.path.join(os.path.join('/home',str(simusername)), str(simhomedir_2)), simID), 'pid')
		
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
			os.system('rm -rf '+simID)
			print "Launch Failed!!!!"
		else:
			# Record simulation data and place an entry in simulation list box
			simData['host'] = simhostname
			simData['pid'] = simpid
			simData['params'] = copy.deepcopy(queueSimParams[0])
			sims[simID] = copy.deepcopy(simData)
			#simListBoxItem = sim_mgr_win.simListBox.findItem(simID + '_(Not_Started)')
			#indexOfItem = sim_mgr_win.simListBox.index(simListBoxItem)
			#sim_mgr_win.simListBox.changeItem(simID + '_(Started)', indexOfItem)
			simListBoxItem = sim_mgr_win.notStartedListBox.findItem(simID)
			sim_mgr_win.notStartedListBox.takeItem(simListBoxItem)
			sim_mgr_win.startedListBox.insertItem(simID)
			#sim_mgr_win.simListBox.setCurrentItem(simID)
			#sim_mgr_win.simListBox.currentItem().setTextColor(qColor.fromRgb(255,0,0,255))
			os.chdir('..')
			print 'Sim ID: ' + simID + '   Sim Host: ' + simhostname + '   Simulation ID: ' + str(simpid)
	else:	
		os.system('rm *')
		time.sleep(5)
		os.chdir('..')
		os.system('rm -rf '+simID)
		print "Launch Failed!!!!"
		
	queueSimParamsList.remove(queueSimParamsList[0])
	queueSimParams.remove(queueSimParams[0])
	
def add_items_to_list():
	newList = []
#	for iaa in range(len(queueSimParamsList)):
#		newList[iaa] = queueSimParamsList[iaa]['simID']
#	for simID in newList:
	for simID in [queueSimParams[iaa]['simID'] for iaa in range(len(queueSimParams))]:
		sim_mgr_win.notStartedListBox.insertItem(simID)
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


class PlotNameWin (Ui_plotNameForm):
	def setupUi(self, parent = None, name = "Plot Name Form", modal = 0, fl = 0):
		Ui_plotNameForm.__init__(self)
	
	def saveSettingsBtn_pressed(self):
		saveSettingsBtn_pressed2(self)
		
	def restoreSettingsBtn_pressed(self):
		restoreSettingsBtn_pressed2(self)
		
	def pointsCBoxChangeAll_activated(self, pointsCBoxIndex):
		self.pointsCBox1.setCurrentItem(pointsCBoxIndex)
		self.pointsCBox2.setCurrentItem(pointsCBoxIndex)
		self.pointsCBox3.setCurrentItem(pointsCBoxIndex)
		self.pointsCBox4.setCurrentItem(pointsCBoxIndex)
		self.pointsCBox5.setCurrentItem(pointsCBoxIndex)
		self.pointsCBox6.setCurrentItem(pointsCBoxIndex)
		self.pointsCBox7.setCurrentItem(pointsCBoxIndex)
		self.pointsCBox8.setCurrentItem(pointsCBoxIndex)
		
	def pointSizeCBoxChangeAll_activated(self, pointSizeCBoxIndex):
		self.pointSizeCBox1.setCurrentItem(pointSizeCBoxIndex)
		self.pointSizeCBox2.setCurrentItem(pointSizeCBoxIndex)
		self.pointSizeCBox3.setCurrentItem(pointSizeCBoxIndex)
		self.pointSizeCBox4.setCurrentItem(pointSizeCBoxIndex)
		self.pointSizeCBox5.setCurrentItem(pointSizeCBoxIndex)
		self.pointSizeCBox6.setCurrentItem(pointSizeCBoxIndex)
		self.pointSizeCBox7.setCurrentItem(pointSizeCBoxIndex)
		self.pointSizeCBox8.setCurrentItem(pointSizeCBoxIndex)
		
	def lineWidthCBoxChangeAll_activated(self, lineWidthCBoxIndex):
		self.lineWidthCBox1.setCurrentItem(lineWidthCBoxIndex)
		self.lineWidthCBox2.setCurrentItem(lineWidthCBoxIndex)
		self.lineWidthCBox3.setCurrentItem(lineWidthCBoxIndex)
		self.lineWidthCBox4.setCurrentItem(lineWidthCBoxIndex)
		self.lineWidthCBox5.setCurrentItem(lineWidthCBoxIndex)
		self.lineWidthCBox6.setCurrentItem(lineWidthCBoxIndex)
		self.lineWidthCBox7.setCurrentItem(lineWidthCBoxIndex)
		self.lineWidthCBox8.setCurrentItem(lineWidthCBoxIndex)
		
	def lineColorCBoxChangeAll_activated(self, lineColorCBoxIndex):
		self.lineColorCBox1.setCurrentItem(lineColorCBoxIndex)
		self.lineColorCBox2.setCurrentItem(lineColorCBoxIndex)
		self.lineColorCBox3.setCurrentItem(lineColorCBoxIndex)
		self.lineColorCBox4.setCurrentItem(lineColorCBoxIndex)
		self.lineColorCBox5.setCurrentItem(lineColorCBoxIndex)
		self.lineColorCBox6.setCurrentItem(lineColorCBoxIndex)
		self.lineColorCBox7.setCurrentItem(lineColorCBoxIndex)
		self.lineColorCBox8.setCurrentItem(lineColorCBoxIndex)
	
	def SaveTimeButton_pressed(self):
		global fileList
		
		if len(fileList) > 0:
			pieces = fileList[0].split('_')
			newLegend1 = pieces[4] + ' ' + pieces[5]
			self.file1Edit.setText(newLegend1)
	
		if len(fileList) > 1:
			pieces = fileList[1].split('_')
			newLegend2 = pieces[4] + ' ' + pieces[5]
			self.file2Edit.setText(newLegend2)
		
		if len(fileList) > 2:
			pieces = fileList[2].split('_')
			newLegend3 = pieces[4] + ' ' + pieces[5]
			self.file3Edit.setText(newLegend3)
		
		if len(fileList) > 3:
			pieces = fileList[3].split('_')
			newLegend4 = pieces[4] + ' ' + pieces[5]
			self.file4Edit.setText(newLegend4)
		
		if len(fileList) > 4:
			pieces = fileList[4].split('_')
			newLegend5 = pieces[4] + ' ' + pieces[5]
			self.file5Edit.setText(newLegend5)
		
		if len(fileList) > 5:
			pieces = fileList[5].split('_')
			newLegend6 = pieces[4] + ' ' + pieces[5]
			self.file6Edit.setText(newLegend6)
		
		if len(fileList) > 6:
			pieces = fileList[6].split('_')
			newLegend7 = pieces[4] + ' ' + pieces[5]
			self.file7Edit.setText(newLegend7)
		
		if len(fileList) > 7:
			pieces = fileList[7].split('_')
			newLegend8 = pieces[4] + ' ' + pieces[5]
			self.file8Edit.setText(newLegend8)
		
	def LegendPosition_selected(self):
		if self.legendCBox.currentText() == 'Customized Position':
			self.x_axisPositionLbl.setEnabled(True)
			self.y_axisPositionLbl.setEnabled(True)
			self.x_axisEdit.setEnabled(True)
			self.y_axisEdit.setEnabled(True)
		else:
			self.x_axisPositionLbl.setEnabled(False)
			self.y_axisPositionLbl.setEnabled(False)
			self.x_axisEdit.setEnabled(False)
			self.y_axisEdit.setEnabled(False)			
		
	def doneBtn_pressed(self):
		global fileList
		global plotType
		simID = sim_view_win.simIDEdit.text().ascii()
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
				plotIdx = int(self.plotOrder1.text().ascii())-1
				newFileList[plotIdx] = fileList[0]
				newFileListText[plotIdx] = self.file1Edit.text().ascii()
				newPointTypeList[plotIdx] = self.pointsCBox1.currentItem()
				newPointSizeList[plotIdx] = self.pointSizeCBox1.currentText()
				newLineWidthList[plotIdx] = self.lineWidthCBox1.currentText()
				newLineColorList[plotIdx] = self.lineColorCBox1.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1
				
			elif loopIdx == 1:
				plotIdx = int(self.plotOrder2.text().ascii())-1
				newFileList[plotIdx] = fileList[1]
				newFileListText[plotIdx] = self.file2Edit.text().ascii()
				newPointTypeList[plotIdx] = self.pointsCBox2.currentItem()
				newPointSizeList[plotIdx] = self.pointSizeCBox2.currentText()
				newLineWidthList[plotIdx] = self.lineWidthCBox2.currentText()
				newLineColorList[plotIdx] = self.lineColorCBox2.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1								
			elif loopIdx == 2:
				plotIdx = int(self.plotOrder3.text().ascii())-1
				newFileList[plotIdx] = fileList[2]
				newFileListText[plotIdx] = self.file3Edit.text().ascii()
				newPointTypeList[plotIdx] = self.pointsCBox3.currentItem()
				newPointSizeList[plotIdx] = self.pointSizeCBox3.currentText()
				newLineWidthList[plotIdx] = self.lineWidthCBox3.currentText()
				newLineColorList[plotIdx] = self.lineColorCBox3.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1			
			elif loopIdx == 3:
				plotIdx = int(self.plotOrder4.text().ascii())-1
				newFileList[plotIdx] = fileList[3]
				newFileListText[plotIdx] = self.file4Edit.text().ascii()
				newPointTypeList[plotIdx] = self.pointsCBox4.currentItem()
				newPointSizeList[plotIdx] = self.pointSizeCBox4.currentText()
				newLineWidthList[plotIdx] = self.lineWidthCBox4.currentText()
				newLineColorList[plotIdx] = self.lineColorCBox4.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1			
			elif loopIdx == 4:
				plotIdx = int(self.plotOrder5.text().ascii())-1
				newFileList[plotIdx] = fileList[4]
				newFileListText[plotIdx] = self.file5Edit.text().ascii()
				newPointTypeList[plotIdx] = self.pointsCBox5.currentItem()
				newPointSizeList[plotIdx] = self.pointSizeCBox5.currentText()
				newLineWidthList[plotIdx] = self.lineWidthCBox5.currentText()
				newLineColorList[plotIdx] = self.lineColorCBox5.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1			
			elif loopIdx == 5:
				plotIdx = int(self.plotOrder6.text().ascii())-1
				newFileList[plotIdx] = fileList[5]
				newFileListText[plotIdx] = self.file6Edit.text().ascii()
				newPointTypeList[plotIdx] = self.pointsCBox6.currentItem()
				newPointSizeList[plotIdx] = self.pointSizeCBox6.currentText()
				newLineWidthList[plotIdx] = self.lineWidthCBox6.currentText()
				newLineColorList[plotIdx] = self.lineColorCBox6.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1
			elif loopIdx == 6:
				plotIdx = int(self.plotOrder7.text().ascii())-1
				newFileList[plotIdx] = fileList[6]
				newFileListText[plotIdx] = self.file7Edit.text().ascii()
				newPointTypeList[plotIdx] = self.pointsCBox7.currentItem()
				newPointSizeList[plotIdx] = self.pointSizeCBox7.currentText()
				newLineWidthList[plotIdx] = self.lineWidthCBox7.currentText()
				newLineColorList[plotIdx] = self.lineColorCBox7.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1
			elif loopIdx == 7:
				plotIdx = int(self.plotOrder8.text().ascii())-1
				newFileList[plotIdx] = fileList[7]
				newFileListText[plotIdx] = self.file8Edit.text().ascii()
				newPointTypeList[plotIdx] = self.pointsCBox8.currentItem()
				newPointSizeList[plotIdx] = self.pointSizeCBox8.currentText()
				newLineWidthList[plotIdx] = self.lineWidthCBox8.currentText()
				newLineColorList[plotIdx] = self.lineColorCBox8.currentItem()
				if newLineColorList[plotIdx] == 'black':
					newLineColorList[plotIdx] = -1			
		#
		# Setup gnuplot script
		#
		if sim_view_win.plotNameEdit.text().ascii() == '':
			sim_view_win.plotNameEdit.setText('selected_plot')
		gplot_file = open(sim_view_win.plotNameEdit.text().ascii()+'.gp','w')
		if sim_view_win.histBtn.isChecked() == 1 or sim_view_win.timeHistBtn.isChecked() == 1 or sim_view_win.byteHistBtn.isChecked() == 1:
			gplot_file.write('set style data hist\n')
			gplot_file.write('set key right top Right\n')
		else:
			if self.legendCBox.currentText() == 'Customized Position':		
					gplot_file.write('set key ' + self.x_axisEdit.text() + ',' + self.y_axisEdit.text() + '\n')
			elif self.legendCBox.currentText() == 'Remove Legend':
					gplot_file.write('unset key\n')
			else:
				gplot_file.write('set key left top Left\n')
				
			if sim_view_win.confIntvlChkBox.isChecked() == 1:
				gplot_file.write('set style data yerrorlines\n')
			else:
				for loopIdx in range(len(fileList)):
					pointtype = newPointTypeList[loopIdx]
					pointsize = newPointSizeList[loopIdx]
					linewidth = newLineWidthList[loopIdx]
					linecolor = newLineColorList[loopIdx]
					
					gplot_file.write('set style line ' + str(loopIdx+1) + ' pt ' + str(pointtype) + ' ps ' + str(pointsize) + ' lw ' + str(linewidth) + ' lc ' + str(linecolor) + ' \n')
				
		if sim_view_win.delayVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'delay (in seconds)\'\n') #{/Symbol m}
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
#   		gplot_file.write('set xtics 0.0,0.2\n')
			gplot_file.write('set format y \"%.1se%S\"\n')
		if sim_view_win.jitterVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'jitter (in seconds squared)\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
#   		gplot_file.write('set xtics 0.0,0.2\n')
			gplot_file.write('set format y \"%.1se%S\"\n') #%csec^2
		if sim_view_win.delayVsTimeBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'delay (in seconds)\'\n')
			gplot_file.write('set xlabel \'simulation time (in 1 second intervals)\'\n')
#   		gplot_file.write('set xtics 0.0,1\n')
			gplot_file.write('set format y \"%.1s %csec\"\n')
		if sim_view_win.delayVsONUBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'delay (in seconds)\'\n')
			gplot_file.write('set xlabel \'# of ONUs\'\n')
			gplot_file.write('set format y \"%.1s %csec\"\n')
		if sim_view_win.utilVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'utilization\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
		if sim_view_win.cyclelenVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'cycle length (in seconds)\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
			gplot_file.write('set format y \"%.1se%S\"\n')
		if sim_view_win.cyclelenVsONUBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'cycle length (in seconds)\'\n')
			gplot_file.write('set xlabel \'# of ONUs\'\n')
			gplot_file.write('set format y \"%.1s %csec\"\n')
		if sim_view_win.grantsizeVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Grant Size (in bytes)\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
			gplot_file.write('set format y \"%.1f\"\n')
		if sim_view_win.reportsizeVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Report Size (in bytes)\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
			gplot_file.write('set format y \"%.1f\"\n')
		if sim_view_win.grantsizePVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Grant Size (in packets)\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
		if sim_view_win.granttimeVsLoadBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Grant Time (in seconds)\'\n')
			gplot_file.write('set xlabel \'data load (in Gbps)\'\n')
			gplot_file.write('set format y \"%.1s %csec\"\n')
		if sim_view_win.histBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Probability\'\n')
		if sim_view_win.timeHistBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Probability\'\n')
			gplot_file.write('set xlabel \'(in seconds)\'\n')
			gplot_file.write('set format x \"%.1s%cs\"\n')
		if sim_view_win.byteHistBtn.isChecked() == 1:
			gplot_file.write('set ylabel \'Probability\'\n')
			gplot_file.write('set xlabel \'(in bytes)\'\n')
			gplot_file.write('set format x \"%.1s%cB\"\n')
		if ((sim_view_win.maxYEdit.text().ascii() != '') and (sim_view_win.minYEdit.text().ascii() != '')):
			gplot_file.write('set yrange ['+sim_view_win.minYEdit.text().ascii()+':'+sim_view_win.maxYEdit.text().ascii()+']\n')
		if ((sim_view_win.maxYEdit.text().ascii() != '') and (sim_view_win.minYEdit.text().ascii() == '')):
			gplot_file.write('set yrange [:'+sim_view_win.maxYEdit.text().ascii()+']\n')
		if ((sim_view_win.maxYEdit.text().ascii() == '') and (sim_view_win.minYEdit.text().ascii() != '')):
			gplot_file.write('set yrange ['+sim_view_win.minYEdit.text().ascii()+':]\n')
		if ((sim_view_win.maxXEdit.text().ascii() != '') and (sim_view_win.minXEdit.text().ascii() != '')):
			gplot_file.write('set xrange ['+sim_view_win.minXEdit.text().ascii()+':'+sim_view_win.maxXEdit.text().ascii()+']\n')
		if ((sim_view_win.maxXEdit.text().ascii() != '') and (sim_view_win.minXEdit.text().ascii() == '')):
			gplot_file.write('set xrange [:'+sim_view_win.maxXEdit.text().ascii()+']\n')
		if ((sim_view_win.maxXEdit.text().ascii() == '') and (sim_view_win.minXEdit.text().ascii() != '')):
			gplot_file.write('set xrange ['+sim_view_win.minXEdit.text().ascii()+':]\n')
		gplot_file.write('set grid\n')
		if plotType == 0:
			gplot_file.write('set terminal x11 font \"times,14\" enhanced \n')
		else:
			gplot_file.write('set terminal fig fontsize 12 \n')
			gplot_file.write('set output "'+sim_view_win.plotNameEdit.text().ascii()+'.fig"\n')
		plotStr = 'plot '
		count = 1
		
		if sim_view_win.confIntvlChkBox.isChecked() == 1:
			for loopIdx in range(len(fileList)):
				if loopIdx > 0:
					plotStr = plotStr + ','
				plotStr = plotStr + '"' + newFileList[loopIdx] + '"'
				#plotStr = plotStr + ' title \'' + newFileListText[loopIdx] + '\'' + ' with yerr linestyle ' + str(loopIdx+1)
				plotStr = plotStr + ' title \'' + newFileListText[loopIdx] + '\''
		else:
			for loopIdx in range(len(fileList)):
				if loopIdx > 0:
					plotStr = plotStr + ','
				plotStr = plotStr + '"' + newFileList[loopIdx] + '"'
				plotStr = plotStr + ' title \'' + newFileListText[loopIdx] + '\'' + ' with linespoints linestyle ' + str(loopIdx+1)
			
#   		if loopIdx == 0:
#   			plotStr = plotStr + ' title \'' + self.file1Edit.text().ascii() + '\''
#   		if loopIdx == 1:
#   			plotStr = plotStr + ' title \'' + self.file2Edit.text().ascii() + '\''
#   		if loopIdx == 2:
#   			plotStr = plotStr + ' title \'' + self.file3Edit.text().ascii() + '\''
#   		if loopIdx == 3:
#   			plotStr = plotStr + ' title \'' + self.file4Edit.text().ascii() + '\''
#   		if loopIdx == 4:
#   			plotStr = plotStr + ' title \'' + self.file5Edit.text().ascii() + '\''
#   		if loopIdx == 5:
#   			plotStr = plotStr + ' title \'' + self.file6Edit.text().ascii() + '\''
#   		if loopIdx == 6:
#   			plotStr = plotStr + ' title \'' + self.file7Edit.text().ascii() + '\''
		plotStr = plotStr + '\n'
		gplot_file.write(plotStr)
		#
		# Setup plot refresh loop file
		
		if sim_view_win.plotRefreshChkBox.isChecked() == 1:
			gplot_file.write('load "loop.gp"')
			loop_file = open('loop.gp','w')
			loop_file.write('pause 15\n')
			loop_file.write('replot\n')
			loop_file.write('reread\n')
			loop_file.close()
		gplot_file.close()
		if plotType == 0:
			os.system('gnuplot -persist '+sim_view_win.plotNameEdit.text().ascii()+'.gp')
		else:
			os.system('gnuplot '+sim_view_win.plotNameEdit.text().ascii()+'.gp')
			os.system('fig2dev -L pdf '+sim_view_win.plotNameEdit.text().ascii()+'.fig '+sim_view_win.plotNameEdit.text().ascii()+'.pdf')
			os.system('fig2dev -L eps '+sim_view_win.plotNameEdit.text().ascii()+'.fig '+sim_view_win.plotNameEdit.text().ascii()+'.eps')
			tex_file = open(sim_view_win.plotNameEdit.text().ascii()+'.tex','w')
			tex_file.write('\\begin{figure}[tb]\n')
			tex_file.write('\\includegraphics[scale=0.75,angle=270]{'+sim_view_win.plotNameEdit.text().ascii()+'.pdf}\n')
			tex_file.write('\\caption{'+sim_view_win.plotCaptionEdit.text().ascii()+'}\n')
			tex_file.write('\\label{fig:'+sim_view_win.plotNameEdit.text().ascii()+'}\n')
			tex_file.write('\\end{figure}\n')
			tex_file.close()
		
		cwdDir = os.getcwd()
		resultsDir = cwdDir + '/A_Results'
		pdfDir = resultsDir + '/pdf_files'
		if not os.path.isdir(resultsDir):
			os.mkdir('A_Results')
		if not os.path.isdir(pdfDir):
			os.mkdir('A_Results/pdf_files')
		os.rename(cwdDir+'/'+sim_view_win.plotNameEdit.text().ascii()+'.gp', resultsDir+'/'+sim_view_win.plotNameEdit.text().ascii()+'.gp')
		os.rename(cwdDir+'/'+sim_view_win.plotNameEdit.text().ascii()+'.fig', resultsDir+'/'+sim_view_win.plotNameEdit.text().ascii()+'.fig')
		os.rename(cwdDir+'/'+sim_view_win.plotNameEdit.text().ascii()+'.pdf', resultsDir+'/'+sim_view_win.plotNameEdit.text().ascii()+'.pdf')
		os.rename(cwdDir+'/'+sim_view_win.plotNameEdit.text().ascii()+'.eps', resultsDir+'/'+sim_view_win.plotNameEdit.text().ascii()+'.eps')
		os.rename(cwdDir+'/'+sim_view_win.plotNameEdit.text().ascii()+'.tex', resultsDir+'/'+sim_view_win.plotNameEdit.text().ascii()+'.tex')

		shutil.copy2(resultsDir+'/'+sim_view_win.plotNameEdit.text().ascii()+'.pdf', pdfDir+'/'+sim_view_win.plotNameEdit.text().ascii()+'.pdf')
		
		os.chdir('..')
		self.hide()

class WaitWin (Ui_WaitForm):	
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)

class SimViewWin (Ui_SimViewForm):
	#def __init__(self, parent = None, name = "Simulation View Form", modal = 0, fl = 0):
		#Ui_SimViewForm.setupUi(self)
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
	
	def pushButtonAutoName_pressed(self):
		global fileList
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


class SimInitWin (Ui_SimInitForm):
	#def __init__(self, parent = None, name = "Simulation Init Form", modal = 0, fl = 0):
		#Ui_SimInitForm.__init__(self)
	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		global simhostname
		restore_parameters(self)
		
		#if setupSimParams[queueIndex]['SCALABLE_VIDEO_TRAFFIC'] == 'SCALABLE_VIDEO_OFF':
			#self.svOffBtn.setChecked(1)
		#if setupSimParams[queueIndex]['SCALABLE_VIDEO_TRAFFIC'] == 'SCALABLE_VIDEO_ON':
			#self.svOnBtn.setChecked(1)
		#if setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_OFF':
			#self.svDropMethod0.setChecked(1)
		#if setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_METHOD_1':
			#self.svDropMethod1.setChecked(1)
		#if setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_METHOD_2':
			#self.svDropMethod2.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_NASC':
			#self.nascBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_IPACT':
			#self.ipactBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LEAST_ASSIGNED':
			#self.leastAssignedBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_APS':
			#self.apsBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LFJ':
			#self.lfjBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LFJ_LPT':
			#self.lfjlptBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LFJ_SPT':
			#self.lfjsptBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LFJ_LNF':
			#self.lfjlnfBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_EAF':
			#self.eafBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_EAAF':
			#self.eaafBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_SPD':
			#self.spdBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_LPD':
			#self.lpdBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_SPD_LPT':
			#self.spdLptBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_LFJ_LPT':
			#self.intvlLfjlptBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_LFJ_SPT':
			#self.intvlLfjsptBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_LFJ_LNF':
			#self.intvlLfjlnfBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_EAF':
			#self.intvlEafBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_EAAF':
			#self.intvlEaafBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_LFJ_LPT':
			#self.jitLfjlptBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_LFJ_SPT':
			#self.jitLfjsptBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_LFJ_LNF':
			#self.jitLfjlnfBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_EAF':
			#self.jitEafBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_EAAF':
			#self.jitEaafBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_SPD':
			#self.jitSpdBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_LPD':
			#self.jitLpdBtn.setChecked(1)
		#if setupSimParams[queueIndex]['OLT_TYPE'] == 'OLT_ONLINE_JIT_TEST':
			#self.jitTestBtn.setChecked(1)
		#if setupSimParams[queueIndex]['DBA_TYPE'] == 'DBA_GATED':
			#self.dbaGatedBtn.setChecked(1)
		#if setupSimParams[queueIndex]['DBA_TYPE'] == 'DBA_FIXED':
			#self.dbaFixedBtn.setChecked(1)
		#if setupSimParams[queueIndex]['DBA_TYPE'] == 'DBA_LIMITED_GATE':
			#self.dbaLimitedBtn.setChecked(1)
		#if setupSimParams[queueIndex]['DBA_TYPE'] == 'DBA_EXCESS':
			#self.dbaExcessBtn.setChecked(1)
		#if setupSimParams[queueIndex]['TRAFFIC_TYPE'] == 'TRAFFIC_POISSON':
			#self.pnBtn.setChecked(1)
		#if setupSimParams[queueIndex]['TRAFFIC_TYPE'] == 'TRAFFIC_SELF_SIMILAR':
			#self.ssBtn.setChecked(1)
		#if setupSimParams[queueIndex]['WDM_TYPE'] == 'WDM_FIXED':
			#self.fixedBtn.setChecked(1)
		#if setupSimParams[queueIndex]['WDM_TYPE'] == 'WDM_TUNABLE':
			#self.tunableBtn.setChecked(1)
		#if setupSimParams[queueIndex]['FIXED_PROP_DELAY'] == 'FIXED_PROP_DELAY_ON':
			#self.fpdOnBtn.setChecked(1)
		#if setupSimParams[queueIndex]['FIXED_PROP_DELAY'] == 'FIXED_PROP_DELAY_OFF':
			#self.fpdOffBtn.setChecked(1)
		#if setupSimParams[queueIndex]['GET_TAIL'] == 'GET_TAIL_ON':
			#self.gtOnBtn.setChecked(1)
		#if setupSimParams[queueIndex]['GET_TAIL'] == 'GET_TAIL_OFF':
			#self.gtOffBtn.setChecked(1)
		#if setupSimParams[queueIndex]['SIM_TRACE'] == 'SIM_TRACE_ON':
			#self.ttOnBtn.setChecked(1)
		#if setupSimParams[queueIndex]['SIM_TRACE'] == 'SIM_TRACE_OFF':
			#self.ttOffBtn.setChecked(1)
		#if setupSimParams[queueIndex]['GRANT_TRACE'] == 'GRANT_TRACE_ON':
			#self.grtOnBtn.setChecked(1)
		#if setupSimParams[queueIndex]['GRANT_TRACE'] == 'GRANT_TRACE_OFF':
			#self.grtOffBtn.setChecked(1)
		#if setupSimParams[queueIndex]['SCHEDULER_MAX_WINDOW'] == '1':
			#self.schedulerMaxWinChkBox.setChecked(1)
		#else:
			#self.schedulerMaxWinChkBox.setChecked(0)
		#self.hostEdit.setText(simhostname)
		#self.grdTimeEdit.setText(setupSimParams[queueIndex]['GUARD_TIME'])
		#self.tuningTimeEdit.setText(setupSimParams[queueIndex]['TUNING_TIME'])
		#self.fpdValueEdit.setText(setupSimParams[queueIndex]['FIXED_PROP_DELAY_VALUE'])
		#self.maxPropDelayEdit.setText(setupSimParams[queueIndex]['MAX_PROP_DELAY'])
		#self.runsEdit.setText(setupSimParams[queueIndex]['NUM_RUNS'])
		#self.numONUEdit.setText(setupSimParams[queueIndex]['NUM_ONU'])
		#self.numHvyONUEdit.setText(setupSimParams[queueIndex]['NUM_HEAVY_ONU'])
		#self.heavyLoadEdit.setText(setupSimParams[queueIndex]['HEAVY_LOAD'])
		#self.numWdmONUEdit.setText(setupSimParams[queueIndex]['NUM_WDM_ONU'])
		#self.numUhWdmONUEdit.setText(setupSimParams[queueIndex]['NUM_UH_WDM_ONU'])
		#self.numLhWdmONUEdit.setText(setupSimParams[queueIndex]['NUM_LH_WDM_ONU'])
		#self.linkSpdEdit.setText(setupSimParams[queueIndex]['LINK_SPEED'])
		#self.startLoadEdit.setText(setupSimParams[queueIndex]['START_LOAD'])
		#self.endLoadEdit.setText(setupSimParams[queueIndex]['END_LOAD'])
		#self.loadIncrEdit.setText(setupSimParams[queueIndex]['LOAD_INCR'])
		#self.startLambdaEdit.setText(setupSimParams[queueIndex]['START_LAMBDA'])
		#self.endLambdaEdit.setText(setupSimParams[queueIndex]['END_LAMBDA'])
		#self.hurstParamEdit.setText(setupSimParams[queueIndex]['SS_HURST_PARAM'])
		#self.numStrmsEdit.setText(setupSimParams[queueIndex]['NUM_SS_STREAMS'])
		#self.fixedGrantSizeEdit.setText(setupSimParams[queueIndex]['FIXED_GRANT_SIZE'])
		#self.maxGrantSizeEdit.setText(setupSimParams[queueIndex]['MAX_GRANT_SIZE'])
		#self.schedulerNumSlotEdit.setText(setupSimParams[queueIndex]['SCHEDULER_NUM_SLOT'])
		#self.schedulerSlotSizeEdit.setText(setupSimParams[queueIndex]['SCHEDULER_SLOT_SIZE'])
		#self.starveThreshEdit.setText(setupSimParams[queueIndex]['STARVE_THRESH'])
		#self.acwEdit.setText(setupSimParams[queueIndex]['AVAIL_COST_WEIGHT'])
		#self.npoEdit.setText(setupSimParams[queueIndex]['NUM_PREFERRED_ONU'])
		#self.simTimeEdit.setText(setupSimParams[queueIndex]['SIM_TIME'])
		#self.queueIndexSlotEdit.setText(str(queueIndex + 1))
		
#	def UpdateCluster(self):
#		#Populating the Cluster Select
#		self.ClusterCB.clear()
#		clustercount = 2
#		lifeline = re.compile(r"(\d) received")
#		report = ("No response","Partial Response","Alive")
#
#		print time.ctime()
#
#		for host in range(2,8):
#			ip = self.ui.IPpart1Edit.text() + '.' + self.ui.IPpart2Edit.text() + '.' + self.ui.IPpart3Edit.text() + '.' + str(host)
#			pingaling = os.popen("ping -q -c2 "+str(ip),"r")
#			print "Testing ",ip,
#			sys.stdout.flush()
#			while 1:
#				line = pingaling.readline()
#				if not line: break
#				igot = re.findall(lifeline,line)
#				if igot:
#					print report[int(igot[0])]
#					if report[int(igot[0])] == 'Alive':
#						self.ClusterCB.addItem("sim"+str(clustercount))
#						clustercount = clustercount + 1
#					else:
#						clustercount = clustercount + 1

	def cancelBtn_pressed(self):
		store_parameters(self)
		self.cancelBtn.setDown(0)
		sim_init_win.hide()
		sim_mgr_win.show()
	def launchBtn_pressed(self):
		self.launchBtn.setDown(0)
		global simhostname
		store_parameters(self)
		#simParamsList = []
		#initialize_data_structure()
		#if self.svOffBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['SCALABLE_VIDEO_TRAFFIC'] = 'SCALABLE_VIDEO_OFF'
		#if self.svOnBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['SCALABLE_VIDEO_TRAFFIC'] = 'SCALABLE_VIDEO_ON'
		#if self.svDropMethod0.isChecked() == 1:
			#setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] = 'SCALABLE_VIDEO_DROPPING_OFF'
		#if self.svDropMethod1.isChecked() == 1:
			#setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] = 'SCALABLE_VIDEO_DROPPING_METHOD_1'
		#if self.svDropMethod2.isChecked() == 1:
			#setupSimParams[queueIndex]['SCALABLE_VIDEO_DROPPING_ALGORITHM'] = 'SCALABLE_VIDEO_DROPPING_METHOD_2'
		#if self.ipactpsfBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_IPACT_PSF'
		#if self.nascBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_NASC'
		#if self.ipactBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_IPACT'
		#if self.leastAssignedBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LEAST_ASSIGNED'
		#if self.apsBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_APS'
		#if self.lfjBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LFJ'
		#if self.lfjlptBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LFJ_LPT'
		#if self.lfjsptBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LFJ_SPT'
		#if self.lfjlnfBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LFJ_LNF'
		#if self.eafBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_EAF'
		#if self.eaafBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_EAAF'
		#if self.spdBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_SPD'
		#if self.lpdBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_LPD'
		#if self.spdLptBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_SPD_LPT'
		#if self.intvlLfjlptBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_LFJ_LPT'
		#if self.intvlLfjsptBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_LFJ_SPT'
		#if self.intvlLfjlnfBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_LFJ_LNF'
		#if self.intvlEafBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_EAF'
		#if self.intvlEaafBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_INTERVAL_EAAF'
		#if self.jitLfjlptBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_LFJ_LPT'
		#if self.jitLfjsptBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_LFJ_SPT'
		#if self.jitLfjlnfBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_LFJ_LNF'
		#if self.jitEafBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_EAF'
		#if self.jitEaafBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_EAAF'
		#if self.jitSpdBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_SPD'
		#if self.jitLpdBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_LPD'
		#if self.jitTestBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['OLT_TYPE'] = 'OLT_ONLINE_JIT_TEST'
		#if self.dbaGatedBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['DBA_TYPE'] = 'DBA_GATED'
		#if self.dbaFixedBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['DBA_TYPE'] = 'DBA_FIXED'
		#if self.dbaLimitedBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['DBA_TYPE'] = 'DBA_LIMITED_GATE'
		#if self.dbaExcessBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['DBA_TYPE'] = 'DBA_EXCESS'
		#if self.pnBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['TRAFFIC_TYPE'] = 'TRAFFIC_POISSON'
		#if self.ssBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['TRAFFIC_TYPE'] = 'TRAFFIC_SELF_SIMILAR'
		#if self.tunableBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['WDM_TYPE'] = 'WDM_TUNABLE'
		#if self.fixedBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['WDM_TYPE'] = 'WDM_FIXED'
		#if self.fpdOnBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['FIXED_PROP_DELAY'] = 'FIXED_PROP_DELAY_ON'
		#if self.fpdOffBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['FIXED_PROP_DELAY'] = 'FIXED_PROP_DELAY_OFF'
		#if self.gtOnBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['GET_TAIL'] = 'GET_TAIL_ON'
		#if self.gtOffBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['GET_TAIL'] = 'GET_TAIL_OFF'
		#if self.ttOnBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['SIM_TRACE'] = 'SIM_TRACE_ON'
		#if self.ttOffBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['SIM_TRACE'] = 'SIM_TRACE_OFF'
		#if self.vtOnBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['VIDEO_TRAFFIC'] = 'VIDEO_TRAFFIC_ON'
			#setupSimParamsList[queueIndex].append('FRAME_RATE')
			#setupSimParams[queueIndex]['FRAME_RATE'] = self.frameRateEdit.text().ascii()
			#setupSimParamsList[queueIndex].append('VIDEO_TRACE_FILE')
			#setupSimParams[queueIndex]['VIDEO_TRACE_FILE'] = self.videoTraceEdit.text().ascii()
			#setupSimParamsList[queueIndex].append('VIDEO_PREDICTION')
			#if self.pvtOnBtn.isChecked() == 1:
				#setupSimParams[queueIndex]['VIDEO_PREDICTION'] = 'VIDEO_PREDICTION_ON'
				#setupSimParamsList[queueIndex].append('PREDICTION_TYPE')
				#setupSimParams[queueIndex]['PREDICTION_TYPE'] = self.PredTypeEdit.text().ascii()
			#else:
				#setupSimParams[queueIndex]['VIDEO_PREDICTION'] = 'VIDEO_PREDICTION_OFF'
			
			#setupSimParamsList[queueIndex].append('TIME_SHIFT')
			#if self.vsOnBtn.isChecked() == 1:
				#setupSimParams[queueIndex]['TIME_SHIFT'] = self.timeShiftEdit.text().ascii()
			#else:
				#setupSimParams[queueIndex]['TIME_SHIFT'] = '0.0'
				
			#setupSimParamsList[queueIndex].append('VIDEO_DBA_TYPE')
			#if self.dbaGatedVideoBtn.isChecked() == 1:
				#setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] = 'VIDEO_DBA_GATED'
			#if self.dbaFixedVideoBtn.isChecked() == 1:
				#setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] = 'VIDEO_DBA_FIXED'
			#if self.dbaLimitedVideoBtn.isChecked() == 1:
				#setupSimParams[queueIndex]['VIDEO_DBA_TYPE'] = 'VIDEO_DBA_LIMITED_GATE'
		#if self.vtOffBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['VIDEO_TRAFFIC'] = 'VIDEO_TRAFFIC_OFF'
		#if self.grtOnBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['GRANT_TRACE'] = 'GRANT_TRACE_ON'
		#if self.grtOffBtn.isChecked() == 1:
			#setupSimParams[queueIndex]['GRANT_TRACE'] = 'GRANT_TRACE_OFF'
		#if self.schedulerMaxWinChkBox.isChecked() == 1:
			#setupSimParams[queueIndex]['SCHEDULER_MAX_WINDOW'] = '1'
		#else:
			#setupSimParams[queueIndex]['SCHEDULER_MAX_WINDOW'] = '0'
		#simhostname = self.hostEdit.text().ascii()
		#setupSimParams[queueIndex]['GUARD_TIME'] = self.grdTimeEdit.text().ascii()
		#setupSimParams[queueIndex]['TUNING_TIME'] = self.tuningTimeEdit.text().ascii()
		#setupSimParams[queueIndex]['FIXED_PROP_DELAY_VALUE'] = self.fpdValueEdit.text().ascii()
		#setupSimParams[queueIndex]['MAX_PROP_DELAY'] = self.maxPropDelayEdit.text().ascii()
		#setupSimParams[queueIndex]['NUM_RUNS'] = self.runsEdit.text().ascii()
		#setupSimParams[queueIndex]['NUM_ONU'] = self.numONUEdit.text().ascii()
		#setupSimParams[queueIndex]['NUM_HEAVY_ONU'] = self.numHvyONUEdit.text().ascii()
		#setupSimParams[queueIndex]['HEAVY_LOAD'] = self.heavyLoadEdit.text().ascii()
		#setupSimParams[queueIndex]['NUM_WDM_ONU'] = self.numWdmONUEdit.text().ascii()
		#setupSimParams[queueIndex]['NUM_UH_WDM_ONU'] = self.numUhWdmONUEdit.text().ascii()
		#setupSimParams[queueIndex]['NUM_LH_WDM_ONU'] = self.numLhWdmONUEdit.text().ascii()
		#setupSimParams[queueIndex]['LINK_SPEED'] = self.linkSpdEdit.text().ascii()
		#setupSimParams[queueIndex]['START_LOAD'] = self.startLoadEdit.text().ascii()
		#setupSimParams[queueIndex]['END_LOAD'] = self.endLoadEdit.text().ascii()
		#setupSimParams[queueIndex]['LOAD_INCR'] = self.loadIncrEdit.text().ascii()
		#setupSimParams[queueIndex]['START_LAMBDA'] = self.startLambdaEdit.text().ascii()
		#setupSimParams[queueIndex]['END_LAMBDA'] = self.endLambdaEdit.text().ascii()
		#setupSimParams[queueIndex]['SS_HURST_PARAM'] = self.hurstParamEdit.text().ascii()
		#setupSimParams[queueIndex]['NUM_SS_STREAMS'] = self.numStrmsEdit.text().ascii()
		#setupSimParams[queueIndex]['FIXED_GRANT_SIZE'] = self.fixedGrantSizeEdit.text().ascii()
		#setupSimParams[queueIndex]['MAX_GRANT_SIZE'] = self.maxGrantSizeEdit.text().ascii()
		#setupSimParams[queueIndex]['SCHEDULER_NUM_SLOT'] = self.schedulerNumSlotEdit.text().ascii()
		#setupSimParams[queueIndex]['SCHEDULER_SLOT_SIZE'] = self.schedulerSlotSizeEdit.text().ascii()
		#setupSimParams[queueIndex]['STARVE_THRESH'] = self.starveThreshEdit.text().ascii()
		#setupSimParams[queueIndex]['AVAIL_COST_WEIGHT'] = self.acwEdit.text().ascii()
		#setupSimParams[queueIndex]['NUM_PREFERRED_ONU'] = self.npoEdit.text().ascii()
		#setupSimParams[queueIndex]['SIM_TIME'] = self.simTimeEdit.text().ascii()
		#queueIndex = self.queueIndexSlotEdit.text().ascii()
		########simID = self.simIdEdit.text().ascii()
		#for iaa in range(len(setupSimParams)):
			#queueSimParams.append(setupSimParams[iaa])
			#queueSimParamsList.append(setupSimParamsList[iaa])
		#setupSimParams = []
		#setupSimParamsList = []
		simpassword = self.passwordEdit.text().ascii()
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
		if queueIndexMax < 100:
			store_parameters(self)
			restore_parameters(self)
			add_simParams()
			add_simParamsList()
			if queueIndex == queueIndexMax:
				queueIndexMax += 1
				self.indexIncreaseButton_pressed()
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
		self.loginBtn.setDown(0)
		simusername = self.usernameEdit.text().ascii()
		simpassword = self.passwordEdit.text().ascii()
		if os.path.isdir(os.path.join('/home',str(simusername))) == False:
			print 'Not a Valid Username, please Try again.' 
			self.usernameEdit.clear()
			self.passwordEdit.clear()
		else:
			ExecutePath = os.path.join('/home',str(simusername))
			os.chdir(os.path.join('/home',str(simusername)))
			simcommandfinal = os.path.join(os.path.join('/home',str(simusername)), 'ls')

			cmd = 'ssh -f -l '+str(simusername)+' '+str(simhostname)+' \'cd '+ExecutePath+'; '+simcommandfinal+' >sim_log &\''
			child = pexpect.spawn(cmd)

			# expect ssh to prompt for a user password
			child.expect(str(simusername)+'@'+str(simhostname)+'\'s' + ' password:')
			print str(simusername)+'@'+str(simhostname)+'\'s' + ' password:'
			# send the password
			child.sendline(str(simpassword))
			child.read()
			if child.isalive() == False:
				self.passwordEdit.setEnabled(False)
				self.logoutBtn.setEnabled(True)
				self.loginBtn.setEnabled(False)
				print 'Logged In Successfully'
				self.launchBtn.setEnabled(True)
			else:
				print 'Logged In Failed'
				self.usernameEdit.clear()
				self.passwordEdit.clear()
				
	def logoutBtn_pressed(self):
		self.logoutBtn.setDown(0)
		simpassword = ''
		self.passwordEdit.clear()
		self.passwordEdit.setEnabled(True)
		self.loginBtn.setEnabled(True)
		self.logoutBtn.setEnabled(False)
		self.launchBtn.setEnabled(False)
		
	def svOnBtn_checked(self):
		self.svButtonGroup.setEnabled(True)
		
	def svOffBtn_checked(self):
		self.svButtonGroup.setEnabled(False)
		
	def vtOnBtn_checked(self):
		global filename
		self.videoTraceEdit.setEnabled(True)
		self.changeTraceBtn.setEnabled(True)
		self.VideoDBABtnGroup.setEnabled(True)
		self.dbaGatedVideoBtn.setEnabled(True)
		self.dbaFixedVideoBtn.setEnabled(True)
		self.dbaLimitedVideoBtn.setEnabled(True)
		self.predictTrafficBox.setEnabled(True)
		self.FRateLbl.setEnabled(True)
		self.frameRateEdit.setEnabled(True)
		self.videoStartBox.setEnabled(True)
		self.ipactpsfBtn.setEnabled(True)
		self.scalableVideoBox.setEnabled(True)
		self.svDropThresholdEdit.setEnabled(True)
		self.svDropSensitivity.setEnabled(True)
		self.svDropStepMinBound.setEnabled(True)
		self.svDropStepMaxBound.setEnabled(True)
		self.svDropStep_NumMAValues.setEnabled(True)
		self.svDropMinBoundLabel.setEnabled(True)
		self.svDropMaxBoundLabel.setEnabled(True)
		
		
		sim_init_win.hide()
		filename = "()"
		while str(filename) == "()":
			filename = tkFileDialog.askopenfilename(title="Select a Video Trace File to be Used", initialdir=(os.path.join(path_2,"Video_Trace_Library")))
		if str(filename) != "()":
			self.videoTraceEdit.setText(filename)
		sim_init_win.show()
		
	def vtOffBtn_checked(self):
		self.videoTraceEdit.clear()
		self.videoTraceEdit.setEnabled(False)
		self.changeTraceBtn.setEnabled(False)
		self.VideoDBABtnGroup.setEnabled(False)
		self.dbaGatedVideoBtn.setEnabled(False)
		self.dbaFixedVideoBtn.setEnabled(False)
		self.dbaLimitedVideoBtn.setEnabled(False)
		self.predictTrafficBox.setEnabled(False)
		self.FRateLbl.setEnabled(False)
		self.frameRateEdit.setEnabled(False)
		self.videoStartBox.setEnabled(False)
		#if self.ipactpsfBtn.isChecked() == 1:
			#self.nascBtn.setChecked(1)
		self.ipactpsfBtn.setEnabled(False)
		self.scalableVideoBox.setEnabled(False)
		self.svDropThresholdEdit.setEnabled(False)
		self.svDropSensitivity.setEnabled(False)
		self.svDropStepMinBound.setEnabled(False)
		self.svDropStepMaxBound.setEnabled(False)
		self.svDropStep_NumMAValues.setEnabled(False)
		self.svDropMinBoundLabel.setEnabled(False)
		self.svDropMaxBoundLabel.setEnabled(False)
	
		
	def pvtOnBtn_checked(self):
		self.PredTypeLbl.setEnabled(True)
		self.PredTypeEdit.setEnabled(True)
	
	def pvtOffBtn_checked(self):
		self.PredTypeLbl.setEnabled(False)
		self.PredTypeEdit.setEnabled(False)
		
	def vsOffBtn_checked(self):
		self.timeShiftLbl.setEnabled(False)
		self.timeShiftEdit.setEnabled(False)
		
	def vsOnBtn_checked(self):
		self.timeShiftLbl.setEnabled(True)
		self.timeShiftEdit.setEnabled(True)
		
	def changeTraceBtn_pressed(self):
		sim_init_win.hide()
		newfilename = "()"
		newfilename = tkFileDialog.askopenfilename()
		if str(newfilename) == "()":
			newfilename = filename
		self.videoTraceEdit.setText(newfilename)
		sim_init_win.show()
		
	#Redefining the close even to give a message box to confirm	
	def closeEvent(self, event):
		self.cancelBtn.setDown(0)
		sim_init_win.hide()
		sim_mgr_win.show()		

	

class MainSimMgrWin (Ui_SimMgr):
#	def __init__(self, parent = None, name = "Simulation Manager", modal = 0, fl = 0):
#		Ui_SimMgr.__init__(self, parent, name, fl)
	#def __init__(self):
		#Ui_SimMgr.__init__(self)
	def __init__(self):
		super(self.__class__, self).__init__()
		print dir(self)
		self.setupUi(self)
		
	def languageChange(self):
		Ui_SimMgr.languageChange(self)
		self.simListBox.clear()
		self.notStartedListBox.clear()
		self.startedListBox.clear()
	def quitButton_pressed(self):
#   	simdatafile = open('sim_mgr_data','w')
#   	marshal.dump(sims,simdatafile)
#   	simdatafile.close()
		os.chdir(os.path.join(os.path.join('/home', str(simusername)), str(simhomedir_2)))
		print '1'
		simpicklefile = open('sim_mgr_data','w')
		print '2'
		pickler = pickle.Pickler(simpicklefile)
		print '3'
		pickler.dump(sims)
		print '4'
		simpicklefile.close()
		print 'Finished Pickle: simpicklefile'
		plotSettingsPicklefile = open('plot_settings_data','w')
		print '5'
		pickler = pickle.Pickler(plotSettingsPicklefile)
		print '6'
		pickler.dump(plotSettings)
		print '7'
		plotSettingsPicklefile.close()
		print 'Finished Pickle: plotSettings'
		sys.exit()
	def newSimButton_pressed(self):
		self.newSimButton.setDown(0)
		global simhostname
		sim_mgr_win.hide()
		restore_parameters(sim_init_win);
		#if simParams['SCALABLE_VIDEO_TRAFFIC'] == 'SCALABLE_VIDEO_OFF':
			#sim_init_win.svOffBtn.setChecked(1)
		#if simParams['SCALABLE_VIDEO_TRAFFIC'] == 'SCALABLE_VIDEO_ON':
			#sim_init_win.svOnBtn.setChecked(1)
		#if simParams['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_OFF':
			#sim_init_win.svDropMethod0.setChecked(1)
		#if simParams['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_METHOD_1':
			#sim_init_win.svDropMethod1.setChecked(1)
		#if simParams['SCALABLE_VIDEO_DROPPING_ALGORITHM'] == 'SCALABLE_VIDEO_DROPPING_METHOD_2':
			#sim_init_win.svDropMethod2.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_NASC':
			#sim_init_win.nascBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_IPACT':
			#sim_init_win.ipactBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_LEAST_ASSIGNED':
			#sim_init_win.leastAssignedBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_APS':
			#sim_init_win.apsBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_LFJ':
			#sim_init_win.lfjBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_LFJ_LPT':
			#sim_init_win.lfjlptBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_LFJ_SPT':
			#sim_init_win.lfjsptBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_LFJ_LNF':
			#sim_init_win.lfjlnfBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_EAF':
			#sim_init_win.eafBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_EAAF':
			#sim_init_win.eaafBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_SPD':
			#sim_init_win.spdBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_LPD':
			#sim_init_win.lpdBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_SPD_LPT':
			#sim_init_win.spdLptBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_LFJ_LPT':
			#sim_init_win.intvlLfjlptBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_LFJ_SPT':
			#sim_init_win.intvlLfjsptBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_LFJ_LNF':
			#sim_init_win.intvlLfjlnfBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_EAF':
			#sim_init_win.intvlEafBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_INTERVAL_EAAF':
			#sim_init_win.intvlEaafBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_JIT_LFJ_LPT':
			#sim_init_win.jitLfjlptBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_JIT_LFJ_SPT':
			#sim_init_win.jitLfjsptBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_JIT_LFJ_LNF':
			#sim_init_win.jitLfjlnfBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_JIT_EAF':
			#sim_init_win.jitEafBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_JIT_EAAF':
			#sim_init_win.jitEaafBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_JIT_SPD':
			#sim_init_win.jitSpdBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_JIT_LPD':
			#sim_init_win.jitLpdBtn.setChecked(1)
		#if simParams['OLT_TYPE'] == 'OLT_ONLINE_JIT_TEST':
			#sim_init_win.jitTestBtn.setChecked(1)
		#if simParams['DBA_TYPE'] == 'DBA_GATED':
			#sim_init_win.dbaGatedBtn.setChecked(1)
		#if simParams['DBA_TYPE'] == 'DBA_FIXED':
			#sim_init_win.dbaFixedBtn.setChecked(1)
		#if simParams['DBA_TYPE'] == 'DBA_LIMITED_GATE':
			#sim_init_win.dbaLimitedBtn.setChecked(1)
		#if simParams['DBA_TYPE'] == 'DBA_EXCESS':
			#sim_init_win.dbaExcessBtn.setChecked(1)
		#if simParams['TRAFFIC_TYPE'] == 'TRAFFIC_POISSON':
			#sim_init_win.pnBtn.setChecked(1)
		#if simParams['TRAFFIC_TYPE'] == 'TRAFFIC_SELF_SIMILAR':
			#sim_init_win.ssBtn.setChecked(1)
		#if simParams['WDM_TYPE'] == 'WDM_FIXED':
			#sim_init_win.fixedBtn.setChecked(1)
		#if simParams['WDM_TYPE'] == 'WDM_TUNABLE':
			#sim_init_win.tunableBtn.setChecked(1)
		#if simParams['FIXED_PROP_DELAY'] == 'FIXED_PROP_DELAY_ON':
			#sim_init_win.fpdOnBtn.setChecked(1)
		#if simParams['FIXED_PROP_DELAY'] == 'FIXED_PROP_DELAY_OFF':
			#sim_init_win.fpdOffBtn.setChecked(1)
		#if simParams['GET_TAIL'] == 'GET_TAIL_ON':
			#sim_init_win.gtOnBtn.setChecked(1)
		#if simParams['GET_TAIL'] == 'GET_TAIL_OFF':
			#sim_init_win.gtOffBtn.setChecked(1)
		#if simParams['SIM_TRACE'] == 'SIM_TRACE_ON':
			#sim_init_win.ttOnBtn.setChecked(1)
		#if simParams['SIM_TRACE'] == 'SIM_TRACE_OFF':
			#sim_init_win.ttOffBtn.setChecked(1)
		#if simParams['GRANT_TRACE'] == 'GRANT_TRACE_ON':
			#sim_init_win.grtOnBtn.setChecked(1)
		#if simParams['GRANT_TRACE'] == 'GRANT_TRACE_OFF':
			#sim_init_win.grtOffBtn.setChecked(1)
		#if simParams['SCHEDULER_MAX_WINDOW'] == '1':
			#sim_init_win.schedulerMaxWinChkBox.setChecked(1)
		#else:
			#sim_init_win.schedulerMaxWinChkBox.setChecked(0)
		#sim_init_win.hostEdit.setText(simhostname)
		#sim_init_win.grdTimeEdit.setText(simParams['GUARD_TIME'])
		#sim_init_win.tuningTimeEdit.setText(simParams['TUNING_TIME'])
		#sim_init_win.fpdValueEdit.setText(simParams['FIXED_PROP_DELAY_VALUE'])
		#sim_init_win.maxPropDelayEdit.setText(simParams['MAX_PROP_DELAY'])
		#sim_init_win.numONUEdit.setText(simParams['NUM_ONU'])
		#sim_init_win.runsEdit.setText(simParams['NUM_RUNS'])
		#sim_init_win.numHvyONUEdit.setText(simParams['NUM_HEAVY_ONU'])
		#sim_init_win.heavyLoadEdit.setText(simParams['HEAVY_LOAD'])
		#sim_init_win.numWdmONUEdit.setText(simParams['NUM_WDM_ONU'])
		#sim_init_win.numUhWdmONUEdit.setText(simParams['NUM_UH_WDM_ONU'])
		#sim_init_win.numLhWdmONUEdit.setText(simParams['NUM_LH_WDM_ONU'])
		#sim_init_win.linkSpdEdit.setText(simParams['LINK_SPEED'])
		#sim_init_win.startLoadEdit.setText(simParams['START_LOAD'])
		#sim_init_win.endLoadEdit.setText(simParams['END_LOAD'])
		#sim_init_win.loadIncrEdit.setText(simParams['LOAD_INCR'])
		#sim_init_win.startLambdaEdit.setText(simParams['START_LAMBDA'])
		#sim_init_win.endLambdaEdit.setText(simParams['END_LAMBDA'])
		#sim_init_win.hurstParamEdit.setText(simParams['SS_HURST_PARAM'])
		#sim_init_win.numStrmsEdit.setText(simParams['NUM_SS_STREAMS'])
		#sim_init_win.fixedGrantSizeEdit.setText(simParams['FIXED_GRANT_SIZE'])
		#sim_init_win.maxGrantSizeEdit.setText(simParams['MAX_GRANT_SIZE'])
		#sim_init_win.schedulerNumSlotEdit.setText(simParams['SCHEDULER_NUM_SLOT'])
		#sim_init_win.schedulerSlotSizeEdit.setText(simParams['SCHEDULER_SLOT_SIZE'])
		#sim_init_win.starveThreshEdit.setText(simParams['STARVE_THRESH'])
		#sim_init_win.acwEdit.setText(simParams['AVAIL_COST_WEIGHT'])
		#sim_init_win.npoEdit.setText(simParams['NUM_PREFERRED_ONU'])
		#sim_init_win.simTimeEdit.setText(simParams['SIM_TIME'])
		#sim_init_win.queueIndexSlotEdit.setText(str(queueIndex))
		sim_init_win.usernameEdit.setText(simusername)
		sim_init_win.usernameEdit.setEnabled(False)
		# del simParamsList[:]
		# initialize_data_structure()
		sim_init_win.show()
		
	def viewSimButton_pressed(self):
		wait_win.waitProgressBar.setPercentageVisible(1)
		wait_win.waitProgressBar.setTotalSteps(5)
		wait_win.waitProgressBar.setProgress(0)
		wait_win.show()
		self.hide()
		self.viewSimButton.setDown(0)
		Selection = False
		for loopIdx in range(self.simListBox.count()):
			if self.simListBox.isSelected(loopIdx) == 1:
				simIdx = loopIdx
				Selection = True
		if Selection:
			simID = self.simListBox.item(simIdx).text().ascii()
			# Clear list box
			sim_view_win.simOutputListBox.clear()
		
			os.chdir(path)
			if os.path.exists(simID) == 1:
				os.chdir(simID)
			wait_win.waitProgressBar.setProgress(1)
			# Check process ID file
			if os.path.exists('pid') == 1:
				pidFile = open('pid','r')
				pidStr = pidFile.readline()
				if pidStr == 'done\n':
					sim_view_win.simStatusLbl.setText('Completed')
				else:
					if pidStr == 'Failed\n':
						sim_view_win.simStatusLbl.setText('Failed')
					else:
						sim_view_win.simStatusLbl.setText('Running: '+pidStr)
			simData = sims[simID]
			sim_view_win.simIDEdit.setText(simID)
			sim_view_win.hostEdit.setText(simData['host'])
			wait_win.waitProgressBar.setProgress(3)
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
					sim_view_win.simOutputListBox.insertItem(filename)
				filename = filedir.readline()
			os.chdir('..')
			wait_win.waitProgressBar.setProgress(5)
			wait_win.hide()
			sim_view_win.show()
		else:
			wait_win.waitProgressBar.setProgress(5)
			wait_win.hide()
			sim_mgr_win.show()
			print "No valid Selection for a Simulation ID to be viewed, Please Try again."
			
	def consolidateBtn_pressed(self):
		wait_win.show()
		self.consolidateBtn.setDown(0)
		global simParams
		simList = []
		for loopIdx in range(self.simListBox.count()):
			if self.simListBox.isSelected(loopIdx) == 1:
				# Add simulation to list
				simList.append(self.simListBox.item(loopIdx).text().ascii())
		# Create a consolidated pseudo-simulation
		if self.consolidateNameEdit.text().ascii() == '':
			self.consolidateNameEdit.setText('consolidated')
		consolidatedName = self.consolidateNameEdit.text().ascii()
		if sims.has_key(consolidatedName) == 1:
			del sims[consolidatedName]
		simData['host'] = 'null'
		simData['pid'] = 0
		simData['params'] = copy.deepcopy(simParams)
		simID = consolidatedName
		sims[simID] = copy.deepcopy(simData)
		if os.path.exists(consolidatedName) == 1:
			os.system('rm -rf '+consolidatedName)
		os.mkdir(consolidatedName)
		# copy files to consolidated directory
		for loopIdx in range(len(simList)):
			dirStr = simList[loopIdx]
			os.system('cp '+dirStr+'/* '+consolidatedName)
		self.simListBox.insertItem(consolidatedName)
		wait_win.hide()
	
	def addSimButton_pressed(self):
		wait_win.show()
		self.addSimButton.setDown(0)
		global simParams
		simList = []
		os.chdir(path)

		# Add the simulation directory
		if self.consolidateNameEdit.text().ascii() == '':
			self.consolidateNameEdit.setText('new_sim')
		addSimName = self.consolidateNameEdit.text().ascii()
		
		if os.path.exists(addSimName) == 0:
			os.mkdir(addSimName)
		
		if sims.has_key(addSimName) == 1:
			del sims[addSimName]
		simData['host'] = 'null'
		simData['pid'] = 0
		simData['params'] = copy.deepcopy(simParams)
		simID = addSimName
		sims[simID] = copy.deepcopy(simData)
		self.simListBox.insertItem(addSimName)
		wait_win.hide()
	
	def removeSimButton_pressed(self):
		wait_win.show() 
		app.processEvents(0)
		self.removeSimButton.setDown(0)
		for loopIdx in range(self.simListBox.count())[::-1]:
			if self.simListBox.isSelected(loopIdx) == 1:
				# Remove selected simulation
				selectedSimID = self.simListBox.item(loopIdx).text().ascii()
				self.simListBox.removeItem(loopIdx)
				os.chdir(path)
				if self.removeDirCheckBox.isChecked() == 1:
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
								#child.expect(str(simusername)+'@'+str(simData['host'])+'\'s' + ' password:')
								#print str(simusername)+'@'+str(simData['host'])+'\'s' + ' password:'
								## send the password
								#child.sendline(sim_init_win.passwordEdit.text().ascii())
								#child.read()
								#child.kill(0)
								#shutil.rmtree(os.getcwd())
								#print selectedSimID + ' was Stopped and Deleted'
						else:
							os.system('rm -rf '+selectedSimID)
				
				del sims[selectedSimID]
		self.removeDirCheckBox.setChecked(0)
		time.sleep(0.05)
		wait_win.hide()
	
	def haltSimBtn_pressed(self):
		#self.haltSimBtn.setDown(0)
		for loopIdx in range(self.startedListBox.count()):
			if self.startedListBox.isSelected(loopIdx) == 1:
				# Halt selected simulation
				selectedSimID = self.startedListBox.item(loopIdx).text().ascii()
				os.chdir(path)
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
		for loopIdx in range(self.simListBox.count())[::-1]:
			if self.simListBox.isSelected(loopIdx) == 1:
				selectedSimID = self.simListBox.item(loopIdx).text().ascii()
				os.chdir(path)
				if os.path.exists(selectedSimID) == 1:
					os.chdir(selectedSimID)
					os.system('xdg-open ' + os.getcwd())
				
	def simListBox_doubleClicked(self,selectedItem):
		selectedSimID = selectedItem.text().ascii()
		print selectedSimID


app = QApplication(sys.argv)
sim_mgr_win = MainSimMgrWin()
sim_init_win = SimInitWin()
sim_view_win = SimViewWin()
wait_win = WaitWin()
plot_name_win = PlotNameWin()
app.setMainWidget(sim_mgr_win)
load_sim_data()
load_plot_settings()
sim_mgr_win.show()
app.exec_loop()
