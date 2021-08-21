s,t=map(int,input().split())
l=[]
for i in range(s+1):
    for j in range(s+1):
        for h in range(s+1):
            if i+j+h<=s and i*j*h<=t:
                l.append(h)
print(len(l))