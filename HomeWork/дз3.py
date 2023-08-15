n = int(input("Введите количество копеек от 0 до 99: "))
if 0 <= n < 100:
    if (n == 1) or n in range(21, 92, 10):
        a = 1
        b = 'копейка'
    elif (2 <= n <= 4) or n in range(22, 93, 10) or n in range(23, 94, 10) or n in range(24, 95, 10):
        a = 1
        b = 'копейки'
    else:
        a = 1
        b = 'копеек'
else:
    a = 0
if a > 0:
    print(n, b)
else:
    print("Число должно быть от 0 до 99.")
