import sys
from sklearn.linear_model import perceptron
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split


def get_data(file):
    data = []
    for line in open(file).readlines():
        row = line.strip().split('\t')
        data.append(row)  
    data = shuffle(data)
    train, test = train_test_split(data, test_size=0.5)
    return train, test


def split_train(train):
    train_data = []     
    train_labels = []   
    for row in train:
        vec = [int(i) for i in row[3].split(',')]
        train_data.append(vec)
        train_labels.append(int(row[0]))
    return train_data, train_labels


def split_test(test):
    test_words = []
    test_data = []
    test_labels = []
    for row in test:
        vec = [int(i) for i in row[3].split(',')]
        test_data.append(vec)
        test_labels.append(int(row[0]))
        test_words.append(row[1])
    return test_words, test_data, test_labels
        

def run_perceptron(train_data, train_labels, test_data):
    net = perceptron.Perceptron(n_iter=100, verbose=0, random_state=None, fit_intercept=True, eta0=0.002)
    net.fit(train_data, train_labels)
    result = net.predict(test_data)
    return result


def evaluate(result, test_labels, test_words):
    total = 0
    correct = 0
    for i in range(0, len(test_words)):
        if result[i] == test_labels[i]:
            correct += 1
        else:
            print('-', test_words[i], 'incorrect class:', result[i], 'correct class:', test_labels[i]);
        total += 1
    return correct/total
  
    
def main():
    file = '/Users/anyway/pronunciation_data.tsv'
    train, test = get_data(file)
    train_data, train_labels = split_train(train)
    test_words, test_data, test_labels = split_test(test)
    result = run_perceptron(train_data, train_labels, test_data)
    print(evaluate(result, test_labels, test_words))
    
main()