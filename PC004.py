# http://www.pythonchallenge.com/pc/def/linkedlist.php

import requests
number = 3875
next = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist.php"
                    "?nothing=" + str(number)).text
print(next)

while True:
    if "Divide by two" in next:
        number /= 2
    else:
        number = int(next.split("next nothing is ")[-1])
    next = requests.get("http://www.pythonchallenge.com/pc/def/linkedlist"
                        ".php?nothing=" + str(number)).text
    print(next)
