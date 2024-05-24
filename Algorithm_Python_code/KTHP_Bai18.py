from Thu_Vien.phepToanVoiSoNguyenLon import *
w=8
p=2147483647
a = int(input('Nhập vào a: '))
b = int(input('Nhập vào b: '))

arrA = convertDecimalToWordByte(a,w,p)
arrB = convertDecimalToWordByte(b,w,p)

e,sum = additionInFp(arrA,arrB,w,p)
print('Tổng trên trường Fp:')
print('Dạng ma trận: ',sum)
print('Dạng số nguyên',convertWordByteToDecimal(sum,w,p))

