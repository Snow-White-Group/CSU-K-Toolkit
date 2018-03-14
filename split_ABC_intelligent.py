#####################
#
# Needed input paramteres from shell
# 1: A.csv
# 2: B.csv
# 3: C.csv
# 4: path to audio files
#
#####################
import sys
import csv
import re
from itertools import islice

parameter = sys.argv

filenameA = parameter[1]
filenameB = parameter[2]
filenameC = parameter[3]
path = parameter[4]

goodDataRows = []
badDataRows = []

# extracting the data from csv A and B with different patterns
# good -> from A we take all data where humans validated it | bad -> rest
# good -> from B we take all data where half of the machines were correct | bad -> rest
def extractABData(filename, pattern):

	global goodDataRows, badDataRows

	with open(filename) as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		for row in islice(reader, 1, None):
			trace = row[6]
			match = re.search(pattern, trace)
			if match:
				goodDataRows.append(row)
			else:
				badDataRows.append(row)

# all rows in C are bad!
def extractCData(filename):
	global badDataRows, train_data_scp

	with open(filename) as csvfile:
		reader = csv.reader(csvfile, delimiter='\t')
		for row in islice(reader, 1, None):
			badDataRows.append(row)

# write the scp files with 10% of data using only goodDataRows and 90% of data with rest
def writeScpFiles():
	global goodDataRows, badDataRows
	train_data_scp = []
	test_data_scp = []

	#  we need this heavy calculation to calculate our modulo value
	n = (len(goodDataRows)+len(badDataRows)) / len(goodDataRows)
	# modulo value = 10 percent of all data divided by n
	mod = round(10 / n)

	for i in range(0, len(goodDataRows)):
		if i % mod == 0:
			test_data_scp.append(goodDataRows[i][0] + " " + path + ("" if path.endswith("/") else "/") + goodDataRows[i][2])
		else:
			train_data_scp.append(goodDataRows[i][0] + " " + path + ("" if path.endswith("/") else "/") + goodDataRows[i][2])

	for i in range(0, len(badDataRows)):
		train_data_scp.append(badDataRows[i][0] + " " + path + ("" if path.endswith("/") else "/") + badDataRows[i][2])

	test_file = open("wav.scp_test", 'w')
	for item in test_data_scp:
		test_file.write("%s\n" % item)

	train_file = open("wav.scp_train", 'w')
	for item in train_data_scp:
		train_file.write("%s\n" % item)

	test_file.close()
	train_file.close()
	print("Entries in train file: " + str(len(train_data_scp)))
	print("Entries in test file: " + str(len(test_data_scp)))

# write text file - copied and adapted from writeScpFiles()
def writeTextFiles():
	global goodDataRows, badDataRows
	train_data_text = []
	test_data_text = []

	n = (len(goodDataRows)+len(badDataRows)) / len(goodDataRows)
	mod = round(10 / n)

	for i in range(0, len(goodDataRows)):
		if i % mod == 0:
			test_data_text.append(goodDataRows[i][0] + " " + goodDataRows[i][3])
		else:
			train_data_text.append(goodDataRows[i][0] + " " + goodDataRows[i][3])

	for i in range(0, len(badDataRows)):
		train_data_text.append(badDataRows[i][0] + " " + badDataRows[i][3])

	test_file = open("text_test", 'w')
	for item in test_data_text:
		test_file.write("%s\n" % item)

	train_file = open("text_train", 'w')
	for item in train_data_text:
		train_file.write("%s\n" % item)

	test_file.close()
	train_file.close()

# write text file for train and test - copied and adapted from writeScpFiles()
def writeUtt2SpkFile():
	global goodDataRows, badDataRows
	train_data_utt2spk = []
	test_data_utt2spk = []

	n = (len(goodDataRows)+len(badDataRows)) / len(goodDataRows)
	mod = round(10 / n)

	for i in range(0, len(goodDataRows)):
		if i % mod == 0:
			test_data_utt2spk.append(goodDataRows[i][0] + " TD")
		else:
			train_data_utt2spk.append(goodDataRows[i][0] + " TD")

	for i in range(0, len(badDataRows)):
		train_data_utt2spk.append(badDataRows[i][0] + " TD")

	test_file = open("utt2spk_test", 'w')
	for item in test_data_utt2spk:
		test_file.write("%s\n" % item)

	train_file = open("utt2spk_train", 'w')
	for item in train_data_utt2spk:
		train_file.write("%s\n" % item)

	test_file.close()
	train_file.close()

# write spk2utt files for train and test
def writeSpk2UttFile():
	global goodDataRows, badDataRows
	train_data_spk2utt = []
	test_data_spk2utt = []

	n = (len(goodDataRows)+len(badDataRows)) / len(goodDataRows)
	mod = round(10 / n)

	train_data_spk2utt = "TD "
	test_data_spk2utt = "TD "

	for i in range(0, len(goodDataRows)):
		if i % mod == 0:
			test_data_spk2utt += goodDataRows[i][0] + " "
		else:
			train_data_spk2utt += goodDataRows[i][0] + " "

	for i in range(0, len(badDataRows)):
		train_data_spk2utt += badDataRows[i][0] + " "

	test_file = open("spk2utt_test", 'w')
	test_file.write("%s\n" % test_data_spk2utt)

	train_file = open("spk2utt_train", 'w')
	train_file.write("%s\n" % train_data_spk2utt)

	test_file.close()
	train_file.close()

# now run the methods
extractABData(filenameA, '[H]\:\s+0-0')
extractABData(filenameB, '[M]\:\s+2-2')
extractCData(filenameC)
print("Entry count: " + str(len(goodDataRows) + len(badDataRows)))

writeScpFiles()
writeTextFiles()
writeUtt2SpkFile()
writeSpk2UttFile()

print("Good data count for test: " + str(len(goodDataRows)))
print("Bad data count for train: " + str(len(badDataRows)))