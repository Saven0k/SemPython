# Дорабатываем класс прямоугольник из прошлого семинара. Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника. Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    """
    Class Rectangle
    """

    def __init__(self,
                 length_cm: float,
                 width_cm: float = None) -> None:
        self.lenth = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm

    def calc_len(self):
        return (self.width + self.lenth) * 2

    def calc_square(self):
        return self.width * self.lenth

    def __add__(self, other):
        return Rectangle(length_cm=
                         abs(self.lenth + other.lenth),
                         width_cm=self.width)

    def __sub__(self, other):
        return Rectangle(length_cm=
                         abs(self.lenth - other.lenth),
                         width_cm=self.width)

    def __eq__(self, other: "Rectangle"):
        return self.calc_square() == other.calc_square()

    def __lt__(self, other):
        return self.calc_square() < other.calc_square()

    def __gt__(self, other):
        return self.calc_square() > other.calc_square()

if __name__ == '__main__':
    r1 = Rectangle(2, 2)
    r2 = Rectangle(3)
    r3 = r2 + r1

    print(f'{r3.calc_len() = }')
    print(f'{r3.calc_square() = }')

    print(r2 > r1)
    print(r2 < r1)
    print(r2 == r1)
    print(r2 != r1)
    print(r1 > r2)
    print(r1 < r2)
