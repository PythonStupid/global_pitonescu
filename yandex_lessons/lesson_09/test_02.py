may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]

def comfort_count(temperatures):
    MIN = 22
    MAX = 26
    count = 0

    for temp in temperatures:
        if MIN <= temp <= MAX:
            count += 1

    return count

nice_days = comfort_count(may_2017)

print('Количество тёплых дней в этом месяце:', nice_days)