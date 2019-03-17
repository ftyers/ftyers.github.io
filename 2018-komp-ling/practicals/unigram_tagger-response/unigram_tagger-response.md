# matplotlib

I am already familiar with regular expressions, so I have started this practical from _matplotlib_. The following code gets ranks and plots them:
````
import sys
import matplotlib.pyplot as plt

freq = []

with open('/Users/anyway/share_ubuntu/UD_Russian-SynTagRus/freq-sorted.txt', 'r') as f:
    f = f.readlines()
for line in f:
    line = line.strip('\n')
    (f, w) = line.split('\t')
    freq.append((int(f), w))

freq.sort(reverse=True)

rank = 1
min = freq[0][0]
ranks = []
for i in range(0, len(freq)): 
    if freq[i][0] < min: 
        rank = rank + 1
        min = freq[i][0]
    ranks.append([rank, freq[i][0], freq[i][1]])
    
x = []
y = []
for line in ranks:
    row = line
    x.append(int(row[0]))
    y.append(int(row[1]))
plt.plot(x, y, 'ro')
plt.show()
````
# ElementTree
The question was how I would get just the Icelandic line and the gloss line. We can just add a condition that does not take in the output lines with tag "T" that stands for translation. So the code will look like:
````
for tier in root.findall('.//tier'):
    if tier.attrib['id'] == 'n':
        for item in tier.findall('.//item'):
            if item.attrib['tag'] != 'T':   # here is the condition
                print(item.text)
````
# scikit learn

My code for perceptone trained on the half of the data can be seen in _perceptron.py_. 
It gives the following output:
````
- #хоругвь# incorrect class: 0 correct class: 1
- #обувь# incorrect class: 0 correct class: 1
- #морковь# incorrect class: 0 correct class: 1
- #бровь# incorrect class: 0 correct class: 1
- #церковь# incorrect class: 0 correct class: 1
0.9955197132616488
````
So, the accuracy is rather high, but the model cannot predict the class correctly, if a word ends with palatalization. To improve the result, we can add one more feature in vector in the dataset which would stand for palatalization in the end of a word. 

# Screenscraping

My final code for "дерево.html" with solved "окончание" issue can be seen in _wiktionary.py_.

# Unigram tagger
My script is called _tagger.py_. It works like this:
```
python3 tagger.py model.tsv input.conllu > output.conllu
```
In the same folder you will also find my model, sample input and output files. 

