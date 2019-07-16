srini,unknown=map(int,input().split())
for i in range(srini+1,unknown):
    s=0
    a=i
    while(a>0):
        c=a%10
        s+=c*c*c
        a//=10
    if(i==s):
      print(i,end=" ")
