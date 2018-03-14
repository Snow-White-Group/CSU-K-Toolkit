import sys
import csv

parameters = sys.argv

contents = {}
result = {}

i = 0

for file in parameters[1:]:
	with open(file, 'r') as csv_file:
		reader = csv.reader(csv_file, delimiter = ',', quotechar = '"')
		contents[i] = set()
		for row in reader:
			for item in row:
				contents[i].add(item)
		i += 1

result = reduce(set.intersection, (val for val in contents.values()))
i =0
with open("intescting_ids.txt", 'w+') as intersecting_ids__file:
	for row in result:
		i += 1
		intersecting_ids__file.write(row + '\n')