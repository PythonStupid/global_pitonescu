bycycles = ['format', 'cyclon', 'gyant', 'merida']
print(bycycles)
print(bycycles[1].title())
print(bycycles[-1].title())

bycycles.append('honda')
bycycles.append('ducati')
bycycles.append('suzuki')

print(bycycles)

bycycles.insert(0, 'yamaha')
print(bycycles)

deletedElement = bycycles.pop(1)
print(f'Deleted element from list is {deletedElement.title()}')