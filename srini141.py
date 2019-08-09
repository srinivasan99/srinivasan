import sys
l=int(input())
m=list(map(int,input().split()))
for i in range(0,l):
    if m.count(m[i])==1:
        print(m[i])
        sys.exit()
print("unique")
