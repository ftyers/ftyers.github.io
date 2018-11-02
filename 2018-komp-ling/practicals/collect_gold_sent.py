from io import open
from conllu import parse_incr

data_file = open('ja_gsd-ud-test.conllu', "r", encoding="utf-8")
all_sent=[]
for tokenlist in parse_incr(data_file):
    sent=[]
    for token in tokenlist:
        sent.append(token['form'])
    all_sent.append(' '.join(sent))

f = open('gold_sent.txt', 'w', encoding='utf-8')
for i in all_sent:
    f.write(i+'\n')
f.close()
