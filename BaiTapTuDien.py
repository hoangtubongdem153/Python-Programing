# Khoi tao tu dien
tuDien = {'cat':'con meo'}
#Xay dung cac tuy chon
print('---------TU-DIEN---------')
print('1. Them mot tu vung')
print('2. Tra cuu nghia')
print('3. Cap nhat nghia')
print('4. Xoa mot tu vung')
print('5. Xoa toan bo tu vung')
print('6. In ra toan bo tu vung')

while(True):
       x= int(input("Nhap lua chon: "))
       if (x==1):
              y = input('Nhap tu vung: ')
              z = input('Nhap nghia: ')
              tuDien.update({y:z})
       elif(x==2):
              y = input('Nhap tu vung can tra: ')
              z = print('Nghia cua {0} la :{1} '.format(y, tuDien.get(y)))
       elif(x==3):
              y = input('Nhap tu can cap nhat nghia: ')
              z = input('Nhap nghia moi: ')
              tuDien.update({y : z})
              print('Cap nhat thanh cong')
       elif(x==4):
              y = input('Nhap tu can xoa: ')
              tuDien.pop(y)
              print('Da xoa')
       elif(x==5):
              y = input('Xac nhan (yes) hoac huy bo (no): ')
              if(y=='yes'):
                     tuDien.clear()
                     print('Da xoa toan bo tu vung')
              else : continue
       elif(x==6):
              print(tuDien)
       else: print('Lua chon khong hop le ! ')
       k = input('Nhap bat ky de tiep tuc (thoat - q): ')
       if(k=='q'):
              break
       else: continue
       