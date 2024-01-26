lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

def chek(lst):
    if (lst < 30) and (lst % 3 == 0):
        return True
    else: 
        return False
    
answer = filter (chek, lst)
print("Тип объекта out_filter: ", type(answer))
print("Отфильтрованный список по условию: ", list(answer))     

