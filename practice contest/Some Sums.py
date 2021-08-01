n,a,b=map(int,input().split())
c=list(range(1,n+1))
d=[]
for i in range(n):
    e=0
    f=0
    g=0
    h=0
    p=0
    e=c[i]//10000
    f=(c[i]-10000*e)//1000
    g=(c[i]-10000*e-1000*f)//100
    h=(c[i]-10000*e-1000*f-100*g)//10
    p=(c[i]-10000*e-1000*f-100*g-10*h)
    if e+f+g+h+p<=b and e+f+g+h+p >=a:
        d.append(c[i])
print(sum(d))
