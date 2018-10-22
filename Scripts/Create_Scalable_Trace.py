
# To Use:
# 1. Place raw traces in working directory.
# 2. Change file names in SECTION ONE
# 3. Run

fyle = []
new_fyle = []
trace = []
lines = []
data = [[], [], [], []]
new_lines = [[], [], [], []]
new_trace = []
num_comment_lines = 0
count_removed = 0
bug_strings = ['\t', '\t\n', '\n', '\r', ' ', '']
Total_Data = 0
Num_Frames = 0

MAX_PACKET_SIZE = 1460
PACKET_OVERHEAD = 58
SCALING_FACTOR = 1.0
FRAME_RATE = 30
NUM_LAYERS = 7		# This includes base layer

# SECTION ONE
fyle.append(open('trace.txt', 'r'))
fyle.append(open('trace (1).txt', 'r'))
fyle.append(open('trace (2).txt', 'r'))
fyle.append(open('trace (3).txt', 'r'))
fyle.append(open('trace (4).txt', 'r'))
fyle.append(open('trace (5).txt', 'r'))
fyle.append(open('trace (6).txt', 'r'))
# END SECTION ONE

#new_fyle.append(open('NEW_layer0.txt', 'w'))
#new_fyle.append(open('NEW_layer1.txt', 'w'))
#new_fyle.append(open('NEW_layer2.txt', 'w'))
#new_fyle.append(open('NEW_layer3.txt', 'w'))

combined_lines = []
packetized_lines = []
combined_data = []
packetized_fyle = open('AA_Combined.txt', 'w')

for layer in range(NUM_LAYERS):
	# Read the layer file
	trace.append(fyle[layer].read())
	
	# Split the file into lines
	lines.append(trace[layer].split('\r\n'))
	
	# Remove blank or useless lines from the file
	for line in lines[layer][::-1]:
		if bug_strings.count(line) == 1:
			lines[layer].remove(line)
			count_removed += 1
	
	# Split the lines into entries
	for line in lines[layer]:
		data[layer].append(line.split('\t'))
	
	# Process some of the entries && recombine entries into lines
	for line in data[layer]:
		if line[0][0] != '#':
			while len(line) > 4:
				line.pop()
			line[1] = str(int(float(line[1])*1000))
			line.insert(4, str(PACKET_OVERHEAD))
			new_lines[layer].append('\t\t'.join(line) + '\t\t{}'.format(layer))
		else:
			if layer == 0:
				num_comment_lines += 1
			new_lines[layer].append('\t\t'.join(line))
	
	# Write the output on a by-layer basis
	new_trace.append('\n'.join(new_lines[layer]))
	#new_fyle[layer].write(new_trace[layer])

# Create an appropriate header
for layer in range(NUM_LAYERS):
	combined_lines.append('# ')
	for line in new_lines[layer][:num_comment_lines]:
		combined_lines.append(line)
combined_lines.append('# ')
combined_lines.append('# ')
combined_lines.append('# Frame#\t\tTime(ms)\t\tType\t\tPayload\t\tOverhead\t\tFlag\t\tLayer')

# Put scalable frames in order
for lineNum in range(num_comment_lines, len(new_lines[0])):
	for layer in range(NUM_LAYERS):
		combined_lines.append(new_lines[layer][lineNum])

# Split the lines into entries again
for line in combined_lines:
	combined_data.append(line.split('\t\t'))

# Packetize each frame and add a flag
for line in combined_data:
	if line[0][0] != '#':
		remaining_data = int(round(SCALING_FACTOR * int(line[3])))
		Total_Data += remaining_data
		Num_Frames = line[0]
		line.insert(5, '0')
		while remaining_data > 0:
			if remaining_data > MAX_PACKET_SIZE:
				line[3] = str(MAX_PACKET_SIZE)
			if remaining_data <= MAX_PACKET_SIZE:
				line[3] = str(remaining_data)
				line[5] = '1'
			remaining_data -= MAX_PACKET_SIZE
			packetized_lines.append('\t\t'.join(line))
	else:
		packetized_lines.append('\t\t'.join(line))

# Recombine the lines and write output file
packetized_trace = '\n'.join(packetized_lines)
packetized_fyle.write(packetized_trace)

# Close files
packetized_fyle.close()
for layer in range(NUM_LAYERS):
	fyle[layer].close()
	#new_fyle[layer].close()

print 'Total_Data = {}'.format(Total_Data)
print 'Num_Frames = {}'.format(Num_Frames)
Avg_Bitrate = Total_Data*8/(float(Num_Frames))*FRAME_RATE
print 'Avg_Bitrate = {:.3f} Mb/s'.format(Avg_Bitrate/1000000)






