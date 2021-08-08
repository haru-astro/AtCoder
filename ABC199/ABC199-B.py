n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
ans=-max(a)+min(b)
if ans>=0:
    print(ans+1)
else:
    print(0)