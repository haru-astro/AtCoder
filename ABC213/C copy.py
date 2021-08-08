from bisect import bisect_left
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
    s=bisect_left(e,a[j])
    t=bisect_left(f,b[j])
    print(s+1 ,t+1)
