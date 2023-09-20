# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например, отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename='log.log',
                    encoding='utf-8',
                    level=logging.NOTSET)



def div(a,b):
    try:
        res = a/b
        return res
    except ZeroDivisionError:
        logging.error("")
        return None

if __name__ == '__main__':
    print(div(1,0))