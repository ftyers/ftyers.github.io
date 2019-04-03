import sys
from sklearn.linear_model import perceptron
from sklearn.model_selection import train_test_split

words = []  # The word, correct label and pronunciation
data = []  # Training examples, e.g. feature vectors
labels = []  # Correct labels

for line in open('pronunciation_data.tsv').readlines():
    row = line.strip().split('\t')
    vec = []
    for i in row[3].split(','):
        vec.append(int(i))
    data.append(vec)
    labels.append(int(row[0]))
    words.append((row[1], row[2], int(row[0])))

    

train = train_test_split(words, data, labels, test_size=0.5)

net = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(train[2], train[4])

result = net.predict(train[3])

total = 0
correct = 0
for i in range(0, len(train[1])):
    if result[i] == train[1][i][2]:
        print('+', result[i], train[1][i]);
        correct = correct + 1
    else:
        print('-', result[i], train[1][i]);
    total = total + 1
print(correct / total)
