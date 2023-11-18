import random

number = random.randrange(1, 11)

while True:
    answer = input('Введите целое число: ')

    if not answer.isdigit():
        print('Введите число!')
        continue

    answer = int(answer)

    if answer > number:
        print('Введенное число больше загадонного числа')
    elif answer < number:
        print('Введенное число меньше загадонного числа')
    else:
        print(' загадонного числа равно загадонному числу')
        break
