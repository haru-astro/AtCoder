from bisect import bisect_left
n,m=map(int,input().split())
g=1000000000000
a=list(map(int,input().split()))
b=list(map(int,input().split()))+[-g,g]
a.sort()
b.sort()
ans=10000000000
for i in range(n):
    p=bisect_left(b,a[i])
    ans=min(ans,abs(b[p]-a[i]))
    ans=min(ans,abs(b[p-1]-a[i]))
print(ans)