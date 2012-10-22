#task 6
str = input()
strSub = input()
cur = 0
current = 0
for i in range(len(str) - len(strSub)):
    newS = str[current:len(str)]
    ind = newS.find(strSub)
    current = current + cur + ind + 1
    if ind != -1:
        print current
