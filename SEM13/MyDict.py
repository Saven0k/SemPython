# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений.



class MyDict(dict):
    def my_get(self, k_, v_ = None):
        try:
            return self[k_]
        except KeyError:
            return v_


if __name__ == "__main__":
    md = MyDict({"one": 1, "two": 2})
    print(md)
    md.my_get("tree")
    print(md)