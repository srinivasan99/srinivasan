bhav,srini=map(int,input().split())
man=input().split()
mah=[]
for p in man:
  if (int(p)%2!=0):
    mah.append(p)
print(mah[srini-1])
