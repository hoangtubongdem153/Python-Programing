import math
def isPrime(n):
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True
n = int(input('Nhập vào n: '))
if isPrime(n):
    print(f'{n} là số nguyên tố')
else:
    print(f'{n} không phải là số nguyên tố')