NOW=list(input())
le=len(NOW)
if le%2==0:
	d=le//2
	NOW[d-1]=NOW[d]='*'
else:
	d=le//2
	NOW[d]='*'
print(*NOW,sep="")
