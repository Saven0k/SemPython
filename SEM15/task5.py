# Задание №5
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.


import argparse
from datetime import date, datetime, timedelta
import logging
from functools import wraps

logging.basicConfig(filename="log_for_tast4.log",
                    encoding='utf-8',
                    level=logging.ERROR,
                    filemode='a')
logger = logging.getLogger(__name__)

MONTHS = (' ', 'янв', 'фев', 'мар', 'апр', 'мая', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')
WEEKDAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')


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


@deco
def create_data(text: str):
    day_, week_, month_ = text.split()
    day_ = int(day_[0])
    week_ = WEEKDAYS.index(week_[:3])
    month_ = MONTHS.index(month_[:3])
    start_date = date(year=date.today().year, month=month_, day=1)
    count = 0
    for i in range(32):
        if start_date.weekday() == week_:
            count += 1
            if day_ == count:
                return start_date
        start_date += timedelta(days=1)
    raise ValueError


# def create_parse():
# #     parser = argparse.ArgumentParser(description='Parse create_data()')
# #     parser.add_argument('--d', '-day',
# #                         type=str)
# #     parser.add_argument('--w', '-weekday',
# #                         type=str)
# #     parser.add_argument('--m', '-month',
# #                         type=str)
# #     args = parser.parse_args()
# #     print(f'В скрипт передано: {args}')
# #     return create_data(f'{args.day} {args.weekday} {args.month} ')

def pars():
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('-d', '--day', type=str)
    parser.add_argument('-w', '--weekday', type=str)
    parser.add_argument('-m', '--month', type=str)
    args = parser.parse_args()
    return create_data(f'{args.day} {args.weekday} {args.month}')


if __name__ == '__main__':
    text = '1-й четверг ноября'
    text2 = '9-я среда мая'
    print(create_data(text2))
    print(pars())
