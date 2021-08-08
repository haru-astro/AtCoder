from math import factorial
n=int(input())
c=list(map(int,(input().split())))
an=1
ans=0
for i in range(n):
    if c[i]>=n:
        an=1
        an=factorial(c[i])//factorial(n)//factorial(c[i]-n)
        ans+=an
print(ans)


