def median(x):
    if not x:
        return "list is empty"
    else:
        x = x.sort()
        for i in len(x):
            x[i] = int(x[i])
        for num in x:
            if len(x) % 2 == 1: #если количество элементов нечетно
                return x[(len(x) + 1) / 2 - 1]
            else:
                return (x[len(x) / 2 - 1] + x[len(x) / 2]) / 2 #если четно

s = input()
x = s.split()
print(median(x))