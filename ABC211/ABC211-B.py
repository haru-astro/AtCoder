s = [0]*4
for i in range(4):
    s[i] = input()
s.sort()
if s == ['2B','3B','H','HR']:
    print("Yes")
else:
    print("No")