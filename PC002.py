# http://www.pythonchallenge.com/pc/def/ocr.html

file = open("PC002_text.txt", "r")
text = "".join(line for line in file)
text = text.replace("\n", "")

# make a dict with the count of occurrence of every character
counter = {}
for i in text:
    if i in counter.keys():
        counter[i] += 1
    else:
        counter[i] = 1

# filter out only characters occurring only once
for char in counter:
    if counter[char] > 1:
        text = text.replace(char, "")
    else:
        continue

print(text)

# more compact solution
text = ''.join([line.rstrip() for line in open('PC002_text.txt')])
counter = {}
for c in text:
    counter[c] = counter.get(c, 0) + 1
avg = len(text) // len(counter)
# regular dict in counter can be replaced by collections.OrderedDict() by
# which the next line would iterate only over the dict, thus making next line
# more efficient
print(''.join([c for c in text if counter[c] < avg]))

