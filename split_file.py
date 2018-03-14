import sys

parameter = sys.argv
filename = parameter[1]
modulator = int(parameter[2])

newTestFile = str(modulator) + '_' + filename
newTrainFile = str(100 - modulator) + "_" + filename

extractcontent = []
leftovercontent = []

with open(filename) as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
for a in xrange(0, len(content)):
    if((a % (100 / modulator)) == 0):
        extractcontent.append(content[a])
    else:
        leftovercontent.append(content[a])

tenpercentfile = open(newTestFile, 'w+')
for item in extractcontent:
  tenpercentfile.write("%s\n" % item)

nintyperentfile = open(newTrainFile, 'w+')
for item in leftovercontent:
  nintyperentfile.write("%s\n" % item)
  
nintyperentfile.close()
tenpercentfile.close()
f.close()