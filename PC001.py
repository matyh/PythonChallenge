# http://www.pythonchallenge.com/pc/def/map.html

import string

sentence = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc " \
           "dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr "\
           "gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw " \
           "ml rfc spj. "

# my first solution
newSentence = ""
chars = string.ascii_lowercase + "ab"
for char in sentence:
    if char in chars:
        newSentence += chars[chars.find(char) + 2]
    else:
        newSentence += char
print(newSentence)

# another solution
intab = string.ascii_lowercase
print(intab)
outtab = string.ascii_lowercase + "ab"
outtab = outtab[2::]
print(outtab)

print(sentence.maketrans(intab, outtab))

print(sentence.translate(sentence.maketrans(intab, outtab)))
