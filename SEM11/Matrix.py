# Задача 3. Создайте класс Матрица.
# Добавьте методы для:
# - вывода на печать,
# - сравнения,
# - сложения,
# - *умножения матриц
import numpy as np




class Matrix:
    """
    Class Maxtrix
    """

    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def __eq__(self, other: "Matrix"):
        return len(self.matrix) == len(other.matrix)

    def __lt__(self, other: "Matrix"):
        return len(self.matrix) < len(other.matrix)

    def __gt__(self, other: "Matrix"):
        return len(self.matrix) > len(other.matrix)


    def addition2(self, other: "Matrix"):
        """
        :param other:
        :return: matrix
        """
        return np.array(self.matrix) + np.array(other.matrix)

    def multiplication(self, other: "Matrix"):
        return np.multiply((self.matrix), (other.matrix))

    def __repr__(self):
        """
        Function repr
        :return:
        """
        return f'Matrix({self.matrix = })'

    def __str__(self):
        """
        Function str
        :return: list
        """
        return f'matrix = {self.matrix}'


if __name__ == '__main__':
    m1 = Matrix([[3, 5, 4], [5, 6, 2]])
    m2 = Matrix([[11, 1, 6], [1, 3, 1]])

    print(f'{m1.multiplication(m2) = }')
    print("------------")
    print(f'{m1.addition2(m2) =  }')
    print("------------")
    print(m1 > m2)
    print("------------")
    print(m1 < m2)
    print("------------")
    print(m1 == m2)
