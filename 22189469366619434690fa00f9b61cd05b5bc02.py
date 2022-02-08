import sys
import math
 
t=""
n = int(input())
l = [str(input()) for i in range(n)]
l.sort()
for i in range(len(l)) :
    t = ""
    l1 = [j for j in l[i] if 64 <= ord(j.upper()) <= 90]
    for j in range(len(l1)-1) :
        if l1[j] == l1[j+1] and l1[j] not in t:
            t+=l1[j]
    if t == "" :
        print("NONE")
    else :
        print(t)
