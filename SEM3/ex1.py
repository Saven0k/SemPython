# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

app = [1, 2, 3,1,1,2,2,31]
def Only(arr):
    temp = []
    for i in arr:
        if (arr.count(i) > 1) and ((i in temp) == False):
            arr.pop(i)
            temp.append(i)
    print(f"{arr} -> {temp}")
Only(app)