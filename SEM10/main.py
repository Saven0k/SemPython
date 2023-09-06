# Задача 1. Решить задания, которые не успели решить на семинаре.

#Все успели

# Задача 2. Доработаем задания 5-6. Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
class Factory:
    def __init__(self,
                 type_animal: str,
                 name: str,
                 age: int,
                 *args, **kwargs):
        self.type_name = str(type_animal)
        self.name = name
        self.age = age
        self.args = args
        self.kwargs = kwargs
    def create_animal(self):
        animal = self.type_animal(self.name, self.age, self.args, self.kwargs)
        print(animal)



class Animal:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    def __str__(self) -> str:
        return f'{self.name} {self.age}'

    def birthday(self):
        self.age += 1


class Dog(Animal):
    def __init__(self,
        name: str,
        age: int,
        color: str,
        breed: str,
        is_domestic: bool = True
                 ) -> None:
        super().__init__(name, age)

        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic

    def __str__(self):
        if self.is_domestic:
            return f'Dog {self.color} {self.breed} домашняя'
        return f'Dog {self.color} {self.breed} дворняга'

class Kotopes(Animal):
    def __init__(self,
        age: int,
        name: str,
        number_heads: int = 2
                 ) -> None:
        super().__init__(name, age)
        self.__number_heads = number_heads

    def __str__(self):
        return f'Kotopes -> number_heads: {self.__number_heads},\
        Возраст: {self.age}, не женат '


class Fish(Animal):

    def __init__(self, name, age, aqua, size):
        super().__init__(name, age)
        self.aqua = aqua
        self.size = size

    def __str__(self):
        if self.aqua:
            return f'{self.name} морская'
        else:
            return f'{self.name} пресноводная'


if __name__ == "__main__":
    dog = Dog('Бобик', 3, "рыжий", "спаниель", True)
    dog2 = Dog('Тузик', 4, "серый", "спаниель", False)
    f1 = Fish("Дори", 1, True, 0.5)
    kt1 = Kotopes(3, "котопес", 2)
    fact = Factory('Dog', 'Bobik', 15, "white")
    print(fact)
    print(dog)
    print(f1)
    print(kt1)
    kt1.birthday()
    print(kt1)

# Задача 3. Возьмите 1-3 любые задания из прошлых семинаров (например сериализация данных), которые вы уже решали. Превратите функции в методы класса,
# а параметры в свойства. Задания должны решаться через вызов методов экземпляра.Задача

#Check file portfolio
