# http://www.pythonchallenge.com/pc/def/integrity.html

from urllib.request import urlopen
import bz2


url = urlopen('http://www.pythonchallenge.com/pc/def/integrity.html').read()
un = str(url).split("un: \\'")[1].split("\\'")[0].replace('\\\\', "\\", -1)  # un as string
pw = str(url).split("pw: \\'")[1].split("\\'")[0].replace('\\\\', "\\", -1)  # pw as string
# convert to the same string as bytes (otherwise there would be double backslashes
un = un.encode('ISO-8859-1').decode('unicode-escape').encode('ISO-8859-1')
pw = pw.encode('ISO-8859-1').decode('unicode-escape').encode('ISO-8859-1')
username = bz2.decompress(un)
password = bz2.decompress(pw)

print("User name is:", str(username))
print("Password is:", str(password))
