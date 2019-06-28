n9=int(input(""))
if n9>1:
	for i in range (2,n9):
		if(n9%i)==0:
			print("no")
			break
	else:
		print("yes")
else:
	print("no")
