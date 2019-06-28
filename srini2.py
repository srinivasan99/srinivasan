s9=input()
flag=1
vow=['a','e','i','o','u']
for v in vow:
    if(s9==v):
        print("Vowel")
        flag=0
        break
if(flag):
    if(s9>='a' and s9<='z'):
        print("Consonant")
    else:
        print("invalid")
