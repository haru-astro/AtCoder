n=int(input())
s=list(input())
q=int(input())
t = [0] * q
a = [0] * q
b = [0] * q
for i in range(q):
    t[i], a[i], b[i] = map(int, input().split())

for j in range(len(t)):
    if t[j]==1:
        g=list(s)
        s[a[j]-1]=g[b[j]-1]
        s[b[j]-1]=g[a[j]-1]
    else:
        f=list(s)
        s[:n]=f[n:]
        s[n:]=f[:n]
print(''.join(s))