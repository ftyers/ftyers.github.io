from sklearn.linear_model import perceptron
from sklearn.model_selection import train_test_split

words = []    # The word, correct label and pronunciation
data = []     # Training examples, e.g. feature vectors
labels = []   # Correct labels

file = 'pronunciation_data.tsv'
for line in open(file, encoding = "utf-8").readlines():
    row = line.strip().split('\t')
    vec = []
    for i in row[3].split(','):
            vec.append(int(i))
    data.append(vec)
    labels.append(int(row[0]))
    words.append((row[1], row[2], int(row[0])))
	
	
net = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net.fit(data,labels)

result = net.predict(data)
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

#Split texts
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.4, random_state=0)
net_final = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net_final.fit(X_train,y_train)
result_final = net_final.predict(X_test)
total = 0
correct = 0
for i in range(0, len(y_test)):
    if result_final[i] == y_test[i]:
        print('+', result_final[i], y_test[i]);
        correct = correct + 1
    else:
        print('-', result_final[i], y_test[i]);
    total = total + 1
print(correct/total)