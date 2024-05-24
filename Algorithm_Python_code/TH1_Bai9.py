# Cài đặt chương trình tính nhân bình phương có lặp a^k mod n

from Thu_Vien.phepToanVoiSoNguyenLon import *
n = int(input('Nhập vào n: '))
a = int(input('Nhập vào a: '))
k = int(input('Nhập vào k: '))

print(f'{a}^{k} mod {n} =',nhanBinhPhuongLap(a,k,n))
