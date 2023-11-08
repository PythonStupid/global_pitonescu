flat = [
    5.55, 22.19, 7.78, 26.86, 5.55,
    29.84, 22.19, 5.55, 16.85, 4.52
]

sum_area = 0

for room in flat:
    sum_area += room

print(f'Общая площадь = {round(sum_area)}')