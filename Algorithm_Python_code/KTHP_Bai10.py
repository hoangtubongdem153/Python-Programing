from Thu_Vien.soNguyenTo import *
def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

print('Nhập vào số nguyên dương n: ',end='')
n = laySoNguyenDuong()
k,s=0,0
for i in range(1,n+1):
    if n%i==0: 
        s+=1
        if isPrime(i):
            k+=1
print(f'{n} có {s} ước số và {k} ước nguyên tố')