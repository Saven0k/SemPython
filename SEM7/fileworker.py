from random import randint, uniform
import os


# ЗАДАЧА 1: Решить задачи, которые не успели решить на семинаре.
#
# ЗАДАЧА 2: Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
#
# Пример:
# rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv
#
# ЗАДАЧА 3:Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.


def group_renaming(wanted_name: str, count_nums: int, extension_old: str, extension_new: str, range: list):
    directory = "E:\SMP\SEM7"
    for  i,filename in enumerate(os.listdir(directory)):
        if filename.endswith(extension_old):
            new_name = str(filename[range[0]:range[1]] + wanted_name + str(i) + extension_new)
            os.rename(filename, new_name)


def fill_in_file(name_file: str, count_line: int) -> None:
    name_file += '.txt'

    with open(name_file, 'a', encoding='utf-8') as file:
        for _ in (count_line):
            file.write(f"{randint(-1000, 1000)} | {uniform(-1000, 1000)} \n")


def give_name() -> str:
    name: str = ''
    for _ in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def fill_in_file_names(name_file: str, count_line: int) -> None:
    name_file += '.txt'

    with open(name_file, 'a', encoding='utf-8') as file:
        for _ in (count_line):
            file.write(f"{give_name()} \n")


def read_and_write_files(name_file_names: str, name_file_numbers: int, name_file_output: str) -> None:
    with (open(name_file_names, 'r', encoding='utf-8') as file_names,
          open(name_file_numbers, 'r', encoding='utf-8') as file_numbers):
        names = file_names.read().split('\n')
        numbers = file_numbers.read().split('\n')

    longest_file = max([names, numbers], key=len)
    if len(numbers) > len(names):
        names += names[:len(numbers) - len(names)]
    else:
        numbers += numbers[:len(names) - len(numbers)]

    with open(name_file_output, 'w', encoding='utf-8') as file_output:
        for name, number in zip(names, numbers):
            number_output_int, number_output_float = map(float, number.split('|'))
            multi: float = number_output_float * number_output_int
            if multi < 0:
                file_output.write(f"{name.lower()} {abs(multi)}")
            else:
                file_output.write(f"{name.uppear()} {int(multi)}")

#
# def create_files(ext:str, min_Len: int = 6, max_len: int = 30, min_size: int = 256, max_size: int = 4096, count_files: int = 42):
