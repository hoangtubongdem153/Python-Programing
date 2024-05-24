import random
import time
from Thu_Vien.soNguyenTo import *

random.seed(time.time())

n = int(input('Nhập vào số phần tử mảng: '))
arr = []
prime =[]
for i in range(n):
    x = random.randint(0,10**5)
    arr.append(x)
    if isPrime(x):
        prime.append(x)
print('Mảng sau khi sinh ngẫu nhiên: ')
print(arr)
if len(prime)==0: print('Không có số nguyên tố nào trong mảng')
else: 
    print('Các số nguyên tố trong mảng:')
    for i in prime:
        print(i,end=' ')
        