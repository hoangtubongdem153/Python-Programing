from Thu_Vien.soNguyenTo import *

a = int(input('Nhập vào A: '))
b = int(input('Nhập vào B: '))

prime = eratothenes(b)
sum=0
for i in range(a,b+1):
    if prime[i]:
        sum+=i

if isPrime(sum):
    print('YES')
else: 
    print('NO')
