from Thu_Vien.soNguyenTo import *
n = int(input('Nhập vào n: '))

#---    Cách thông thường
print('Cách thông thường:')
for i in range(2,n+1):
    if isPrime(i):
        print(i,end=' ')
print()
#----	Sàng Erosthenes
print('Sàng Erosthenes:')
prime_Erosthenes = eratothenes(n)
for i in range(len(prime_Erosthenes)):
    if prime_Erosthenes[i]:
        print(i,end=' ')
print()
#---    Sàng phân đoạn
print('Sàng phân đoạn:')
prime_phan_doan = eratothenesPhanDoan(n)
for i in range(len(prime_Erosthenes)):
    if prime_phan_doan[i]:
        print(i,end=' ')
print()