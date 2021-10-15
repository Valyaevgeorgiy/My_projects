import re
def names():
    global name
    name = input('Пожалуйста, введи своё имя правильно: ')
    print(f'{name}, привет :) ')
def privet():
    global name, s
    print()
    print("Вас горячо приветствует бот шифрования и дешифрования текста методом шифра Цезаря!")
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

def data_zapros():
    global x, y, z, txt, txt2
    df, xs = False, 0
    x = input('Что ты хочешь организовать: шифрование или дешифрование? : ')
    y = input('На каком языке нужно провести операцию: русский или английский? : ')
    z = input('Какой шаг сдвига (вправо) тебе необходим для шифрования ( > 0) или дешифрования ( < 0)? : ')
    txt, txt2 = input('Набери здесь текст для проведения операции: '), ''
    z1 = ''
    for i in range(len(z)):
        if z[i] != '-':
            if z[i].isdigit():
                z1 += z[i]
        else:
            df = True
    z = int(z1)
    if df:
        xs -= z
        z = xs

def zapros_auto():
    global s
    s = input('А хочешь быстро узнать уникальную шифровку своего текста автоматически? : ')

def shifr_Cesar_auto():
    txt, s, j, v = input('Набери здесь текст для проведения операции: '), '', 0, 0
    x = [len(i) for i in re.findall(r'\b\w+\b', txt)]
    z, x0, sas, txt2 = x[0], 0, 0, ''
    engl_low = [chr(j) for j in range(97, 123)]
    engl_upp = [engl_low[i].upper() for i in range(len(engl_low))]
    engl_alph = engl_low + engl_upp
    ru_low = [chr(i).lower() for i in range(1040, 1072)]
    ru_upp = [ru_low[i].upper() for i in range(len(ru_low))]
    ru_alph = ru_low + ru_upp

    for i in range(len(txt)):
        if txt[i].isalpha():
            if (txt[i - 1].isspace()):
                x0 += 1
                z = x[x0]
            if txt[i].isupper():
                if txt[i] in engl_alph:
                    sas = 26
                    txt2 += str(engl_alph[((engl_alph.index(txt[i])) + z) % sas].upper())
                else:
                    sas = 32
                    txt2 += str(ru_alph[((ru_alph.index(txt[i])) + z) % sas].upper())
            else:
                if txt[i] in engl_alph:
                    sas = 26
                    txt2 += str(engl_alph[((engl_alph.index(txt[i])) + z) % sas].lower())
                else:
                    sas = 32
                    txt2 += str(ru_alph[((ru_alph.index(txt[i])) + z) % sas].lower())
        elif txt[i].isdigit():
            txt2 += txt[i]
        else:
            if (txt[i - 1].isspace()):
                x0 += 1
                z = x[x0]
            txt2 += str(txt[i])
    print()
    print(f'{name}, представляю твоему вниманию зашифрованный текст: ')
    print(txt2)
    print()

def shifr_Cesar():
    global txt, txt2, z
    sas = 0
    for i in range(len(txt)):
        if txt[i].isalpha():
            if txt[i].isupper():
                if txt[i] in engl_alph:
                    sas = 26
                    txt2 += str(engl_alph[((engl_alph.index(txt[i])) + z) % sas].upper())
                else:
                    sas = 32
                    txt2 += str(ru_alph[((ru_alph.index(txt[i])) + z) % sas].upper())
            else:
                if txt[i] in engl_alph:
                    sas = 26
                    txt2 += str(engl_alph[((engl_alph.index(txt[i])) + z) % sas].lower())
                else:
                    sas = 32
                    txt2 += str(ru_alph[((ru_alph.index(txt[i])) + z) % sas].lower())
        else:
            txt2 += str(txt[i])

    print()
    if z > 0:
        print(f'{name}, представляю твоему вниманию зашифрованный текст: ')
        print(txt2)
    else:
        print(f'{name}, представляю твоему вниманию расшифрованный текст: ')
        print(txt2)
    print()

def chistka():
    global x, y, z, txt, txt2
    x, y, z, txt, txt2 = 0, 0, 0, '', ''

def again():
    global eb
    eb = 0
    xs = input(f'{name}, желаешь ли ты пошифровать по-Цезарски ещё?: ')
    if (xs.lower() == 'да') or (xs.lower() == 'yes'):
        print('Поехалиии!')
        eb = True
    else:
        print(f'Хорошо, спасибо за использование бота.')
        eb = False

def goodbye():
    print()
    print('С вами был ваш покорный слуга, Георгий Валяев!')
    print('Всё, пока ...', end='')
    print('... пока!')

def auto_process():
    global s
    zapros_auto()
    if (s.lower() == 'да') or (s.lower() == 'yes') or (s.lower() == 'конечно') or (s.lower() == 'ну да') or (s.lower == 'дэ'):
        return True
    else:
        return False

def auto_1():
    global opp
    shifr_Cesar_auto()
    chistka()

def manual_2():
    data_zapros()
    shifr_Cesar()
    chistka()

engl_low = [chr(j) for j in range(97,123)]
engl_upp = [engl_low[i].upper() for i in range(len(engl_low))]
ru_low = [chr(i).lower() for i in range(1040, 1072)]
ru_upp = [ru_low[i].upper() for i in range(len(ru_low))]
engl_alph, ru_alph = engl_low + engl_upp, ru_low + ru_upp

privet()
while True:
    opp = auto_process()
    if opp:
        auto_1()
        again()
        if eb:
            print("Вас горячо приветствует бот шифрования и дешифрования текста методом шифра Цезаря!")
            continue
        else:
            goodbye()
            break
    else:
        print(f"{name}, отнесись к следующим вопросам осознанно и целенаправленно)")
        manual_2()
        again()
        if eb:
            print("Вас горячо приветствует бот шифрования и дешифрования текста методом шифра Цезаря!")
            continue
        else:
            goodbye()
            break