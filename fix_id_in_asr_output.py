# argv[1]: reads asr output file
# argv[2]: writes corrected asr output file with good id's

import sys
import csv
import re
from itertools import islice

parameter = sys.argv

filenameA = parameter[1]
output = parameter[2]

goodDataRows = []


def extractCorrectOnes(filename):
	global goodDataRows

	with open(filename) as f:
	    content = f.readlines()
	    for line in content:
	    	if "user-" in line:
	    		_id, trash = line.split("_", 1)
	    		trash, _id = _id.split("-")
	    		if int(_id) < 10:
	    			_id = '00' + _id
    			elif int(_id) < 100:
	    			_id = '0' + _id
    			goodDataRows.append(re.sub(r"user-((\d{1}_)|(\d{2})_)", "user-%s_" % _id, line))
    		else:
    			goodDataRows.append(line)

def writeTextFiles():
	global goodDataRows

	file = open(output, 'w')
	for item in goodDataRows:
		file.write("%s" % item)

	file.close()

# now run the methods
extractCorrectOnes(filenameA)
writeTextFiles()