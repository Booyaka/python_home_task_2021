"""Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий
из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл. Проверить сохранённые
данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО, задаём в словаре
значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи считать, что объём данных
в файлах во много раз меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби  (hobby.csv):
скалолазание,охота
горные лыжи

"""

from itertools import zip_longest

with open('users.txt', 'r', encoding='utf-8') as f_users:
    read_users = f_users.readlines()

with open('hobby.txt', 'r', encoding='utf-8') as f_hobby:
    read_hobby = f_hobby.readlines()

with open('data.txt', 'w', encoding='utf-8') as f_data:
    # my_dict = {k: v for k, v in zip_longest(read_users, read_hobby)}
    my_dict = {}
    # print(dir(my_dict))
    for k, v in zip_longest(read_users, read_hobby):
        my_dict.setdefault(k, v)
    f_data.write(str(my_dict))