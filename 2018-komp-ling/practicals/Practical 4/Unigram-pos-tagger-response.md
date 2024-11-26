# Regular expressions
```
import re

s = 'Привет мир!'

re.search(r'м[а-я]+', s)
```
>> 
<_sre.SRE_Match object; span=(7, 10), match='мир'>


```
m = re.search(r'м[а-я]+', s)
m.group()
```
>> 
'мир'


```
m.span()
```
>> 
(7, 10)

```
re.sub('[а-я]', 'x', s)
```
>>> 
'Пxxxxx xxx!'

# matplotlib

> pip install matplotlib
```
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
[Here](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%204/graph.png) is the result 

# ElementTree
>
```
import xml.etree.ElementTree as ET
tree = ET.parse('isl-ex.xml')
root = tree.getroot()
print(root.tag)
```
> xigt-corpus
```
for tier in root.findall('.//tier'):
        if tier.attrib['id'] == 'n':
                for item in tier.findall('.//item'):
                        print(item.text)
```
>(Þau) Jón og María eru vinir.

>they.NEUT Jón og María are friends

>Jón and María are friends.

Changes to get only icelandic and glosses: I added condition of tag name:
```
for tier in root.findall('.//tier'):
    if tier.attrib['id'] == 'n':
        for item in tier.findall('.//item'):
            if item.attrib['tag'] != 'T':
                print(item.text)
```
                
>(Þau) Jón og María eru vinir.

>they.NEUT Jón og María are friends

# scikit learn

For this tutorial I wrote code in Google Colab, so there are some syntax changes.
>!wget http://xixona.dlsi.ua.es/~fran/pronunciation_data.tsv
```
import sys
from sklearn.linear_model import perceptron

words = []    # The word, correct label and pronunciation
data = []     # Training examples, e.g. feature vectors
labels = []   # Correct labels
for line in open('pronunciation_data.tsv').readlines():
  row = line.strip().split('\t')
  vec = []
  for i in row[3].split(','):
    vec.append(int(i))
  data.append(vec)
  labels.append(int(row[0]))
  words.append((row[1], row[2], int(row[0])))
  
net = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(data,labels)  
```
>Perceptron(alpha=0.0001, class_weight=None, early_stopping=False, eta0=0.002,
>      fit_intercept=True, max_iter=None, n_iter=100, n_iter_no_change=5,
>      n_jobs=None, penalty=None, random_state=None, shuffle=True, tol=None,
>      validation_fraction=0.1, verbose=0, warm_start=False)
      
Then I [printed out](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%204/output.txt) the accuracy:
```
total = 0
correct = 0
for i in range(0, len(words)):
	if result[i] == words[i][2]:
		print('+', result[i], words[i]);
		correct = correct + 1
	else:
		print('-', result[i], words[i]);
	total = total + 1
print(correct/total)
```
Okay, let's shuffle our data and split it into train and test parts:
```
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.33, random_state=42)
net = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(X_train,y_train)

result = net.predict(X_test)

total = 0
correct = 0
for i in range(0, 737):
    if result[i] == words[i][2]:
        print('+', result[i], words[i]);
        correct = correct + 1
    else:
        print('-', result[i], words[i]);
    total = total + 1
```
The result is [here](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%204/output2.txt).
What's the accuracy?
```
accuracy_score(y_test, result)
```
>0.9986431478968792

Pretty good.

And what's the confusion matrix?
>array([[651,   0],
>       [  1,  85]])
      
# Unigram tagger
I prepared training [data](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%204/model.tsv) from [universal dependencies corpus for Russian](https://github.com/UniversalDependencies/UD_Russian-GSD/blob/master/ru_gsd-ud-train.conllu) and deleted all comments using this bash command:

>sed '/^#/d' ru_gsd-ud-train.conllu > corpus.txt

and deleted all blank lines using this:

>sed '/^\s*$/d' corpus.txt > tagger_base.txt

Then I wrote [python code](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%204/tagger.py) to count the most frequent tag per word and most frequent tag in general and then to predict the pos-tag for each word. It runs with:

> $ python3 tagger.py [text to be tagged] [output file]



