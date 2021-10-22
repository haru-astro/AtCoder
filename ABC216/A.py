import math

a=float(input())

x=int(a)
y=math.floor((a-int(a))*10)

if 0<=y and y<=2:
    print(str(x)+'-')
elif 3<=y and y<=6:
    print(x)
else:
    print(str(x)+'+')
