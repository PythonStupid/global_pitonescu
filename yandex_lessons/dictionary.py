unit_to_multiplier = {
    'mm': 10**-3,
    'cm': 10**-2,
    'dm': 10**-1,
    'm': 1,
    'km': 10**3
}

try:
    mult = unit_to_multiplier['cm']
except KeyError as e:
    # можно также присвоить значение по умолчанию вместо бросания исключения
    raise ValueError(f'Undefined unit: {e.args[0]}')

print(mult)