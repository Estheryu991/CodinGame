import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = input().split()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

starts=""
ends=""
for i in range(len(s)):
    starts += s[i][0]
for i in range(len(s)-1, -1, -1):
    ends += s[i][-1]
print(starts+ends)
