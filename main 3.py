#  ************************************   18.07.2023   ЗАМЫКАНИЯ   *****************************

# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner
#
#
# i = outer(5)
# print(i(10))
#
#
# j = outer(6)
# print(j(20))
#
#
# print(outer(4)(6))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func("Москва")
# res1()
# res1()
# res2 = func("Сочи")
# res2()
# res2()
# res1()

# students = {
#     "Alice": 98,
#     "bob": 67,
#     "Chris": 85,
#     "David": 75,
#     "Ella": 54,
#     "Fiona": 35,
#     "Grace": 69
# }
#
#
# # def make(lower, upper):
# #     def inner(exam):
# #         return {k: v for k, v in exam.items() if lower <= v < upper}
# #
# #     return inner
# #
# #
# # bal_A = make(80, 100)
# # bal_B = make(70, 80)
# # bal_C = make(50, 70)
# # bal_D = make(0, 50)
# # print(bal_A(students))
# # print(bal_B(students))
# # print(bal_C(students))
# # print(bal_D(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a + b
#
#     def replace():
#         print()
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())  # сумма
# print(obj1.sub())  # разность
# print(obj1.mul())  # произведение

#  *******************************  Анонимные функции  (Lambda - выражения)  ************

# def summa(x, y):
#     return x + y
#
#
# print(summa(1, 2))
#
# print((lambda x, y: x + y)(1, 2))
# print((lambda x=5, y=7: x + y)())
# print((lambda *args: sum(args))(1, 7, 8, 9, 4, 5, 6))


# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4)
#
#
# for t in c:
#     print(t("abc_"))

# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(42)
# print(f(1))
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer(42)
# print(f1(1))
#
# outer2 = lambda n: lambda x: x + n
#
# f2 = outer(42)
# print(f2(1))
#
# print((lambda n: lambda x: x + n)(42)(1))
#
# print((lambda n: lambda x: lambda y: x + n + y)(2)(4)(6))

# d = {'c': 10, 'a': 15, 'b': 4}
# q = list(d.items())
# print(q)
# q.sort(key=lambda i: i[1], reverse=True)
# print(q)
# d1 = dict(q)
# print(d1)

# players = [
#     {'name': 'Антон', 'last name': 'Бирюков', 'rating': 9},
#     {'name': 'Алексей', 'last name': 'Бодня', 'rating': 10},
#     {'name': 'Федор', 'last name': 'Сидоров', 'rating': 4},
#     {'name': 'Михаил', 'last name': 'Семенов', 'rating': 6},
# ]
#
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
#
# res2 = sorted(players, key=lambda item: item['rating'], reverse=True)
# print(res2)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[3](12, 5)
# print(b)

# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье'),
#
# }
#
#
# d[2]()

# # map(func, iter), filter(func, iter)
#
# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, 5, 10]
# # a = list(map(mult, lst))
# a = list(map(lambda t: t * 2, lst))
# print(a)

# t = (2.88, -1.75, 100.55)
#
# t2 = tuple(map(lambda x: int(x), t))
# print(t2)
# t3 = tuple(map(int, t))
# print(t3)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# filter(func, item)

# t = ('abcd', 'abc', 'cdert', 'def', 'gfi')
#
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)

# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: (s > 75) and s < 80, b))
# print(res)


#  *************************************  20.07.2023  Декоратор  ***********************

# def hello():
#     return 'Hello "hello"'
#
#
# def super_func(func):
#     print('Hello "super_func"')
#     print(func())
#
#
# super_func(hello)

# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print("code after")
#
#     return wrap
#
#
# def func_test():
#     print("Hello 'func_test'")
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('*' * 20)
#         func()
#         print('=' * 20)
#
#     return wrap
#
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print("Hello 'func_test'")
#
# @my_decorator
# def hello():
#     print('Hello "hello"')
#
#
# func_test()
# hello()

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     c = 0
#
#     def wrap():
#         nonlocal c
#         c += 1
#         fn()
#         print("Вызов функции:", c)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print(arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Резникова")

# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print('kwargs', kwargs)
#         fn(*args, **kwargs)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_full_name("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_full_name("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)


# def multiply(arg):  # 3
#     def outer(func):  # return_num
#         def wrap(*args, **kwargs):  # num
#             return arg * func(*args, **kwargs)
#
#         return wrap
#     return outer
#
#
# @multiply(3)
# def return_num(num):
#     return num

#
# print(return_num(5))
# def typed(*args, **kwargs):
#     def outer(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Неверный тип данных")
#
#                 for k in kwargs:
#                     if type(f_kwargs[k]) != kwargs[k]:
#                         raise TypeError("Неверный тип данных", kwargs[k])
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return outer
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello!"):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, "!"))
#
# print(typed_fn2("Hello", "world", "!"))
# # print(typed_fn2(6, 4, 2))
#
# print(typed_fn3("Hello", "world", z=5))

# # print(int('100', 2))
# # print(int('100', 8))
# # print(int('100', 16))
#
# print(bin(18))  # 0b10010
# print(oct(18))  # 0o22
# print(hex(18))  # 0x12
#
# print(0b10010 + 0o22)

# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# # print(e * 3)
# # print("t" in e)
# print(e[1])

# print("C:\\folder\\file.txt")
# print(r"C:\folder\file.txt")

# name = "Дмитрий"
# age = 25
# print("Меня зовут", name, '\b.', "Мне", age, "лет.")
# print(f"Меня зовут {name}. Мне {age} лет.")

# print(f"Число: {5 + 5}")
# print(f"Число: {10 / 3:.2f}")

#  ********************************  25.07.2023                  *******************

# x = 10
# y = 5
# print(f"{x=} x {y} / 2 = {x * y / 2}")

# dir_name = 'my_doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')
# print(r'home' + "\\" + dir_name + "\\" + file_name)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)

# s = "Test string for me"
# arr = [ord(x) for x in s]
# print("ASCII коды:", arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print("Среднее арифметическое:", arr)
# arr += [ord(x) for x in input("-> ")[:3] if ord(x) not in arr]
# print(arr)
# print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(1055))

# a = 97
# b = 122
# if b > a:
#     a, b = b, a
# for i in range(b, a + 1):
#     print(chr(i), end=" ")
#
# # if a > b:
# #     for i in range(b, a):
# #         print(chr(i), end=" ")
# # else:
# #     for i in range(a, b + 1):
# #         print(chr(i), end=" ")

# from random import randint
#
# SHORTEST = 8
# LONGEST = 16
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():
#     rand_len = randint(SHORTEST, LONGEST)
#     res = ""
#     for i in range(rand_len):
#         rand_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         # print(rand_char)
#         res += rand_char  # res = res + rand_charq
#
#     return res
#
#
# print("Ваш случайный пароль:", random_password())
# s = "hello, WORLD! I am learning Python!"
# # print(s.capitalize())
# # print(s.lower())
# # print(s.upper())
# # print(s.swapcase())
# # print(s.title())
#
# print(s.count("h", 1, -4))

#  **************************************** 15.08.23 ********************************
print("Hello git")
