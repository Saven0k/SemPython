# Задание №3
# Напишите для задачи 1 тесты unittest. Проверьте
# следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери
# символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов

from task2 import *
import pytest

def test_one_clean_text():
    assert clean_text('Some test, тест'), 'Test one dont ok'

def test_otwo_clean_text():
    assert clean_text('Some milk in dog, 12312awdawd'), 'Test one dont ok'

def test_othree_clean_text():
    assert clean_text('Мама я хочу быть пиратом, Eyyy lets go!'), 'Test one dont ok'


if __name__ == '__main__':
    pytest.main(['--vv'])

