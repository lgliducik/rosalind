# coding: utf-8

# 3 task
l = input()
f = open("test.txt",'w')
i = 0
newl = []
for element in l:
    if l[i] == "A": 
        newl.append('T')
        i = i + 1
    else:
        if l[i] == "C": 
            newl.append('G')
            i = i + 1
        else:
            if l[i] == "T": 
                newl.append('A')
                i = i + 1
            else:
                if l[i] == "G": 
                    newl.append('C')
                    i = i + 1
rev = newl[::-1]
for i in range(len(rev)):
    f.write(rev[i])
print rev

