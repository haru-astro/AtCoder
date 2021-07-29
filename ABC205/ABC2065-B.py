n=int(input())
a=list(map(int,input().split()))
a.sort()
ans = list(range(1,n+1))
if ans==a:
    print("Yes")
else:
    print("No")