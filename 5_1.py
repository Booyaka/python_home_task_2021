"""Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
odd_to_15 = odd_nums(15)

"""


def my_gen(num):
    gen = (_ for _ in range(1, num + 1) if _ % 2 != 0)
    my_list = list(gen)
    new_list = []
    for _ in my_list:
        new_list.append(_)
    yield new_list


number = int(input('Give me a number: '))
print(*my_gen(number))


def my_other_gen(num):
    for el in range(1, num + 1):
        if el % 2 != 0:
            yield el


number = int(input('Give me a number: '))
for i in my_gen(number):
    print(i)