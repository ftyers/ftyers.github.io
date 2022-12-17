from max_match import MaxMatch

with open('word_forms_train.txt') as f:
    dictionary = f.read().split()

with open('train_sentences.txt') as f:
    train_sentences = f.read().split()

f = open('MaxMatchSentences_train.txt', 'w')
count = 0
for i in train_sentences:
    a = MaxMatch(i, dictionary)
    f.write(a)
    count += 1
    print (count)
f.close()
print (count)
print(len(train_sentences))
print ('Done')