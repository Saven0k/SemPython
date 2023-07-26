# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
# Пример:
# Ввод:
# 1/2
# 1/3
# Вывод:
# 5/6 1/6

#start

dr1 = str(input("Введите первую дробь: "))
dr2 = str(input("Введите вторую дробь: "))
def Sum(dr1, dr2):
    znm1, znm2 = dr1[2], dr2[2]
    temp, temp1, temp2 = 0, 0, 0
    for i in range(1, 100):
        if (i % int(znm1) == 0) and (i % int(znm2) == 0) and (i > int(znm1)) and (i > int(znm2)):
            temp = i
            temp1 = i // int(znm1)
            temp2 = i // int(znm2)
            break
    res1 = int(dr1[0]) * temp1 + int(dr2[0]) * temp2
    res2 = temp
    if res1 == res2:
        result = 1
        print(f"Сумма дробей = {result}")
    else:
        result = (f"{int(dr1[0]) * temp1 + int(dr2[0]) * temp2} / {temp}")
        print(f"Сумма дробей = {result}")

def Multi(dr1, dr2):
    print(f"Произведение дробей = {str(int(dr1[0]) * int(dr2[0]))}/{str(int(dr1[2]) * int(dr2[2]))}")

Sum(dr1, dr2)
Multi(dr1, dr2)

#https://github.com/Saven0k/SMP