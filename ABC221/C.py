import copy
n=sorted(input())
num=len(n)

ke=0
if num % 2==0:
    ke=num/2
else:
    ke=(num-1)/2

s1=[]
s2=[]

n.sort(reverse=True)

while len(n)>=2:
    if len(n)>=2:
        s1.append(n[0])
        n.pop(0)
        s2.append(n[0])
        n.pop(0)
    else:
        break
    if len(n)>=2:
        s2.append(n[0])
        n.pop(0)
        s1.append(n[0])
        n.pop(0)
    else:
        break


if num % 2 == 1:
    s1.append(n[0])

s1.sort(reverse=True)
s2.sort(reverse=True)

s12="".join(s1)
s13="".join(s2)

ss1=int(s12)*int(s13)

if num % 2 == 1:
    s2.append(s1[len(s1)-1])
s1.pop(len(s1)-1)
s1.sort(reverse=True)
s2.sort(reverse=True)

s12="".join(s1)
s13="".join(s2)

ss2=int(s12)*int(s13)

if ss2-ss1 >=1:
    print(ss2)
else:
    print


