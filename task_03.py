number = int(input('Введите число: '))
factorial = 1
for i in range(1, number+1):
    factorial *= i

print(f'Факториал числа {number}! = {factorial}')