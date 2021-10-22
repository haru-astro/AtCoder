import copy
s=list(input())
g=len(s)
t=copy.copy(s)
l=[]
for i in range(g):
    s.pop(0)
    s.append(t[0])
    r="".join(s)
    t=copy.copy(s)
    l.append(r)
print(min(l))
print(max(l))