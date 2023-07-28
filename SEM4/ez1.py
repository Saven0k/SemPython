# Напишите функцию для транспонирования матрицы.
# Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]

import numpy
my_list = [[1, 2, 3], [4, 5, 6]]

def plan(my_list: list[int]) -> list[int]:
    print(f"{my_list} -> {numpy.array(my_list).transpose()}")
    

plan(my_list)