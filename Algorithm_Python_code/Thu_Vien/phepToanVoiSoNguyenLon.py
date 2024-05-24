import math

def convertDecimalToWordByte(n,w,p):
    m= math.ceil(math.log(p,2))
    t = math.ceil(m/w)
    a=[]
    for i in range(0,t):
        a.append((n>>(w*i))&(2**w-1))
    a.reverse()
    return a 
def convertWordByteToDecimal(a,w,p):
    n=0
    m= math.ceil(math.log(p,2))
    t = math.ceil(m/w)
    for i in range(0,t):
        n=(n<<w) +a[i]
    return n
def addition(arrA,arrB,w,p):
    arrA.reverse()
    arrB.reverse()
    c=[]
    m= math.ceil(math.log(p,2))
    t = math.ceil(m/w)
    e=0
    for i in range(0,t):
        c.append((arrA[i]+arrB[i]+e)&(2**w-1))
        e=((arrA[i]+arrB[i]+e)>>w)&1
    c.reverse()
    arrA.reverse()
    arrB.reverse()
    return (e,c)
def subtraction(arrA,arrB,w,p):
    arrA.reverse()
    arrB.reverse()
    c=[]
    m= math.ceil(math.log(p,2))
    t = math.ceil(m/w)
    e=0
    for i in range(0,t):
       c.append((arrA[i]-arrB[i]-e)&(2**w-1))
       e=((arrA[i]-arrB[i]-e)>>w)&1
    c.reverse()
    arrA.reverse()
    arrB.reverse()
    return (e,c)
def multiprecision(arrA,arrB,w,p):
    arrA.reverse()
    arrB.reverse()
    m= math.ceil(math.log(p,2))
    t = math.ceil(m/w)
    c=[0 for i in range(0,2*t)]
    for i in range(0,t):
        u=0
        for j in range(0,t):
            sum = c[i+j] +arrA[i]*arrB[j]+u
            u = sum>>w
            c[i+j] = sum&0xff
        c[i+t] = u
    c.reverse()
    arrA.reverse()
    arrB.reverse()
    return (c)

def squaring(a,w,p):
    return multiprecision(a,a,w,p)

def additionInFp(arrA:list,arrB:list,w,p):
    e,arrC = addition(arrA,arrB,w,p)
    if (e == 1) or (convertWordByteToDecimal(arrC,w,p)>=p):
        arrP = convertDecimalToWordByte(p,w,p)
        return subtraction(arrC,arrP,w,p)
    return e,arrC
def subtractionInFp(arrA:list,arrB:list,w,p):
    
    e,arrC=subtraction(arrA,arrB,w,p)
    
    if (e == 1):
        arrP = convertDecimalToWordByte(p,w,p)
        return addition(arrC,arrP,w,p)
    return e,arrC
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


    