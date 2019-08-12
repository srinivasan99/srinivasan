sri=input()
m=0
for i in range(len(sri)-1):
    for j in range(i+1,len(sri)):
        k=sri[i:j]
        if k==k[::-1]:
            if len(k)>m:
                m=len(k)
print(m)
