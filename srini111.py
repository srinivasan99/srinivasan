bhav,srini=map(int,input().split())
zen=list(map(int,input().split()[:srini]))
zig=[]
for i in zen:
   if(i<=i+1):
     zig.append(i)
print(zig[srini-1])
