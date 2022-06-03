q = int(input())
a = []
for _ in range(q):
    a.append(input())

l=[]
for i in range(q):
    if a[i]!='READ':
        l.append(a[i])
    else:
        print(l[len(l)-1])
        l.pop(-1)

