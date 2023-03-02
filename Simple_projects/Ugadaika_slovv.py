import random

def names():
    name = input('Пожалуйста, введи своё имя правильно: ')
    print(f'{name}, привет :) ')

def privet():
    global name
    print()
    print("Вас горячо приветствует Угадайка слов!")
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

def parsing_words():
    global words, i1
    words, i1 = [], ''
    with open('russia_words.txt', mode='r', encoding='utf-8') as xxs:
        for i in xxs:
            for j in range(len(i)):
                if i[j] != "\n":
                    i1 += i[j].lower()
            if i1 == 'ад' or i1 == 'ас' or i1 == 'ах' or i1 == 'го' or i1 == 'да' or i1 == 'на' or i1 == 'ор':
                words.append(i1)
            if i1 == 'ум' or i1 == 'ух' or i1 == 'эх' or i1 == 'юг' or i1 == 'яд':
                words.append(i1)
            if (len(i1) >= 3):
                if i1[-3:] == '...':
                    i2 = i1[:-3].lower()
                    i1 = ''
                    words.append(i2)
                elif i1[-2:] == '..':
                    i2 = i1[:-2].lower()
                    i1 = ''
                    words.append(i2)
                elif i1[-1] == '.':
                    i2 = i1[:-1].lower()
                    i1 = ''
                    words.append(i2)
                elif i1[-1] == '\ufeff':
                    i2 = i1[:-1].lower()
                    i1 = ''
                    words.append(i2)
                else:
                    i2 = i1.lower()
                    i1 = ''
                    words.append(i2)
    print(f'На данный момент в нашей базе {len(words)} русских слов(а)!')

def get_word(text_list):
    word = random.choice(text_list)
    return word.upper()

def print_word(word_, list_):
    for c in word_:
        if c in list_:
            print(c, end=' ')
        else:
            print('_', end=' ')
    print()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ ⎞
                   |    
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |     ⎛ 
                   |
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼⎞
                   |
                   |
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     ⎛▼
                   |
                   |
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      ▼
                   |
                   |
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    word_completion = ['*' for _ in range(len(word))]       # список, содержащий символы _ на каждую букву задуманного слова
    guessed = False                                         # сигнальная метка
    guessed_letters = []                                    # список уже названных букв
    guessed_words = []                                      # список уже названных слов
    tries = 6                                               # количество попыток
    print(display_hangman(tries))
    print(f'Слово из {len(word)} букв ', *word_completion, sep='')

    error_words = ['Не то печатаешь, давай заново',
                   'Что печатаешь, двоечник! Заново',
                   'Ошибка. Пробуй заново',
                   'Кто тебя учил текст набирать? Удаляю и снова печатай',
                   'Неверный текст, снова давай',
                   'Галиматья, опять давай',
                   'Чушь! Нет таких букв в алфавите. Снова давай']
    guessed_list = ['Ты уже писал такое. Напряги извилины',
                    'Тебе надо на свежий воздух. То же самое пишешь',
                    'Было уже. Попробуй еще',
                    'Опять! было уже',
                    'Что заладил одно и то же. Давай думай еще',
                    'Нет. Было уже. Еще варианты']
    win_words = ['Выиграл! Красава! ', 'Угадал, Дай пять! Хотя нет, можешь нажать пять раз [Enter]',
                 'Ты разгадал! Всеми правдами и неправдами ты сделал это']
    guess_words = ['Есть такая буква', 'Угадал букву']
    not_guess_words = ['Нет такого слова', 'Вот и не угадал', 'Не угадал', 'Не то слово',
                       'Хватит себя мучать. Угадывай буквы', 'Нет. Не выдумаывай']
    not_guess_letter = ['Нет такой буквы', 'Вот и не угадал', 'Не угадал', 'Не та буква',
                        'Подумай еще и начни с другой буквы', 'Нет. Не выдумаывай']
    loser_words = ['Ты loser!', 'Ха! Не угадал. Ты проиграл', 'Ты не смог угадать', 'Game over']

    while not guessed:
        word_input = input('Введи букву ').upper()
        if not word_input.isalpha():
            print(get_word(error_words))
            continue
        if (word_input in guessed_letters) or (word_input in guessed_words):
            print(get_word(guessed_list))
            continue

        if len(word_input) > 1:
            if word_input == word:
                print(get_word(win_words))
                break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print(get_word(not_guess_words))
                print(display_hangman(tries))
                print(f'Слово из {len(word)} букв ', *word_completion, sep='')

        if len(word_input) == 1:
            guessed_letters.append(word_input)
            if word_input in word:
                guessed = True
                for i in range(len(word)):
                    if word[i] == word_input:
                        word_completion[i] = word_input
                    if not word_completion[i].isalpha():
                        guessed = False
                if guessed:
                    print(f'Да! Слово из {len(word)} букв - это', *word_completion, sep=' ')
                    print(get_word(win_words))
                else:
                    print(get_word(guess_words))
                    print(display_hangman(tries))
                    print(f'Слово из {len(word)} букв ', *word_completion, sep='')
            else:
                tries -= 1
                print(get_word(not_guess_letter))
                print(display_hangman(tries))
                print(f'Слово из {len(word)} букв ', *word_completion, sep='')
        if tries == 0:
            print(get_word(loser_words))
            break

def again():
    global eb
    eb = 0
    xs = input(f'{name}, желаешь ли поугадать словечки русские снова?: ')
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

privet()
parsing_words()
play(get_word(words))
while True:
    again()
    if eb:
        print("Вас горячо приветствует Угадайка слов!")
        print('Поехалиии')
        play(get_word(words))
        continue
    else:
        goodbye()
        break