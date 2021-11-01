"""Реализовать класс Stationery (канцелярская принадлежность):
определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

"""


class Stationery:
    def __init__(self, title='a pig!'):
        self.title = title

    def draw(self):
        print(f'Just drawing {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Just drawing {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Just drawing {self.title}')


class Handle(Stationery):
    pass


pen = Pen('a cat!')
pen.draw()
pencil = Pencil('a dog!')
pencil.draw()
handle = Handle()
handle.draw()