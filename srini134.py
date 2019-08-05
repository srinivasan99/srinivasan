import sys, string, math
l,b = map(int,input().split())
for i in range(1,min(l,b)+1) :
    if (l%i==0)  and (b%i==0) : ans = i
print(ans)
