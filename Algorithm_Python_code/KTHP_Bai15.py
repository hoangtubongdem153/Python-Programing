from Thu_Vien.soNguyenTo import *
def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

print('Nhập vào số nguyên dương n: ',end='')
n = laySoNguyenDuong()
prime = eratothenes(n)
print('Các cặp số thoả mãn là')
emty = True
pre = -1
for i in range(3,n+1,2):
    if prime[i]:
        if pre != -1:
            emty=False
            print(f'({pre},{i})')
        pre = i
    else:
        pre = -1
if emty:
    print('Không có cặp số nào.')