# Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.

import math
class Rectangle:

    def __init__(self,
                 length_cm: float,
                 width_cm: float = None) -> None:
        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm



    def check(self):
        try:
            if self.length > 0 and self.width > 0:
                return f'Треугольник со стронами {self.length} , {self.width} создан!'
            else:
                raise ValueError
        except ValueError:
            return f'Нельзя создать прямоугольник с сторонами < 0'

    def __repr__(self):
        return f'{self.length =}, {self.width =}'



def find_x(a: float, b: float, c: float) -> None:
    try:
        if isinstance(a, str) and  isinstance(b, str) and isinstance(c, str):
            raise ValueError
        else:
            d = (float(b) ** 2) - 4 * float(a) * float(c)
            if d < 0:
                return "Корней нет"
            elif d == 0:
                x = -float(b) / (2 * float(a))
                return (f"{x} - корень уравнения")
            elif d > 0:
                x_1 = str((-b + math.sqrt(d)) / 2 * a)
                x_2 = str((-b - math.sqrt(d)) / 2 * a)
                my_list = [x_1, x_2]
                return (f"{' , '.join(my_list)} - корни уравнения")
    except ValueError:
        return f'Надо передавать значения типа float or int'


if __name__ == '__main__':
    # #1

    r1 = Rectangle(length_cm=-3,
                   width_cm=-1)
    print(r1.check())

    #2
    print(find_x("12", "12", "5"))
    print(find_x(5, 1, 2))
