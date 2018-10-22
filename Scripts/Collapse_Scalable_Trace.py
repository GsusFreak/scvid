FRAME_RATE = 24

f = open('Transporter_2_24FPS_2EL.txt','r')
trace = f.read()
lines = trace.split('\r\n')
for line in lines:
	if line.count('#') >= 1:
		lines.remove(line)
info = []
for line in lines:
	info.append(line.split('\t\t'))

totalBytes = 0
#print info
for line in info:
	if len(line) > 1:
#		print line
		totalBytes = totalBytes + int(line[3])

bandwidth = (totalBytes/int(info[-2][0]))*FRAME_RATE
print totalBytes
print int(info[-2][0])
print bandwidth
