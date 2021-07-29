from math import factorial
p = int(input())
ans = 0

for i in range(1,11):
    mon = factorial(i+1)
    res = p%mon
    ans = res//factorial(i)
    p -= res
print(ans)