l=int(input ()) 
m=list(map(int, input ().split()))
x=[]
for i in range(0,l):
	if i==m[i]:
		x.append(i)
for i in range(0,len(x)):
	print(x[i],end=" ")
if len(x)==0:
	print("-1")
