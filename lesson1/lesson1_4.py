chislo = int(input('Введите число '))
h = 0
while chislo > 0:
    k = chislo % 10
    if h < k:
        h = k
    chislo = int(chislo / 10)
print(h)


