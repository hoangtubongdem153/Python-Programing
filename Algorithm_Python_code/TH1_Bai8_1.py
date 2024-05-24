from Thu_Vien.euclid import *
p = int(input('Nhập vào p: '))
a = int(input('Nhập vào a: '))

gcd,x,y =extendEuclid(a,p)
if gcd == 1:
    print(f'{a}^-1 mod {p} = {x}')
else:
    print('Không tồn tại nghịch đảo')
