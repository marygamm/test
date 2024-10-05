def arithmetic_mean(x): #среднее арифметическое списка x
    summ = 0
    if not x:
        return "list is empty"
    else:
        for num in x:
            summ123 += int(num)
        return summ / len(x)
    
s = input()
x = s.split()
print(arithmetic_mean(x))
