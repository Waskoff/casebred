with open('input.txt', 'r', encoding='utf-8') as f:
    list_string = f.readlines()
txt = ''
for el in list_string:
    if el.find('\n') != -1:
        el = el[:el.find('\n')] + el[el.find('\n')+1:] + ' '
    del_line = '@"#$%^&*()_-+=|/{}[]:;<>`~\''
    for char in el:
        if char not in del_line:
            txt += char
for char in txt:
    symbols = '?.,!'
    if char in symbols and txt[txt.find(char)-1] == ' ':
        txt = txt[:txt.find(char)-1] + txt[txt.find(char):]
words_txt = txt.split()
words_txt_2 = words_txt.copy()
word_unique = []
for word in words_txt:
    if word not in word_unique:
        word_unique.append(word)
dictionary = {}
for word in word_unique:
    next_word = []
    n = words_txt.count(word)
    for num in range(n):
        if words_txt.index(word, num)+1 < len(words_txt):
            next_word.append(words_txt[words_txt.index(word, num)+1])
            words_txt.remove(words_txt[words_txt.index(word)])
    dictionary[word] = next_word
print(dictionary)

word_upper = []
for el in words_txt_2:
    if el[0].isupper():
        word_upper.append(el)
print(word_upper)

from random import *

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


