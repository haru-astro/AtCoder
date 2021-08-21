import copy
import math 
n=int(input())
a=list(map(int,input().split()))
b=copy.copy(a)
ans=0
for i in range(n):
    del a[0]
    c=copy.copy(a)
    if b[i] in a:
        while b[i] in c:
            c.remove(b[i])
        ans+=len(c)
    else:
        ans=ans+len(c)
print(ans)

