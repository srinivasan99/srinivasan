import sys,string, math,itertools

l,k = input().split()
l,k = int(n),int(k)
L1 = [ int(x) for x in input().split()]
L2 = [ int(x) for x in input().split()]
L3 = []
for i in range(0,k) :
    L1.append(L2[i])
    L3.append(max(L1))
print(*L3)
