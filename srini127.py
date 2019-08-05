import sys, string, math
l = input()
dic1 = {}
for c in l :
    if c in dic1 :
        dic1[c] += 1
    else :
        dic1[c] = 1
f = 0
for x in dic1 :
    if dic1[x] > f :
        f = dic1[x]
        key = x
print(key)
