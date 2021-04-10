with open('input.txt', 'r') as f:
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
words_txt2 = words_txt.copy()

print(words_txt)
word_dict = {}
a = []

for word in words_txt:
    if word not in words_txt:
        word_dict[word] = a
