import math
def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def reverse_interger(n):
    r = 0
    while n>0:
        r = r*10 + n%10
        n=n//10
    return r

def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

print('Nhập vào số nguyên dương n: ',end='')
n = laySoNguyenDuong()
print(f'Các số emirp nhỏ hơn hoặc bằng {n}: ')
emty = True
for i in range(2,n+1):
    if isPrime(i) and isPrime(reverse_interger(i)):
        print(i,end=' ')
        emty = False
if emty:
    print('Không có số nào.')