import sys
import subprocess

seenIds = []
valid = True

for idx, arg in enumerate(sys.argv):
        if not idx == 0:
                isFirst = True
                with open(arg) as inputFile:
                        lines = inputFile.readlines()
                        for line in lines:
                                id = line.split(",")[0]
                                if(isFirst):
                                        isFirst = False
                                else:
                                        for seenId in seenIds:
                                                if seenId == id:
                                                        valid = False
                                                        break
                                        seenIds.append(id)
                        print('Result: ' + str(valid))