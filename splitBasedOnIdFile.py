import sys
import subprocess

train = []
test = []
content = []
ids = []

if len sys.argv < 3:
	print('Worng input!\n')
	print('First parameter should be your trainId File\n')
	print('Secound parameter should be your data File\n')

trainIdFile = sys.argv[1]
allDataFile = sys.argv[2]

with open(trainIdFile) as idFile:
	with open(allDataFile) as dataFile:
		ids = idFile.readlines()
		content = dataFile.readlines()
		for point in content:
			for id in ids:
				if id in point:
					train.append(point)
				else 
					test.append(point)

with open(allDataFile + '_test', 'w+') as outputFile:
    for entry in test:
		outputFile.write(entry)

with open(allDataFile + '_train', 'w+') as outputFile:
    for entry in train:
		outputFile.write(entry)