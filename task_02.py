res = 0
for i in range(0,12):
    salary = int(input(f'Введите зарплату за {i+1} месяц: '))
    res += salary

print(f'Свредняя зарплата за год {res/12}')