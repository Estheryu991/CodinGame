import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

c = int(input())
h = input().split(',')
a = h.index('ID')
b = h.index('MEMBER_NUMBER')
d = {}
for i in range(c):
    r = input().split(',')
    d[r[b]] = d.get(r[b],[]) + [int(r[a])]
b = 0
for i in d.keys():
    l = d[i]
    if(len(l)>1):
        print(",".join(str(j) for j in sorted(l)))
        b=1
if not b:
    print("NONE")
