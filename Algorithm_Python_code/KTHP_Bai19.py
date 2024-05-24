from Thu_Vien.soNguyenTo import *

a = int(input('Nhập vao A: '))
b = int(input('Nhập vao B: '))
c = int(input('Nhập vao C: '))
n = int(input('Nhập vao n: '))
m = int(input('Nhập vao m: '))

emty = True
for x in range(n,m+1):
    if isPrime(a*x*x+b*x+c):
        print(x,end=' ')
        emty=False
if emty:
    print('Không có giá trị nào')



        