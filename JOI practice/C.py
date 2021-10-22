n,m = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

while len(a)==0 & len(b)==0:
    t=min([a[0],b[0]])
    print(t)
    if a[0]==t:
        a.pop(0)
    else:
        b.pop(0)
    
for i in range(len(a)):
    print(a[0])
    a.pop(0)
for i in range(len(b)):
    print(b[0])
    b.pop(0)