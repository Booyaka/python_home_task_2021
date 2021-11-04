from abc import abstractmethod, ABC


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    @abstractmethod
    def roar(self):
        pass


class Coat(Clothes):
    def roar(self):
        pass

    def sum(self, v):
        self.v = v
        result = v/6.5 + 0.5
        return result


class Costume(Clothes):
    def roar(self):
        pass

    def sum(self, h):
        self.h = h
        result = 2*h + 0.3
        return result


coat = Coat(0)
costume = Costume(0)
print(coat.sum(40) + costume.sum(170))