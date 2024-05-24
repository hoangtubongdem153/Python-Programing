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
def isPrimeFermat(n,t):
    if n==2: return True
    if n<2: return False
    if n%2==0:
        return False
    for i in range(t):
        a= 2
        if nhanBinhPhuongLap(a,n-1,n)!= 1:
            return False 
    return True
n = int(input('Nhap vao n: '))
t = int(input('Nhap vao t: '))
if isPrimeFermat(n,t):
    print('la so nguyen to')
else:
    print('khong phai so nguyen to')
#Trong trường hợp n là số carmichael thì thuật toánn Fermat sẽ cho kết quả sai
#Điều kiện cần và đủ để hợp số n là số carmichael la:
#   Không phải là bình phương của một số
#   n-1 chia cho p-1 với mọi p là ước của n
