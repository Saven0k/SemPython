import csv
import json
# import magic
import os
import pickle


# Вспоминаем задачу 3 из прошлого семинара.
# Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию,
# которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.

def txt_to_json(input_filename: str,
                output_filename: str):
    with open(input_filename, 'r') as f:
        data = f.read().split("\n")[:-1]
    data = [{i.split()[0].capitalize(): i.split()[1]} for i in data]

    with open(output_filename, 'w') as f:
        json.dump(data, f, indent=4)


#
# {
#     level:{
#         id:name,
#         ...
#     },
#     ...
# }


# Задание №2
# Напишите функцию, которая в бесконечном цикле
# запрашивает имя, личный идентификатор и уровень
# доступа (от 1 до 7).
# После каждого ввода добавляйте новую информацию в
# JSON файл.
# Пользователи группируются по уровню доступа.
# Идентификатор пользователя выступает ключём для имени.
# Убедитесь, что все идентификаторы уникальны независимо
# от уровня доступа.
# При перезапуске функции уже записанные в файл данные
# должны сохраняться.


def uniq_id(data: dict, id: str) -> bool:
    for i in data.values():
        if id in i.keys():
            return False
    return True


def get_name(file_name) -> None:
    file_name += '.json'
    while True:
        id = input("Enter id: ")
        name = input("Enter name: ")
        level = input("Enter level key: ")

        try:
            with open(file_name, 'r', encoding='utf-8') as fr:
                new_dict: dict = json.load(fr)
        except:
            new_dict: dict = {str(i): {} for i in range(1, 8)}

        if uniq_id(new_dict, id):
            new_dict[level].update({id: name})
        else:
            continue

        with open(file_name, 'w', encoding='utf-8') as fw:
            json.dump(new_dict, fw, indent=2)


# Напишите функцию, которая сохраняет созданный в
# прошлом задании файл в формате CSV.

def json_to_csv(filename: str) -> None:
    with open(f'{filename}.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        rows = []
        for level, users in data.items():
            for id, name in users.items():
                rows.append({'level': level,
                             'name': name,
                             'id': id})

    with open(f'{filename}.csv', 'w') as res:
        csv_write = csv.DictWriter(res, fieldnames=['level',
                                                    'name',
                                                    'id'])
        csv_write.writeheader()
        csv_write.writerows(rows)


# Прочитайте созданный в прошлом задании
# csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл,
# где каждая строка csv файла представлена как
# отдельный json словарь.
# Имя исходного и конечного файлов
# передавайте как аргументы функции.
def csv_to_json(filename: str) -> None:
    with open(f'{filename}.csv', 'r') as f:
        data = f.read().split('\n')
    print(data)
    res = []

    for i in data[:-1]:
        print(i)
        # level, name, id = i.replace('\r', '').split()
        level, name, id = i[:-2].split(',')
        res.append({'id': f'{id:06}',
                    'level': level,
                    'name': name,
                    'hash': hash(id + name)})
    with open(f'{filename}.json', 'w', encoding='utf-8', newline='') as f:
        json.dump(res, f, indent=4)


def find_json_in_picle(dir: str = 'r1') -> None:
    files = list(filter(lambda x: '.json' in x, os.listdir()))
    for file in files:
        filename, *_ = file.split('.')
        with (open(file, 'r') as fr,
              open(f'{filename}.pickle', 'wb') as fw):
            data = json.load(fr)
            pickle.dump(data, fw)


# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах,
# а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
# Пример:
# test/users/names.txt
# Результат в json для names.txt:
# {
# "name": names.txt
# "parent": users,
# "type": "file"
# # "size": 4096
# }


#155 изменяем lambda фулл список без json
def travel_directory(dir: str = "C:Users\Евгений\PycharmProjects\r1", new_filename: str = "new_File") -> None:
    files = os.listdir()
    for file in files:
        with (open(f'{new_filename}.csv', 'w') as w_csv,
              open(f'{new_filename}.json', 'w') as w_json,
              open(f'{new_filename}.pickle', 'wb') as w_pickle):
            name = file
            parents = os.path.dirname(file)
            # type = magic.from_file(file)
            type = "file"
            size = os.path.getsize(file)

            rows = []
            rows.append({'name': name,
                         'parents': parents,
                         'type': type,
                         'size': size})



            json_res = {"name": name,
                        "type": type,
                        "parents": parents,
                        "size": size}
            json.dump(json_res, w_json, indent=2)

            csv_write = csv.DictWriter(w_csv, fieldnames=['name',
                                                          'parents',
                                                          'type',
                                                          'size'])
            csv_write.writeheader()
            csv_write.writerows(rows)


            pickle.dump(json_res, w_pickle)


if __name__ == '__main__':
    # txt_to_json('result.txt', "output.json")
    # get_name('users')
    # json_to_csv('users')
    # csv_to_json('users')
    # find_json_in_picle('r1')
    travel_directory("C:Users\Евгений\PycharmProjects\r1", "new_file")