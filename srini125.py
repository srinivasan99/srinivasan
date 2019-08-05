import sys, string, math
o = int(input())
sm = 0
while o :
    a = n%10
    sm = sm + a*a
    o //= 10
print(sm)
