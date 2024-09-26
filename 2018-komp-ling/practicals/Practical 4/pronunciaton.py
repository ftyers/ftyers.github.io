import sys
from sklearn.linear_model import perceptron
from sklearn.model_selection import train_test_split

words = []  # The word, correct label and pronunciation
data = []  # Training examples, e.g. feature vectors
labels = []  # Correct labels

for line in open('pronunciation_data.tsv', 'r', encoding='utf-8').readlines():
    row = line.strip().split('\t')
    vec = []
    for i in row[3].split(','):
        vec.append(int(i))
    data.append(vec)

    labels.append(int(row[0]))
    words.append((row[1], row[2], int(row[0])))

X_train, X_test, y_train, y_test, word_test, word_tr = train_test_split(data, labels, words, test_size=0.5,
                                                                        random_state=42)

net = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(X_train, y_train)

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
print(correct / total)
