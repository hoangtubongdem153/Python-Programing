from Thu_Vien.phepToanVoiSoNguyenLon import *
w=8
p = int(input('Nhập vào p: '))
a = int(input('Nhập vào a: '))
b = int(input('Nhập vào b: '))

arrA = convertDecimalToWordByte(a,w,p)
arrB = convertDecimalToWordByte(b,w,p)
print('Hiệu chính xác bôi a và b:',subtraction(arrA,arrB,w,p))

e,sub =  subtractionInFp(arrA,arrB,w,p)

print('Trừ trên trường Fp:')
print('Dạng ma trận: ',sub)
print('Dạng số nguyên: ',convertWordByteToDecimal(sub,w,p))