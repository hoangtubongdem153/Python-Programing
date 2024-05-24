from Thu_Vien.soNguyenTo import *
from math import *
def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

print('Nhập vào n: ')
n = laySoNguyenDuong()

prime = eratothenes(int(sqrt(n)))

res = []
for i in range(len(prime)):
    if prime[i]:
        res.append(i**2)
#Cách 1
def isSnum(x):
    global res
    for i in range(len(res)):
        if res[i]>x: return False
        if x%res[i]==0: return True
    return False
print('Các số thoả mãn: ')
emty = True
for i in range(n):
    if isSnum(i):
        print(i,end=' ')
        emty = False
if emty:
    print('Không có số nào.')

# # Cách 2
# check = [False for i in range(n)]

# for i in res:
#     for x in range(i,n,i):
#         if check[x] == False:       
#             check[x] = True
#             print(x,end=' ')
        
