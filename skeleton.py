n=int(input())
p=input().index('#')
a=0
for i in range(n):
 l=r=-1
 s=input()
 for j in range(len(s)):l=(l,j)[s[j]!='.'and l<0]
 for j in range(len(s)-1,-1,-1):r=(r,j)[s[j]!='.'and r<0]
 a+=l<p<r
 if p==l:a+=s[l]=='['
 if p==r:a+=s[r]==']'
print(a)
