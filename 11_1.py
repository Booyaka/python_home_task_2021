"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый — с декоратором @classmethod. Он должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй — с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

"""


class Data:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def val(obj):
        if 0 < int(obj[:2]) <= 31 and 0 < int(obj[3:5]) <= 12 and 0 < int(obj[6:]) <= 2021:
            return 'Validation success!'

    @classmethod
    def spl(cls, data):
        my_data = data
        my_list = my_data.split('-')
        dig_list = []
        for _ in my_list:
            i = int(_)
            dig_list.append(i)
        return dig_list


print(Data.spl('11-10-2021'))
print(Data.val('11-10-2021'))