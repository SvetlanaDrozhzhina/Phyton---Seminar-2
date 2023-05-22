n = int(input("Введите колличество монет на столе: "))
k = 0
for i in range(n):
    v = int(input("Сторона монеты (1 -герб; 0-решка): "))
    if v == 1:
        k += 1
print(k if k<n/2 else n-k)