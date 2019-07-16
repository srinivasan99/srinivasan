#N
ln=list(map(int,input().split()))
a9=ln[0]
b1=ln[1]
a9=a9^b1
b1=a9^b1
a9=a9^b1
print(a9,b1)
