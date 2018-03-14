import sys
import subprocess

train = []
test = []
content = []

if len(sys.argv) < 3:
        print('Bad Input!\n')
        print('1. parameter should be your Id-File\n')
        print('3. parameter should be your data-File\n')

idFile = sys.argv[1]
allDataFile = sys.argv[2]

print('id-File is:	' + idFile)
print('data-File is:	' + allDataFile)


with open(allDataFile) as dataFile:
	content = dataFile.readlines()
	with open(idFile) as input:
		ids = input.readlines()
		for point in content:
			for id in ids:
				if id.strip() in point.split(',')[0].strip():
					train.append(point)
					continue



with open('extractedData.csv', 'w+') as outputFile:
    for entry in train:
                outputFile.write(entry)