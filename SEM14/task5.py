# Задание №5
# На семинарах по ООП был создан класс прямоугольник
# хранящий длину и ширину, а также вычисляющую периметр,
# площадь и позволяющий складывать и вычитать
# прямоугольники беря за основу периметр.
# Напишите 3-7 тестов unittest для данного класса.
import unittest
class Rectangle:
    """
    Class Rectangle
    """


    def __init__(self,
                 length_cm: float,
                 width_cm: float = None) -> None:
        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm


    def calc_len(self):
        return (self.width + self.length) * 2

    def calc_square(self):
        return self.width * self.length

    def __add__(self, other):
        return Rectangle(length_cm=
                         abs(self.length + other.length),
                         width_cm=self.width)

    def __sub__(self, other):
        return Rectangle(length_cm=
                         abs(self.length - other.length),
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

class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.r1 = Rectangle(length_cm=2)
        self.r2 = Rectangle(length_cm=2,width_cm=4)
        self.r3 = Rectangle(length_cm=2)

    def test_step_1(self):
        self.assertEqual(self.r1, self.r3)

    def test_step_2(self):
        self.assertTrue(self.r1 == self.r3, 'Dont corrent')


if __name__ == '__main__':
    unittest.main(['--vv'])
