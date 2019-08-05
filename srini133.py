import sys, string, math

def collinear(r1, y1, x2, y2,x3, y3):
    if ((y3 - y2)*(x2 - r1) == (y2 - y1)*(x3 - x2)):
        return  "yes"
    else:
        return "no"


r1,y1 = map(int,input().split())
x2,y2 = map(int,input().split())
x3,y3 = map(int,input().split())
res = collinear(r1, y1, x2, y2, x3, y3)
print(res)

