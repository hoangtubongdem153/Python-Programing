from Thu_Vien.soNguyenTo import *
def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

print('Nhập vào số nguyên dương n: ',end='')
n = laySoNguyenDuong()
prime = eratothenes(n)
count=0
for i in range(n+1):
    if prime[i]:
        count+=1
print(f'Số các số nguyên tố nhỏ hơn hoặc bằng {n} = {count}')