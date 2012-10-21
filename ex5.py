l = input()
f = open("text.txt",'w')
alph = {
    'UUU': 'F',
    'CUU': 'L',
    'AUU': 'I',
    'GUU': 'V',
    'UUC': 'F','CUC' :'L','AUC': 'I',
'GUC': 'V','UUA': 'L','CUA' :'L','AUA' :'I','GUA' :'V', 'UUG' :'L','CUG' :'L',      
'AUG': 'M','GUG': 'V','UCU' :'S','CCU' :'P','ACU': 'T','GCU' :'A','UCC' :'S',
'CCC': 'P','ACC': 'T','GCC': 'A','UCA' :'S','CCA': 'P','ACA': 'T','GCA': 'A',
'UCG' :'S', 'CCG': 'P', 'ACG': 'T','GCG': 'A','UAU' :'Y', 'CAU' :'H','AAU': 'N',
'GAU' :'D','UAC' :'Y','CAC': 'H','AAC': 'N','GAC': 'D','UAA' :'Stop','CAA': 'Q',
'AAA': 'K','GAA': 'E','UAG' :'Stop','CAG' :'Q','AAG': 'K','GAG': 'E','UGU' :'C',
'CGU': 'R','AGU': 'S','GGU': 'G','UGC' :'C','CGC': 'R','AGC': 'S','GGC': 'G',
'UGA' :'Stop', 'CGA': 'R','AGA':'R','GGA': 'G','UGG' :'W','CGG': 'R','AGG': 'R','GGG': 'G' }


i = 0
newl = []
for element in l:
    if i<len(l)/3:

        newstr = l[ i * 3 : ( i + 1 ) * 3 ]
        s = alph[newstr]
        newl.append(s)
    i = i + 1
string = ''
ii = 0
for element in newl:
    if newl[ii] != 'Stop':
        string = string + element
        ii = ii + 1
print string
f.write(string)