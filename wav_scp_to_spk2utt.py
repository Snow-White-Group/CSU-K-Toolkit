# arg[1]: reads a wav.scp file
# arg[2] writes spk2utt where every utterance has it's own speaker

import sys

parameter = sys.argv

filenameA = parameter[1]
output = parameter[2]

goodDataRows = []


def extractCorrectOnes(filename):
	global goodDataRows

	with open(filename) as f:
	    content = f.readlines()
	    for line in content:
	    	line = line.strip()
	    	id, path = line.split(" ", 2)
	    	goodDataRows.append(id + " " + id + "\n")

def writeTextFiles():
	global goodDataRows

	file = open(output, 'w')
	for item in goodDataRows:
		file.write("%s" % item)

	file.close()

# now run the methods
extractCorrectOnes(filenameA)
writeTextFiles()