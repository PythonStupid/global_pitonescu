# Передадим в программу данные
beaufort    = 6     # Сильный ветер
is_raining  = False # Дождя нет
temperature = 16    # Не жарко

if not is_raining or beaufort <= 4 and temperature > 22:
    print('Идём гулять, на улице хорошо')
else:
    print('Сидим дома, читаем Практикум')

# not is_raining or beaufort <= 4 and temperature > 22
# True or False
# True