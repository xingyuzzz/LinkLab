import json


def writetojsonfile(path, filename, data):
    filePathName = './' + path + '/' + filename + '.json'
    with open (filePathName, 'w')as f:
        json.dump(data, f)

path = './'
filename = 'calorValues.json'

with open("coordination.txt", "r") as file:
    List1 = file.readlines()
with open("Colorvalues.txt", "r") as file2:
    List2 = file2.readlines()
#strip the blank lines
position = []
colors = []
for i in List1:
    newline = i.rstrip()
    position.append(newline)
for i in List2:
    newline = i.rstrip()
    colors.append(newline)


colorList = {}
length = len(position)
flag = 0
while flag < length:
    colorList[position[flag]] = colors[flag]
    flag +=1



writetojsonfile(path, filename, colorList)



