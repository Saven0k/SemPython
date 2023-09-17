# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.


# Задание №5
# Доработаем прямоугольник и добавим экономию памяти
# для хранения свойств экземпляра без словаря __dict__.

# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.
from Side import *

class Rectangle:
    """
    Class Rectangle
    """
    __width__ = Side(0, 7)
    __length__ = Side(2, 10)

    def __init__(self,
                 length_cm: float,
                 width_cm: float = None) -> None:
        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm

    @property
    def get_length(self):
        return self.length

    @get_length.setter
    def get_length(self, new_length):
        if new_length < 0:
            raise ValueError("не может быть меньше нуля")
        else:
            self.lenth = new_length



    @property
    def get_width(self):
        return self.width

    @get_width.setter
    def get_width(self, new_width):
        if new_width < 0:
            raise ValueError("< 0")
        else:
            self.width = new_width

    def calc_len(self):
        return (self.width + self.length) * 2

    def calc_square(self):
        return self.width * self.length

    def __add__(self, other):
        return Rectangle(length_cm=
                         abs(self.lenth + other.length),
                         width_cm=self.width)

    def __sub__(self, other):
        return Rectangle(length_cm=
                         abs(self.lenth - other.length),
                         width_cm=self.width)

    def __eq__(self, other: "Rectangle"):
        return self.calc_square() == other.calc_square()

    def __lt__(self, other):
        return self.calc_square() < other.calc_square()

    def __gt__(self, other):
        return self.calc_square() > other.calc_square()

    def __repr__(self):
        return f'Rectangle(length_cm={self.length}, ' \
               f'width_cm={self.width})'

    def __str__(self):
        return f'Длинна: {self.length}, ' \
               f'Ширина: {self.width}.'


if __name__ == '__main__':
    r1 = Rectangle(length_cm=2,
                   width_cm=11)
    print(r1)
    # r2 = Rectangle(3)
    # r3 = r2 + r1
    #
    # print(f'{r3.calc_len() = }')
    # print(f'{r3.calc_square() = }')
    #
    # print(r2 > r1)
    # print(r2 < r1)
    # print(r2 == r1)
    # print(r2 != r1)
    # print(r1 > r2)
    # print(r1 < r2)
    #
    # print("Check get-set\n")
    # print(r1.length, r1.width)
    # r1.lenth = 5
    # r1.width = 2
    #
    # print(r1.length, r1.width)
    #
    # r1.lenth = -1
    #
    # print(r1.length, r1.width)



