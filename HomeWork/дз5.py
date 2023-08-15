
lst = [int(input("Введите элемент списка: ")) for i in range(int(input("Количество элементов в списке: ")))]

positive_lst = [num for num in lst if num > 0]

max_element = max(positive_lst)

print("Исходный список:", lst)
print("Список только с положительными элементами:", positive_lst)
print("Наибольший элемент:", max_element)
