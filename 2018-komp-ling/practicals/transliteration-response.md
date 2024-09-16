# Transliteration
### 1. Frequency list
Download a parsed sentences file from https://github.com/UniversalDependencies:
> [ru_pud-ud-test.conllu (1,5 Mb)](https://github.com/mapozhidaeva/ftyers.github.io/blob/master/2018-komp-ling/practicals/translit/ru_pud-ud-test.conllu)

Write a code counts frequency of words in a text:
> [frequency.py](https://github.com/mapozhidaeva/ftyers.github.io/blob/master/2018-komp-ling/practicals/translit/transliterate.py)

Use one of these commands to 
```
cat ru_pud-ud-test.conllu | python3 frequency.py
```

```
python3 frequency.py < ru_pud-ud-test.conllu > text.txt
```

To get a list sorted by frequency:
```
python3 frequency.py < ru_pud-ud-test.conllu | sort -nr  > text.txt
```

Or it's also possible to use the for loop Fran advised (I just wrote the same with the format function):
```sh
for i in freq:
    print ('{}\t{}'.format(i[0], i[1]))
```
Now I have a unique word list arranged by frequency

### 2. Translit dictionary
To follow the steps below, you can open [generate_alphabet.py](https://github.com/mapozhidaeva/ftyers.github.io/blob/master/2018-komp-ling/practicals/translit/generate_alphabet.py)
Let's generate a dictionary we will use to tranliterate. 
First let's use unicode to simply generate Russian alphabet (both capital letters and lower-case):

```sh
for i in range (1040, 1104):
    if chr(i) == 'е':
        rus_letters.append(chr(i))
        rus_letters.append('ё')
    if chr(i) == 'Е':
        rus_letters.append(chr(i))
        rus_letters.append('Ё')
    else:
        rus_letters.append(chr(i))

print (rus_letters)
```
And I manually typed its reflexion to the English alphabet, then combined the two lists into a dictinary:
```sh
rus_letters = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
eng_letters = ['A', 'B', 'V', 'G', 'D', 'E', 'Yo', 'Zh', 'Z', 'I', 'Y', 'K', 'L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'F', 'Kh', 'Ts', 'Ch', 'Sh', 'Shch', "'", 'Y', "'", 'E', 'Yu', 'Ya', 'a', 'b', 'v', 'g', 'd', 'e', 'yo', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', "'", 'y', "'", 'e', 'yu', 'ya']

with open('trans_dict.txt', 'w') as f:
    for i in range(len(rus_letters)):
        f.write('{}\t{}\n'.format(rus_letters[i], eng_letters[i]))
```

The results are in the file [trans_dict.txt](https://github.com/mapozhidaeva/ftyers.github.io/blob/master/2018-komp-ling/practicals/translit/trans_dict.txt), which we will be using in the next code.

### 3. Finally transliteration
To follow this part, you can open the file [transliterate.py](https://github.com/mapozhidaeva/ftyers.github.io/blob/master/2018-komp-ling/practicals/translit/transliterate.py)
Please, follow the comments in the code:
```sh
import sys

# dict to store Russian to English letters
vocab = {} 
#let's import it from the file:
f = open('trans_dict.txt', 'r')
for i in f.readlines():
    i = i.strip('\n')
    r, e = i.split('\t')
    vocab[r] = e

# This string will help us check whether we need to change Russian 'е' to 'e' or 'ye'
# Because 'e' changes to 'ye' after a vowel, 'ь', 'ъ' or at the beginning of the sentence
vowels = 'уУеЕъЪаАоОэЭьЬяЯиИюЮыЫ'

for line in sys.stdin.readlines():
    #we only need the lines with tabulation:
    if '\t' not in line:
        continue
    row = line.split('\t')
    if len(row) != 10:
        continue
    #subst is the result of a transliterated word 
    subst = ''
    # this is to check if it's the beginning of a word:
    p = ''
    for i in row[1]:
        # checking if the letter is a Cyrillic letter:
        if i in vocab:
            # checking if it's a 'e' after at a particular position:
            if i == 'е' and (p in vowels or p == ''):
                subst+= 'y' + vocab[i]
            elif i == 'Е' and (p in vowels or p == ''):
                subst+= 'Y' + vocab[i]
            else:
                subst += vocab[i]
                p = i
        else:
            subst += i

    print ('{}\t{}'.format(row[1], subst))
    subst = ''
    p = ''
f.close()
```
# Voila!
The result is stored in the file text.txt

The code is a little far from perfect. For example, it doesn't check if the whole word is in CAPS. Instead every time it sees a capital 'Ш' or 'Ч' it makes it 'Sh' and 'Сh', which is most of the times fine. 

### Questions

What to do with ambiguous letters ? For example, Cyrillic `е' could be either je or e.
- I explained it i the code: 
'e' changes to 'ye' after a vowel, 'ь', 'ъ' or at the beginning of the sentence, so I check the previous letter first (if it's beginning of a word, then I use the empty variable 'p' for 'previous') if it's in the string 'уУеЕъЪаАоОэЭьЬяЯиИюЮыЫ'.

Can you think of a way that you could provide mappings from many characters to one character ?
For example sh → ш or дж → c ?
- for English transliteration I guess it's better to use IPA, because it will be a mess if we use the simple letter to letter dictionary method. Transliteration only makes sense if the language has clear and not ambiguous rules for spelling. However we might need to solve this problem for languages like German, where if we speak about German-to-Russian transliteration 'sch' can be 'сх' (if the are in two different syllables) or 'ш' (if the are in the same syllable). However there seem to be restrictions on the first case. The idea is to find them or use the dictionary to see if the word consists of 2 or more different words.

How might you make different mapping rules for characters at the beginning or end of the string ?
- use the variable "previous letter" as I did and for the end of the string - check if it's the last letter in the word by index.



