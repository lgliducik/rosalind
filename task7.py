

f = open("test_7.txt",'r')
count_GC = 0
i = 0
str_ = []
while 1:
    str1 = f.readline()
    if str1 == "": 
    	 print str_[-1],count_GC
         break
    str2 = f.readline()
    if str2 == "": break
    count_next = float(str2.count("G")+str2.count("C"))/float(len(str2))
    
    if count_GC < count_next:
        count_GC = count_next 
        str_.append(str1)
    i = i + 1