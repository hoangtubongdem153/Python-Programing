from Thu_Vien.soNguyenTo import *
from math import *
def laySoNguyenDuong():
    n = int(input())
    while n<=0:
        n = int(input('Vui lòng nhập vào một số nguyên dương: '))
    return n

def main():
    print('Nhập vào n: ')
    n = laySoNguyenDuong()
    prime = eratothenes(n)
    res = []
    for i in range(n):
        if prime[i]:
            res.append(i)
    emty = True
    for i in range(0,len(res)-2):
        for j in range(i+1,len(res)-1):
            if res[i]+res[j] >= n: break
            for k in range(j+1,len(res)):
                tmp = res[i] + res[j] + res[k]
                if tmp == n:
                    print(f'{n} = {res[i]} + {res[j]} + {res[k]}')
                    emty = False
                if tmp > n:
                    break
    if emty: print('Không thể tách.')
main()