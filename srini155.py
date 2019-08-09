p=int(input())
m=list(map(int,input().split()))
m=sorted(m)
m=m[::-1]
q=0
for i in range(p):
   q=int(str(q)+str(m[i]))
print(q)
