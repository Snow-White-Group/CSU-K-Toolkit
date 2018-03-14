# argv[1]: reads a csv file and splits it by mod 10
import sys

parameter = sys.argv
filename = parameter[1]
newfilename_10 = "10_" + filename
newfilename_90 = "90_" + filename

extractcontent = []
leftovercontent = []

with open(filename) as f:
    content = f.readlines()

# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
for a in xrange(0, len(content)):
    if(a % 10 == 0):
        extractcontent.append(content[a])
    else:
        leftovercontent.append(content[a])

tenpercentfile = open(newfilename_10, 'w+')
for item in extractcontent:
  tenpercentfile.write("%s\n" % item)

nintyperentfile = open(newfilename_90, 'w+')
for item in leftovercontent:
  nintyperentfile.write("%s\n" % item)

nintyperentfile.close()
tenpercentfile.close()
f.close()
