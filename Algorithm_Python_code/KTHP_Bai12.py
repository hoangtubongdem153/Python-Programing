from Thu_Vien.soNguyenTo import *

def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

print('Nhập vào số nguyên dương n: ',end='')
n = laySoNguyenDuong()
print('Nhập vào số nguyên dương lẻ k: ',end='')
k = laySoNguyenDuong()
prime = eratothenes(n)
res = []
for i in range(n+1):
    if prime[i]:
        res.append(i)
print('Các bộ số thoả mãn: ')
emty=True
for i in range(0, len(res)-k):
    sum=0
    for j in range(k):
        sum+=res[i+j]
    if sum <= n: 
        if prime[sum]:
            emty = False
            print(f'({res[i]}',end='')
            for j in range(1,k):
                print(f',{res[i+j]}',end='')
            print(')')
if emty:
    print('Không có bộ số nào.')
                 
