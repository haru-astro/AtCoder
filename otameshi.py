n=1000000000001
#
ans1=0
trueans=0
ans2=1
t=1
for i in range(n):
    ans1+=i
    trueans=i+1
    for j in range(n):
        ans2-=trueans
        while ans2<=ans1:
            ans2+=(1+t)
            t+=1
            if ans1==ans2:
                print(trueans)
                s=ans2
                break
            elif ans1<=ans2:
                s=ans2
                break
        if ans1<=ans2:
            break
