words, words2, i1 = [], [], ''
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
        else:
            i11 = i1.lower()
            words2.append(i11)
            i1 = ''
print(words)
print()
print(len(words))
print()
print(words2)
print()
print(len(words2))