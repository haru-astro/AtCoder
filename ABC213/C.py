h,w,n=map(int,input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i], b[i]= map(int, input().split())

e=list(set(a))
f=list(set(b))
e.sort()
f.sort()

for j in range(n):
    s=e.index(a[j])
    t=f.index(b[j])
    print(s+1 ,t+1)

