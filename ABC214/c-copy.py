import copy
from bisect import bisect_left
n=int(input())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
tt=copy.copy(t)
t.sort()
l=[]
ans=0
for i in range(len(t)):
    g=t[i]
    for j in range(len(t)-1):
        if g<=t[i+j+1]+s[i+j+1]:
            l.append(t[i+j+1]+s[i+j+1])
        else:
            l.append(g)
        if g>=t[i+j+1]+s[i+j+1]:
            break
    if len(l)<=n:
        break
print(l)    