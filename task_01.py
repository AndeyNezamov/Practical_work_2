count = 0
for i in range(0,10):
    number = int(input('Введите число: '))
    if number % 2 == 0:
        if number > 0:
            count += 1
print(f'Количество четных положительных чисел: {count}')