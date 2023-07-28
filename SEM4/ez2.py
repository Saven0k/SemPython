# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

def rev_kwargs(**data):  # -> dict{*data : *data} - >dict{}:
    res_dict = {}
    for k, v in data.items():
        res_dict[v] = k
        print(res_dict)
    return res_dict

# Можно ли сделать так?
# def rev_kwargs(**data):  # -> dict{*data : *data} - >dict{}:
#     res_dict = {v: k for k, v in data.items()}
#     return res_dict


print(rev_kwargs(res=1, rev=[1, 2, 3]))
print(rev_kwargs(rev=[1, 2, 3], revr=0))
print(rev_kwargs(N=None, string=str(1)))
