import math
import time
import random

random.seed(time.time())
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
def isPrimeMillerRabin(n,t):
    if (n==2): 
        return True
    if (n%2==0) or (n<3):
        return False
    #Phân tích n thành dạng r*2^s
    r = n-1
    s=0
    while (r%2==0):
       s+=1
       r = int(r/2)
    
    for i in range(t):
        a = random.randint(2,n-1)
        y = nhanBinhPhuongLap(a,r,n)
        if (y!=1) and (y!=(n-1)):
            j=1
            while (j<=s-1) and (y!=(n-1)):
                y = y**2 % n
                if y == 1:
                    return False
                j = j+1
            if y != (n-1):
                return False
    return True 
n = int(input('Nhập vào n: '))
if isPrimeMillerRabin(n,10):
    print(f'{n} là số nguyên tố')
else: 
    print(f'{n} không phải là số nguyên tố')
print(f'Xác suất để n là số nguyên tố là {1-(1/4)**10}')
#Xác suất để n là số nguyên tố là 1-(1/4)^t