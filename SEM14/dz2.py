# Возьмите 1-3 задания из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним тесты.
# 2-5 тестов на задание в трёх вариантах:
# - doctest,
# - unittest,
# - pytest.





#SEM 5

def fib(n):
    """A function that removes number fibonachi for n
            >>> print(list(fib(5)))
            [0, 1, 1, 2, 3]

            >>> print(list(fib(7)))
            [0, 1, 1, 2, 3, 5, 8]

            >>> print(list(fib(1)))
            [0]
    """
    a, b = 0, 1
    for __ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    print(list(fib(5)))