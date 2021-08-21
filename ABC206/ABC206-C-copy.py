n=int(input())
a=list(map(int,input().split()))
a.sort()
allnum=len(a)*(len(a)-1)//2
b=list(set(a))
ans=0
for i in range(len(b)):
    s=a.count(b[i])
    ans=ans+(s*(s-1)//2)
print(allnum-ans)