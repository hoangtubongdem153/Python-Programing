from Thu_Vien.euclid import *
a = int(input('Nhập vào a: '))
b = int(input('Nhập vào b: '))

gcd,x,y =extendEuclid(a,b)
print('gcd =',gcd)
if gcd == 1:
    print('Nghịch đảo a =',x)
    print('Nghịch đảo b =',y)
