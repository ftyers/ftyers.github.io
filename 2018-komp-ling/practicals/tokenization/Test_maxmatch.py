from max_match import MaxMatch

with open('word_forms_train.txt') as f:
    dictionary = f.read().split()

with open('test-sentences.txt') as f:
    sentences = f.read().split()

f = open('MaxMatchSentences_TEST.txt', 'w')
count = 0
for i in sentences:
    a = MaxMatch(i, dictionary)
    f.write(a)
    count += 1
    print (count)
f.close()
print (count)
print(len(sentences))
print ('Done')