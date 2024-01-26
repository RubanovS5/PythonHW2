# Напишите функцию month_to_season(), которая принимает 1 аргумент — номер месяца — и возвращает название сезона, к которому относится этот месяц.
def month_to_season(month):
    if month in [1,2,12]:
        return ("Зима")
    elif month in [3,4,5]:
            return ("Весна")
    elif month == [6,7,8]:
        return ("Лето")
    elif month == [9,10,11]:
         return ("Осень")
    else:
         return ("Некорректный ввод месяца")

month = int(input("Введите номер месяца: "))
number = month_to_season(month)
print("Сезон:", number)
    