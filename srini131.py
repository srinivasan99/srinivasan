import sys, string, math
b = int(input())
m = b
L = []
for i in range( 2,m) :
    if b%i == 0 : L.append(i)
    while b%i == 0 : b //= i
if len(L) == 0 : print(m)
else :           print(*L)
