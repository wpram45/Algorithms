import sys
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
   
    return [ atoi(c) for c in re.split('(\d+)', text) ]

n = int(input())

alist=[]
for i in range(n):
 
    alist.append(str(input()))

alist.sort(key=natural_keys)
print(*alist,sep="\n")