n,x=map(int,input().split())
a = list(map(int,input().split()))

for i in range(n):
    if i %2==1:
        a[i]-=1
if sum(a)<=x:
    print("Yes")
else:
    print("No")
    
