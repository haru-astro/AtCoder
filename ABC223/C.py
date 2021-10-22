from bisect import bisect_left
n=int(input())
ab = [map(int, input().split()) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
l=[]
t=0
for i in range(n):
    t+=(a[i]/b[i])
    l.append(t)
#lは時間の和
l.append(0)
s=t/2
u=0
q1=bisect_left(l,s)
#q1q2は何番目にあるかq1が爆発するとこ
#listにおいてq1で爆発
#l[q1-1]は×発前までにかかった時間
for i in range(q1):
    u+=a[i]
g=t-l[q1]
h=l[q1-1]
asd=abs(h-g)
asdf=asd
ansss=(a[q1]-asd)/2
if h>=g:
    print(u+ansss)
else:
    print(u+ansss+asd)
