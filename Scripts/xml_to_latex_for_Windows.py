# Please not that this script is for Windows only!!!

import os
import xml.etree.ElementTree as ET

cwd = os.getcwd()

fileNameList = []
trees = []
roots = []
latexOut = []
stylesList = []

o = "{urn:schemas-microsoft-com:office:office}"
x = "{urn:schemas-microsoft-com:office:excel}"
ss = "{urn:schemas-microsoft-com:office:spreadsheet}"

for file in os.listdir(cwd):
	if os.path.isfile(cwd + '\\' + file):
		fyleBreakdown = file.split('.')
		if file != 'xml_to_latex.py' and file != '' and fyleBreakdown[1] == 'xml':
			fileNameList.append(cwd + '\\' + file)

# print 'Files in the current directory:'
# for file in fileNameList:
	# print file

for iaa in range(len(fileNameList)):
	#.xml to Data Structure Converter

	numRows = 0
	numCols = 0
	sheetName = ''
	data = []
	styles = []
	emptyDict = {'value': '', 'style': ''}
	emptyStr = ''
	#	Format is (isBold, isItalics)		'styleID': ['0', '0']
	emptyStylesDict = {}
	newRows = []
	trees.append(ET.parse(fileNameList[iaa]))
	roots.append(trees[iaa].getroot())
	for item in roots[iaa].iter(ss + 'Worksheet'):
		sheetName = item.get(ss + 'Name')
		print 'Name of file: ' + sheetName
	for item in roots[iaa].iter(ss + 'Table'):
		numCols = item.get(ss + 'ExpandedColumnCount')
		numRows = item.get(ss + 'ExpandedRowCount')
		print 'Number of columns: {}'.format(numCols)
		print 'Number of rows: {}'.format(numRows)
		print '\n'
	
	emptyRow = []
	for row in range(int(numRows)):
		data.append(emptyRow[:])
		for col in range(int(numCols)):
			data[row].append(emptyStr[:])
	for row in range(int(numRows)):
		styles.append(emptyRow[:])
		for col in range(int(numCols)):
			styles[row].append(emptyStr[:])
	iaaRows = 0
	for row in roots[iaa].iter(ss + 'Row'):
		# rows.append(row)
		iaaCols = 0
		for cell in row.findall(ss + 'Cell'):
			styles[iaaRows][iaaCols] = cell.get(ss + 'StyleID')
			for dataField in cell.findall(ss + 'Data'):
				data[iaaRows][iaaCols] = dataField.text
			iaaCols += 1
		iaaRows += 1
	
	stylesList.append(emptyStylesDict)
	for style in roots[iaa].iter(ss + 'Style'):
		styleID_1 = style.get(ss + 'ID')
		stylesList[iaa][styleID_1] = ['0', '0']
		font = style.find(ss + 'Font')
		if font == None:
			stylesList[iaa][styleID_1][0] = None
			stylesList[iaa][styleID_1][1] = None
		else:
			stylesList[iaa][styleID_1][0] = font.get(ss + 'Bold')
			stylesList[iaa][styleID_1][1] = font.get(ss + 'Italic')
	# print stylesList, '\n'
	# for neighbor in roots[iaa].iter():
		# print neighbor.tag, neighbor.attrib, neighbor.text
		# print '\n'
	
	# # Remove any blank data entries
	# for row in data:
		# for point in row:
			# if point == '':
				# row.remove(point)
	print data, '\n'
	print styles, '\n'
	print stylesList[iaa], '\n'
	
	
	# Data structure to Latex Table Converter
	latexOut.append('')
	latexOut[iaa] += ''
	
	startStr = '\\begin{table*}[!t]\n% increase row spacing, adjust to taste\n'
	startStr += '\\renewcommand{\\arraystretch}{1.2}\n'
	startStr += '\\caption{Caption1}\n'
	startStr += '\\label{tab:Label1}\n'
	startStr += '\\centering\n'
	startStr += '\\begin{tabular}{|'
	for ibb in range(int(numCols)):
		startStr += 'c|'
	startStr += '}\n\\hline\n'
	latexOut[iaa] += startStr
	
	for icc in range(int(numRows)):
		for idd in range(int(numCols)):
			if styles[icc][idd] == None or styles[icc][idd] == '':
				styles[icc][idd] = 'Default'
			if stylesList[iaa][styles[icc][idd]][0] == '1':
				data[icc][idd] = '\\textbf{' + data[icc][idd] + '}'
			if stylesList[iaa][styles[icc][idd]][1] == '1':
				data[icc][idd] = '\\textit{' + data[icc][idd] + '}'
			data[icc][idd] = data[icc][idd].replace('_', ' ')
	
	iaaNewRows = 0
	for row in range(int(numRows)):
		newRows.append(emptyRow[:])
		newRows[iaaNewRows] = ' & '.join(data[iaaNewRows])
		iaaNewRows += 1
	joinStr = ' \\\\ \\cline{1-'+ str(numCols) + '}\n\\hline\n'
	latexOut[iaa] += joinStr.join(newRows)
	endStr = ' \\\\ \\cline{1-' + str(numCols) + '}\n\\hline\n\\end{tabular}\n\\end{table*}\n'
	latexOut[iaa] += endStr
	
	print latexOut[iaa]
	
	tempList = fileNameList[iaa].split('.')
	tempList[1] = 'txt'
	fileNameList[iaa] = '.'.join(tempList)
	fyle = open(fileNameList[iaa], 'w')
	fyle.write(latexOut[iaa])
	fyle.close()
	
	
	