
_last = {}



# Задача: Расчет финансовых показателей портфеля акций
#
# Описание задачи:
# Вы являетесь инвестором и хотите создать программу для расчета нескольких финансовых показателей вашего портфеля акций. Создайте модуль Python под названием "portfolio.py", который будет содержать функции для выполнения следующих операций:
#
# Расчет общей стоимости портфеля акций:
#
# Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float принимает два аргумента:
# stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.), и значениями - количество акций каждого символа.
# prices - словарь, где ключами являются символы акций, а значениями - текущая цена каждой акции.
# Функция должна вернуть общую стоимость портфеля акций на основе количества акций и их текущих цен.
# Расчет доходности портфеля:



def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    global _last
    _last = prices
    return sum([vi * vj for ki, vi in stocks.items() for kj, vj in prices.items() if ki == kj])

#
# Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float принимает два аргумента:
# initial_value - начальная стоимость портфеля акций.
# current_value - текущая стоимость портфеля акций.
# Функция должна вернуть процентную доходность портфеля.


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    return round(100 - (initial_value * 100 / current_value))


# Определение наиболее прибыльной акции: Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str принимает два аргумента:
# stocks - словарь с акциями и их количеством. prices - словарь с акциями и их текущими ценами. Функция должна вернуть символ акции (ключ),
# которая имеет наибольшую прибыль по сравнению с ее начальной стоимостью. Начальная стоимость - первый вызов calculate_portfolio_value, д
# анные из этого вызова следует сохранить в защищенную переменную на уровне модуля.
# Пример:
# Пришло:
# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
# prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
# Вышло:
# MSFT


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    temp_dit = {k1: round((v * 100 / v1)) for k, v in prices.items() for k1, v1 in _last.items() if k == k1}
    for k, v in temp_dit.items():
        if v == max(temp_dit.values()):
            return k
    # return (f"{k for k, v in temp_dit.items() if v == max(temp_dit.values())}")
    # ПОчему не работает такой вариант(вывод  <generator object get_most_profitable_stock.<locals>.<genexpr> at 0x7f424a3edf50>)


