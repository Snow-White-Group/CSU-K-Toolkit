# 1 correct language
# 0 incorrect language

import sys
import subprocess

content = []
result = []

for idx, arg in enumerate(sys.argv):
        if not idx == 0:
                isFirst = True
                with open(arg) as inputFile:
                        content = inputFile.readlines()
                        for line in content:
                                splitted = line.split("	")
                                if(isFirst):
                                        isFirst = False
                                else:
                                        id = splitted[2][1:-1].split('.wav')[0]
                                        if '_' in id:
                                                partOfId = id.split('_', 1)[0].split('-')[1]
                                                fixpartOfId = partOfId
                                                if len(partOfId) == 2:
                                                        fixpartOfId = '0' + partOfId
                                                if len(partOfId) == 1:
                                                        fixpartOfId = '00' + partOfId
                                                id = id.replace(partOfId, fixpartOfId, 1)

                                        # language
                                        language = splitted[5].lower().replace('"', '')                            
                                        label = -1
                                        if 'correct' in language:
                                                print(id + ' is labeld as 1')
                                                label = 1
                                        if 'incorrect' in language:
                                                print(id + ' is labeld as 0')
                                                label = 0
                                    
                                        result.append(id + ',' + str(label) + '\n')

with open("grammer_label.csv", 'w+') as outputFile:
    for entry in result:
                outputFile.write(entry)
print('saved output to: grammer_label.csv') 