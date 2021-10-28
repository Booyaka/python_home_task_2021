"""Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3
a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
Сможете ли вывести имя функции, например, в виде:

"""
from functools import wraps


def type_logger(func):
    @wraps(func)
    def tag_logger(*args):
        makeup = func(*args)
        return print(makeup, type(makeup))

    return tag_logger


@type_logger
def calc_cube(x):
    return x ** 3


number = int(input('Pls enter a number: '))
calc_cube(number)
print(calc_cube.__name__)