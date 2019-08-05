import sys, string, math
k = input()
L = []
for c in k :
    k = ord(c) + 3
    if k > ord('Z') : k -= 26
    L.append(chr(k))
k2 = ''.join(L)
print(k2)
