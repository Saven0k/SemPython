# # Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
# 'name' : 'kg'
my_dict = {
    'box': 1,
    'matches': 0.5,
    'boxlunch': 2,
    'appliances': 1,
    'first aid kit': 0.5,
    'kettle': 3,
    'bottle': 2.5,
    'clothes': 5
}


def Bag(my_dict):
    carrying = 5.0  # kg
    full_mass = 0.0
    print(f"Грузоподъёмность рюкзака = {carrying}")
    if full_mass == 5.0 or len(my_dict) == 0:
        print("Рюкзак полностью забит")
        exit()
    else:
        bag_2(my_dict, carrying, full_mass)


def bag_2(my_dict, carrying, full_mass):
    if full_mass == 5.0:
        print("Рюкзак полностью забит")
        exit()
    if len(my_dict) == 0:
        print("Рюкзак забит полностью")
        exit()
    else:
        for key, value in my_dict.items():
            if (full_mass + value) <= carrying:
                del my_dict[key]
                full_mass += value
                print(f"{key} в рюкзаке, сейчас вес рюкзака = {full_mass}")
                bag_2(my_dict, carrying, full_mass)
            if value > (carrying - full_mass):
                del my_dict[key]
                print(
                    f"{key} положить нельзя, переизбыток = {value - (carrying - full_mass)} , сейчас вес рюкзака = {full_mass}")
                bag_2(my_dict, carrying, full_mass)


def gg(my_dict, carrying, full_mass):
    for key, value in my_dict.items():
        if


Bag(my_dict)