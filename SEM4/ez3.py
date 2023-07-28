# # Напишите программу банкомат.
# # ✔ Начальная сумма равна нулю
# # ✔ Допустимые действия: пополнить, снять, выйти
# # ✔ Сумма пополнения и снятия кратны 50 у.е.
# # ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# # ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# # ✔ Нельзя снять больше, чем на счёте
# # ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# # операцией, даже ошибочной
# # ✔ Любое действие выводит сумму денег
# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

def main():
    log_list = []  # История операции
    start_sum = 0  # Стартовая сумма
    count_operation = 0
    while True:
        menu(start_sum, log_list, count_operation)


def menu(start_sum: int, log_list: list[int], count_operation: int):
    if count_operation == 3:
        start_sum += (start_sum // 100 * 3)
    var = int(input("Выберите действие:\n1 - Пополнить баланс\n2 - Снять деньги\n0 - Exit\n : "))
    if var == 1:
        count_operation += 1
        get_money(start_sum, log_list, count_operation)
    if var == 2:
        count_operation += 1
        put_money(start_sum, log_list, count_operation)
    if var == 0:
        exit()
    if var == 100:
        print(log_list)
        menu(start_sum, log_list, count_operation)


def get_money(start_sum: int, log_list: list[int], count_operation: int):
    max_balace = 5000000  # Максимальная сумма баланса
    summ = int(input("Введите сумму, на которую хотите пополнить баланс: "))
    percent = summ // 100 * 10
    if summ % 50 == 0:
        if start_sum < max_balace:
            start_sum += summ
            print(f"Баланс: {start_sum}")
            log_list.append(f"+ {summ}, balance = {start_sum}")
            menu(start_sum, log_list, count_operation)
        else:
            print("ТАк как баланс больше 5млн коммисия становить 10%")
            start_sum += (summ - percent)
            print(f"Баланс: {start_sum}")
            log_list.append(f"+ {summ}, balance = {start_sum}")
            menu(start_sum, log_list, count_operation)
    else:
        print("Повторите операцию")
        get_money(start_sum, log_list, count_operation)


def put_money(start_sum: int, log_list: list[int], count_operation: int):
    if start_sum == 0:
        print(f"Операция не возможна, баланс равен {start_sum}")
    else:
        min_l = 30
        max_l = 600
        wealth_tax = 10  # Налог на богатство (%)
        panal = 1.5  # Коммисия за снятие (%)
        summ = int(input("Введите сумму, которую хотите снять: "))
        percent = 0
        if 30 <= summ // 100 * 1.5 <= 600:
            percent = summ // 100 * 1.5
        if percent == 600:
            percent == 600
        else:
            percent = 30

        if summ % 50 == 0:
            if summ < start_sum:
                start_sum = start_sum - summ - percent
                print(f"Баланс: {start_sum}")
                log_list.append(f"-{summ}, balance= {start_sum}")
                menu(start_sum, log_list, count_operation)
            else:
                print(f"На балансе не хватает средст для снятия, повторите попытку")
                print(f"Баланс: {start_sum}")
                put_money(start_sum, log_list, count_operation)

        else:
            print("Повторите операцию")
            put_money(start_sum, log_list, count_operation)


main()

