import math
def isF_number(n):
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum+=i
    return sum == n
def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

print('Nhập vào số nguyên dương n: ',end='')
n = laySoNguyenDuong()
print(f'Các số F-number nhỏ hơn hoặc bằng {n}: ')
emty = True
for i in range(2,n+1):
    if (isF_number(i)):
        print(i,end=' ')
        emty = False
if emty:
    print('Không có số nào.')
        
    