n=input()
s='0'
l=[]
for i in range(10):
    g=s*i+n
    l.append(g)
h=[]
for j in range(len(l)):
    n=''.join(list(reversed(l[j])))
    h.append(n)
if len(set(l)&set(h))>=1:
    print("Yes")
else:
    print("No")