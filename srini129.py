import sys, string, math
s,b = map(int,input().split())
for i in range(max(s,b), s*b+1) :
    if (i%s== 0) and (i%b == 0) :
        ans = i
        break
print(ans)
