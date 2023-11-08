# Функция для вычисления периметра куба
def calc_cube_perimeter(side):
    return side * 12

# Функция для вычисления площади куба
def calc_cube_area(side):
    return (side * side) * 6

full_length = calc_cube_perimeter(3) * 8
full_area = calc_cube_area(3) * 8

print('Необходимый метраж палок для 8 кубов:', full_length)
print('Необходимая площадь стекла для 8 кубов, кв.м:', full_area)