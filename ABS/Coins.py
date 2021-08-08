a=int(input())
b=int(input())
c=int(input())
x=int(input())

ans=0
for i in range(a+1):
    d=0
    d=x-(500*i)
    if d>=0 and 100*b+50*c>=d:
        for j in range(b+1):
            g=0
            g=d-(100*j)
            if g>=0 and g<=50*c:
                    ans=ans+1
print(ans)
    
