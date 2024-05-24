import math
def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

def nhanBinhPhuongLap(a,k,n):
    b=1
    if (k==0):
        return (b)
    A = a
    t = round(math.log2(k))
    if (k%2==1):
        b=a
    k=k>>1
    for i in range(1,t+1):
        A = A**2 % n
        if (k%2==1):
            b = A*b % n
        k=k>>1
    return b
def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True
print('Nhập vào a: ')
a = laySoNguyenDuong()
print('Nhập vào k: ')
k = laySoNguyenDuong()
print('Nhập vào n: ')
n = laySoNguyenDuong
if isPrime(nhanBinhPhuongLap(a,k,n)):
    print(f'{a}^{k} mod {n} là một số nguyên tố')
else:
    print(f'{a}^{k} mod {n} không phải là một số nguyên tố')
