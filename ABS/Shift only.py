n=int(input())
l=list(map(int,input().split()))
c=2
ans=[]
for i in range(n):
    a=0
    while l[i]%c==0:
        l[i]/=c
        a+=1
    ans.append(a)
ans.sort()
print(ans[0])