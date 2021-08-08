n=int(input())
a=list(map(int,input().split()))
a.sort(reverse=True)
b=0
c=0
for i in range(n):
    if i%2==0:
        b=b+a[i]
    else:
        c=c+a[i]
print(b-c)
