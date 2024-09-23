cart = [i for i in range(1, int(input('Введите количество карточек: '))+1)]
for _ in range(0, len(cart)-1):
    number_cart = int(input('Введите номер оставшейся карточки: '))
    if number_cart in cart:
        cart.remove(number_cart)

print(f'Номер пропавшей карточки: {cart[0]}')