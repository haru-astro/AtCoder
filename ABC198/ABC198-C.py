import math
r,x,y=map(int,input().split())
d=math.sqrt(x*x+y*y)
if d==r:
    print(1)
elif d<=2*r:
    print(2)
else:
    print(math.ceil(d/r))