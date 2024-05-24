from Thu_Vien.soNguyenTo import *

def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

print('Nhập vào số nguyên dương n: ',end='')
n = laySoNguyenDuong()
print(f'Các số T-Prime nhỏ hơn hoặc bằng {n}: ')
prime = eratothenes(int(math.sqrt(n)))
emty = True
for i in range(len(prime)):
    if prime[i]:
        print(i*i,end=' ')
        emty=False
if emty:
    print('Không có số nào.')