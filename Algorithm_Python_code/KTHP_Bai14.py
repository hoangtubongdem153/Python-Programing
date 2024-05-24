from Thu_Vien.soNguyenTo import *

def reverse_interger(n):
    r = 0
    while n>0:
        r = r*10 + n%10
        n=n//10
    return r
print('Các số thoả mãn là: ')
for i in range(100,1000):
    if isPrime(i):
        r = reverse_interger(i)
        if int(r**(1/3)) == (r**(1/3)):
            print(i,end=' ')
