s1,s2=map(int,input().split())
nnn=[]
tt=[]
gcd=1
for i in range(1,s1+1):
    if(s1%i==0):
        nnn.append(i)
for j in range(1,s2+1):
    if(s2%j==0):
        tt.append(j)
for y in nnn:
    if y in tt:
        gcd=gcd*y
print(gcd)
