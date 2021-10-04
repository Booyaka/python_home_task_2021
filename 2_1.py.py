"""Выяснить тип результата выражений:
15 * 3
15 / 3
15 // 2
15 ** 2

"""

example = [15 * 3, 15 / 3, 15 // 2, 15 ** 2]

for i, n in enumerate(example):
    print(example[i], type(n))