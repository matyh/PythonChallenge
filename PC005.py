# http://www.pythonchallenge.com/pc/def/peak.html

from urllib import request
import pickle

link = request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
# print(link.read().replace('\n', ''))
data = pickle.load(link)
print(data)
for line in data:
    print(''.join([char * occurrence for char, occurrence in line]))


# try to reverse
channel = open('PC005_try.txt', 'r')
code = []
for line in channel:
    lineList = []
    for char in range(len(line)):
        if char not in lineList[:][0]:
            lineList.append((char, 1))
        else:
            lineList[-1] = (char, lineList[-1][1] + 1)
    print(lineList)
