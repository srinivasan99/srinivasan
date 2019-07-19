s1,l=map(int,input().split())
t=[]
m=[]
lcm=1
r=max(s1,l)
for i in range(1,r):
    if(s1%i==0 and l%i==0):
        t.append(i)
        s1=s1//i
        l=l//i
m.append(s1)
m.append(l)
for u in t:
    lcm=lcm*u
for r in m:
    lcm=lcm*r
print(lcm)
