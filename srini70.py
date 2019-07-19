s9=int(input())
flag2=0
if s9>2:
    for i in range(3,int(s9/2)):
        if N1%i==0:
            flag2=1
            print("no")
            break
if flag2==0 or s9==2:
    print("yes")
