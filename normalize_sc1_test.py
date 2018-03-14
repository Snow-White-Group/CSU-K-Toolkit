import sys
import csv
import re
from itertools import islice

parameter = sys.argv

input_csv = parameter[1]
output_csv = parameter[2]

goodDataRows = []

def fixRows(input_csv):
	global goodDataRows

	headrow = []
	headrow.append('Id')
	headrow.append('Prompt')
	headrow.append('Wavfile')
	headrow.append('RecResult')
	headrow.append('Transcription')
	headrow.append('language')
	headrow.append('meaning')
	goodDataRows.append(headrow)

	csv_file = open(input_csv)
	reader = csv.reader(csv_file, delimiter='\t')
	for row in reader:
		if row[0] != 'Id':
			new_row = []
			new_row.append(row[0])
			new_row.append(row[1])
			new_row.append(row[2])
			new_row.append(row[3])
			new_row.append(row[3])
			new_row.append(row[4])
			new_row.append(row[5])
			goodDataRows.append(new_row)
	csv_file.close()

def writeTextFiles(input_csv):
	global goodDataRows

	file = open(input_csv, 'w')
	writer = csv.writer(file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

	for row in goodDataRows:
		writer.writerow(row)

	file.close()

# now run the methods
fixRows(input_csv)
writeTextFiles(output_csv)