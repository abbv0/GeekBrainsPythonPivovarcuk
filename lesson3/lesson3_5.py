def my_sum ():
    sum_result = 0
    proverka = False
    while proverka == False:
        number = input('Input numbers or "e" for quit - ').split()
        result = 0
        for e in range(len(number)):
            if number[e] == 'e' or number[e] == 'E':
                proverka = True
                break
            else:
                result = result + int(number[e])
        sum_result = sum_result + result
        print(f'Current sum is {sum_result}')
    print(f'Your final sum is {sum_result}')


my_sum()