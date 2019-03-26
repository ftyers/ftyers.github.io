
### Regular expressions


```python
import re 
s = 'Привет мир!'
re.search(r'м[а-я]+', s)
```




    <re.Match object; span=(7, 10), match='мир'>




```python
m = re.search(r'м[а-я]+', s)
m.group()
```




    'мир'




```python
m.span()
```




    (7, 10)




```python
re.sub('[а-я]', 'x', s)
```




    'Пxxxxx xxx!'



### Libraries and modules in Python


```python
%matplotlib inline 
```


```python
import sys
import matplotlib.pyplot as plt

x = []
y = []

fd = open('ranks.txt', 'r')
for line in fd.readlines():
        line = line.strip()
        if line == '':
                continue

        row = line.split('\t')
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, 'ro')
plt.show()
```


![png](output_7_0.png)


### ElementTree


```python
import xml.etree.ElementTree as ET

tree = ET.parse('isl-ex.xml')
```


```python
tree
```




    <xml.etree.ElementTree.ElementTree at 0x7fc9404d62e8>




```python
root = tree.getroot()
```


```python
print(root.tag)
```

    xigt-corpus



```python
for tier in root.findall('.//tier'):
        if tier.attrib['id'] == 'n':
                for item in tier.findall('.//item'):
                        print(item.text)
```

    (Þau) Jón og María eru vinir.
    they.NEUT Jón og María are friends
    Jón and María are friends.


To get just the Icelandic line and the gloss line we can filter by tag:


```python
for tier in root.findall('.//tier'):
        if tier.attrib['id'] == 'n':
                for item in tier.findall('.//item'):
                    if item.attrib['tag'] != 'T': 
                        print(item.text)
```

    (Þau) Jón og María eru vinir.
    they.NEUT Jón og María are friends


#### scikit learn

Let's create ```pronuncation.py```, where data is splitted into train and test parts:

```data_train, data_test, label_train, label_test, words_train, words_test = train_test_split(data, labels, words, test_size=0.5)```

accuracy is 0.9955 - almost 1

Let's look at the wrong classified words and the nearest letters' characteristics. Add temporary code to ```pronunciation.py```:


```python
for i in range(0, len(words_test)):
    if result[i] != words_test[i][2]:
        print('-', result[i], words_test[i], data_test[i])
```

    - 0 ('#любовь#', '[lʲʊˈbofʲ]', 1) [1, 0, 0, 0, 0, 0, 0, 0]
    - 0 ('#обувь#', '[ˈobʊfʲ]', 1) [1, 0, 0, 0, 0, 0, 0, 0]
    - 0 ('#церковь#', '[ˈt͡sɛrkəfʲ]', 1) [1, 0, 0, 0, 0, 0, 0, 0]
    - 0 ('#кровь#', '[krofʲ]', 1) [1, 0, 0, 0, 0, 0, 0, 0]
    - 0 ('#червь#', '[t͡ɕerfʲ]', 1) [0, 0, 0, 0, 0, 0, 0, 0]
    - 0 ('#бровь#', '[brofʲ]', 1) [1, 0, 0, 0, 0, 0, 0, 0]


All of them have 'ь#' after the target letter and are pronounced like /f/. But the feature set is the same for found words and words like "активность". The desicion is to mark 'в' which is followed by 'ь#' as 'в#', because 'ь' doesn't affect the consonant devoicing at the end of the word.

### Screenscraping

Fixed script ```wiktionary.py``` works such a way:

```bash
$ cat дерево.html | python3 wiktionary.py
 -дерев-	1a^	ˈdʲerʲɪvə```

symbol ^ marks special cases of inflection.
It also works for "страх":

```bash
$ cat страх.html | python3 wiktionary.py
 -страх-.	3a	strax
```

### Unigram tagger

```tagger.py``` uses language model from previous practical to tag the text in .conllu file. Input is saved in *input.conllu*, output - in *output.conllu*

```bash
$ python3 tagger.py  model.tsv < input.conllu | head 
# sent_id = 1
# text = Русские соболя.
1	Русские	-	PROPN	-	-	-	-	-	-
2	соболя	-	NOUN	-	-	-	-	-	-
3	.	-	PUNCT	-	-	-	-	-	-
# sent_id = 2
```              

Let's look at the mistakes and count the accuracy:


```python
with open('o_henry.conllu') as inp, open('output.conllu') as out:
    mistakes = 0
    word_tag_inp = [(line.split('\t')[1], line.split('\t')[3]) for line in inp if not line.startswith('#') and line != '\n']
    tags_out = [line.split('\t')[3] for line in out if not line.startswith('#') and line != '\n']
    total = len(tags_out)
    for i in range(total):
        if word_tag_inp[i][1] != tags_out[i]:
            mistakes +=1
            print(word_tag_inp[i][0], tags_inp[i], tags_out[i], sep = '\t')
    print((total-mistakes)*100/total)
```
Молли	VERB	PROPN
и	PART	CCONJ
что	PRON	SCONJ
Да	CCONJ	PART
все	PRON	DET
и	PART	CCONJ
ни	CCONJ	PART
Русские	ADJ	PROPN
что	PRON	SCONJ
щеки	ADV	NOUN
да	CCONJ	PART
хорошо	ADV	ADJ
русских	NOUN	ADJ
все	PART	DET
Рэнсом	NOUN	PROPN
и	PART	CCONJ
Рэнсом	NOUN	PROPN
что	PRON	SCONJ
все	PRON	DET
что	PRON	SCONJ
все	PRON	DET
все	PRON	DET
Малыша	NOUN	PROPN
пусть	PART	SCONJ
Малыша	NOUN	PROPN
полицейский	NOUN	ADJ
полицейского	NOUN	ADJ
чем	SCONJ	PRON
Малыша	NOUN	PROPN
Малыша	NOUN	PROPN
98.86749716874291
1. Accuracy = 98.9 %
2. We can see some mistakes in original tagging) for example, 'Молли' should be PROPN
3. In the unigram model we can store such single-word features in the unigram model as Zaliznjak code, semantic class, etc


```python

```
