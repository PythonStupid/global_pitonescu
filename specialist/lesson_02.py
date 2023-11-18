import random

n1 = None
n2 = None

while True:
    n1 = random.randrange(1, 11)
    n2 = random.randrange(1, 11)
    right_answer = n1 + n2
    
    user_answer = input(f'Сколько будет {n1} + {n2}: ')
    test = user_answer.replace('.', '', 1)
    
    if not test.isdigit():
        print('Нужно ввести число, но не строку! Попробуйте снова!')
    else:
        break

user_answer = test == user_answer if int(user_answer) else float(user_answer)

if user_answer == right_answer:
    print(f'Ты прав! {n1} + {n2} равно {right_answer}')
else:
    print(f'Ты не прав! Правильный ответ: {right_answer}')

if 1 == 2:
    pass
else:
    pass
