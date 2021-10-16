"""*(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
не используя ключевое слово yield.

"""

number = int(input('Give me a number: '))
print([_ for _ in range(1, number + 1) if _ % 2 != 0])