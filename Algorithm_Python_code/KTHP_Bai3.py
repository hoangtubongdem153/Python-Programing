from Thu_Vien.soNguyenTo import *
def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

print('Nhập vào số nguyên dương n: ',end='')
n = laySoNguyenDuong()
k,q,p,s=0,0,0,0
for i in range(1,n+1):
    if n%i==0: 
        p+=i
        s+=1
        if isPrime(i):
            k+=1
            q+=i
print('Giá trị cần tính =',end=' ')
print(n+p+s-q-k)