countdown_str = ''

for i in reversed(range(0, 11)):
    countdown_str += str(i) + ', '

countdown_str += 'поехали!'
print(countdown_str)