# /*The program: Your program must display the missing digit for each line.
#   INPUT:
# Line 1 : An integer N, the number of lines to read.
# N next lines : A string line of 9 digits without spaces.

# OUTPUT:
# Line 1 : The missing digit.

# CONSTRAINTS:
# 0 < N < 1000
# */

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    c=list(map(int,input()))
    print(next(i for i in range(10) if i not in c))
