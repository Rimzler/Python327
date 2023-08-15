a = [int(input("-> ")) for i in range(int(input("Количество элементов в списке: ")))]
s = k = 0
for i in range(len(a)):
    if a[i] != 0:
        s += a[i]
        k += 1
print("Среднее арифметическое: ", s / k)
