"""
Extract_Results.py

This script extracts the relevent data from all of the simulation
result folders in the current working directory, moves it to a new
folder called Results, and renames the files to reflect which
simulation they came from.

If the Results folder is already present, the script will not do
anthing. Additional files in the current working directory
should not mess anything up, but additional folders (especially
the Results folder) certainly have the potential to mess things
up. 

v1.0 -- 2017-01-01


"""


import os
import shutil

cwd = os.getcwd()
flag = 0

#If there is not already a folder to store the results in, make one.
resultsDir = cwd + '/Results'
if not os.path.isdir(resultsDir):
	os.mkdir('Results')
else:
	flag = 1

if flag != 1:
	dirList = []
	
	#This section makes a list of the current subdirectories.
	for item in os.listdir(cwd):
		if os.path.isdir(cwd + '/' + item):
			if item not in 'Results':
				dirList.append(cwd + '/' + item)

	for subDir in dirList:
		#This section makes a list of files in each subdirectory.
		subdirFileList = []
		for item in os.listdir(subDir):
			if os.path.isfile(subDir + '/' + item):
				subdirFileList.append(item)

		#This section picks out the files that are unwanted.
		markedForDelete = []
		for iaa in subdirFileList:
			if '_xl' in iaa:
				markedForDelete.append(iaa)
			elif 'od_pn_vid' in iaa:
				pass
			elif 'vod_pn_vid' in iaa:
				pass
			elif 'vods_pn_vid' in iaa:
				pass
			else:
				markedForDelete.append(iaa)

		#This section deletes the files that are unwanted.
		for iaa in markedForDelete:
			subdirFileList.remove(iaa)

		#This section copies each file, renames it, and
		#moves it to the results directory.
		for iaa in subdirFileList:
			shutil.copy2(subDir + '/' + iaa, resultsDir + '/' + iaa)
			
			#if 'BluePlanet_' in subDir:
				#title = 'BP'
			#elif 'FindingNeverland_' in subDir:
				#title = 'FNL'
			#elif 'HarryPotter_' in subDir:
				#title = 'HP'
			#elif 'LakeHouse_' in subDir:
				#title = 'LH'
			#elif 'Speed_' in subDir:
				#title = 'Sp'
			#else:
				#title = '--'

			#if '_Q20_' in subDir:
				#Q = '20'
			#elif '_Q25_' in subDir:
				#Q = '25'
			#elif '_Q30_' in subDir:
				#Q = '30'
			#elif '_Q35_' in subDir:
				#Q = '35'
			#elif '_Q40_' in subDir:
				#Q = '40'
			#elif '_Q45_' in subDir:
				#Q = '45'
			#else:
				#Q = '--'
			
			junk, folderName = os.path.split(subDir)
			
			os.chdir(resultsDir)
			replaceString = folderName + '_pn_vid'
			# print replaceString
			# for fileName in os.listdir("."):
				# if '_Q' not in fileName:
			os.rename(iaa, iaa.replace("pn_vid", replaceString))
			os.chdir(cwd)





