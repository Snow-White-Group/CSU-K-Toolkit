# arg[1]: reads a csv file, where Id is in column 3
# arg[2]: writes same file but with fixed id's
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

	with open(filename) as csv_file:
		reader = csv.reader(csv_file, delimiter='\t')
		for row in reader:
			if "user-" in row[2]:
				_id, trash = row[2].split("_", 1)
				trash, _id = _id.split("-")
				if int(_id) < 10:
					_id = '00' + _id
				elif int(_id) < 100:
					_id = '0' + _id

				row[2] = re.sub(r"user-((\d{1}_)|(\d{2})_)", "user-%s_" % _id, row[2])
				goodDataRows.append(row)
			else:
				goodDataRows.append(row)

def writeTextFiles(filename):
	global goodDataRows

	file = open(output, 'w')
	writer = csv.writer(file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)


	for row in goodDataRows:
		writer.writerow(row)

	file.close()

# now run the methods
extractCorrectOnes(filenameA)
writeTextFiles(filenameA)