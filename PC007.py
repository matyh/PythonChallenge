# http://www.pythonchallenge.com/pc/def/oxygen.html

from urllib.request import urlopen
import png, re

image = urlopen('http://www.pythonchallenge.com/pc/def/oxygen.png')
(w, h, rgba, _) = png.Reader(image).read()
mid = int(h / 2)
img = list(rgba)
print(img)
result = [img[mid][i] for i in range(0, len(img[mid]), 4 * 7) if
          img[mid][i] == img[mid][i + 1] == img[mid][i + 2]]
# print(result)
sentence = ''.join([chr(i) for i in result])
lastWord = ''.join([chr(int(i)) for i in re.findall('\d+', sentence)])
print(lastWord)
