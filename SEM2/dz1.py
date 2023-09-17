# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое
# представление.
# Функцию hex используйте для проверки своего результата.

def Ten_To_SixTeen(number: int):
    temp = "0123456789ABCDEF"
    result = ""
    number = int(input("Введите целое число: "))
    while number > 0:
        result = temp[number % 16] + result
        number = number // 16
    print(result)

Ten_To_SixTeen()