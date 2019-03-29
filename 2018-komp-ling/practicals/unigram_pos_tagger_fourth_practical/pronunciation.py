import sys
from sklearn.linear_model import perceptron
from sklearn.model_selection import train_test_split

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

#splitting the data
data_train, data_test, labels_train, labels_test, words_train, words_test = train_test_split(data, labels, words, test_size=0.5, random_state=42)

net_half = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
net_half.fit(data_train,labels_train)

result = net_half.predict(data_test)

total = 0
correct = 0
for i in range(0, len(labels_test)):
	if result[i] == labels_test[i]:
		print('+', result[i], words_test[i]);
		correct = correct + 1
	else:
		print('-', result[i], words_test[i]);
	total = total + 1
print(correct/total)