import re
txt, s, j, v = input(), '', 0, 0
x = [len(i) for i in re.findall(r'\b\w+\b',txt)]
z, x0, sas, txt2 = x[0], 0, 0, ''
engl_low = [chr(j) for j in range(97,123)]
engl_upp = [engl_low[i].upper() for i in range(len(engl_low))]
engl_alph = engl_low + engl_upp
ru_low = [chr(i).lower() for i in range(1040, 1072)]
ru_upp = [ru_low[i].upper() for i in range(len(ru_low))]
ru_alph = ru_low + ru_upp

print(x)

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
print(txt2)
