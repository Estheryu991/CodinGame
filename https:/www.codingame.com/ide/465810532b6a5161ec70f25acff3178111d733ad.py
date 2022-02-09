// Given a number N, print N minus N where all digits have been reversed.

// 2 -> (reversed) 2 -> 2-2 = 0
// 57-> (reversed) 75 -> 57-75 = -18
// Input
// Line 1: An integer N
// Output
// Line 1: N minus N where all digits have been reversed.
// Constraints
// 0 ≤ N ≤ 10000
// Example
// Input
// 7
// Output
// 0


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(n-int(str(n)[::-1]))

