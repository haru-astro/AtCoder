n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(1,n+1):
    if a[i-1] > 10:
        sum += a[i-1] 
        sum -= 10
print(sum)
