n,k=map(int,input().split())
third=1
first=1 
sum=0
for i in range(1,n+1):
    sum+=i*100*k
for j in range(1,k+1):
    sum+=j*n
print(sum)
