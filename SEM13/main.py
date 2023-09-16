# Задача №1
# Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.


def correct_input():
    while True:
        try:
            num = float(input('Enter number: '))
            break
        except ValueError as e:
            print(f'You write not number. Error: {e}')
    return num




if __name__ == '__main__':
    print(correct_input())
