kolvo_elementov = int(input('Введите количество элементов списка'))
spisok=[]

i=0
while i<kolvo_elementov:
    spisok.append(input('Введите элемент списка'))
    i=i+1
print(spisok)

e=0
for element in range(int(len(spisok)/2)):
        spisok[e], spisok[e + 1] = spisok[e + 1], spisok[e]
        e += 2
print(spisok)