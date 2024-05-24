from math import sqrt
def isPrime(n):
    if n==0 or n==1: return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
def laySoNguyenDuong():
    n = int(input())
    while n<2 or n>10:
        n = int(input('Vui lòng nhập vào một số nguyên dương >=2 và <=10: '))
    return n

print('Nhập vào số nguyên dương n: ',end='')
n = laySoNguyenDuong()
print(f'Các số nguyên tố có {n} chữ số là: ')
for i in range(10**(n-1),10**n):
    if isPrime(i):
        print(i,end=' ')