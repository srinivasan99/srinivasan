import sys, string, math
q,b = map(int,input().split())
k = 0
for i in range(q,b+1) :
    for j in range(2,i) :
        if i%j == 0 :
            break
    else :
        k += 1
print(k)
