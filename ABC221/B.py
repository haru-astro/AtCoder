import copy
s=list(input())
t=input()
s1=copy.copy(s)
si="".join(s1)
if si==t:
    print("Yes")
    exit()
for i in range(len(s)-1):
    s=0
    ss=0
    s=copy.copy(s1)
    ss=copy.copy(s1)
    s.pop(i)
    s.insert(i+1,s1[i])
    ss="".join(s)
    if ss==t:
        print("Yes")
        break
else:
    print("No")
