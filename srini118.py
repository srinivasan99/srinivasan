import sys, string, math

def IsIso(string7, string8):
    m = len(string7)
    n = len(string8)
    if m != n:
        return False
    marked = [False] * 256
    map = [-1] * 256
    for i in range(n):
        if map[ord(string7[i])] == -1:
            if marked[ord(string8[i])] == True:
                return False
            marked[ord(string8[i])] = True
            map[ord(string7[i])] = string8[i]
        elif map[ord(string7[i])] != string8[i]:
            return False
    return True

# Driver program
s7,s8 = input().split()
if IsIso(s7,s8) : print('yes')
else :            print('no')
