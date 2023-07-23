# Khai bao set
thungPhieu = set()
# Khai bao random
import random
# Khai bao Menu
while(True):
       print('---------MENU---------')
       print("1. Them mot so dien thoai")
       print("2. Xoa mot so dien thoai")
       print("3. Xem sdt du thuong")
       print("4. Quay so trung thuong")
       x= int(input("Nhap lua chon cua ban: "))
       if( x==1):
              sdt = input("Nhap so dien thoai: ")
              thungPhieu.add(sdt)
       elif( x==2):
              if(len(thungPhieu) ==0):
                     print("Chua co so du thuong!")
                     continue
              else:
                     sdt = input("Nhap so dien thoai can xoa: ")
                     thungPhieu.discard(sdt)
       elif(x==3):
              if(len(thungPhieu) ==0):
                     print("Chua co so du thuong!")
                     continue
              else:
                     print("Cac so tham gia du thuong la: ")
                     for sdt in thungPhieu:
                            print(sdt)
       elif(x==4):
              i = random.randint(0, len(thungPhieu)-1)
              thungPhieulist  = list(thungPhieu)
              print("Chuc mung nguoi co sdt {0} da trung thuong".format(thungPhieulist[i]))
              thungPhieu.discard(thungPhieulist[i])
       else: print("Lua chon khong hop le !")
       temp = input("Nhap bat ky de tiep tuc !")