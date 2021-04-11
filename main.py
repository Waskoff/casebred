"""

Case-study Бредогенератор
Разработчики:
Бикметов Э.Б. = 40%, Бычков К.А. = 35%, Кондрашов М.С. = 35%

"""
from random import *

# Asking for a file name
filename = input('Введите название файла (с расширением (.txt)) : ')
with open(filename, 'r', encoding='utf-8') as f:
    list_string = f.readlines()
txt = ''

# deleting/fixing symbols
for el in list_string:
    if el.find('\n') != -1:
        el = el[:el.find('\n')] + el[el.find('\n') + 1:] + ' '
    del_line = '@"#$%^&*()_—+=|/{}[]:;<>`~\'»«'
    for char in el:
        if char not in del_line:
            txt += char

for char in txt:
    symbols = '?.,!'
    if char in symbols and txt[txt.find(char) - 1] == ' ':
        txt = txt[:txt.find(char) - 1] + txt[txt.find(char):]

# making words lists
words_txt = txt.split()
words_txt_2 = words_txt.copy()
word_unique = []

# unique words list
for word in words_txt:
    if word not in word_unique:
        word_unique.append(word)

# making dictionary
dictionary = {}
for word in word_unique:
    lst = []
    ind = words_txt_2.index(word)

    while ind != -1:
        try:
            ind = words_txt_2.index(word) + 1
            lst.append(words_txt_2[ind])
            del words_txt_2[ind - 1]
        except:
            ind = -1
    if word[-1] in '.!?':
        lst = []
    dictionary[word] = lst

# First symbol is upper list
word_upper = []
for el in words_txt:
    if el[0].isupper():
        word_upper.append(el)

# Asking for a number of sentences & generating string
num_sent = int(input('Введите колличество генерируемых предложений: '))
for i in range(num_sent):
    w1 = choice(word_upper)
    sent = [w1]
    while len(sent) < 20:
        try:
            w1 = sent[-1]
            w1 = choice(dictionary[w1])
            sent.append(w1)
        except:
            if len(sent) < 5:
                try:
                    w1 = choice(dictionary[w1])
                    sent.append(w1)
                except:
                    w1 = choice(word_upper)
                    sent = [w1]
            else:
                break
    if sent[-1][-1] in '.!?':
        print(' '.join(sent))
    elif sent[-1][-1] in ',':
        sent[-1] = sent[-1][:-1]
        print(' '.join(sent) + '.')
    else:
        print(' '.join(sent) + '.')
