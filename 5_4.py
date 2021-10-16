"""Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего,
например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]

Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно сделать оптимизацию
кода по памяти, по скорости.

"""
from time import perf_counter
from sys import getsizeof

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

start = perf_counter()
my_list = []
for i in range(1, len(src)):
    if src[i] > src[i - 1]:
        my_list.append(src[i])
print(f'{my_list}, {getsizeof(my_list)}, {perf_counter() - start}')

start = perf_counter()
my_list = []
my_comp = [my_list.append(src[i]) for i in range(1, len(src)) if src[i] > src[i - 1]]
print(f'{my_list}, {getsizeof(my_list)}, {perf_counter() - start}')