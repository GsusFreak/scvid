

frameRate = 24 #frames per second
frameNum = 30000 + 1 #add the zeroth frame
enhancementLayers = 3
numOfPacketsPerFrame = 10

text = ''
for iaa in range(3):
	text += '# '
	for ibb in range(65):
		text += '-'
	text += '\n'

for frame in range(frameNum):
	for layer in range(enhancementLayers):
		for pack in range(numOfPacketsPerFrame):
			packet = pack + 1
			text += '\t\t'
			text += str(frame)
			text += '\t\t'
			text += str(int(round((1000/frameRate)*frame)))
			text += '\t\t'
			if [0].count(frame%16) == 1:
				text += 'I\t\t'
			if [4, 8, 12].count(frame%16) == 1:
				text += 'P\t\t'
			if [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15].count(frame%16) == 1:
				text += 'B\t\t'
			if packet is numOfPacketsPerFrame:
				#text += str(1000 + 10*frame - 58)
				text += str(1010)
			else:
				text += '1460'
			text += '\t\t58\t\t'
			if packet is numOfPacketsPerFrame:
				text += '1\t\t'
			else:
				text += '0\t\t'
			text += str(layer)
			text += '\n'
	
myFile = open('Test_Trace_1.txt', 'w')
myFile.write(text)
myFile.close()
