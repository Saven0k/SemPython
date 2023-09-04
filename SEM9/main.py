import json
import csv
import random
import math
import functools


# Нахождение корней квадратного уравнения
def find_x(a: float, b: float, c: float) -> None:
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


# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
def generate_csv_file(file: str, start: int, end: int) -> None:
    with open(f'{file}.csv', 'w') as f:
        rows = []
        for i in range(random.randint(100, 1000)):
            rows.append({'first': random.randint(start, end),
                         'second': random.randint(start, end),
                         'third': random.randint(start, end)})

        csv_write = csv.DictWriter(f, fieldnames=['first',
                                                  'second',
                                                  'third'])
        csv_write.writeheader()
        csv_write.writerows(rows)


# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.

def deck_first(func):
    @functools.wraps(func)
    def wrapper(filename, start, end):
        res = []
        with open(f'{filename}.csv', 'r') as f:
            data = csv.reader(f)
            for i in data:
                a, b, c = map(int, i)
                res.append(func(a, b, c))

        return res

    return wrapper


# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
def wr_res_to_json(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open('test.json', 'w') as f:
            res = func(*args, **kwargs)
            json.dump(res, f, indent=4)
        return res

    return wrapper
