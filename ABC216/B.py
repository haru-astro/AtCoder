n=int(input())
st = [map(str,input().split()) for _ in range(n)]
s, t = [list(i) for i in zip(*st)]

for i in range(0,n-1):
    for j in range(1,n):
        if s[i]+t[i]==s[j-i]+t[j-1]:
            