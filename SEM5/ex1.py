# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os


# Первый вариант
#
# def m(string: str):
#     *_, prefix = string.split("/")
#     name, prefix = prefix.split(".")
#     print({"/".join(_), name, prefix})
#
#
# m("C:/tec/bot/dop/main.css")



#Второй вариант
def main(string: str):
    name, ind = os.path.basename(string).replace(".", " ").split()
    print(name, ind)
    tmp = string.replace(f"{name}", "").replace(f"{ind}", "")
    my_list = [tmp, name, ind]
    return my_list

print(main("C:/tec/bot/dop/main.css"))