def names():
    name = input('Пожалуйста, введи своё имя правильно: ')
    print(f'{name}, привет :) ')

def privet():
    global name
    print()
    print("Вас горячо приветствует калькулятор систем счисления!")
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
    global xs, xd, xf
    xs = input(f'{name}, введи своё число для перевода: ')
    if xs.isdigit():
        xs = int(xs)
    print('Ответь на следующие 2 вопроса в числовом формате (например, 20 или 10)')
    xd = int(input('В какой системе счисления у тебя состоит введённое число? : '))
    xf = int(input('В какую систему счисления тебе нужно перевести число? : '))

def schislenie():
    global xs, xd, xf, y, count
    y, count = 0, 0
    if xf == 10:
        while xs != 0:
            ldg = xs % 10
            y += ldg * (xd ** count)
            count += 1
            xs //= 10




