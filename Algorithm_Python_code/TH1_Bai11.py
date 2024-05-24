from Thu_Vien.soNguyenTo import *
n = int(input('Nhập vào n: '))
res = PollardsRho(n,1)
if res == -1:
    print('Không tìm thấy thừa số không tầm thường')
else:
    print(f"Thừa số không tầm thường của {n} là: {res}")