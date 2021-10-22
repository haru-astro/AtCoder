n=int(input())
a=list(map(int,input().split()))
l=[]
for i in range(0,2001):
    l.append(a.count(i))
for j in range(1,101):
    if j in l:
        print(l.index(j))
        break

