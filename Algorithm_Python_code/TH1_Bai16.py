from Thu_Vien.doiSanhMau import *

p = input('Nhập vào substring: ')
T = input('Nhập vào string: ')

position = backTrack(p,T)
if position == -1:
    print('Không tìm thấy chuỗi')
else:
    print('Tìm thấy chuỗi tại vị trí thứ',position)