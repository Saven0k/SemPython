# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class Side:

    def __init__(self, max_len: int, min_len: int):
        self.max_len = max_len
        self.min_len = min_len
    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value):
        if self.min_len <= value <= self.max_len:
            raise ValueError("value not okey")
