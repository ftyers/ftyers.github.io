
# coding: utf-8

# In[ ]:


keys = []
values = []
path = 'rus-lat.tsv'
path_1 = 'text.txt'

# compile the dictionary, using a table of correspondence between russian and latin chars
f = open(path)
for line in f:
    r, l = line.split('\t')
    keys.append(r.strip())
    keys_up = [r.strip().capitalize()]
    keys.extend(keys_up)

    values.append(l.strip())
    values_up = [l.strip().capitalize()]
    values.extend(values_up)

    corresp_table = dict(zip(keys, values))

f.close()

# the transliteration of char 'Е'('е') depends on some extra conditions: after vowels, 'ъ', 'ь' it's transliterated
# as 'Ye'('ye'), in other cases it's 'E'('e')
cond = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ъ', 'ь']
n_string = ''

t = open(path_1)
for line in t:
    for char in line:
        pr_char = line[(line.index(char))-1]
        if line.index(char) == 0 and char == 'е' or pr_char in cond and char == 'е':
            char = 'ye'
        elif line.index(char) == 0 and char == 'Е' or pr_char in cond and char == 'Е':
            char = 'Ye'
        elif char in corresp_table.keys():
            char = corresp_table[char]
        else:
            char = char
        n_string += char
        
t.close()

# write transliterated text to a new file
with open('trans_text.txt', 'w') as e:
    e.write(n_string)

