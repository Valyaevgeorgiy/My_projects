from random import randint

def privet():
    global name
    print("Игра - 'Угадайка число!'")
    name = input('Пожалуйста, вводи своё имя правильно: ')
    print(f'{name}, привет :) ')
    print()
    print('Если ты случайно ввёл(а) неправильное имя, или оно оказалось мемным, начни игру с самого начала, пожалуйста.')
    print()

def po():
    print('Добро пожаловать в числовую угадайку!')
    print(f'{name}, мы играем в пределах целых чисел с диапазоном от - 1 000 000 и до 1 000 000 включительно')
    print()

def is_chis(a):
    p = a[1:]
    if a.isdigit():
        if int(a) >= (-1_000_000):
            return True
        else:
            return False
    elif p.isdigit():
        if int(a) >= (-1_000_000):
            return True
        else:
            return False
    else:
        return False

def is_chis2(a1):
    p1 = a1[1:]
    if a1.isdigit():
        if (int(a1) > cs) and (int(a1) <= 1_000_000):
            return True
        else:
            return False
    elif p1.isdigit():
        if (int(a1) > cs) and (int(a1) <= 1_000_000):
            return True
        else:
            return False
    else:
        return False

def is_true(x):
    p2 = x[1:]
    if (x.isdigit()):
        if (cs <= int(x) <= cx):
            return True
        else:
            return False
    elif p2.isdigit():
        if (cs <= int(x) <= cx):
            return True
        else:
            return False
    else:
        return False

def nachalo():
    global num, x, s, count, cx, cs

    while True:
        cs = input(f'{name}, выбери по своему желанию левую границу диапазона целых чисел: ')
        b0 = is_chis(cs)
        if b0:
            cs1 = int(cs)
            cs = cs1
            break
        else:
            print('Введён неправильный формат данных, либо твоё число оказалось за границами')
            continue

    while True:
        cx = input(f'{name}, выбери по своему желанию правую границу диапазона целых чисел: ')
        b = is_chis2(cx)
        if b:
            cx1 = int(cx)
            cx = cx1
            break
        else:
            print('Введён неправильный формат данных, либо число оказалось за границами')
            continue
    num = randint(cs, cx)
    x = input(f'Введи любое целое число от {cs} до {cx}: ')
    s = is_true(x)
    count = 0

def zaprosy():
    print()
    print(f'{name}, мы вас поздравляем, ты угадал(а), ура!')
    print('Большое спасибо, что сыграл(а) в числовую угадайку. Еще увидимся...')
    print()
    y = input('А хотел(а) бы ты узнать, сколько попыток пришлось потратить тебе за всю игру?: ')
    if (y.lower() == 'да') or (y.lower() == 'yes'):
        print(f'OK, ты потратил(а) {count} попыток в сумме')
        print()
        if 1 <= count <= 3:
            print('Да ты крутышка)')
        elif 4 <= count <= 15:
            print('Хорооооооооошо')
        elif 16 <= count <= 30:
            print('Сойдёт)')
        elif 31 <= count <= 299:
            print('Мемно)')
        elif 300 <= count <= 1000:
            print('Жиза, как долго')
        print()
    else:
        print(f'Хорошо, спасибо ещё раз за игру.')

def again():
    global eb
    eb = 0
    xs = input(f'{name}, желаешь ли ты сыграть в числовую угадайку снова?: ')
    if (xs.lower() == 'да') or (xs.lower() == 'yes'):
        print('Поехалиии!')
        eb = True
    else:
        print(f'Хорошо, спасибо ещё раз за игру.')
        eb = False

def goodbye():
    print()
    print('С вами был ваш покорный слуга, Георгий Валяев!')
    print('Всё, пока ...', end='')
    print('... пока!')

print()
privet()
po()
print()
nachalo()
print()

while True:
    if s:
        x1 = int(x)
        while x1 != num:
                if x1 > num:
                    print('Твоё число больше загаданного, хе :)')
                    count += 1
                    print()
                elif x1 < num:
                    print('Твоё число меньше загаданного, хе :)')
                    count += 1
                    print()
                x = input(f'{name}, попробуй ввести целое число от {cs} до {cx}: ')
                s = is_true(x)
                if s:
                    x1 = int(x)
                    continue
                else:
                    print('К сожалению, ты ввёл(а) неправильные данные')
                    x = input(f'Попробуй снова ввести целое число от {cs} до {cx}: ')
                    s = is_true(x)
                    break

        else:
            zaprosy()
            again()
            if eb:
                po()
                nachalo()
                continue
            else:
                goodbye()
                break
    else:
        print('К сожалению, ты ввёл(а) неправильные данные')
        x = input(f'Попробуй снова ввести целое число от {cs} до {cx}: ')
        s = is_true(x)
        print()