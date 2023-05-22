n = int(input("Введите число: "))
i = 1
num = 0
while i < n:
    print(2 ** num, end=' ')
    i *= 2
    num += 1