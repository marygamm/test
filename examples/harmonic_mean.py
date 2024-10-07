def harmonic_mean(x): #среднее гармоническое списка x
    summ = 0
    if not x:
        return "list is empty"
    else:
        for num in x:
            summ += 1 / int(num)
        return len(x) / summ
    
s = input()
x = s.split()
print(harmonic_mean(x))