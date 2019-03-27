from produce_dictionary import Dict
from extract_gold_stand import Gold_standart
from extract_test_sent import Test_sent
from Evaluation import Eval

parsed_sent=[]

def main():
    print('Insert file name of train corpus')
    train = str(input())
    print('Insert file name of test corpus')
    test = str(input())

    dict = Dict.make_dict(train)
    gold_standart = Gold_standart.extract_seg_sent(test)
    test_sent = Test_sent.extact(test)

    def maxmatch(sentence, dictionary):
        global parsed_sent
        if len(sentence) == 0:
            return 'list is empty'
        for i in range(len(sentence), -1, -1):
            firstword = sentence[0:i]
            remainder = sentence[i:]
            if firstword in dictionary:
                parsed_sent.append(firstword)
                return maxmatch(remainder, dictionary)
            if i == 1:
                firstword = sentence[0]
                remainder = sentence[1:]
                parsed_sent.append(remainder)
                parsed_sent.append(firstword)

    def parser(used_dict, sentences):
        global parsed_sent
        res = []
        for sent in sentences:
            maxmatch(sent, used_dict)
            res.append(' '.join(parsed_sent))
            parsed_sent=[]
        print('All sentences were parsed')
        return res

    result = parser(dict, test_sent)
    Eval.score(gold_standart,result)

main()