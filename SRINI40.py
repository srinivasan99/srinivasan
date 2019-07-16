zub=input()
o9=0
for i in range(len(zub)):
    if (zub[i].isalpha() or zub[i].isnumeric() or zub[i]==" "):
      continue
    o9=o9+1
else:
    print(o9)
