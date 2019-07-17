#N
SR=0
Num = int(input(""))
DI= 0
while(Num > 0):
    SR= Num % 10
    DI = DI+SR
    Num = Num //10
print(DI)
