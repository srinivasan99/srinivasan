s1=list(input())
yy2=[]
for j in s1:
   if j not in s2:
      s2.append(j)
if s1==s2:
   print("Yes")
else:
   print("No")
