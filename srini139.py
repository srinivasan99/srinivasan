l=int(input())
x=[]
k=list(map(int,input().split()))
for i in range(0,l-1):
    for j in range(i+1,l):
        if k[i]==k[j]:
            x.append(k[j])
z=list(set(k)^set(x))
print(z[0])
