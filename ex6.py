#task 6
import sys


strin = sys.argv[1]
strSub = sys.argv[2]
cur = 0
current = 0
for i in range(len(strin) - len(strSub)):
    newS = strin[current:len(strin)]
    ind = newS.find(strSub)
    current = current + cur + ind + 1
    if ind != -1:
        print current
