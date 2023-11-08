may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]
may_2018 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23, 18, 22, 23, 11]

def comfort_count(temperatures):
    LOW_TEMPERATURE = 22
    HIGH_TEMPERATURE = 26
    days_count = 0

    for i in temperatures:
        if LOW_TEMPERATURE <= i <= HIGH_TEMPERATURE:
            days_count += 1

    print(f'Количество тёплых дней в этом месяце: {days_count}')

comfort_count(may_2017)
comfort_count(may_2018)