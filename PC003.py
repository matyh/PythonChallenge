# http://www.pythonchallenge.com/pc/def/equality.html

text = ''.join([line.rstrip() for line in open('PC003_text.txt', 'r')])
result = ''
for i in range(len(text)):
    if text[i].islower():
        if (text[i - 3:i] + text[i + 1:i + 4]).isupper() and (text[i-4] + text[i+4]).islower():
            result += text[i]

print(result)
