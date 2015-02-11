# small Python code to sort logs based on time-stamps
import re

# read lines from this file
fname="K:\Python\logs.txt"
with open(fname) as fd:
	lines_list = fd.readlines()
fd.close()

# check for timestamp. Store it in dictionary, sort and print them.
myDict = {}
for line in lines_list:
	match = re.search("OccurredAt: (\d+):(\d+):(\d+):(\d+),", line)
	if match:
		# Converting hour, minute and second into milliseconds (in that order)
		key = (match.group(1)*60*60*1000) + (match.group(2)*60*1000) + (match.group(3)*1000) + match.group(4)
		if key in myDict:
			myDict[key] = myDict[key] + "\r" + line[:-1]
		else:
			myDict[key] = line[:-1]
	else:
		print("*********** Something wrong !! *************** with data [" + line[:-1] + "]")

for temp in sorted(myDict.keys()):
	print(myDict[temp])