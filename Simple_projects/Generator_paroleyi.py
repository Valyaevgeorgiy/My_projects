import random

def names():
    name = input('Пожалуйста, введи своё имя правильно: ')
    print(f'{name}, привет :) ')

def privet():
    global name
    print()
    print("Вас горячо приветствует генератор безопасных и надёжных паролей!")
    print()
    name = input('Пожалуйста, введи своё имя правильно: ')
    print(f'{name}, привет :) ')
    while True:
        x = input('Если ты случайно ввёл(а) неправильное имя, или оно оказалось мемным, то напиши "да", в обратном случае - "нет": ')
        if (x.lower() == 'да'):
            names()
            continue
        else:
            break
    print()
    print("Отнесись к следующим вопросам осознанно и целенаправленно)")

def zapros_auto():
    global ssd
    ssd = input('А если тебе СРОЧНО нужны надёжные пароли за 5 сек, то напиши здесь "да" или "нет": ')

def data_zapros():
    global x, y, z, s, s1, a, t, chars, chars2, w, count
    print()
    print(f'Итак, {name}, ответь, пожалуйста, на следующие вопросы: ', end='\n')
    x = int(input('Какое количество паролей ты хочешь сгенерировать? : '))
    y = input('Пароль какой длины тебя интересует? : ')
    y1 = ''
    for i in range(len(y)):
        if y[i].isdigit():
            y1 += y[i]
    y = int(y1)
    z = input('Стоит ли включить в пароли цифровые символы (1234567890) ? : ')
    s = input('Необходимо ли использовать в генерации паролей прописные буквы (ABCDEFGHIJKLMNOPQRSTUVWXYZ) ? : ')
    s1 = input('Стоит ли использовать строчные буквы (abcdefghijklmnopqrstuvwxyz) ? : ')
    a = input('Нужно ли использовать также спецсимволы (!#$%&*+-=?@^_) ? : ')
    t = input('Хочешь ли ты иметь в своих паролях неоднозначные символы (il1Lo0O) ? : ')
    print()
    w, chars, chars2, count = [], [], [], 0


def chistka():
    global x, y, z, s, s1, a, t, chars, chars2, w, count
    w.clear()
    chars.clear()
    chars2.clear()
    x, y, z, s, s1, a, t, count, h1, h2, h3, h4, h5 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

def generation_auto():
    global w, chars, chars2, count, x, y
    w, chars, chars2, count, x, y = [], [], [], 0, random.randint(8, 15), random.randint(7, 13)
    while count != x:
        for _ in range(y):
            h1, h2, h3, h4 = random.choice(digits), random.choice(uppters), random.choice(lowters), random.choice(punct)
            w += [h1, h2, h3, h4]
            chars.append(random.choice(w))
            w.clear()
            if len(chars) != 1:
                random.shuffle(chars)
        chars2.append(''.join(chars))
        chars.clear()
        count += 1
    print()
    print(f'Предлагаю твоему вниманию {x} самых клёвых и надёжных паролей по твоим запросам: ', end='\n')
    print(*chars2, sep='\n')
    print()

def generation():
    global count
    while count != x:
        for _ in range(y):
            if (z.lower() == 'да') or (z.lower() == 'yes') or (z.lower() == 'конечно') or (z.lower() == 'ну да') or (z.lower == 'дэ'):
                h1 = random.choice(digits)
                w.append(h1)
            if (s.lower() == 'да') or (s.lower() == 'yes') or (s.lower() == 'конечно') or (s.lower() == 'ну да') or (s.lower == 'дэ'):
                h2 = random.choice(uppters)
                w.append(h2)
            if (s1.lower() == 'да') or (s1.lower() == 'yes') or (s1.lower() == 'конечно') or (s1.lower() == 'ну да') or (s1.lower == 'дэ'):
                h3 = random.choice(lowters)
                w.append(h3)
            if (a.lower() == 'да') or (a.lower() == 'yes') or (a.lower() == 'конечно') or (a.lower() == 'ну да') or (a.lower == 'дэ'):
                h4 = random.choice(punct)
                w.append(h4)
            if (t.lower() == 'да') or (t.lower() == 'yes') or (t.lower() == 'конечно') or (t.lower() == 'ну да') or (t.lower == 'дэ'):
                h5 = random.choice(xx)
                w.append(h5)

            chars.append(random.choice(w))
            w.clear()
            random.shuffle(chars)
        chars2.append(''.join(chars))
        chars.clear()
        count += 1
    print()
    print('Предлагаю твоему вниманию самые клёвые и надёжные пароли по твоим запросам: ', end='\n')
    print(*chars2, sep='\n')
    print()

def again():
    global eb
    eb = 0
    xs = input(f'{name}, желаешь ли ты сгенерировать новые пароли ещё?: ')
    if (xs.lower() == 'да') or (xs.lower() == 'yes'):
        print('Поехалиии!')
        eb = True
    else:
        print(f'Хорошо, спасибо за использование генератора паролей.')
        eb = False

def goodbye():
    print()
    print('С вами был ваш покорный слуга, Георгий Валяев!')
    print('Всё, пока ...', end='')
    print('... пока!')

def auto_process():
    zapros_auto()
    if (ssd.lower() == 'да') or (ssd.lower() == 'yes') or (ssd.lower() == 'конечно') or (ssd.lower() == 'ну да') or (ssd.lower == 'дэ'):
        return True
    else:
        return False

digits = [str(i) for i in range(10)]
lowters = [chr(i) for i in range(97, 123)]
del lowters[8]
del lowters[11]
del lowters[14]
uppters = [chr(i).upper() for i in range(97, 123)]
del uppters[11]
del uppters[14]
punct = [i for i in '!#$%&*+-=?@^_.']
xx = [str(i) + str(j) for i in 'il1Lo0O' for j in 'il1Lo0O' if i != j]
h1, h2, h3, h4, h5 = 0, 0, 0, 0, 0

privet()
opp = auto_process()
if opp:
    generation_auto()
    chistka()
    while opp:
        again()
        if eb:
            print("Вас горячо приветствует генератор надёжных и безопасных паролей")
            print()
            print("Отнесись к следующим вопросам осознанно и целенаправленно)")
            opp = auto_process()
            if opp:
                generation_auto()
                chistka()
                continue
            else:
                opp = True
                data_zapros()
                generation()
                chistka()
                continue
        else:
            goodbye()
            break

else:
    data_zapros()
    generation()
    chistka()
    while True:
        again()
        if eb:
            print("Вас горячо приветствует генератор надёжных и безопасных паролей")
            print()
            print("Отнесись к следующим вопросам осознанно и целенаправленно)")
            opp = auto_process()
            if opp:
                generation_auto()
                chistka()
                continue
            else:
                opp = True
                data_zapros()
                generation()
                chistka()
                continue
        else:
            goodbye()
            break