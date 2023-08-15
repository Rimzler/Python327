def avg(fn):
    def wrap(*args):
        print("Среднее арифметическое:", fn(*args) / len(args))
    return wrap


@avg
def summa(*args):
    a = ""
    for i in args:
        a += str(i) + ", "
    print("Сумма чисел:", a[:-2], "=", sum(args))
    return sum(args)


summa(2, 3, 3, 4)
