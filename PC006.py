# http://www.pythonchallenge.com/pc/def/channel.html
# http://www.pythonchallenge.com/pc/def/channel.zip to download the file

import zipfile

# first file number is 90052 as indicated  in the source of the default page
nextNo = 90052
# we need to extract comments from the relevant txt files in the zip file
file = zipfile.ZipFile('PC006.zip')
pairs = []
for i in range(len(file.infolist()) - 1):
    text = file.open(str(nextNo) + '.txt').read().decode()
    # print(text)
    comment = file.getinfo(str(nextNo) + '.txt').comment.decode()
    pairs.append((nextNo, comment))
    nextNo = text.split('nothing is ')[-1]
result = ''
for (x, y) in pairs:
    result += y
print(result)
