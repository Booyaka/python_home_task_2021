"""Создать собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверить его работу на данных,
вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
завершиться с ошибкой.


"""


class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


num = int(input('Pls enter a number that we"ll divide by zero: '))
zero = 0
try:
    result = num / zero
    if zero == 0:
        raise MyOwnErr('Lol')
except (ZeroDivisionError, MyOwnErr) as err:
    print(f'But we cannot divide by zero: {err}')