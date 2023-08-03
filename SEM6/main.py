# Напишите небольшую программу, которая импортирует модуль "portfolio.py" и демонстрирует использование всех трех функций.
# Создайте словари для акций и цен, запустите функции и выведите результаты.

import portfolio

#APPL - > Apple Inc
#BA - > The Boeing COmpany
#DIS - > The Walt Disney Company
#NIKE - > Nike Inc
stocks = {"APPL": 5, "BA": 115, "DIS": 25, "NIKE": 50}
prices = {"APPL": 196.1, "BA": 237.7, "DIS": 88.39, "NIKE":110.44}


print(portfolio.calculate_portfolio_value(stocks, prices))

print(portfolio.calculate_portfolio_return(505, 1090)) #НЕ понял как сделать с процентом

prices = {"APPL": 1156.1, "BA": 223.7, "DIS": 818.39, "NIKE":11110.44}

print(portfolio.get_most_profitable_stock(stocks, prices))
