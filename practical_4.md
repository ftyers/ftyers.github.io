### Practical 4

1. Сначала я запустила код из раздела *Regular expressions*, все сработало как надо!
2. После попробовала *matplotlib*

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

С помощью *sklearn* у меня получилось запустить perceptron, я разделила данные на тестовую и тренировочную выборку с помощью:
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

```python
import sys
from sklearn.linear_model import perceptron
from sklearn.model_selection import train_test_split
import numpy as np

words = []   
data = []    
labels = []   

for line in open('/Users/rysshe/comp_ling_files/prac_2/ranks.tsv').readlines():
    row = line.strip().split('\t')
    vec = []
    for i in row[3].split(','):
        vec.append(int(i))
    data.append(vec)
    labels.append(int(row[0]))
    words.append((row[1], row[2], int(row[0])))
    
X, y = np.array(data), np.array(labels)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

net = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(X_train, y_train)

result = net.predict(X_test)

total = 0
correct = 0
for i in range(0, len(result)):
    if y_test[i] == result[i]:
        correct = correct + 1

    total = total + 1
print(correct/total)

```
correct/total = 0.9977628635346756
Очень хороший результат!

3. Screenscraping



```python
def strip_html(h):
	o = ''
	inTag = False
	for c in h: 
		if c == '<':
			inTag = True
			continue
		if c == '>':
			inTag = False
			continue
		if not inTag:
			o = o + c
	return o

tem = '_'
zkod = '_'
ipa = '_'
for line in sys.stdin.readlines(): 
        line = line.strip()
        text = strip_html(line);

        if text.count('Корень:') > 0:
                stem = text.split(':')[1].strip('.')
        if text.count('МФА') > 0:
                ipa = text.split('[')[1].split(']')[0]
        if text.count('тип склонения') > 0:
                zkod = text.split('тип склонения')[1].strip().split(' ')[0]

        if stem != '_' and zkod != '_' and ipa != '_':
                print('%s\t%s\t%s' % (stem, zkod, ipa))
                stem = '_'
                zkod = '_'
                ipa = '_'
                
h1 = '_';
for line in sys.stdin.readlines(): 
	if line.count('<h1>') > 0: 
		h1 = strip_html(line)

	if h1 != 'Русский': 
		continue

```

4. Unigram tagger 

Код моего теггера можно посмотреть в файлe tagger.py, его можно запустить с помощью: $ python3 tagger.py [input_file] model.tsv
Output будет записан в файл tagged
Слова из [input_file] я привела к их леммам и искала их по словарю, созданному из model.tsv.
К сожалению, возможности теггера ограничиваются только словами, присутствующими в модели. Слова, которых в модели нет, он отмечает как
OOV - out of vocab

>>> Could you store other single-word features in your unigram model ? Which features might you like to store ?

Да, я предполагаю, что в качестве фич можно хранить тег предыдущего слова! Это могло бы быть очень полезно, но это уже не unigramm, а bigramm tager :)




