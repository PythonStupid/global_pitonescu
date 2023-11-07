bunny_counter = ''  # Создали переменную bunny_counter, её значение - пустая строка.

for i in range(1, 6):
    bunny_counter += str(i) + ', '

print(bunny_counter + 'вышел зайчик погулять!')