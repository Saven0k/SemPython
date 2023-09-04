table = [
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0],
]

scf = [(0, 0), (4,4),(6,5),
(1, 4), (3, 5), (5, 6), (2, 7)]


def cheess(table:list, var: list):
    for i, g in var: table[i][g] = 1
    for i in table:
        print(f"{i}\n")
    for i in range(0, 8):
        if table[i].count(1) > 1:
            print(f"Ферзи попадаються друг на друга на линии {i}")
            return False
        else:
            for j in range(0, 8):
                if table[i][j] == table[i+1][j] == 1:
                    print(f"Ферзи попадаються друг на друга в точках ({i}:{j}) ({i+1}:{j})")
                    return False
                elif (table[i][j] == 1 == table[7-i][7-j]) and (7-i) == (7 - j):
                    print(f"Ферзи попадаються длруг на друга на точках ({i}:{j})({7-i}:{7-j})")
                    return False
                elif ((7-i) - (7 - j) == 1) and table[i][j] == 1 == table[7-1][7-j]:
                    print(f"Ферзи попадаються друг на друга на токках диагонали прямой ({i}:{j}) ({7-i}:{7-j}")
                    return False
                elif ((7-j) - (7-i) == 1) and table[i][j] == 1 == table[7-i][7-j]:
                    print(f"Ферзи попадаються друг на друга на токчках диагонали обратаной ({i}:{j}) ({7 - i}:{7 - j}")
                    return False
    return True
    # for i in table:
    #     print(f"{i}\n")

print(cheess(table,scf ))
