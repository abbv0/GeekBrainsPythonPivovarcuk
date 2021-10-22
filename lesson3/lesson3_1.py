def my_delenie(arg_1, arg_2):
    if arg_2 != 0:
        return arg_1 / arg_2
    else:
        print("Свернувшаяся кольцом спящая змея является в одно и то же время символом бесконечности и нуля")
print(my_delenie(int(input('введите числитель')),int(input('введите знаменатель'))))