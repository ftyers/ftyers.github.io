from nltk.tokenize import word_tokenize
import sys

cnt = 0
splt = list('--------')

for sent in sys.stdin:
    cnt += 1
    print('# sent_id = ' + str(cnt))
    print('# text = ' + sent)
    for i, word in enumerate(word_tokenize(sent)):
        res = []
        res.append(str(i))
        res.append(word)
        res.extend(splt)
        line = '\t'.join(res)
        print(line)
