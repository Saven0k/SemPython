# Решить задачи, которые не успели решить на семинаре.
# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.
import argparse
import math
import logging
from functools import wraps

logging.basicConfig(filename="log_for_d1.log",
                    encoding='utf-8',
                    level=logging.ERROR,
                    filemode='a')
logger = logging.getLogger(__name__)


def deco(func: callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as message_errors:
            logger.error(f'Функция {func.__name__} '
                         f'с аргументами {args = }, '
                         f'{kwargs =} выдавала ошибку: '
                         f'{message_errors = }')
        return None

    return wrapper

def pars():
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('-x',
                        type=float)
    parser.add_argument('-y',
                        type=float)
    parser.add_argument('-z',
                        type=float)
    args = parser.parse_args()
    return find_x(args.x, args.y, args.z)


@deco
# Нахождение корней квадратного уравнения
def find_x(a: float, b: float, c: float):
    try:
        if isinstance(a, str) or isinstance(b, str) or isinstance(c, str):
            raise Exception
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
    except Exception as e:
        return f'{e =} Надо передавать значения типа float or int'


if __name__ == '__main__':
    print(find_x(2, '5', 2))
    # print(pars())
