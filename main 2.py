# name = "Виктор"
# age = 25
# # print("Меня зовут", name, ". Мне", age, "лет")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print()
# print("Меня зовут", name, ". Мне", age, "лет", sep="--", end="\n\n")
# print("Продолжение строки.")

# name = input("Введите имя: ")
# print("Hello, ", name, "!", sep="")

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# num = int(num)
# power = int(power)
# res = num ** power
# print(res)

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# num4 = int(input("Введите четвертое число: "))
#
# print(round(num1 + num2) / (num3 + num4), 2)

# b1 = True  # 1
# b2 = False # 0
# print(b1 + 5)
# print(b2 + 5)
#
# print(type(b1))

# False = "пустая строка", 0

# print(bool("Python")) # TRUE
# print(bool("")) # False
# print(bool(0)) # False
# print(bool(False)) # False
# print(bool(None)) # False

# a = None
# print(a)
# print(a is None)
# a = 5
# print(a)

# print(5 < 2)
# print("привет" > "ПРИВЕТ")

# print(2 < 4 > 9)  # True && False
# print(2 * 5 > 7 >= 4 + 3)  # True && True
# print(3 * 3 <= 7 >= 2)  # False

# a = 10
# b = 5
# c = a == b
# print(a, b, c) # 10 5 False

# && - and
# // - or
# ! - not

# print(5 - 3 == 2 or 1 + 3 ==4)

# print(not 9 - 5)

# cnt = 5
# if cnt < 10:
#     cnt += 1
#     print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 125
# b = 25
# if a > b:
#     print("a > b")
# elif b > a:
#     print("b > a")
# else:
#     print("a == b")

# a = 125
# b = 25
# if a > b:
#     print("a > b")
# if b > a:
#     print("b > a")
# if a == b:
#     print("a == b")


# a = int(input("Введите первую сторону: "))
# b = int(input("Введите вторую сторону: "))
# c = int(input("Введите третью сторону: "))
#
# if a == b == c:
#     print("Треугольник равносторонний")
# elif a == b or a == c or b == c:
#     print("треугольник равнобедренный")
# else:
#     print("треугольник разносторонний")

# day = int(input('Введите день недели цифрой: '))
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня не существует")

# month = int(input("Введите месяц цифрой: "))
# if month == 1 or month == 2 or month == 12:
#     print("зима")
# elif 3 <= month <= 5:
#     print("весна")
# elif 6 <= month <= 8:
#     print("лето")
# elif 9 <= month <= 11:
#     print("осень")
# else:
#     print("несуществующий месяц")

# _________________________23.06.2023____________________________________

# n = int(input("Введите количество ворон от 0-9: "))
# if 0 <= n <= 9:
#     print("На ветке", end=" ")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# password = 'qwerty'
#
# match password:
#     case 'admin':
#         print('Учетная запись администратор')
#     case 'user':
#         print('Пользователь')
#     case 'moderator':
#         print('Модератор')
#     case _:
#         print('Пароль не верен')

# day = "вторник"
# time = 17
#
# match day:
#     case 'понедельник' | 'вторник' | 'среда' | 'четверг' | 'пятница' if 9 <= time <= 16:
#         print("рабочий день")
#     case 'суббота' | 'воскресенье':
#         print("выходной день")
#     case _:
#         print("такого дня не существует или не рабочее время")

# Тернарное выражение

# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 30, 40
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a, b = 20, 0
# print("На 0 делить нельзя" if b == 0 else a / b)
# print(a / b)
# print("Код ниже")

# try:   # попытаться
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:    # исключение
#     print("Что-то пошло не так")

# try:
#     n = int(input("введите делимое: "))
#     m = int(input("введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("нельзя делить на 0")

# try:
#     n = int(input("введите делимое: "))
#     m = int(input("введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки. Нельзя делить на 0")
# else:  # срабатывает когда в блоке try не возникло исключение
#     print("Все нормально. Вы ввели числа", n, "и", m)
# finally:  # выводится в любом случае
#     print("конец программы")

# a = input("Введите первое значение: ")
# b = input("Введите второе значение: ")
#
# try:
#     a = int(a)
#     b = int(b)
# except ValueError:
#     a = str(a)
# finally:
#     print(a + b)

# i = 0
# while i < 5:
#     print("i =", i)
#     i += 1

# итерация - один шаг цикла

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i, end=" ")
#     i += 1

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2:
#         res += a
#     a += 1
# print("Сумма целых нечетных чисел:", res)

# n = input("Введите целое число: ")
#
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("число не целое")
#         n = input("Введите целое число: ")
#
# if n % 2 == 0:
#     print("четное")
# else:
#     print("нечетное")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# res = 1
# while True:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     res *= n
# print(res)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл завершен, i=", i)

# ________________________________________________22.06.23___________________________________________

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while i < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 1
# while i <= 5:
#     j = 1
#     while j <= 16:
#         if i % 2:
#             print("+", end="")
#         else:
#             print("-", end="")
#         j += 1
#     print()
#     i += 1

# for element in collection:
#   тело цикла

# for i in "Helloe!":
#     print(i)

# for color in 'red', 'bleu', 'green':
#     print(color)

# for element in range(start, stop, step):
#   тело цикла

# for i in range(1, 15, 2):
#     print(i, end=" ")
#
#
# print()
#
# i = 1
# while i < 15:
#     print(i, end=" ")
#     i += 2

# a = int(input("Введите целое число: "))
# for i in range(1, a + 1):
#     if a % i == 0:
#         print(i, end=" ")

# a = int(input("Ведите целое от 10 до 100: "))
# for i in range(10, 100):
#     if i % 10 == i // 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print("Done!")

# w = int(input("Введите ширину прямоугольника: "))
# h = int(input("Введите высоту прямоугольника: "))
#
# for i in range(h):
#     for j in range(w):
#         if i == 0 or j == 0 or i == h - 1 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# a = [letter * 2 for letter in "Hello"]
# print(a)

# num = [i for i in range(20) if i % 2 == 0]
# print(num)

#  Список (list)
# nums = [8, 3, 4, 1, 9, "Hello", 2.5]
# #      [0, 1, 2, 3, 4,    5,     6]
# #      [-7,-6,-5,-4,-3,  -2,    -1]
# print(nums)
# # print(type(nums))
# # print(nums[0])
# # print(nums[-1])
# # print(nums[3])
# # nums[3] = 256
# # nums[0] += 100
# # print(nums)
# print(len(nums))

# s = []
# print(s)
# print(type(s))
#
# b = list('Hello')
# print(b)
# print(type(b))

# n = list(range(2, 10, 3))
# print(n)

# n = 5
# a = [i for i in range(1, n + 1)]
# print(a)

# a = [i * 3 for i in 'list']
# print(a)

# a = [1, 2, 3]
# b = [4, 5]
# c = a + b
# print(c)
# d = c * 3
# print(d)


# a = [0] * int(input("Количество элементов в списке: "))
# # print(a)
# for i in range(len(a)):
#     a[i] = input("->")
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Количество элементов в списке: ")))]  !!ВАЖНО!!!!!!
# print(a)


# a = ['один', 'два', 'три', 'четыре', 'пять']
#
# for i in range(len(a)):
#     print(a[i], end=" ")
# print()
# for el in a:
#     print(el, end=" ")

# a = [int(input("-> ")) for i in range(int(input("n = ")))]
# print(a)
# s = 0
# for i in range(len(a)):
#     if a[i] < 0:
#         s += a[i]
# print("Сумма отрицательных элементов = ", s)

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количество четных элементов: ", k)
# print("Количество нечетных элементов: ", s)

# a = [int(input("-> ")) for i in range(int(input("n : ")))]
# print(a)
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end=" ")
# -------------------------------------------27.06.23------------------------------------

# a = int(input("Число от 1 до 99: "))
# kop = a
# if 11 <= kop <= 14:
#     print(a, "копеек")
# else:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")

# import math
#
#
# num1 = math.sqrt(4)
# num2 = math.ceil(3.2)
# num3 = math.floor(3.8)
# num4 = math.pi
# print(num1)
# print(num2)
# print(num3)
# print(num4)

# from math import *
#
# num2 = ceil(3.2)
# num3 = floor(3.8)
#
# print(num2)
# print(num3)


# import time

# sec = time.time()
# print(sec)
# local = time.ctime(787883562)
# print(local)
# res = time.localtime()
# print(res.tm_year)

# import time
# import locale
#
# locale.setlocale(locale.LC_ALL, "ru")

# print(time.strftime("Сегодня %B %d, %Y", time.localtime(787883562)))
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime(787883562)))
# print("Программа запустилась...")
# time.sleep(5)
# print("Программа завершилась")

# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# print("Время выполнения программы", finish - start, "секунд")

# Срезы: список[start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# a = s[0:4:1]
# print(a)

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# # print(s[::-1])
# # print(s[::2])
# # print(s[1::2])
# # print(s[:1])
# # print(s[6:7])
# # print(s[3:4])
# # print(s[4::1])
# # print(s[4:1:-1])
# # print(s[2:5])
# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3:5] = []
# print(s)
# del s[0]
# print(s)

#  Методы списков
# s = [1, 2, 3, 4, 5, 6, 7]
# print(s)
# s.append(99)  # Добавляет элемент в конец списка
# print(s)
# s.extend([8, 9, 10])  # добавляет в список итерируемый объект (несколько элементов)
# print(s)
# s.extend("add")
# print(s)
# s.insert(5, 100)  # добавляет элемент в список, первый параметр - индекс, второй параметр - добавляемое значение
# print(s)

# s = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print(x, "не делится на 3 без остатка")
# print(s)


# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)  # [2, 1, 4, 3]

# a = [1, 2, 3]
# b = [11, 22, 33, 44, 55]
# c = []
#
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append((a[i]))
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

# s = [4, 0, 2, 0, 3, 0, 6, 0, 0, 7]
# s.remove(0)  # удаляет первый найденный элемент из списка по заданному значению
# print(s)
# last = s.pop()  # удалил последний элемент из списка и вернул удаляемое значение
# print(last)
# print(s)
#
# last = s.pop(-3)  # удалил последний элемент из списка
# print(last)
# print(s)
#
# s.clear()  # очищает список
# print(s)

# a = [int(input("-> ")) for i in range(int(input("Количество элементов в списке: ")))]
# print(a)
# print("Введите индекс: ")
# k = int(input("k = "))
# a.pop(k)
# print(a)

# s = [4, 0, 2, 0, 3, 0, 6, 0, 0, 7]
# print(s)
# num = s.count(0)  # считает количество заданных элементов в списке
# print(num)
# ind = s.index(0, 2)  # возвращает индекс первого найденного элемента по его значению
# print(ind)
# -----------------------------------------29.06.23-----------------------------------------

# a = [1, 2, 3]
# b = a.copy()
# print("a =", a, id(a))
# print("b =", b, id(b))
# a.append(20)
# print("a =", a, id(a))
# print("b =", b, id(b))
# b.append(30)
# print("a =", a, id(a))
# print("b =", b, id(b))

# a = [1, 2, 3]
# a.reverse()  # перестраивает элементы списка в обратном порядке
# print(a)

# s = [9, 7, 3, 8, 4, 2, 6]
# s.sort(reverse=True)  # сортировка (по умолчанию - по возрастанию, reverse=True - сортировка по убыванию)
# print(s)

# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len, reverse=True)
# print(s2)

# Генерация случайных данных

import random
from random import *

# print(random())
# print(randint(5, 9))
# print(randrange(2, 9, 2))  # randrange(start, stop, step)
# print(uniform(10.5, 25.5))

# city = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(choices(city, k=3))
#
# s = [55, 66, 77, 88, 99, 4, 7, 9, 4, 5, 6, 1, 2, 7, 3]
# print(choices(s, k=5))
from random import randint

# a = [randint(50, 100) for i in range(10)]
# print(a)


# lst = [5, 3, 4, 2, 1, 8, 7, 9, 6, 0]
# print(len(lst))
# print(min(lst))
# print(max(lst))
# print(sum(lst))

# a = [randint(1, 100) for i in range(10)]
# print(a)
# m = max(a)
# print("MAX:", m)
# a.remove(m)
# a.insert(0, m)
# print(a)

# a = [randint(1, 100) for i in range(10)]
# print(a)
# minim = min(a)
# print("Min:", minim)
# ind = a.index(minim)
# print("Индекс:", ind)
# del a[:ind]
# print(a)

# x = list('1a2b3c4d')
# print(x)
# print('a' not in x)
# print('x' in x)

# lst = []
# if len(lst) == 0:
#     print("Список пустой")

from random import randint

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# # c = a + b
# # print("Третий список: ", c)
# # c = []
# # for i in range(len(a)):
# #     if a[i] not in c:
# #         c.append(a[i])
# # for i in range(len(b)):
# #     if b[i] not in c:
# #         c.append(b[i])
#
# # c = []
# # for i in range(n1):
# #     if a[i] in b and a[i] not in c:
# #         c.append(a[i])
# # print("Третий список: ", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print("Третий список: ", c)

from random import randint

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(m)
# print()
# # print(m[1][2])
# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t\t")
#     print()

# -----------------------------------------------04.07.2023---------------------------------------

# Функции
# print()


# def hello(name, word):  # аргументы
#     print("Hello", name, "Say", word)
#
#
# hello("Irina", "hi")  # параметры

# def getSum(a, b):
#




# -----------------------------------------------06.07.2023-------------------------------

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(type(tpl))
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = tuple()
# print(a)
# print(type(a))

from random import randint

# s = tuple([randint(0, 10) for i in range(5)])
# print(s)

# t1 = tuple("Hello")
# t2 = tuple("World")
# t3 = t1 + t2
# print(t3)
# print(t3.count('a'))
# ch = 'w'
# if ch in t3:
#     print(t3.index(ch))
# else:
#     print("такого символа нет")

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1) + 1
#             return second
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 2, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

#-------------------------------------------13.07.2023-----------------------------------------

#-------------------------------------18.07.2023-------------------------------------------

