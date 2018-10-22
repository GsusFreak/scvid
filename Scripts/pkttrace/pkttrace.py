#!/usr/bin/python

#
# Georgia Southern University Network Research Laboratory
#
# Title: Video trace to Packet trace converter
#
# Description: This script converts the following video trace file formats: mp4new, mp4fgs, mp4, and h263/h261 from the Arizona State 
#              University Video Trace library(http://trace.eas.asu.edu) into packet traces using the following encapsulation 
#              protocols: tcp,http,udp,rtp,rtmp
#
# Authors: Rami Haddad
#
# Version: 1.5
#
# Date: 9/17/2014
# 

import sys
import glob
import os
import math

#header sizes
rtpHeaderSize=12
rtmpHeaderSize=0
rtmpChunkSize=128	# default RTMP chunk size (feel free to modify it)
udpHeaderSize=8
ipV4HeaderSize=20
ipV6HeaderSize=40
tcpHeaderSize = 20

#you really need to change this
#value to accomodate for whatever
#application you're using
#The value of 381 was derived from
#http://dev.opera.com/articles/view/mama-http-headers-report/
httpHeaderSize = 381

#the ethernet header size
#includes cost of checksum
ethernetHeaderSize=18

#MTU size
mtuSize=1500

#
# Function name: main
#
# Description: Entry point.  Reads command line arguments and sets
#              the encapsulation parameters accordingly.  Calls
#		encapsulation routines on a file or group of files
#
# Inputs: None
#
# Outputs: None
#
#
def main():

		for argument in sys.argv:
			if argument == "-help":
				print("")
				print("Usage: pkttrace -t={mp4new, mp4fgs, mp4, h263, h261} -p={tcp, rtp, rtmp, udp, http} -enet={on, off} inputfile outputfile") 
				print("")
				sys.exit(0)

		# If no arguments were given, print a helpful message
		if len(sys.argv) <= 3:
			print("")
			print("Usage: pkttrace -p={tcp, rtp, rtmp, udp, http} -enet={on, off} input output")
			print("")
			print("                     For More usage help use: pkttrace -help")
			print("")
			sys.exit(0)


		#enumeration switch
		useEnum = 0
		#RTMP Chunk Size Flag
		csFlag = 0
		# Flag indicating the first video packet
		firstpkt = 1
		#trace format switch
		tFormat=""
		#encapsulation method switch
		eMethod=""
		#ethernet encapsulation switch
		enet=""
		#RTMP chunk size
		chunkSize=rtmpChunkSize
		#switch to use the glob library
		useGlob = None
		#appendation switch
		globAppend= None
		#default path for glob searching is
		#current directory
		globPath = "./"
		#mss size to be calculated
		mss=0
		#header and footer overhead to be calculated
		overhead=0
		#encapsulation info string
		encapInfo=""
		#list of files to grind
		fileList = []		
		CleanList = []
		
		#output File list
		outfileList = []
		
		programList = []
		
		#list of specified encapsulated files to
		#use for size determination
		encapFileList = []
		#overhead for the application layer
		appLayerOverhead = 0
		tsScalar = float(1)
		prediction = False
		
		#input/output trace name switch
		input = True
		
		
		#process arguments
		for argument in sys.argv:
			#check for .txt,.data,.dat extension on argument
			if argument[len(argument)-6:len(argument)] == ".encap" and input:
				encapFileList.append(argument)
			elif argument[len(argument)-3:len(argument)] == ".py":
				programList.append(argument)
			#check for glob switch
			elif argument == "-g":
				useGlob = 1
			#check for enumeration argument
			elif argument == "-n":
				useEnum = 1
			#change the glob search path if specified
			elif argument[0:4] == "-gp=":
				globPath = argument[4:len(argument)]
			#process RTMP chunk size
			elif argument[0:4] == "-cs=":
				chunkSize = int(argument[4:len(argument)])
				csFlag = 1
			#process trace format argument
			elif argument[0:3] == "-t=":
				tFormat = argument[3:len(argument)]
			#process encapsulation method argument
			elif argument[0:3] == "-p=":
				eMethod = argument[3:len(argument)]
			#process encapsulation method argument
			elif argument[0:3] == "-s=":
				tsScalar = float(argument[3:len(argument)])
			#process ethernet encapsulation argument
			#default is off
			elif argument[0:6] == "-enet=":
				enet = argument[6:len(argument)]
			else:
				for i in range(len(argument)):
					if argument[len(argument)-i:len(argument)-i+1] == ".":
						if input:
							fileList.append(argument)
							input = False
						else:
							outfileList.append(argument)
							input = True
						break

		if useGlob != 1 and len(fileList) != len(outfileList):
			print("\n" + "File naming Error: Please, specify an input file name then an output file name")
			sys.exit()
		
		print(str("time stamp scalar:" + str(tsScalar)))
		
		
		#perform checks of argument validity 		
			
		#check to make sure that the necessary command line switches
		#are set: -t -p.
				
		#check -t argument
		if not(tFormat == "mp4new" or tFormat == "mp4fgs" or tFormat == "mp4" or tFormat == "h263" or tFormat == "h261" or tFormat == ""):
			print("-t argument not valid.")
			print("Valid arguments: mp4new, mp4fgs, mp4, h263, h261")
			sys.exit()
		
		if tFormat=="":
			print("No trace format specified; the system will attempt to determine the format on a file by file basis")

		#check -p argument
		if not(eMethod == "tcp" or eMethod == "rtp" or eMethod == "rtmp" or eMethod == "udp" or eMethod == "http"):
			print("-p argument not valid.")
			print("Valid arguments: tcp,rtp,rtmp,udp,http")
			sys.exit()

		#check -cs argument
		if (csFlag == 1):
			if not(eMethod == "rtmp"):
				print("The use of -cs argument is not valid except with -p=rtmp.")
				sys.exit()
		if (chunkSize < 128 or chunkSize > 65536):
			print("-cs argument not valid.")
			print("RTMP chunk size has to be within the Range (65536 - 128) Bytes")
			sys.exit()

		#check -enet argument
		if not(enet == "on" or enet == "off"):
			print("-enet argument not valid.")
			print("Valid arguments: on, off")
			sys.exit()
		
		#dump list and use Glob
		if useGlob == 1:
			#use glob to search directory for all files
			#exclude .encap and .py files
			FFBIList = glob.glob(globPath + "/*.*")
			
			for file in FFBIList:
				if file[len(file)-6:len(file)] != ".encap":
					if file[len(file)-3:len(file)] != ".py":
						CleanList.append(file)
						#print file
						#print file[len(file)-6:len(file)]

			fileList = CleanList
		else:
			for file in fileList:
				if file[len(file)-3:len(file)] != ".py":
					CleanList.append(file)

			fileList = CleanList
			
		#calculate overhead and mss size based on encapsulation method
		if eMethod == "http":
			appLayerOverhead = httpHeaderSize
			overhead = tcpHeaderSize
			encapInfo = "http/tcp/ip"
		if eMethod == "tcp":
			overhead = tcpHeaderSize
			encapInfo = "tcp/ip"
		if eMethod == "rtp":
			#appLayerOverhead = rtpHeaderSize
			overhead = udpHeaderSize + rtpHeaderSize
			encapInfo = "rtp/udp/ip"
		if eMethod == "rtmp":
			#appLayerOverhead = rtmpHeaderSize
			overhead = tcpHeaderSize + rtmpHeaderSize
			encapInfo = "rtmp/tcp/ip"
		if eMethod == "udp":
			overhead = udpHeaderSize
			encapInfo = "udp/ip"

		overhead = overhead + ipV4HeaderSize
		
		mss = mtuSize - overhead
		
		#add ethernet encapsulation if specified.  This step
		#is performed after calculating mss because
		#the type II encapsulation's size + header and
		#footer adheres to 1518 bytes max size, whereas
		#the mtu for everything else
		if enet == "on":
			overhead = overhead + ethernetHeaderSize
			encapInfo = encapInfo + "/ethernet"
		
		print("Encapsulation Used:" + encapInfo)

		if eMethod == "rtmp":
			mss = chunkSize
			print("RTMP Chunk Size:" + str(mss))
		else:
			print("mss:" + str(mss))
			print("overhead:" + str(overhead))
		
		print(fileList)		
		
		#encapsulate files
		for inFile in fileList:
			print("Reading file:" + inFile)
			
			if useGlob != 1:
				outputfile = outfileList.pop(0)
			else:
				outputfile = inFile

			#check for null trace format specification
			#and attempt to determine the format for the file
			if tFormat == "":
				traceForm = detFormat(inFile)
			else:
				traceForm = tFormat

			#if the format comes back undefined, skip
			if traceForm == "undefined":
				print("Skipping file due to detection errors.")
				continue
				
			prediction = forecastExist(inFile, traceForm)
			
			
			
			#import the trace list
			packetList = importTrace(inFile, traceForm, tsScalar, prediction)
				
			print("Encapsulating file:" + inFile)
			encapsulate(packetList, outputfile, useGlob, traceForm, mss, overhead, appLayerOverhead, useEnum, enet, inFile, prediction,eMethod,firstpkt)
			
			
		print(str(len(fileList)) + " trace files processed")


#
# Function name: detFormat
#
# Description: Attempts to determine the trace file type
#              if no trace format is specified.
#
# Inputs: fileToTest- The name of the file with which
#         to check the formatting.
#
# Outputs: tFormat- A string containing the format type.
#
#
def detFormat(fileToTest):
	
	inFile = open(fileToTest, "r")
	tFormat = "undefined"
	
	#skip past header, if there is one
	while True:
		lineread = inFile.readline()
		if not lineread:
			break
		if lineread[0] != "#":
			#split on white space
			trace = lineread.split()
			
			#determine trace type & presence of Prediction by reading the first line
			if trace[0] == "0":
				if trace[1] == "0.0000" or trace[1] == "0.000000":
					tFormat = "mp4new"

					break
				elif trace[1] == "0":
					tFormat = "h264"
				
					break
				elif trace[1] == "I":
					tFormat = "h263"

					break
			elif trace[2] == "0":
				tFormat = "mp4"

				break
			else:
				tFormat = "mp4fgs"

				break
			
	
	inFile.close() 
	
	print("Determined trace file type:" + tFormat)

	return tFormat
	
def forecastExist(fileToTest, tFormat):

	inFile = open(fileToTest, "r")
	
	#skip past header, if there is one
	while True:
		lineread = inFile.readline()
		if not lineread:
			break
		if lineread[0] != "#":
			#split on white space
			trace = lineread.split()
			
			if tFormat == "mp4new":
				if len(trace) == 8:
					forecast = True
				else:
					forecast = False
				break
			elif tFormat == "h264":
				if len(trace) == 8:
					forecast = True
				else:
					forecast = False
				break
			elif tFormat == "h263":
				if len(trace) == 4:
					forecast = True
				else:
					forecast = False
				break
			elif tFormat == "mp4":
				if len(trace) == 5:
					forecast = True
				else:
					forecast = False
				break
			elif tFormat == "mp4fgs":
				if len(trace) == 7:
					forecast = True
				else:
					forecast = False
				break
				
	inFile.close() 	
	
	if forecast:
		print("Prediction Information Tagged: YES")
	else:
		print("Prediction Information Tagged: NO")
		
	return forecast
	
#
# Function name: importTrace
#
# Description: Reads a trace file, grabs frame type, time stamp
#	           and corrects frame index.  The fine grain
#		       scalable format ASU provides does not, however
#		       contain time stamp information, so that data is
#	           zeroed out.
#
# Inputs: fileToGrind- The name of the file to import
#		  tFormat- The video trace format to import
#		  tsScalar- the time stamp scalar to multiply
#
# Outputs: Returns a list of unfragmented video traces
#
#
def importTrace(fileToGrind,tFormat,tsScalar,prediction):
	inList=[]
	frameNo=0
	timeStamp=0
	frameType=""
	frameSize=0
	frameInc=0
	fileToOpen=fileToGrind
	inFile = open(fileToOpen,"r")
	tsOffset = 1
	tsOffsetDetermined = False
	
	#winread = inFile.readline()
	
	#read file until EOF
	while True:
		lineread = inFile.readline()
		if not lineread:
			break
		if lineread[0] != "#" and len(lineread) > 5:
			#set expressions to parse, in this case
			#the regex used are python default
			#to split on whitespace
			trace = lineread.split()

			#add packet data based on trace format
			#mp4new format
			if tFormat == "mp4new" or tFormat == "h264":
				
				#get frame Number
				frameNo = int(trace[0])

				#begin conversion of time stamp
				timeStamp = float(trace[1]) * float(tsScalar)
	
				frameType = trace[2]

				#get frame size
				frameSize = int(trace[3])
				
				#get FFBI Info.
				if prediction:
					FFBIinfo = float(trace[7])

			#mp4fgs format.  It should be noted
			#the the mp4fgs traces have no timestamp
			#information in them
			if tFormat == "mp4fgs":

				#get frame number
				frameNo = int(trace[0])

				#time stamp is null
				timeStamp=0

				#get frame type
				frameType = trace[1]

				#frame size is in bits
				fs = int(trace[2])
				
				#get FFBI Info. is in bits
				if prediction:
					FFBIbits = int(trace[6])
				
				#align frame size to 8 bits
				if fs % 8 == 0:
					frameSize = fs
				else:
					frameSize = fs + (8 - fs % 8)
					
				#align frame size to 8 bits
				if prediction:
					if FFBIbits % 8 == 0:
						FFBIinfo = FFBIbits
					else:
						FFBIinfo = FFBIbits + (8 - FFBIbits % 8)
						
				#divide by 8 to convert to bytes
				frameSize=frameSize / 8
				
				if prediction:
					FFBIinfo=FFBIinfo / 8
				
		
			#mp4 old format
			if tFormat == "mp4":

				#get frame number
				frameNo = int(trace[0])

				#get time stamp
				#double casting is necessary
				#to stop python from whining about
				#base conversion for decimal points
				timeStamp = float(trace[2])* float(tsScalar)

				#get frame type
				frameType = trace[1]

				#get frame size
				frameSize = int(trace[3])
				
				#get FFBI Info.
				if prediction:
					FFBIinfo = int(trace[4])

			#h263,h261 format
			if tFormat == "h263" or tFormat == "h261":

				#frame number is not specified, so just keep
				#incrementing from the initialized frame number
				#of 0
				frameNo=frameInc
				frameInc = frameInc + 1

				#get time stamp
				timeStamp = float(trace[0]) * float(tsScalar)

				#get frame type
				frameType = trace[1]

				#get frame size
				frameSize = int(trace[2])
				
				#get FFBI Info.
				if prediction:
					FFBIinfo = int(trace[3])

			# Set up the timestamp to always be in ms
			if tsOffsetDetermined == False and frameNo != 0 and timeStamp < 1:
				tsOffsetDetermined = True
				tsOffset = 1000

			#add the packet to the list
			if prediction:
				tPacket = tempPktWithPred(frameNo, int(timeStamp * tsOffset), frameSize, frameType, FFBIinfo)
			else:
				tPacket = tempPkt(frameNo, int(timeStamp * tsOffset), frameSize, frameType)
						
			inList.append(tPacket)
	
	inFile.close()
	
	print("total usable lines in trace file:" + str(len(inList)))
	
	#if the outlist is not mp4fgs, rearrange  timestamp
	if tFormat != "mp4fgs":
		
		#clone the inList
		sortedList=[]
		tStampList=[]
		#the first sorted list will get
		#destroyed when searching
		sortedList[:]=inList[:]
		
		#sort cloned list by time stamp
		#sortedList.sort(timeStampCompare)
		
		newFrameNo=0
		
		#iterate through and re-establish
		# new frame order on sorted list
		for packet in sortedList:
			packet.frameNo = newFrameNo
			newFrameNo = newFrameNo + 1
			#we are going to destroy sorted list
			#when we do searching, so we will
			#copy the time stamp info again
			tStampList.append(packet.timeStamp)
			
		#print tStampList
		
		#return sortedList
		
		#search self.FFBIinfo = FFBIinfo for matching time stamp values
		#and pass the correct frame number
		
		#values for progress display
		percent = 0
		maxvalue = len(inList)
		
		#packet iterator index
		index=0
		
		
		#iterate through the inlist
		for packet in inList:
			
			timeStamp = packet.timeStamp
			
			#iterate through sorted packet list
			#and correct for frame number
			for sortedPacket in sortedList:
				if sortedPacket.timeStamp == timeStamp:
					packet.frameNo = sortedPacket.frameNo
					#destroy list to speed up future searching
					sortedList.remove(sortedPacket)
					break
			
			#reorder timestamp
			packet.timeStamp = tStampList[index]
			
			progress  = int(100*index/maxvalue) + 1
			
			index=index+1
			
			#print maxvalue
			#print "Correcting timestamp and packet order:" + str(progress) + "%\r",
			
			if progress > percent:
				percent = progress
				#print fix for python nullifying the line
				sys.stdout.flush()
				print("Correcting timestamp and packet order:" + str(progress) + "%", end='\r') #Newer Python Version than 2.7
				#print "Correcting timestamp and packet order:" + str(progress) + "%\r", #Python 2.7 Version
	print("")
	return inList
		

#
# Function name: encapsulate
#
# Description: Sends video traces to a fragmentation
#		       subroutine and displays progress.  Writes
#			   fragmented traces to file.
#
# Inputs: inList- The list of video Traces to encapsulate
#		  mss- The maximum segment size of fragmentation
#		  overhead- Header and footer overhead of the packet
#         appLayerOverhead- Overhead of data from the application layer
#         used, for example, in HTTP tunneling
#		  useEnum- Frame type enumeration switch for
#	      enet- Ethernet encapsulation switch
#
# Outputs: filename + .encap- A fragmented Trace File
#
#

def encapsulate(inList, outputfile, useGlob, traceForm, mss, overhead, appLayerOverhead, useEnum, enet, fileName, prediction,eMethod, firstpkt): 
	
	#outList=[]
	
	outFile = open(fileName + ".temp","w")
		
	#number of total written lines in the file
	numlines = 0
	
	# Maximum Frame Fragment Count
	maxFramePacketCount = 0
	
	progressCount = 0
	lastPercent = 0
	progressMax = len(inList)
	
	#iterate the in list to get our list of datagram sizes
	for listItem in inList:
		
		#generate a fragmented list of current trace
		#and extend it to the master encapsulated list
		fragList = fragment(listItem, mss, overhead, appLayerOverhead, useEnum, enet, prediction,eMethod, firstpkt)
		#outList.extend(fragList)
		
		# Determine the Largest Number of Fragments
		currentFragmentCount = len(fragList)
		if currentFragmentCount > maxFramePacketCount:
			maxFramePacketCount = currentFragmentCount
		
		for fragPkt in fragList:
			#correct packet type for enumeration switch
			pktType = fragPkt.pktType
			
			pktType = pktType.upper()
			
			if pktType == "PB":
				pktType = "B"
			
			if useEnum == 1:
				if pktType == "I":
					pktType = "1"
				if pktType == "P":
					pktType = "2"
				if pktType == "B":
					pktType = "3"
					
			if prediction:
				if len(str(fragPkt.FFBIinfo)) <= 5:
					outLine = str(fragPkt.frameNo) + "\t" + "\t" + str(fragPkt.timeStamp)  + "\t" + "\t" \
					+ str(pktType) + "\t" + "\t" + str(fragPkt.dataSize) + "\t" + "\t" + str(fragPkt.overhead) + "\t" + "\t" + str(fragPkt.FFBIinfo) + "\t" + "\t" + "\t" + str(fragPkt.FFBIoverhead) + "\t" + "\t" + "\t" + str(fragPkt.pktcount) + "\n"
				else:
					outLine = str(fragPkt.frameNo) + "\t" + "\t" + str(fragPkt.timeStamp)  + "\t" + "\t" \
					+ str(pktType) + "\t" + "\t" + str(fragPkt.dataSize) + "\t" + "\t" + str(fragPkt.overhead) + "\t" + "\t" + str(fragPkt.FFBIinfo) + "\t" + "\t" + str(fragPkt.FFBIoverhead) + "\t" + "\t" + "\t" + str(fragPkt.pktcount) + "\n"
			else:
				outLine = str(fragPkt.frameNo) + "\t" + "\t" + str(fragPkt.timeStamp) + "\t" + "\t" \
				+ str(pktType) + "\t" + "\t" + str(fragPkt.dataSize) + "\t" + "\t" + str(fragPkt.overhead) + "\n"			
			outFile.write(outLine)	
			
			#increment number of lines written
			numlines = numlines + 1
		
		#increment the progress counter without wasting time making too many
		#display refreshes
		progressCount = progressCount + 1
		progress = int(progressCount * 100 / progressMax)
		if progress > lastPercent:
			lastPercent=progress
			sys.stdout.flush()
			print("Fragmenting and encapsulating:" + str(progress) + "%", end='\r')  #Newer Python Version than 2.7
			#print "Fragmenting and encapsulating:" + str(progress) + "%\r", #Python 2.7 Version
	
	print("")
	
	#close file
	outFile.close()
	#wow, we have to do all this
	#just to correctly append the top
	#of the file, hooray
	print("Finalizing File")
	finalizeFile(fileName, outputfile, useGlob, traceForm, numlines, maxFramePacketCount, prediction)
	
	os.remove(fileName + ".temp")
	

	
#
# Function name: finalizeFile
#
# Description: Rewrites file with the number of usable lines
#              as the top line of the file and adds time stamp diffs
#
# Inputs: filename- the file to finalize
#		  numlines- the number of usable lines in the file
#
# Outputs: A list of fragmented packets
#
#
def finalizeFile(fileName, outputfile, useGlob, tFormat, numlines, maxNumOfPackets, prediction):
	#open the temp file
	inTemp = open(fileName + ".temp","r")
	if useGlob == 1:
		outFile = open(fileName + ".encap","w")
	else:
		outFile = open(outputfile,"w")
	
	#write number of lines to top of output file
	outLine = "# Number of Lines = " + str(numlines) + "\n"
	outFile.write(outLine)
	if not prediction:
		outFile.write("# Original_Video_trace = " + fileName + "\n")
		outFile.write("# Video_trace_format = " + tFormat + "\n")
	inFile = open(fileName, "r")
	winread = inFile.readline()
	
	while winread[0] == "#":
		if winread[0] == "#":
			outLine = str(winread)
			outFile.write(outLine)
		winread = inFile.readline()
	inFile.close()
	
	
	if prediction:
		outFile.write("#" + "\n")
		outFile.write("# Frame                                                                                                                   Last" + "\n")
		outFile.write("# Number     Time(ms)         Type            Payload       Overhead       For. Payload       For. OHD    For. Pkt Count  Packet of Frame" + "\n")
		outFile.write("#---------------------------------------------------------------------------------------------------------------------------------------------" + "\n")
	else:
		outFile.write("#" + "\n")
		outFile.write("# Frame                                                                    Last" + "\n")
		outFile.write("# Number     Time(ms)         Type            Payload       Overhead       Packet of Frame" + "\n")
		outFile.write("#----------------------------------------------------------------------------------------------------" + "\n")
	
	
	lastLine = inTemp.readline()
	
	lastLine = lastLine.strip()
	
	initial = True;
	
	#read temporary in file line by line and copy it
	#to out file
	while True:
		lineread = inTemp.readline()
		
		lineread = lineread.strip()
		
		if not lineread:
			outFile.write(lastLine + "\t" + "\t" + "1" + "\n")
			break
		else:
			#get time stamp difference
			splitLine = lineread.split()
			splitLast = lastLine.split()
			
			#get current and previous time stamp
			currentTs = int(splitLine[0])
			lastTs = int(splitLast[0])
		
			#get time stamp difference
			tsDiff = currentTs - lastTs
			
			if tsDiff != 0:
				tsDiff = 1
				
			outFile.write(lastLine + "\t" + "\t" + str(tsDiff) + "\n")
			
			lastLine = lineread
	
	inTemp.close()
	outFile.close()

#
# Function name: fragment
#
# Description: fragments a video trace and returns a list of fragmented packets
#
# Inputs: packet- The packet to fragment
#	      mss- Maximum fragmented segment size
#	      overhead- Header and footer overhead
#         appLayerOverhead- Overhead of data from the application layer
#         used, for example, in HTTP tunneling
#	      useEnum- Frame type enumeration switch
#		  enet- Ethernet encapsulation switch
#
# Outputs: A list of fragmented packets
#
#
def fragment(packet, mss, overhead, appLayerOverhead, useEnum, enet, prediction, eMethod, firstpkt):
	outList = []
	rtmpPktCount = 0

	
	#grab packet characteristics
	pktType = packet.pktType
	frameNo = packet.frameNo
	timeStamp = packet.timeStamp
	if prediction:
		FFBIinfo = packet.FFBIinfo
	
	initial = True
	
	if useEnum == 1:
		if pktType == "I":
			pktType = "1"
		if pktType == "P":
			pktType = "2"
		if pktType == "Pb" or pktType == "B":
			pktType = "3"
	
	if prediction:
		FFBIoverhead, pktcount = FFBIfragment(FFBIinfo, mss, overhead, appLayerOverhead, enet, eMethod, firstpkt)

				
	#add pure app layer (HTTP) TCP split packets if needed
	while appLayerOverhead + overhead > mss:
		#size of these packets are pure http overhead
		if prediction:
			tPacket = tempPktWithSplitSizeWithPred(frameNo, timeStamp, 0, mss, pktType, FFBIinfo, FFBIoverhead, pktcount)
		else:
			tPacket = tempPktWithSplitSize(frameNo, timeStamp, 0, mss, pktType)
		outList.append(tPacket)
		#account for normal overhead
		appLayerOverhead = (appLayerOverhead + overhead) - mss
	
	#set the size to the packet size + remaining HTTP layer overhead
	size = int(packet.size)

#	if (eMethod == "rtmp"):
#		if (size <= mss):
#			appLayerOverhead = 59
#		elif (size <= 2*mss):
#			appLayerOverhead = 103
#		else:
#			appLayerOverhead = 103 + 41 * int(math.ceil((size-8192.0)/4096.0))
#		
#		size = size + appLayerOverhead
#		appLayerOverhead = 0
			
	
	#add packets of maxSize to the list
	while size + appLayerOverhead > mss:
		if eMethod == "rtmp":
			rtmpPktCount = rtmpPktCount + 1
			
			if (frameNo == 0 and firstpkt == 1):
				firstpkt = 0
				appLayerOverhead = 23
			elif rtmpPktCount == 1:
				appLayerOverhead = 19
			elif rtmpPktCount == 2:
				appLayerOverhead = 4
			else:
				appLayerOverhead = 1
		tOverhead = overhead + appLayerOverhead

		if eMethod == "rtmp":
			if size - mss >= 128:
				tMss = mss
			elif size <= 65536:
				tMss = size
				rtmpPktCount = 0
			else:
				tMss = size - 128
		else:
			tMss = mss - appLayerOverhead
		#appLayerOverhead should be depleted now
		appLayerOverhead = 0
		if prediction:
			tPacket = tempPktWithSplitSizeWithPred(frameNo, timeStamp, tMss, tOverhead, pktType, FFBIinfo, FFBIoverhead, pktcount)
		else:
			tPacket = tempPktWithSplitSize(frameNo, timeStamp, tMss, tOverhead, pktType)
		outList.append(tPacket)
		size = size - tMss
	
	if not(size==0):
		#if the -enet switch is set
		#make sure final smallest packet is at least
		#64 bytes in size
		rtmpPktCount = rtmpPktCount + 1
		if enet == "on":
			if eMethod != "rtmp":
				if size + overhead + appLayerOverhead < 48:
					size = 48 - overhead - appLayerOverhead
		if eMethod == "rtmp":
			if (frameNo == 0 and firstpkt == 1):
				firstpkt = 0
				appLayerOverhead = 23
			elif rtmpPktCount == 1:
				appLayerOverhead = 19
			elif rtmpPktCount == 2:
				appLayerOverhead = 4
			else:
				appLayerOverhead = 1

		rtmpPktCount = 0
	
		#add the last packet to the list and return
		#the list.  AppLayerOverhead should be depleted
		#if not, we add here because we can
		if prediction:
			tPacket = tempPktWithSplitSizeWithPred(frameNo, timeStamp, size, overhead + appLayerOverhead, pktType, FFBIinfo, FFBIoverhead, pktcount)
		else:
			tPacket = tempPktWithSplitSize(frameNo, timeStamp, size, overhead + appLayerOverhead, pktType)

		outList.append(tPacket)	
	return outList
	
#
# Function name: FFBIfragment
#
# Description: fragments FFBI Information
#
# Inputs: FFBIinfo- The FFBI information to fragment
#		mss- Maximum fragmented segment size
#		overhead- Header and footer overhead
#		appLayerOverhead- Overhead of data from the application layer
#				used, for example, in HTTP tunneling
#		useEnum- Frame type enumeration switch
#		enet- Ethernet encapsulation switch
#
# Outputs: A list of fragmented packets
#
#
def FFBIfragment(FFBIinfo, mss, overhead, appLayerOverhead, enet, eMethod, firstpkt):
	outList = []
	rtmpPktCount = 0
	
	initial = True
	
	FFBIoverhead = 0
	pktcount = 0
	
	#add pure app layer (HTTP) TCP split packets if needed 
	while appLayerOverhead + overhead > mss:
		#size of these packets are pure http overhead
		#tPacket = tempPktWithSplitSize(frameNo, timeStamp, 0, mss, pktType, FFBIinfo)
		#outList.append(tPacket)
		#account for normal overhead
		appLayerOverhead = (appLayerOverhead + overhead) - mss
		FFBIoverhead = FFBIoverhead + mss
	
	#set the size to the packet size + remaining HTTP layer overhead
	size = int(FFBIinfo)


	#add packets of maxSize to the list
	while size + appLayerOverhead > mss:
		if eMethod == "rtmp":
			rtmpPktCount = rtmpPktCount + 1
			
			if (frameNo == 0 and firstpkt == 1):
				firstpkt = 0
				appLayerOverhead = 23
			elif rtmpPktCount == 1:
				appLayerOverhead = 19
			elif rtmpPktCount == 2:
				appLayerOverhead = 4
			else:
				appLayerOverhead = 1
		tOverhead = overhead + appLayerOverhead

		if eMethod == "rtmp":
			if size - mss >= 128:
				tMss = mss
			elif size <= 65536:
				tMss = size
				rtmpPktCount = 0
			else:
				tMss = size - 128
		else:
			tMss = mss - appLayerOverhead

		#appLayerOverhead should be depleted now
		appLayerOverhead = 0
	
		FFBIoverhead = FFBIoverhead + tOverhead
		size = size - tMss
		pktcount += 1
	
	if not(size==0):
		#if the -enet switch is set
		#make sure final smallest packet is at least
		#64 bytes in size
		rtmpPktCount = rtmpPktCount + 1
		pktcount += 1
		
		if enet == "on":
			if eMethod != "rtmp":
				if size + overhead + appLayerOverhead < 48:
					size = 48 - overhead - appLayerOverhead
		if eMethod == "rtmp":
		
			if (frameNo == 0 and firstpkt == 1):
				firstpkt = 0
				appLayerOverhead = 23
			elif rtmpPktCount == 1:
				appLayerOverhead = 19
			elif rtmpPktCount == 2:
				appLayerOverhead = 4
			else:
				appLayerOverhead = 1

		FFBIoverhead = FFBIoverhead + overhead + appLayerOverhead
		
	return FFBIoverhead, pktcount

#
# Function name: exportPktList (deprecated, but possible future use)
#
# Description: Writes list of fragmented packets to a file.
#
# Inputs: pktList- The fragmented list to write
#		  fileName- The name of the file to write to
#
# Outputs: None
#
#
def exportPktList(pktList, fileName, prediction):
	outFile = open(fileName,"w")
	
	#outFile.write(str(len(pktList)) + "\n")
	
	
	for pktItem in pktList:
		if prediction:
			outLine = str(pktItem.frameNo) + "\t" + str(pktItem.timeStamp) + "\t" \
			+ str(pktItem.pktType) + "\t" + str(pktItem.size) + "\t" + str(pktItem.FFBIinfo) + "\t\t0\n"
		else:
			outLine = str(pktItem.frameNo) + "\t" + str(pktItem.timeStamp) + "\t" \
			+ str(pktItem.pktType) + "\t" + str(pktItem.size) + "\t\t0\n"			
		outFile.write(outLine)
	outFile.close()

#
# Function name: timeStampCompare
#
# Description: Overrides the default list compare function to
#              compare by trace time stamp.
#
# Inputs: Two video traces: a and b
#
# Outputs: Boolean comparator value used by Python for list sorting
#
#
def timeStampCompare(a, b):
	if a.timeStamp > b.timeStamp:
		return 1
	elif a.timeStamp == b.timeStamp:
		return 0
	else: # a.timeStamp<b.timeStamp
		return -1

	
#
# Class Name: tempPkt
#
# Description: A temporary container for traces.
#	           used for both unfragmented and fragmented
#	           traces
#
# Inputs: frameNo- The frame number of the trace/packet
#		  timeStamp- The time stamp of the trace/packet
#		  size- The size of the trace/packet
#		  pktType- The type of the trace/packet
#
# Outputs: None
#
#
class tempPkt:
	def __init__(self, frameNo, timeStamp, size, pktType):
		self.timeStamp = timeStamp
		self.size = size
		self.pktType = pktType
		self.frameNo = frameNo
		
		
class tempPktWithPred:
	def __init__(self, frameNo, timeStamp, size, pktType, FFBIinfo):
		self.timeStamp = timeStamp
		self.size = size
		self.pktType = pktType
		self.frameNo = frameNo
		self.FFBIinfo = FFBIinfo
		
#
# Class Name: tempPktWithSplitSize
#
# Description: A temporary container for traces.
#	           used for both unfragmented and fragmented
#	           traces
#
# Inputs: frameNo- The frame number of the trace/packet
#		  timeStamp- The time stamp of the trace/packet
#		  dataSize- The size of the packet data payload
#		  overhead- The size of the current packet overhead
#		  pktType- The type of the trace/packet
#
# Outputs: None
#
#
class tempPktWithSplitSize:
	def __init__(self, frameNo, timeStamp, dataSize, overhead, pktType):
		self.timeStamp = timeStamp
		self.dataSize = dataSize
		self.overhead = overhead
		self.pktType = pktType
		self.frameNo = frameNo
		
class tempPktWithSplitSizeWithPred:
	def __init__(self, frameNo, timeStamp, dataSize, overhead, pktType, FFBIinfo, FFBIoverhead, pktcount):
		self.timeStamp = timeStamp
		self.dataSize = dataSize
		self.overhead = overhead
		self.pktType = pktType
		self.frameNo = frameNo
		self.FFBIinfo = int(FFBIinfo)
		self.FFBIoverhead = FFBIoverhead
		self.pktcount = pktcount
		
#specify the system to exit
#when the call to main ends	
if __name__ == "__main__":
    sys.exit(main())
    
