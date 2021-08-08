n,k=map(int,input().split())
a=list(map(int,input().split()))
b=a.sort()
#anが皆に配れた和
an=0
while k//n>=1:
    k=k-n
    an=an+1
ans=[]
#kが余った数
for i in (1,k):
    1+an.appned(b)
for j in (k+1,n):
    ans.appned(an)
print(ans)
