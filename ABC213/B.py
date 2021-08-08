import copy
n=int(input())
a=list(map(int,input().split()))
b=copy.copy(a)
a.remove(max(a))
c=max(a)
print(b.index(c)+1)