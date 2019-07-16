#a
a9=list(input())
b1=" "
for i in range(len(a9)):
    if b1 in a9:
        a9.remove(b1)
print(len(a9))
