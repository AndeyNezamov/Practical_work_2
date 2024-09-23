a = int(input('Введите точку А: '))
b = int(input('Введите точку B: '))
count = 0
res = 0
for i in range(a,b):
    if i % 3 == 0:
        res += i
        count += 1

print(f'Среднее арифметическое всех чисел отрезка [{a}:{b}] кратное трем = {res / count}')