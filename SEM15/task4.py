# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответствует формату.

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


if __name__ == '__main__':
    text = '1-й четверг ноября'
    text2 = '9-я среда мая'
    print(create_data(text2))
