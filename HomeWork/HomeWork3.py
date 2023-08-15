k = int(input('Введите количество копеек (от 0 до 99): '))
if 0 <= k < 100:
    if (k == 1) or k in range(21, 92, 10):
        n = 1
        s = 'копейка'
    elif (2 <= k <= 4) or k in range(22, 93, 10) or k in range(23, 94, 10) or k in range(24, 95, 10):
        n = 1
        s = 'копейки'
    else:
        n = 1
        s = 'копеек'
else:
    n = 0
if n > 0:
    print(k, s)
else:
    print('Должно быть число от 0 до 99')
