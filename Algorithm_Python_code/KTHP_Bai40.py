from Thu_Vien.soNguyenTo import *
from Thu_Vien.euclid import *
def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

print('Nhập vào n: ')
n = laySoNguyenDuong()
print('Nhập vào mảng: ')
arr=[int(input()) for i in range(n)]
max=arr[0]
for i in range(1,n):
    if max<arr[i]: max = arr[i]
prime = eratothenes(max)
count =0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if prime[gcd(arr[i],arr[j])]:
            count+=1
print('Số cặp thoả mãn =',count)

