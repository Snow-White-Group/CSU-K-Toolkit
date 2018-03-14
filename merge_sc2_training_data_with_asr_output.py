# argv[1]: reads sc1 train csv
# argv[2]: reads asr output file
# argv[3]: output csv file where all sc1 train entries are have asr output as rec_result
import sys
import csv
import re
from itertools import islice

parameter = sys.argv

filename = parameter[1]
asr_output = parameter[2]
asr_data_csv = parameter[3]

goodDataRows = []

def extractCorrectOnes(filename):
	global goodDataRows

	with open(asr_output) as f:
	    content = f.readlines()
	    addHeaderToGoodDataRows(filename)
	    for line in content:
	    	# TODO check whether empty results are included
	    	_id, sentence = line.split(" ", 1)
	    	fetchcolvalue(filename, _id, sentence)
	print(len(goodDataRows))


def fetchcolvalue(filename, id, asr_output_sentence):
	global goodDataRows
	csv_file = open(filename)
	reader = csv.reader(csv_file, delimiter='\t')
	for row in reader:
		if row[0]  == id:
			row[2] = asr_output_sentence.strip().lower() if asr_output_sentence.strip().lower() else row[2]			
			goodDataRows.append(row)
			break
	csv_file.close()

def addHeaderToGoodDataRows(filename):
	global goodDataRows
	csv_file = open(filename)
	reader = csv.reader(csv_file, delimiter='\t')
	headline = next(reader)
	goodDataRows.append(headline)

def writeTextFiles(filename):
	global goodDataRows

	file = open(filename, 'w')
	writer = csv.writer(file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

	for row in goodDataRows:
		writer.writerow(row)

	file.close()

# now run the methods
extractCorrectOnes(filename)
writeTextFiles(asr_data_csv)