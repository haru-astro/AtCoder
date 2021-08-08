n,y=map(int,input().split())
d=[-1]
e=[-1]
f=[-1]
for i in range(n+1):
    for j in range(n+1-i):
        k=n-j-i
        if 10000*i+5000*j+1000*k==y:
            d.append(i)
            e.append(j)
            f.append(k)
if len(d)>=2:
    print(d[1],e[1],f[1])
else:
    print(d[0],e[0],f[0])
    
