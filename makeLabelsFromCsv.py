# 1 means correct language and correct meaning
# 2 means incorrect language and correct meaning
# 3 means incorrect language and incorrect meaning

import sys
import subprocess

content = []
result = []

for idx, arg in enumerate(sys.argv):
    if not idx == 0:
        with open(arg) as inputFile:
            content = inputFile.readlines()
            for line in content:
                splitted = line.split("	")

                if splitted[0] != "Id":
                    # language
                    language = splitted[5].lower().replace('"', '')
                    meaning = splitted[6].lower().replace('"', '')                
                    label = '-1'
                    if 'correct' in language and 'correct' in meaning:
                        label = '1,0,0'
                    if 'incorrect' in language  and 'correct'in meaning:
                        label = '0,1,0'
                    if 'incorrect' in language and 'incorrect' in meaning:
                        label = '0,0,1'
                    line = ''
                    if len(result) < len(content):
                        line += splitted[0].replace('"','') + ',' + label + '\n'
                    else:
                        line += splitted[0].replace('"','') + ',' + label

                    result.append(line)

with open("gen_labeled_data.csv", 'w+') as outputFile:
    outputFile.writelines(result)
