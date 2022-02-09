import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
y = int(input())

for i in range(1000):
    if n**i==y:
        print(i)
        break
