sweets = ['Батончик', 'Сникерс', 'Мишка Косолапый', 'Коровка']
kids = ['Витя', 'Маша', 'Марина']

for kid in kids:
    print(f'{kid} получит конфетки: ')
    for sweet in sweets:
        print(f'\t- {sweet}')
print('Все детки получили конфетки!')