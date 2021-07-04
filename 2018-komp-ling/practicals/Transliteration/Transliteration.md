
# Dict

Create dict from conluu file


```python
test_conllu = 'C:\\input\\ru.conllu'
vocab_dict = {}
with open(test_conllu, "r", encoding = 'utf-8') as data:
    for line in data:
        row = line.split('\t')
        if(str(row[0]).isdigit()):
            if(row[1] in vocab_dict):
                vocab_dict[row[1]] += 1
            else:
                vocab_dict[row[1]] = 1
```

Trasnfer dict data to list and sort it


```python
freq = []

for w in vocab_dict:
    freq.append((vocab_dict[w], w))

freq.sort(reverse=True)
```

We will need ranked frequences. The best way to avoid further processing is to write sorted list into our fuile instead of dict


```python
fd = open('C:\\input\\freq_list.txt', 'w+', encoding = 'utf-8')
for w in freq:
    #print(vocab_dict[w], w)
    fd.write('%d\t%s\n' % (w[0], w[1]))
fd.close()
```

I assume that ranking equals frequency according to the example from the task.
That is why I think we can skip further code because our freq_list.txt file already have all tokens properly ranked

# Transliterator

transl.txt has table of transliterations


```python
translit_file = 'C:\\input\\transl.txt'
translit_dict = {}
with open(translit_file, "r", encoding = 'utf-8') as data:
    for line in data:
        row = line.split(' ')
        translit_dict[row[0]] = row[1]
```

This is our function for one word transliteration


```python
def rus_to_latin(word):
    latin_word = ''
    for letter in word:
        if (letter in translit_dict):
            latin_word += translit_dict[letter]
        else:
            latin_word += letter
    return 'Translit = ' + latin_word
```

go trhough conluu file and crated the data to be fritten


```python
test_conllu = 'C:\\input\\ru.conllu'
write_lines = []

with open(test_conllu, "r", encoding = 'utf-8') as data:
    for line in data:
        row = line.split('\t')
        
        if(str(row[0]).isdigit()):
            row[9] = rus_to_latin(row[1])
            write_lines.append(row)
        else:
            write_lines.append(line)
```

write results to file


```python
fd = open('C:\\input\\ru_modified.conllu', 'w+', encoding = 'utf-8')
for w in write_lines:
    if(type(w) == str):
        fd.write('%s' % (w))
    elif (type(w) == list):
        for ind in range(len(w)):
            fd.write('%s\t' % (w[ind]))
        fd.write('\n')
fd.close()
```
