from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def cloth_calc(self):
        pass


class Coat(Clothes):
    def __init__(self, arg):
        self.cloth = arg

    @property
    def cloth_calc(self):
        tmp = round(self.cloth / 6.5 + 0.5, 1)
        return tmp


class Costume(Clothes):
    def __init__(self, arg):
        self.cloth = arg

    @property
    def cloth_calc(self):
        tmp = round(2 * self.cloth + 0.3, 1)
        return tmp


red_coat = Coat(49)
white_costume = Costume(1.75)

print(f'Summ cloth : {red_coat.cloth_calc + white_costume.cloth_calc}')
