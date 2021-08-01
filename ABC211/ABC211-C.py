n,k=map(int,input().split())
c=list(map(int,input().split()))
a=[]
b=0
for i in range(n-k+1):
    a=[]
    for j in range(k):
        if c[i+j] not in a:
            a.append(c[i+j])
            if b<len(a):
                b=len(a)
print(b)

