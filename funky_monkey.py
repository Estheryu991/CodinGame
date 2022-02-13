import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
day = input()
funkiness = float(input())

str = "funky monkey friday" if day=="friday" else "monkey";
#check if the day is monkey or Freitag 
if funkiness >= 7 : 
    str = str.upper()

for i in range(n-1):
    print(str,end=" ");
print(str);
