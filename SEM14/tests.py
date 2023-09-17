
#SEM2

def Ten_To_SixTeen(number: int):
    temp = "0123456789ABCDEF"
    result = ""
    while number > 0:
        result = temp[number % 16] + result
        number = number // 16
    return result
