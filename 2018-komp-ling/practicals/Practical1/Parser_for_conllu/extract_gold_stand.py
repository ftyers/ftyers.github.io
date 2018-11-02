from io import open
from conllu import parse_incr

class Gold_standart:
    def extract_seg_sent(g):
        data_file = open(g, "r", encoding="utf-8")
        all_sent=[]
        for tokenlist in parse_incr(data_file):
            sent=[]
            for token in tokenlist:
                sent.append(token['form'])
            all_sent.append(' '.join(sent))
        data_file.close()
        print('Gold stadart was extracted')
        return all_sent