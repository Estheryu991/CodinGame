import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
day = input()
funkiness = float(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if day == 'friday':
    if funkiness >= 7:
        print((n-1) * 'FUNKY MONKEY FRIDAY ' + 'FUNKY MONKEY FRIDAY') 
    else:
        print((n-1) * 'funky monkey friday ' + 'funky monkey friday')
else:
    if funkiness >= 7:
        print ((n-1) * 'MONKEY ' + 'MONKEY')
    else:
        print((n-1) * 'monkey ' + 'monkey')

