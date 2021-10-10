"""Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
num_translate("one")
"один"
num_translate("eight")
"восемь"

Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для перевода:
какой тип данных выбрать, в теле функции или снаружи.

"""


def num_translate(number):
    for k, v in num_dict.items():
        if number == k:
            return v


num_dict = {'null': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', "for": 'четыре', 'five': 'пять',
            'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
num = input('What is your favourite number between null and ten? ')
print(f'It is "{num_translate(num)}" in Russian you know')