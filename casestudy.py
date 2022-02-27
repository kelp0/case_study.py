from textblob import TextBlob

text = input()
sentences = text.count('.') + text.count('?') + text.count('!')
words = text.count(' ') + 1
syllables = 0
blob = TextBlob(text)
if 97 <= ord(text[0].lower()) <= 122:
    vowels_en = ['a', 'e', 'i', 'o', 'u', 'y']
    for letter in vowels_en:
        syllables += (text.lower()).count(letter)
    ASL = words / sentences
    ASW = syllables / words
    FRE = 0.39 * ASL + 11.8 * ASW - 15.59
else:
    vowels_rus = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']
    for letter in vowels_rus:
        syllables += (text.lower()).count(letter)
    ASL = words / sentences
    ASW = syllables / words
    FRE = 206.835 - 1.3 * ASL - 60.1 * ASW
if FRE <= 25:
    difficulty = 'Текст трудно читается (для выпускников ВУЗов).'
elif 50 >= FRE > 25:
    difficulty = 'Текст немного трудно читать (для студентов).'
elif 80 >= FRE > 50:
    difficulty = 'Простой текст (для школьников).'
else:
    difficulty = 'Текст очень легко читается (для младших школьников).'
print('Предложений:',sentences)
print('Слов:',words)
print('Слогов:',syllables)
print('Средняя длина предложения в словах:',ASL)
print('Средняя длина слова в слогах:',ASW)
print('Индекс удобочитаемости Флеша:',FRE)
print(difficulty)
if 97 <= ord(text[0].lower()) <= 122:
    analysisPol = blob.polarity
    analysisSub = blob.subjectivity
else:
    final = blob.translate(to='en')
    analysisPol = final.polarity
    analysisSub = final.subjectivity
if analysisPol > 0.5:
    print('Тональность текста: положительный')
elif -0.5 <= analysisPol <= 0.5:
    print('Тональность текста: нейтральный')
elif analysisPol < -0.5:
    print('Тональность текста: отрицательный')
analysisSub = round(analysisSub * 100,1)
analysisSub = 100 - analysisSub
print('Объективность:',analysisSub,'%')
