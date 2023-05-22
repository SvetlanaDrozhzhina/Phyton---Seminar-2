summa = int(input("Введите сумму чисел: "))
proizvedenie = int(input("Введите произведение чисел: "))
stop = 0
for i in range(summa):
    if stop == 1:
        break
    for j in range(proizvedenie):
        if summa == i + j and proizvedenie == i * j:
            print(f"Первое число {i}, второе число {j} ")
            stop += 1
else:
    print("заданы не верные значения, повторите попытку")