from Thu_Vien.phepToanVoiSoNguyenLon import *
(w,p)=(8,2147483647)
a = int(input('Nhập vào số a: '))
b = int(input('Nhập vào số b: '))
arrA = convertDecimalToWordByte(a,w,p)
arrB = convertDecimalToWordByte(b,w,p)
e,sum = addition(arrA,arrB,w,p)
print('Tổng chính xác bội =',e,sum)