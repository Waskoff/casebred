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
dict = {}
for word in word_unique:
    next_word = []
    n = words_txt.count(word)
    for num in range(n):
        if words_txt.index(word, num)+1 < len(words_txt):
            next_word.append(words_txt[words_txt.index(word, num)+1])
            words_txt.remove(words_txt[words_txt.index(word)])

    dict[word] = next_word
print(dict)