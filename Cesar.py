result = []
alpH = ["А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М", "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х", "Ц", "Ч", "Ш", "Ш", "Ъ", "Ы", "Ь", "Э", "Ю", "Я"]
alph = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
word = str(input("Введите слово, которое хотите зашифровать: "))
sdvig = int(input("С каким сдвигом зашифровать слово: "))
while sdvig >= 64:
    sdvig -= 33
while sdvig < 0:
    sdvCo = int(input("Вы ввели некорректное число для сдвига, попробуйте ещё раз: "))
for i in range (len(word)):
    if word[i] not in alph and word[i].lower() not in alph:
        result.append(word[i])
    elif word[i] in alpH:
        s = alpH.index(word[i])
        if abs((s + sdvig)) - abs(len(alpH)) >= 0:
            result.append(alpH[abs(len(alpH) - (s + sdvig))])
        else:
            result.append(alpH[s + sdvig])
    else:
        s = alph.index(word[i])
        if abs((s + sdvig)) - abs(len(alph)) >= 0:
            result.append(alph[abs(len(alph) - (s + sdvig))])
        else: result.append(alph[s + sdvig])
print(*result, sep="")