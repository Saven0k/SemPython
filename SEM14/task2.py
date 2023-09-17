import unittest
from Task1 import *

# Задание №2
# Напишите для задачи 1 тесты doctest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с у


class TestCleanText(unittest.TestCase):
    def test_one_clean_text(self):
        self.assertEqual(clean_text('Some text, текст'),'some text ')

    def test_two_clean_text(self):
        self.assertEqual(clean_text('Some milk in dog, 12312awdawd'), 'some milk in dog awdawd')

    def test_three_clean_text(self):
        self.assertEqual(clean_text('Мама я хочу быть пиратом, Eyyy lets go!'), '     eyyy lets go', msg='Что то пошло не так')


if __name__ == '__main__':
    unittest.main()