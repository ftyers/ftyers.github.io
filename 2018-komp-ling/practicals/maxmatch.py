import os


script_dir = os.path.dirname(__file__)
rel_path_dict = "dict.txt"
rel_path_test = "test.txt"
abs_path_dict = os.path.join(script_dir,rel_path_dict)
abs_path_test = os.path.join(script_dir,rel_path_test)


def dictionary():#extrac the words from the 2nd column of the conllu file.
    with open(abs_path_dict, 'r') as f:
        f = f.read()
        f = f.split()
        w = []
        for i in f:
            if len(i) <= 8:
                if 't' not in i and 's' not in i:
                    w.append(i)
    return w


def max_match(text,wordsdict):# Do the maxmatch algorithm
    wordsdict = sorted(wordsdict,key=lambda i:len(i),reverse=True)
    len_max = len(wordsdict[0])
    tokenized = []
    while text:
        if len_max > len(text):
            len_max = len(text)
        if len_max > 1:
            if text[0:len_max] in wordsdict:
                tokenized.append(text[0:len_max])
                text = text[len_max:]
                len_max = len(wordsdict[0])
            else:
                len_max -= 1
        elif len_max == 1:
            tokenized.append(text[0:1])
            text = text[1:]
            len_max = len(wordsdict[0])
    tokenized = ' '.join(tokenized)
    return tokenized



def text_clenser():#Extract the sentences from the 2nd column of the conllufile
    with open(abs_path_test, 'r') as test:
        test = test.read()
        test = test.split()
        sentence = []
        for i in test:
            if len(i) >= 6:
                if 't' not in i:
                    sentence.append(i)
    return sentence


def main(text,dict):#writing the results
    n=0
    while n < len(text):
        sent = text[n]
        print(sent)
        print('to')
        print(max_match(sent,dict))
        print()
        n += 1


if __name__ == '__main__':
    main(text_clenser(),dictionary())






