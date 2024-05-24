def isQPrime(n):
    count = 2
    for i in range(2, n):
        if n % i == 0:
            count += 1
    return count == 4

n = int(input("Nhập vào số N: "))
emty = True
print(f"Các số Q-Prime nhỏ hơn hoặc bằng {n} là: ")
for i in range(2, n+1):
    if isQPrime(i):
        emty = False
        print(i, end=' ')
if emty:
    print("Không có số nào")
