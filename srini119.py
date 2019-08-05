import sys, string, math
kk = input()
mm = list(s)
for i in range(0,len(mm),2) :
    mm[i],mm[i+1] = mm[i+1],mm[i]
res = ''.join(mm)
print(res)
