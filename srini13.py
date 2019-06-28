n,q9=map(int,input().split())
if(q9<=100000):
    for x in range(n+1,q9):
        if(x%2!=0):
          print(x,end=" ")
