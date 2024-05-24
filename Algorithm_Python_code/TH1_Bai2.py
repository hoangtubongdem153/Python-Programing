# Cho p=2147483647; W=8. Với t là độ dài từ của p, hãy nhập các giá trị a, b E [0, 2^Wt) từ bàn phím và AD thuật toán cộng chính xác bội 
# để thực hiện tính giá trị c, với c = a + b mod 2^Wt.

from Thu_Vien.phepToanVoiSoNguyenLon import *
(w,p)=(8,2147483647)
a = int(input('Nhập vào số a: '))
b = int(input('Nhập vào số b: '))
arrA = convertDecimalToWordByte(a,w,p)
arrB = convertDecimalToWordByte(b,w,p)
e,sum = addition(arrA,arrB,w,p)
print('Tổng chính xác bội =',e,sum)
