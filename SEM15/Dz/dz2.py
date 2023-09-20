# Решить задачи, которые не успели решить на семинаре.
# Возьмите любые 1-3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.

import argparse
import logging
from functools import wraps

logging.basicConfig(filename="log_dz1.log",
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


def create_parse():
    parser = argparse.ArgumentParser(description='aw)')
    parser.add_argument('--n', '-number',
                        type=int)
    args = parser.parse_args()
    print(f'В скрипт передано: {args}')
    return Ten_To_SixTeen(args.n)


# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление.
# Функцию hex используйте для проверки своего результата.

@deco
def Ten_To_SixTeen(number: int):
    try:
        if isinstance(number, str):
            raise Exception
        else:
            temp = "0123456789ABCDEF"
            result = ""
            while number > 0:
                result = temp[number % 16] + result
                number = number // 16
            print(result)
    except Exception as e:
        return f'{e = } Надо передавать значения типа int'


if __name__ == '__main__':
    print(Ten_To_SixTeen('15'))
    # print(create_parse())
