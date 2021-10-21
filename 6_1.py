"""Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) —
получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
[
    ...
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('141.138.90.60', 'GET', '/downloads/product_2'),
    ('173.255.199.22', 'GET', '/downloads/product_2'),
    ...
]

"""

with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    line = f.readline()
    print(line)
    for line in f:
        my_tuple = line.split(" ")[0], line.split(" ")[5][1:], line.split(" ")[6]
        print(f'{my_tuple}, {type(my_tuple)}')  # Выводить списком не стал, как вы и говорили =)