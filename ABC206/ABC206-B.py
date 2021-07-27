a,b,c,d = map(int,input().split())
num = -1
diff = c*d-b
if 0<diff:
    num = (a+diff-1)//diff
print(num)