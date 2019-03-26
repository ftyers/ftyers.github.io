### Vladislav Mikhailov, MKL181

# Unigram-tagger

## Regular expressions

```
import re

s = 'Привет мир!'

re.search(r'м[а-я]+', s)
```
>> out
<_sre.SRE_Match object; span=(7, 10), match='мир'>


```
m = re.search(r'м[а-я]+', s)
m.group()
```
>> out
'мир'


```
m.span()
```
>> out
(7, 10)

```
re.sub('[а-я]', 'x', s)
```
>>> out
'Пxxxxx xxx!'

## Libraries and modules in Python

* matplotlib for plotting graphs and data visualisation
* ElementTree for parsing XML and well-formed HTML
* scikit learn for doing machine learning

#### Matplotlib

```
$ wget https://raw.githubusercontent.com/vmkhlv/ftyers.github.io/master/2018-komp-ling/practicals/practical2-response/ranks.txt
$ head ranks.txt
```
>> out
1    70048    ,
2    45571    .
3    22727    в
4    21243    и
5    16177    "
6    12898    -
7    10531    на
8    10434    не
9    7464    что
10    6833    с

```
import sys
import matplotlib.pyplot as plt


x, y = [], []

for line in open('ranks.txt').readlines():
line = line.strip()
if line == '':
continue

row = line.split('\t')
x.append(int(row[0]))
y.append(int(row[1]))

plt.plot(x, y, 'ro')
plt.show()
```

#### ElementTree

```
$ wget http://depts.washington.edu/uwcl/odin/isl-ex.xml
```

```
import xml.etree.ElementTree as ET


tree = ET.parse('isl-ex.xml')
root = tree.getroot()
root.tag
```
>> out
'xigt-corpus'


```
for tier in root.findall('.//tier'):
if tier.attrib['id'] == 'n':
for item in tier.findall('.//item'):
print(item.text)
```
>> out
(Þau) Jón og María eru vinir.
they.NEUT Jón og María are friends
Jón and María are friends.

### How would you get just the Icelandic line and the gloss line ?

```
for tier in root.findall('.//tier'):
if tier.attrib['id'] == 'n':
print(tier.findall('.//item')[0].text)

if tier.attrib['id'] == 'w-pos':
for item in tier.findall('.//item'):
print(item.text, end=' ')
```
>> out
(Þau) Jón og María eru vinir.
PUNC PRON PUNC NOUN VERB NOUN VERB NOUN PUNC 

#### scikit learn

```
$ wget http://xixona.dlsi.ua.es/~fran/pronunciation_data.tsv
```

#### An exercise for the reader is to split the data in two randomly and train on one half and test on the other half. 
```
import sys
import numpy as np
import pandas as pd
from sklearn.linear_model import perceptron
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split


# reading in the pronunciation file as a dataframe
df = pd.read_csv('pronunciation_data.tsv', sep='\t', names=['label', 'word', 'transcription', 'vector'])
# converting string values into int
df.vector = [[int(i) for i in vector.split(',')] for vector in df.vector]
df.label = df.label.astype(int)
# randomize
df = shuffle(df)

# splitting the data into train and test 50/50 (if I get the task right)
train_i, test_i = train_test_split(np.arange(len(df)), test_size=0.5)
train, test = df.iloc[train_i], df.iloc[test_i]

# train my cool perceptron
my_cool_perceptron = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
my_cool_perceptron.fit(train.vector.tolist(), train.label.tolist())
```

#### What kind of accuracy do you get ?

```
# make cool predictions
my_cool_result = my_cool_perceptron.predict(test.vector.tolist())
# mean accuracy
my_cool_perceptron.score(test.vector.tolist(), test.label.tolist())
```
>> out
0.9937275985663082

```
# creating a list of tuples: word, correct label and pronunciation
my_cool_words = [(row.word, row.transcription, row.label) for row in test.itertuples()]
print(*my_cool_words[:5], sep='\n')
```
>> out
('#вся#', '[fsʲa]', 1)
('#звание#', '[ˈzvanʲɪje]', 0)
('#столкновение#', '[stəlknɐˈvʲenʲɪje]', 0)
('#клевета#', '[klʲɪvʲɪˈta]', 0)
('#штуковина#', '[ʂtʊˈkovʲɪnə]', 0)

####  What kind of errors does the classifier make ? 

```
for i in range(0, len(my_cool_words)):
if my_cool_result[i] != my_cool_words[i][2]:
print('-', my_cool_result[i], my_cool_words[i])
```
>> out

- 0 ('#нелюбовь#', '[nʲɪlʲʊˈbofʲ]', 1)
- 0 ('#обувь#', '[ˈobʊfʲ]', 1)
- 0 ('#кровь#', '[krofʲ]', 1)
- 0 ('#червь#', '[t͡ɕerfʲ]', 1)
- 0 ('#морковь#', '[mɐrˈkofʲ]', 1)
- 0 ('#явь#', '[jæfʲ]', 1)
- 0 ('#хоругвь#', '[xɐˈrukfʲ]', 1)

#### How do you think you might be able to improve on the accuracy ?

We can improve on the accuracy if we add the following rule:
if a word ends with 'вь', then the output label from the classifier should be /f/ (1)

## Screenscraping

**I leave the second problem (dealing with the окончание) as an exercise for the reader.**

#### страх

```
$ wget -q -O - "http://ru.wiktionary.org/wiki/страх"
```

#### To do the task, I used requests and BeautifulSoup libraries. These libraries allow me for not getting lost in a bunch of for-if-loops

```
import re
import requests
from bs4 import BeautifulSoup as bs


def wiki(cool_word):

    article = bs(requests.get('http://ru.wiktionary.org/wiki/' + cool_word).text, 'html5lib')
    stem = str([s for s in article.select('p') if 'Корень' in str(s)][0].text).strip('. \n')
    if 'окончание' in stem:
        stem = stem.split('окончание')[0].strip('; ')
    pronunciation = re.findall('МФА:\s.+', str(article.get_text()))[0].replace('\xa0', ' ').replace('(файл)', '').split('[')[1].split(']')[0]
    declension = str([d for d in article.find_all('p') if 'склонение' in str(d)][0].text).replace('\xa0', ' ').split('тип склонения')[1].split()[0].strip()

    return print(stem, 'IPA: {}'.format(pronunciation), 'Зализняк: {}'.format(declension), sep='\n')
```

### How to use
```
$ echo <word> | python wiktionary.py
```
#### страх
```
$ echo 'страх' | python wiktionary.py
```
>> out
страх
Корень: -страх-
IPA: strax
Зализняк: 3a


#### дерево
```
$ echo 'дерево' | python wiktionary.py
```
>> out
дерево
Корень: -дерев-
IPA: ˈdʲerʲɪvə
Зализняк: 1a^

## Unigram tagger
#### How to use
```
$ cat my_cool_input.conllu | python3 tagger.py model.tsv 
```

#### Example output
```
1    Анкета    _    _    _    _    _    _    _
2    .    _    PUNCT    _    _    _    _    _
1    Начальник    _    NOUN    _    _    _    _    _
2    областного    _    _    _    _    _    _    _
3    управления    _    NOUN    _    _    _    _    _
4    связи    _    NOUN    _    _    _    _    _
5    Семен    _    PROPN    _    _    _    _    _
6    Еремеевич    _    _    _    _    _    _    _
7    был    _    AUX    _    _    _    _    _
8    человек    _    NOUN    _    _    _    _    _
9    простой    _    ADJNOUN    _    _    _    _    _
10    ,    _    PUNCT    _    _    _    _    _
11    приходил    _    VERB    _    _    _    _    _
12    на    _    ADP    _    _    _    _    _
13    работу    _    NOUN    _    _    _    _    _
14    всегда    _    ADV    _    _    _    _    _
15    вовремя    _    ADV    _    _    _    _    _
16    ,    _    PUNCT    _    _    _    _    _
17    здоровался    _    _    _    _    _    _    _
18    с    _    ADP    _    _    _    _    _
19    секретаршей    _    _    _    _    _    _    _
20    за    _    ADP    _    _    _    _    _
21    руку    _    NOUN    _    _    _    _    _
22    и    _    CCONJ    _    _    _    _    _
23    иногда    _    ADV    _    _    _    _    _
24    даже    _    PART    _    _    _    _    _
25    писал    _    VERB    _    _    _    _    _
26    в    _    ADP    _    _    _    _    _
27    стенгазету    _    _    _    _    _    _    _
28    заметки    _    _    _    _    _    _    _
29    под    _    ADP    _    _    _    _    _
30    псевдонимом    _    _    _    _    _    _    _
31    "    _    PUNCT    _    _    _    _    _
32    Муха    _    NOUN    _    _    _    _    _
33    "    _    PUNCT    _    _    _    _    _
34    .    _    PUNCT    _    _    _    _    _
```

## Questions

* How accurate is the tagger?

It doesn't deal good with OOV tokens. If there is no such tiken in our language model, then it doesn't annotate the token with POS-tag.

* How could you improve performance without incorporating context ...
using Python string functions ?

I have implemented .lower() method so that to marry the cases of the surface forms in the input file and in the dictionary

using screen scraping ?

Probably finding information about wordforms and POS, merge them into one paradigm for a particular word, so that to expand the language model.
