from Thu_Vien.soNguyenTo import *
a = int(input('Nhập vào a: '))
b = int(input('Nhập vào b: '))

prime = eratothenesPhanDoan(b)
sum=0
for i in range(a,b+1):
    if prime[i]:
        sum+=i
print(f'Tổng các số nguyên tố nằm trong khoảng [{a},{b}] là {sum}')