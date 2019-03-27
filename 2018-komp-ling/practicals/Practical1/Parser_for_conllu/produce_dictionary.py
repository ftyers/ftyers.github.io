from io import open
from conllu import parse_incr

class Dict:
    def make_dict(conllu_train):
        all_sent=[]
        data_file = open(conllu_train, "r", encoding="utf-8")
        for tokenlist in parse_incr(data_file):
            for token in tokenlist:
                all_sent.append(token['form'])
        k = list(set(all_sent))
        k.sort(key = lambda s: len(s), reverse=True)
        data_file.close()
        print('Dictionary is successfully created. Number of words is {}'.format(len(k)))
        return k