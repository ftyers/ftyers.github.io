## Regular expressions

###### regexp.py
```
import re

s = 'Привет мир!'

print(re.search(r'м[а-я]+', s))

m = re.search(r'м[а-я]+', s)
print(m.group())
print(m.span())

print(re.sub('[а-я]', 'x', s))
```
Output:
```
<re.Match object; span=(7, 10), match='мир'>
мир
(7, 10)
Пxxxxx xxx!
```

## Libraries and modules in Python

##### matplotlib

```
$ head ranks.txt
```
```
1       70048   ,
2       45571   .
3       22727   в
4       21243   и
5       16177   "
6       12898   -
7       10531   на
8       10434   не
9       7464    что
10      6833    с

```

plot.py
```
import sys
import matplotlib.pyplot as plt

x = []
y = []

fd = open('ranks.txt', 'r', encoding='utf-8')
for line in fd.readlines():
    line = line.strip()
    if line == '':
        continue
    row = line.replace('\ufeff', '').split('\t')
    x.append(int(row[0]))
    y.append(int(row[1]))

plt.plot(x, y, 'ro')
plt.show()
```

![output](https://files.slack.com/files-pri/TD571G43V-FH966V3G8/untitled.png)

##### ElementTree

###### gloss.py
```
import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding='utf-8')
tree = ET.parse(r'isl-ex.xml', parser=parser)
root = tree.getroot()

for tier in root.findall('.//tier'):
    if tier.attrib['id'] == 'n':
        for item in tier.findall('.//item'):
            print(item.text)
```
```
(Þau) Jón og María eru vinir.
they.NEUT Jón og María are friends
Jón and María are friends.
```

> How would you get just the Icelandic line and the gloss line ?

To get the Icelandic line:
```
for tier in root.findall('.//tier'):
    if tier.attrib['id'] == 'n':
        for item in tier.findall('.//item'):
            if item.attrib['tag'] == 'L':
                print(item.text)
```
```
(Þau) Jón og María eru vinir.
```
To get the gloss line:
```
for tier in root.findall('.//tier'):
    if tier.attrib['id'] == 'n':
        for item in tier.findall('.//item'):
            if item.attrib['tag'] == 'T':
                print(item.text)
```
```
Jón and María are friends.
```

##### scikit learn
###### pronunciation.py
```
import sys
from sklearn.linear_model import perceptron
from sklearn.model_selection import train_test_split

words = []    # The word, correct label and pronunciation
data = []     # Training examples, e.g. feature vectors
labels = []   # Correct labels

for line in open('pronunciation_data.tsv', 'r', encoding='utf-8').readlines():
    row = line.strip().split('\t')
    vec = []
    for i in row[3].split(','):
        vec.append(int(i))
    data.append(vec)

    labels.append(int(row[0]))
    words.append((row[1], row[2], int(row[0])))
    
X_train, X_test, y_train, y_test, word_test, word_tr = train_test_split(data, labels, words, test_size=0.5, random_state=42)
    
net = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(X_train,y_train)

result = net.predict(X_test)

total = 0
correct = 0
for i in range(0, len(word_tr)):
    if result[i] == word_tr[i][2]:
        print('+', result[i], word_tr[i])
        correct = correct + 1
    else:
        print('-', result[i], word_tr[i])
    total = total + 1
print(correct/total)
```

> What kind of accuracy do you get ? What kind of errors does the classifier make ? How do you think you might be able to improve on the accuracy ?

The accuracy level is ``0.9973118279569892``, the classifier made mistakes only 3 times: 
```
- 0 ('#церковь#', '[ˈt͡sɛrkəfʲ]', 1)
- 0 ('#бровь#', '[brofʲ]', 1)
- 0 ('#нелюбовь#', '[nʲɪlʲʊˈbofʲ]', 1)
```
As we see, all words end with 'вь', so we can add more examples ending with 'вь' to our train set

## Screenscraping

```
$ wget -q -O - "http://ru.wiktionary.org/wiki/страх" > страх.html
$ wget -q -O - "http://ru.wiktionary.org/wiki/дерево" > дерево.html
```

> I leave the second problem (dealing with the окончание) as an exercise for the reader.

The code can be found in wiktionary.py
Output:
```
-дерев-	1a^	ˈdʲerʲɪvə
```

## Unigram tagger

Code of unigram tagger can be found in tagger.py. How to run:
```
python train.py model.tsv sample.txt > output.tsv
```
Example of output:
```
1       В       ADP     _       _       _       _       _
2       жизни   NOUN    _       _       _       _       _
3       Левы    NOUN    _       _       _       _       _
4       Одоевцева       NOUN    _       _       _       _       _
5       ,       PUNCT   _       _       _       _       _
6       из      ADP     _       _       _       _       _
7       тех     DET     _       _       _       _       _
8       самых   ADJ     _       _       _       _       _
9       Одоевцевых      NOUN    _       _       _       _       _
10      ,       PUNCT   _       _       _       _       _
11      не      PART    _       _       _       _       _
12      случалось       NOUN    _       _       _       _       _
13      особых  ADJ     _       _       _       _       _
14      потрясений      NOUN    _       _       _       _       _
15      -       NOUN    _       _       _       _       _
16      она     PRON    _       _       _       _       _
17      в       ADP     _       _       _       _       _
18      основном        ADJ     _       _       _       _       _
19      протекала       NOUN    _       _       _       _       _
20      .       PUNCT   _       _       _       _       _
```

> How accurate is the tagger ?

Evaluation code can be found in evaluation.py, the accuracy score is ``0.8142076502732241``

> How could you improve performance without incorporating context ...
using Python string functions ?
using regular expressions ?
using screen scraping ?

Well, I guess the best improvement would be lemmatization or stemming, which we can actually reach by using any of the three above mentioned methods.

> Could you store other single-word features in your unigram model ? Which features might you like to store ?

We can store, for instance, the root of a word, which we can get by screen scraping!