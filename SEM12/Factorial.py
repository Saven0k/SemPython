#Задание №1
# Создайте класс-функцию, который считает факториал числа при вызове экземпляра. Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых чисел и их факториалов.

#Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.


import json
class Factorial:

    def __init__(self, size: int):
        self._size = size
        self.archiv: list = []

    def show_archiv(self):
        return self.archiv

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('factorial.json', 'w', encoding='utf-8') as f:
            json.dump(self.archiv, f)

    def __call__(self, number: int):
        res: int = 1
        for i in range(1, number + 1):
            res *= i
        if len(self.archiv) >= self._size:
            self.archiv.pop(0)
        self.archiv.append({number: res})
        return res


if __name__ == '__main__':
    f1 = Factorial(size = 4)
    for i in range(1, 8):
        print(f1(i))

    print(f1.show_archiv())

    with f1 as cope_:
        for i in range(1, 5):
            print(cope_(i))