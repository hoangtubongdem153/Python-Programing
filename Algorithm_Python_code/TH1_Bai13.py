import math
import random 
import time
from Thu_Vien.phepToanVoiSoNguyenLon import *
random.seed(time.time())

def isPrimeFermat(n,t):
    if n==2: return True
    if n<2: return False
    if n%2==0:
        return False
    for i in range(t):
        a= random.randint(2,n)
        if nhanBinhPhuongLap(a,n-1,n)!= 1:
            return False 
    return True

n = int(input('Nhập vào n: '))
if isPrimeFermat(n,10):
    print(f'{n} là số nguyên tố')
else:
    print(f'{n} không phải là số nguyên tố')