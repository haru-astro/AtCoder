import math
import copy
import itertools
s,k=map(str,input().split())
k=int(k)
ans=0

ss=list(s)
ss.sort()
sss=list(s)
lista=[]

for i in range(len(ss)-1):
    ans=0
    t=itertools.permutations(len(ss)-1) 
    if k-t>=t:
        k=k-t
        ans+=1
        
    lista.append(ss[ans])
    ss.pop(ans)
lista.append(ss[0])
print("".join(lista))