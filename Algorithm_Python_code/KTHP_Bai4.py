from Thu_Vien.soNguyenTo import *
a = int(input('Nhập vào a: '))
b = int(input('Nhập vào b: '))

prime = eratothenes(b)
count = 0
for i in range(a,b+1):
    if prime[i]:
        count+=1
print(f'Số số nguyên tố nằm trong khoảng [{a},{b}] là {count}')