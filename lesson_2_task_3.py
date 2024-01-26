import math

def square(side):
    if isinstance(side, int):
        return side * side
    else:
        return math.ceil(side * side)

side = float(input("Введите сторону квадрата: "))
area = square(side)
print("Площадь квадрата:", area)