s=input()
l=[]
for i in range(len(s)):
    for j in range(len(s-1)):
        l.append(s[i])
        l.append(s[i]+s[j+2])
        
g=list(set(l))
print(len(g)%(1**9+7))