people = int(input('Введите количество учеников: '))
rating = [int(input(f'Введите оценку {i+1} ученика: ')) for i in range(0,people)]
count_5 = 0
count_4 = 0
count_3 = 0
for i in rating:
    if i == 5:
        count_5 += 1
    elif i == 4:
        count_4 += 1
    elif i == 3:
        count_3 += 1

if count_4 < count_3 > count_5:
    print('Сегодня больше троешников')
elif count_3 < count_4 > count_5:
    print('Сегодня больше хорошистов')
else:
    print('Сегодня больше отличников')
