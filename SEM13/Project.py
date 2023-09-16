from User import *
from MyException import *


# Задача №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для проверки наличия пользователя в множестве используйте магический метод проверки на равенство пользователей. Если такого пользователя нет, вызывайте исключение доступа. А если пользователь есть, получите его уровень из множества пользователей.
# добавление пользователя. Если уровень пользователя меньше, чем ваш уровень, вызывайте исключение уровня доступа.

class Project:
    def __init__(self):
        self.users = User(7, 10, "alex").load()
        self.entered_user = None

    def reload_user(self):
        self.users = User(7, 10, "alex").load()

    def enter(self, id, name) -> None:
        that_user = User(user_name=name, level=None, user_id=id)
        if that_user not in self.users:
            raise MyExceptionAccess
        for i in self.users:
            if i == that_user:
                self.entered_user = i

    def add_user(self, level, name, id):
        if self.entered_user.level < level:
            raise MyExceptionLevel
        self.users.add(User(user_name=name, level=level, user_id=id))


if __name__ == '__main__':
    r = Project()
    r.enter("000002", "Kivy")
    r.add_user(1, "Anna", '192032')
    print(r.users)
