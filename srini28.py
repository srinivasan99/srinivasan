import statistics
q=int(input()) 
l=list(map(int,input().split()))
print("%d"%(statistics.median(l)))
