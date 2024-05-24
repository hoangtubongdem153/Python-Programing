from Thu_Vien.soNguyenTo import *
from Thu_Vien.euclid import *
def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

print('Nhập vào a: ')
a = laySoNguyenDuong()
print('Nhập vào b: ')
b = laySoNguyenDuong()
prime = eratothenes(b)
emty = True
print('Các cặp số thoả mãn: ')
for i in range(a,b):
    for j in range(i+1,b+1):
        if prime[gcd(i,j)]:
            emty = False
            print(f'({i},{j})',end=' ')
if emty:
    print('Không có cặp số nào')


