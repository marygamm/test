def filter_missed_values(L): #функция принимает на вход список и убирает из него элементы типа None
    LL = []
    for num in L:
        if num is not None:
            LL.append(num)
    return LL

L = [3.14, None, None, 2.71, 1.41]
print(L)
print(filter_missed_values(L)) # [3.14, 2.71, 1.41]