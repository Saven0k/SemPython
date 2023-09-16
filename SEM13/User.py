# Задание №4
# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.
import json


class User:

    def __init__(self, user_id, level, user_name) -> None:
        self.__user_id = user_id
        self.level = level
        self.user_name = user_name

    def load(self):
        with open('user.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        users: set = set()
        for i in data:
            users.add(User(*i.values()))
        return users

    def __eq__(self, other):
        return self.user_name == other.user_name and self.__user_id == other.__user_id

    def __hash__(self):
        return int(self.__user_id)
    def __repr__(self):
        return f'{self.__user_id = },\n {self.level =},\n {self.user_name =}\n\n'


if __name__ == '__main__':
    u = User(10, 10, 'Test')
    print(u.load())
