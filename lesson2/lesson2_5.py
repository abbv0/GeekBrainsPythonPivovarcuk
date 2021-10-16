my_list = [7, 5, 3, 3, 2]
vstavka = int(input('Введите элемент в рейтинг, 0 - выход '))
while vstavka != 0:
    for e in range(len(my_list)):
        if my_list[e] == vstavka:
            my_list.insert(e + 1, vstavka)
            break
        elif my_list[0] < vstavka:
            my_list.insert(0, vstavka)
        elif my_list[-1] > vstavka:
            my_list.append(vstavka)
        elif my_list[e] > vstavka and my_list[e + 1] < vstavka:
            my_list.insert(e + 1, vstavka)
    print(f"Актуальный список - {my_list}")
    vstavka = int(input("Введите число "))