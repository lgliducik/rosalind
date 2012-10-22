# coding: utf-8
import sys


# 2 task
l = sys.argv[1]
newl = l.replace('T','U')
f = open("test.txt",'w')
f.write(newl)
print newl
