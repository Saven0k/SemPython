# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# - doctest,
# - unittest,
# - pytest.
import pytest
from tests import Ten_To_SixTeen

def first_test_view():
    assert Ten_To_SixTeen(12) == 'C', 'first test dont do success!'

def second_test_view():
    assert Ten_To_SixTeen(9) == '9', 'Second test dont do success!'

def third_test_view():
    assert Ten_To_SixTeen(1111) == '457', 'Third test dont do success!'


if __name__ == '__main__':
    pytest.main()
