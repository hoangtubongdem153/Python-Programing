from Thu_Vien.phepToanVoiSoNguyenLon import *
p,w = 2147483647,8

a = int(input('Nhập vào a: '))
print(convertDecimalToWordByte(a,w,p))

b=[]
print("Nhập vào ma trận: ")
for i in range(4):
   b.append(int(input())) 
print(convertWordByteToDecimal(b,w,p))