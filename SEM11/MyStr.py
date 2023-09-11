import time

# Создайте класс МояСтрока где будут доступны все возможности str и дополнительно хранится имя автора строки и время создания (time.time)

class MyStr(str):
    """
    Class MyStr
    """
    def __new__(cls, value: str, name: str):
        """
        Function new
        :param value: imp str
        :param name:  name writer
        """
        instance = super().__new__(cls, value)
        instance.name = name
        instance.value = value
        instance.time_create = time.time()
        return instance

    def __repr__(self):
        """
        Function repr
        :return: MyStr
        """
        return f'MyStr({self.value = } , {self.name =})'

    def __str__(self):
        """
        Function str
        :return: str
        """
        return f'value = {self.value}, name = {self.name}, time = {self.time_create}'

