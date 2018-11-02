from io import open
from conllu import parse_incr

class Test_sent:
    def extact(test_file):
        all_sent = []
        data_test = open(test_file, "r", encoding="utf-8")
        for tokenlist in parse_incr(data_test):
            all_sent.append(tuple(dict(tokenlist.metadata).values())[1])
        print('Test sentences are extracted')
        return all_sent