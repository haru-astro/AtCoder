l = [int(a) for a in input().split()]
l.sort()
if l[2]-l[1]==l[1]-l[0]:
    print("Yes")
else:
    print("No")