import sys, string, math
sr = int(input())
rev = 0
while sr :
    rev = rev*10 + sr%10
   sr //= 10
print(rev)
