n=int(input())
t = [0] * n
x = [0] * n
y = [0] * n
for i in range(n):
    t[i], x[i], y[i] = map(int, input().split())
for i in n:
    if t[i]==(x[i]-y[i-1])+(y[i]-y[i-1]):
        continue
    else:
        break
