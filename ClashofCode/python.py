Given a list of numbers, the score of the list is calculated as follows:

if a number appears an odd number of times in the list, add it to the score, else subtract it from the score.

You must output the score of the list

Line 1: An integer N
Line 2: A list of N integers

Sortie
Line 1 : The score

Contraintes
2 ≤ N ≤ 100
0 < integer < 1e6

Example

Entrée
2
100 100

Sortie
-200


import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in input().split():
    x = int(i)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print("answer")
