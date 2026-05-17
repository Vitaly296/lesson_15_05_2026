import random as rnd
a = rnd.randint(1, 100) # Создаем переменную со случайным значением

while True:
    attempts_str = input('Введите число попыток, за которое угадаете наше число от 1 до 100: ')
    try:
        attempts = int(attempts_str)
        break
    except:
        print('Требуется ввести число')

p = 0


while True:    
    while True:
        b_str = input('Введите число: ')
        try:
            b = int(b_str)
            break
        except:
            print('Требуется ввести число')

    if p == attempts:
        print(f'Вы не угадали, наше число = {a}')
        break
    else:

        if b == a:
            print('Вы угадали!')
            break

        elif b < a:
            print('Больше')
            p += 1
        
        elif b > a:
            print('Меньше')
            p += 1