# 4 task
import sys


l1 = sys.argv[1]
l2 = sys.argv[2]
i = 0
rez = 0
for element in l1:
    for element in l2:
        if i < len(l1):
            if l1[i] != l2[i]: 
                rez = rez + 1
            i = i + 1
print rez
