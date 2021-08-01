n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
f=[]
for i in range(n):
    for j in range(m):
        c=abs(a[i]-b[j])
        f.append(c)
f.sort()
print(f[0])

