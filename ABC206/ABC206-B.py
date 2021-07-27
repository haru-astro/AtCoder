a,b,c,d = map(int,input().split())
num = 0
while a+(num*b)>=num*c*d:
    num = num + 1
    if a+(num*b)-num*c*d < a+((num+1)*b)-(num+1)*c*d:
        print(-1)
        break
else:
    print(num)