from nltk.tokenize import word_tokenize
import sys
s = 0
j = ['-']*8
for sentence in sys.stdin:
    s+=1
    print('# sent_id = '+str(s))
    print('# text = '+sentence)
    for ind, word in enumerate(word_tokenize(sentence)):
        res = []
        res.append(str(ind))
        res.append(word)
        res.extend(j)
        k = '\t'.join(res)
        print(k)
