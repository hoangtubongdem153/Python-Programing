import math
import random 
import time
random.seed(time.time())
def gcd(a,b):
    while b>0:
        tmp = a % b
        a = b
        b = tmp
    return a
#-----------------------------------------------------#  
def eratothenes(n):
    prime=[True for i in range(0,n+1)]
    prime[0] = False
    prime[1] = False
    p=2
    for p in range(2,n):
        if (prime[p]==True):
            for i in range(p*p,n+1,p):
                prime[i]=False
    return prime
#-----------------------------------------------------#  
        
def eratothenesPhanDoan(n):
    prime=[True for i in range(0,n+1)]
    delta = int(math.sqrt(n))
    tmp = eratothenes(delta)
    for i in range(delta+1):
        prime[i]=tmp[i] 
    for i in range(delta,n+1,delta): #Duyệt các phân đoạn
        # m: giá trị lớn nhất trong đoạn
        m = i + delta -1
        if m > n:
            m = n
        
        for j in range(2,int(math.sqrt(m))+1): #Duyệt các giá trị từ 2 đến căn(m)
            if prime[j]: # Nếu là số nguyên tố
                for p in range(i-i%j,m+1,j): #Duyệt các bội của số nguyên tố đó nằm trong phân đoạn đang xét
                    if (i<=p<=m):
                        prime[p]=False
    return prime
#-----------------------------------------------------#      
def isPrime(n):
    if n<2: return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0: return False
    return True

#-----------------------------------------------------#  
def phanTichThuaSoNguyenTo(n):
    if isPrime(n):
        print(n,'= 1 *',n)
        return
    prime = []
    f = []
    p=2
    x = n
    while p<=x: 
        count=0
        while x%p ==0:
            x=int(x/p)
            count+=1
        if (count > 0):
            prime.append(p)
            f.append(count)
        p+=1
    print(prime)
    print(f)
#-----------------------------------------------------#  
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
#-----------------------------------------------------#       

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
#---------------------------------------------------------#
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

#---------------------------------------------------------#
def PollardsRho(n,c):
    a,b =2,2
    if (c==10): return -1
    while (True):
        a = (a**2+c)%n
        b = (b**2+c)%n
        b = (b**2+c)%n
        d= gcd(abs(a-b),n)
        if 1<d<n: return d
        if d == n: return PollardsRho(n,c+1)

#---------------------------------------------------------#

def getRandomBit(k):
    return random.randint(0,2**k-1)

def RandomSearch(k,t):
    n=getRandomBit(k)
    for i in range(2,100):
        if n == i: continue
        if n % i ==0: return RandomSearch(k,t)
    if isPrimeMillerRabin(n,t):
        return n
    return RandomSearch(k,t)


    
#---------------------------------------------------------#


 


    
    
        
        
         
         
                
    
