from Thu_Vien.soNguyenTo import *

l = int(input('Nhập vào L: '))
r = int(input('Nhập vào R: '))

prime = eratothenes(r)
res = []
for i in range(l,r+1):
    if prime[i]:
        res.append(i)


sum = 0

for i in range(0,len(res)-1):
    for j in range(i+1,len(res)):
        sum+= res[i]*res[j]
     
print('Tổng thoả mãn =',sum)
