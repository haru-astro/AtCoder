x=int(input())
if x%1111==0:
    print("Weak")
else:
    if x==1234 or x==2345 or x==3456 or x==4567 or x==5678 or x==6789 or x==7890 or x==8901 or x==9012 or x==123 :
        print("Weak")
    else:
        print("Strong")