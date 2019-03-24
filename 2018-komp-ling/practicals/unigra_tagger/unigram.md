# matplotlib

Получение рангов для нашего текста

````
import matplotlib.pyplot as plt

freq = []
ranks = []

#load data
with open('./../freq.txt', 'r') as f:
    f = f.readlines()
for line in f:
    line = line.strip('\n')
    (f, w) = line.split('\t')
    freq.append((int(f), w))

freq.sort(reverse=True)

#ranking data
rank = 1
min = freq[0][0]
for i in range(0, len(freq)): 
    if freq[i][0] < min: 
        rank +=1
        min = freq[i][0]
    ranks.append([rank, freq[i][0], freq[i][1]])
    
#do the plots
x = []
y = []
for line in ranks:
    row = line
    x.append(int(row[0]))
    y.append(int(row[1]))
plt.plot(x, y, 'b*')
plt.show()
````
# ElementTree

### How would you get just the Icelandic line and the gloss line ? 

````
for tier in root.findall('.//tier'):
    if tier.attrib['id'] == 'n':
        for item in tier.findall('.//item'):
            if item.attrib['tag'] != 'T':   # here is the condition
                print(item.text)
````

# scikit learn

### Perceptron answers
````
- #хоругвь# incorrect class: 0 correct class: 1
- #обувь# incorrect class: 0 correct class: 1
- #морковь# incorrect class: 0 correct class: 1
- #бровь# incorrect class: 0 correct class: 1
- #церковь# incorrect class: 0 correct class: 1
0.982857142857142856
````
To improve the quiality of our model we should use MLP, or deeper (than 1 layer) models 

# Screenscraping

done in __screencap.py__

