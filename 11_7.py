"""Реализовать проект «Операции с комплексными числами». Создать класс «Комплексное число». Реализовать перегрузку
методов сложения и умножения комплексных чисел. Проверить работу проекта. Для этого создать экземпляры класса
(комплексные числа), выполнить сложение и умножение созданных экземпляров. Проверить корректность полученного
результата.

"""


class ComplexNumber:
    def __init__(self, num):
        self.num = num

    def __mul__(self, other):
        return ComplexNumber((self.num.real + other.num.real) * (self.num.imag + other.num.imag))

    def __floordiv__(self, other):
        return ComplexNumber((self.num.real + other.num.real) // (self.num.imag + other.num.imag))


comp_1 = ComplexNumber(1 + 2j)
comp_2 = ComplexNumber(2 + 4j)
print(comp_1 * comp_2)
print(comp_1 // comp_2)