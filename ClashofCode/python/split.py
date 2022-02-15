a, b = [int(i) for i in input().split()]
print(chr((a*b)%26+97))
