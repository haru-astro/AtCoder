n=int(input())
s=list(map(int,input().split()))
t=list(map(int,input().split()))
print(t[0])
l=[t[0]]
ans=t[0]
for i in range(len(t)):
    ans=t[i]
    if t[i-1]+s[i-1]<=ans:
        ans=t[i-1]+s[i-1]
        print(ans)
        l.append(ans)
    else:
        print(ans)
        l.append(ans)
    if len(l)>=n:
        break


