a = int(input('input km: '))
b = int(input('input  max km: '))
day = 1
print(f'{day}-й день: {a}')
while a <= b:
    a = a + a * 0.1
    day += 1
    print(f'{day}-й день: {round(a, 2)}')
print(f'На {day}-й спорсмен достиг результата - не менее {int(b)} км.')
