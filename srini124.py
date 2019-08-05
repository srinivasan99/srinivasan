import sys, string, math
b,k = map(int,input().split())
k = k%b
L = list(map(int,input().split()))
L2 = L[-k:] + L[:-k]
print(*L2)
