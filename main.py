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
word_unique = []
for word in words_txt:
    if word not in word_unique:
        word_unique.append(word)

for word in word_unique:
    word_to_pop = words_txt
    next_words = []
    try:
        while word_to_pop.index(word) != -1:
            try:
                next_words.append(word_to_pop[word_to_pop.index(word)+1])
                word_to_pop.pop(word_to_pop.index(word))
            except IndexError:
                stop = True
    except ValueError:
        stop = True
    print(word,next_words)