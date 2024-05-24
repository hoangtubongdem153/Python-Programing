from Thu_Vien.soNguyenTo import *
from math import *

a = int(input('Nhập vào A: '))
b = int(input('Nhập vào B: '))

prime = eratothenes(b)
res=[]

print("Các số thoả mãn: ")
for i in range(1,ceil(sqrt(b))):
    if i*i<b:
        for j in range(1,ceil(sqrt(b))):
            if (a<=i*i+j*j<=b) and prime[i*i+j*j]:
                res.append(i*i+j*j)
res =[int(i) for i in set(res)]
res.sort()
if len(res)==0:
    print('Không có số nào')
else:
    for i in res:
        print(i,end=' ')

        


