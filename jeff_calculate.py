  v,n=[int(i) for i in input().split()]
   for i in range(n):
   j=input().split()
   t=j[0]
   a=int(j[1])
   if t=="W":v-=a
   else:v+=a
  print(v)

#another zum Biespiel 

# v, n = [int(i) for i in input().split()]
# for i in range(n):
#     it = input().split()
#     t = it[0]
#     a = int(it[1])
#     v = v + a if t == "D" else v - a
# print(v)
