"""
Export_Results_to_Excel.py
v2 is not compatible with v1 simulations.

"""


import os
import shutil
# import tablib
import datetime
import copy

#def csv2list(addr):
	#fyle2 = open(addr, 'r')
	#whole_fyle.read(fyle2)
	#half_blob = whole_fyle.split('\n')
	#blob_length = len(half_blob)
	#fyle2.close()
	
	#full_blob = [None] * blob_length
	#fyle = open(addr, 'r')
	#line = fyle.readline()
	#if bug_strings.count(line) != 1:
		#full_blob[iaa] = half_blob[iaa].split(',')
	#fyle.close()
	#return full_blob
	
def csv2list(addr):
	addr = open(addr, 'r')
	fyle = addr.read()
	addr.close()
	half_blob = fyle.split('\n')
	full_blob = []
	for line in half_blob[::-1]:
		if bug_strings.count(line) == 1:
			half_blob.remove(line)
	blob_length = len(half_blob)
	full_blob = [None] * blob_length
	for iaa in range(blob_length):
		full_blob[iaa] = half_blob[iaa].split(',')
	return full_blob




cwd = os.getcwd()
flag = 0
bug_strings = ['\t', '\t\n', '\n', '\r', ' ', '']

#If there is not already a folder to store the results in, make one.
resultsDir = cwd + '/Results'
if not os.path.isdir(resultsDir):
	os.mkdir('Results')
else:
	flag = 1

if flag != 1:
	dirList = []
	files = {}
	fileNames = []
	fyleInfo = {}
	packet_drop_dict = {}
	length = {}
	size = {}
	
	#This section makes a list of the current subdirectories.
	for item in os.listdir(cwd):
		if os.path.isdir(cwd + '/' + item):
			if item != 'Results':
				dirList.append(cwd + '/' + item)

	for subDir in dirList:
		
		#Add this simulation's dropped_packets file to the dictionary
		temp = subDir.split('/')
		packet_drop_dict[temp[-1]] = {}
		packet_drop_dict[temp[-1]]['util_length'] = {}
		packet_drop_dict[temp[-1]]['util_size'] = {}
		packet_drop_dict[temp[-1]]['blob'] = csv2list(subDir + '/' + 'A_Dropped_Scalable_Packets')
		packet_drop_dict[temp[-1]]['overall_length'] = len(packet_drop_dict[temp[-1]]['blob'])
		util_list = ['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9']
		if packet_drop_dict[temp[-1]]['overall_length'] > 0:
			overall_size = 0
			for util in util_list:
				packet_drop_dict[temp[-1]]['util_length'][util] = 0
				packet_drop_dict[temp[-1]]['util_size'][util] = 0
			for line in packet_drop_dict[temp[-1]]['blob']:
				overall_size += int(line[2])
				for util in util_list:
					if util == line[-1]:
						packet_drop_dict[temp[-1]]['util_length'][util] += 1
						packet_drop_dict[temp[-1]]['util_size'][util] += int(line[2])
			for util in util_list:
				if packet_drop_dict[temp[-1]]['util_length'][util] != 0:
					packet_drop_dict[temp[-1]]['util_size'][util] /= packet_drop_dict[temp[-1]]['util_length'][util]
				else:
					packet_drop_dict[temp[-1]]['util_size'][util] = 0
			if packet_drop_dict[temp[-1]]['overall_length'] != 0:
				packet_drop_dict[temp[-1]]['overall_size'] = overall_size / packet_drop_dict[temp[-1]]['overall_length']
			else:
				packet_drop_dict[temp[-1]]['overall_size'] = 0
		else:
			for util in util_list:
				packet_drop_dict[temp[-1]]['util_length'][util] = 0
				packet_drop_dict[temp[-1]]['util_size'][util] = 0
			packet_drop_dict[temp[-1]]['overall_size'] = 0
		del packet_drop_dict[temp[-1]]['blob']

		##Add this simulation's dropped_packets file to the dictionary
		#temp = subDir.split('/')
		#packet_drop_dict[temp[-1]] = {}
		#packet_drop_dict[temp[-1]]['blob'] = csv2list(subDir + '/' + 'A_Dropped_Scalable_Packets')
		#packet_drop_dict[temp[-1]]['overall_length'] = len(packet_drop_dict[temp[-1]]['blob'])
		#util_list = ['0.1','0.2','0.3','0.4','0.5','0.6','0.7','0.8','0.9']
		#if packet_drop_dict[temp[-1]]['overall_length'] > 0:
			#overall_size = 0
			#for util in util_list:
				#length[util] = 0
				#size[util] = 0
			#for line in packet_drop_dict[temp[-1]]['blob']:
				#overall_size += int(line[2])
				#for util in util_list:
					#if util == line[-1]:
						#length[util] += 1
						#size[util] += int(line[2])
			#for util in util_list:
				#size[util] /= length[util]
			#packet_drop_dict[temp[-1]]['overall_size'] = overall_size / packet_drop_dict[temp[-1]]['overall_length']
		#else:
			#for util in util_list:
				#length[util] = 0
				#size[util] = 0
			#packet_drop_dict[temp[-1]]['overall_size'] = 0
		#del packet_drop_dict[temp[-1]]['blob']
		#packet_drop_dict[temp[-1]]['util_length'] = length
		#packet_drop_dict[temp[-1]]['util_size'] = size

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
			junk, folderName = os.path.split(subDir)
			temp = iaa.split('_')
			fyle = open(subDir + '/' + iaa, 'r')
			files[temp[0] + '_' + folderName] = fyle.read()
			fileNames.append(temp[0] + '_' + folderName)
	
	# Convert files to .csv format
	odFile = []
	vodFile = []
	vodsFile = []
	os.chdir(resultsDir)
	for fileName in fileNames:
		blob = files[fileName]
		lines = blob.split('\n')
		firstEntry = []
		fileNameParts = fileName.split('_')
		newFileName = []
		firstEntry.append(fileNameParts[0])
		for part in fileNameParts[1::]:
			newFileName.append(part)
		firstEntry.append('_'.join(newFileName))
		firstEntry[1].replace(',','.')
		for line in lines:
			if bug_strings.count(line) == 1:
				lines.remove(line)
		for line in lines:
			expandedLine = line.split(' ')
			firstEntry.append(expandedLine[1])
		if firstEntry[0] == 'od':
			if packet_drop_dict[firstEntry[1]] != []:
				firstEntry.append(' ')
				firstEntry.append(' ')
				for util in util_list:
					firstEntry.append(str(packet_drop_dict[firstEntry[1]]['util_length'][util]))
				firstEntry.append(str(packet_drop_dict[firstEntry[1]]['overall_length']))
				firstEntry.append(' ')
				firstEntry.append(' ')
				for util in util_list:
					firstEntry.append(str(packet_drop_dict[firstEntry[1]]['util_size'][util]))
				firstEntry.append(str(packet_drop_dict[firstEntry[1]]['overall_size']))
		if firstEntry[0] == 'od':
			odFile.append(','.join(firstEntry[1::]))
		if firstEntry[0] == 'vod':
			vodFile.append(','.join(firstEntry[1::]))
		if firstEntry[0] == 'vods':
			vodsFile.append(','.join(firstEntry[1::]))
		
		#newBlob = ','.join(firstEntry)
		#fyle = open(fileName, 'w')
		#fyle.write(newBlob)
		#fyle.close()
	
	odFile.sort()
	vodFile.sort()
	vodsFile.sort()
	
	all_data = []
	all_data.append('od:,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9, ,Num Packets:,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,Total, ,Avg Pkt Size:,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,Total')
	for line in odFile:
		all_data.append(line)
	all_data.append(' ')
	all_data.append('vod:,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9')
	for line in vodFile:
		all_data.append(line)
	all_data.append(' ')
	all_data.append('vods:,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9')
	for line in vodsFile:
		all_data.append(line)
	
	final_all_data = '\n'.join(all_data)
	todaysDate = datetime.datetime.now().strftime ("%Y-%m-%d")
	fyle = open('data_' + todaysDate + '.csv', 'w')
	fyle.write(final_all_data)
	fyle.close()
	
	odFile.insert(0, 'simulation,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9')
	vodFile.insert(0, 'simulation,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9')
	vodsFile.insert(0, 'simulation,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9')
	
	finalODFile = '\n'.join(odFile)
	fyle = open('odFile.csv', 'w')
	fyle.write(finalODFile)
	fyle.close()
	finalVODFile = '\n'.join(vodFile)
	fyle = open('vodFile.csv', 'w')
	fyle.write(finalVODFile)
	fyle.close()
	finalVODSFile = '\n'.join(vodsFile)
	fyle = open('vodsFile.csv', 'w')
	fyle.write(finalVODSFile)
	fyle.close()
	
	
	#od_tablib_data = tablib.Dataset()
	#vod_tablib_data = tablib.Dataset()
	#vods_tablib_data = tablib.Dataset()

	#od_tablib_data = tablib.Dataset().load(open('odFile.csv').read())
	#vod_tablib_data = tablib.Dataset().load(open('vodFile.csv').read())
	#vods_tablib_data = tablib.Dataset().load(open('vodsFile.csv').read())
	
	#all_data = tablib.Dataset()
	## all_data = tablib.Databook((od_tablib_data, vod_tablib_data, vods_tablib_data))
	#all_data.append(['od:', '', '', '', '', '', '', '', '', ''])
	#for row in od_tablib_data:
		#all_data.append(row)
	#all_data.append(['', '', '', '', '', '', '', '', '', ''])
	#all_data.append(['vod:', '', '', '', '', '', '', '', '', ''])
	#for row in vod_tablib_data:
		#all_data.append(row)
	#all_data.append(['', '', '', '', '', '', '', '', '', ''])
	#all_data.append(['vods:', '', '', '', '', '', '', '', '', ''])
	#for row in vods_tablib_data:
		#all_data.append(row)
	
	#todaysDate = datetime.datetime.now().strftime ("_%Y-%m-%d")
	#fyle = open('data' + todaysDate +'.xlsx', 'w')
	#fyle.write(all_data.xlsx)
	#fyle.close()




