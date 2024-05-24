from Thu_Vien.soNguyenTo import *

def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

print('Nhập vào số nguyên dương n: ',end='')
n = laySoNguyenDuong()
prime = eratothenes(n)
res = []
emty = True
print('Các cặp số thoả mãn là: ')
for i in range(n+1):
    if prime[i]:
        res.append(i)
for i in range(0, len(res)-1):
    for j in range(i+1,len(res)):
        if isPrime(res[i]+res[j]) and isPrime(res[j]-res[i]):
            emty = False
            print(f'{res[i]},{res[j]}')
if emty:
    print('Không có cặp số nào.')
