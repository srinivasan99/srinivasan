s9=int(input())
flag2=0
if(s9>2):
    for i in range(2,int(s9/2)+1):
        if s9%i==0:
            print("yes")
            flag2=1
            break
if flag2==0 or s9==2:
    print("no")
