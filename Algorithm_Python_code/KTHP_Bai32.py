import math
import time
import random
from Thu_Vien.euclid import *
random.seed(time.time())

def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

def RandomSearch(min,max):
    n=random.randint(min,max)
    for i in range(2,100):
        if n == i: continue
        if n % i ==0: return RandomSearch(min,max)
    if isPrime(n):
        return n
    return RandomSearch(min,max)
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
def getFn(p,q):
    return (p-1)*(q-1)
def getE(fn):
    for e in range(2,fn):
        if gcd(e,fn)==1:
            return e
def getD(e,fn):
    gcd,x,y = extendEuclid(e,fn)
    return x 
def getCipherRSA(plain,e,n):
    return nhanBinhPhuongLap(plain,e,n)
def getPlainRSA(cipher,d,n):
    return nhanBinhPhuongLap(cipher,d,n)
p = RandomSearch(100,500)
q = RandomSearch(100,500)
print(f'p,q = {p},{q}')
n = p*q
print('n =',n)
fn = getFn(p,q)
e = getE(fn)
d = getD(e,fn)
print('fn =',fn)
print('e =',e)
print('d =',d)
plain = int(input('Nhập vào bản rõ: '))
cipher = getCipherRSA(plain,e,n)
print('Bản rõ:',plain)
print('Bản mã: ',cipher)
print('Bản rõ sau khi giải mã: ',getPlainRSA(cipher,d,n))



