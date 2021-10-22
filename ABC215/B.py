import math
n=int(input())
nas=0
if n>2**32:
    print(59)
else:
    for i in range(1,60000):
        g=i**2
        nas+=1
        if g>n:
            break

        print(nas-1)
