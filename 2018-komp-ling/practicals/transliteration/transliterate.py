# Транслитерация с русского на английский
text = input('Введите текст на русском для транслитерации на английский:')


# Соберем словарь для транслитерации
with open('table.tsv', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
    trans = {}
    for line in lines:
        row = line.split('\t')
        key = row[0]
        value = row[1]
        trans[key] = value


# Буква Е (Ё) русского алфавита транслитерируется в латинский алфавит как Ye, 
# если стоит в начале слова, после гласных и знаков Ъ и Ь. Во всех остальных случаях – как E.
current_char = ['start']
context_for_ye = [' ', 'а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я', 'ъ', 'ь']

trans_text = []

for letter in text:
    if letter in trans:
        previous_char = current_char.pop()
        if letter == 'е' or letter == 'ё':
            if previous_char in context_for_ye:
                char = 'ye'
            else:
                char = 'e'
        elif letter == 'Е' or letter == 'Ё':
            if previous_char == ' ':
                char = 'Ye'
            else:
                char = 'E'
        else:
            char = trans[letter]
        current_char.append(letter)
        trans_text.append(char)

output_text = ''.join(trans_text)

print(output_text)


# Пример работы алгоритма
# Съешь ещё этих мягких французских булок, да выпей же чаю. Тёмное дерево ёлка. В Елец приехал огурец! АУЕ?
# S″yesh' yeshche etikh myagkikh frantsuzskikh bulok, da vypey zhe chayu. Temnoye derevo yelka. V Yelets priyekhal ogurets! AUE?