n=int(input())
d=[int(input())for i in range(n)]
d.sort()
e=[]
for j in range(n):
    if d[j] not in e:
        e.append(d[j])
print(len(e))