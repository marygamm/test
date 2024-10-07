def geometric_mean(x): #среднее геометрическое списка x
    pr = 1
    if not x:
        return "list is empty"
    else:
        for num in x:
            pr *= int(num)
        return pr ** (1 / len(x))
    
s = input()
x = s.split()
print(geometric_mean(x))