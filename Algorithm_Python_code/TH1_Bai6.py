from Thu_Vien.phepToanVoiSoNguyenLon import *
w=8
p = int(input('Nhập vào p: '))
a = int(input('Nhập vào a: '))
b = int(input('Nhập vào b: '))

arrA = convertDecimalToWordByte(a,w,p)
arrB = convertDecimalToWordByte(b,w,p)

print('Tích của a và b =',multiprecision(arrA,arrB,w,p))
