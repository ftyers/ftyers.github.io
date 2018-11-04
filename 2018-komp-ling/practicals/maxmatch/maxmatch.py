from conllu import parse
from argparse import ArgumentParser
import sys
import numpy


def editDistance(r, h):
    '''
    This function is to calculate the edit distance of reference sentence and the hypothesis sentence.
    Main algorithm used is dynamic programming.
    Attributes:
        r -> the list of words produced by splitting reference sentence.
        h -> the list of words produced by splitting hypothesis sentence.
    '''
    d = numpy.zeros((len(r) + 1) * (len(h) + 1), dtype=numpy.uint8).reshape((len(r) + 1, len(h) + 1))
    for i in range(len(r) + 1):
        for j in range(len(h) + 1):
            if i == 0:
                d[0][j] = j
            elif j == 0:
                d[i][0] = i
    for i in range(1, len(r) + 1):
        for j in range(1, len(h) + 1):
            if r[i - 1] == h[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                substitute = d[i - 1][j - 1] + 1
                insert = d[i][j - 1] + 1
                delete = d[i - 1][j] + 1
                d[i][j] = min(substitute, insert, delete)
    return d


def getStepList(r, h, d):
    '''
    This function is to get the list of steps in the process of dynamic programming.
    Attributes:
        r -> the list of words produced by splitting reference sentence.
        h -> the list of words produced by splitting hypothesis sentence.
        d -> the matrix built when calulating the editting distance of h and r.
    '''
    x = len(r)
    y = len(h)
    list = []
    while True:
        if x == 0 and y == 0:
            break
        elif x >= 1 and y >= 1 and d[x][y] == d[x - 1][y - 1] and r[x - 1] == h[y - 1]:
            list.append("e")
            x = x - 1
            y = y - 1
        elif y >= 1 and d[x][y] == d[x][y - 1] + 1:
            list.append("i")
            x = x
            y = y - 1
        elif x >= 1 and y >= 1 and d[x][y] == d[x - 1][y - 1] + 1:
            list.append("s")
            x = x - 1
            y = y - 1
        else:
            list.append("d")
            x = x - 1
            y = y
    return list[::-1]


def alignedPrint(list, r, h, result):
    '''
    This funcition is to print the result of comparing reference and hypothesis sentences in an aligned way.


    Attributes:
        list   -> the list of steps.
        r      -> the list of words produced by splitting reference sentence.
        h      -> the list of words produced by splitting hypothesis sentence.
        result -> the rate calculated based on edit distance.
    '''
    # print ("REF:",)
    for i in range(len(list)):
        if list[i] == "i":
            count = 0
            for j in range(i):
                if list[j] == "d":
                    count += 1
            index = i - count
            # print (" "*(len(h[index])),)
        elif list[i] == "s":
            count1 = 0
            for j in range(i):
                if list[j] == "i":
                    count1 += 1
            index1 = i - count1
            count2 = 0
            for j in range(i):
                if list[j] == "d":
                    count2 += 1
            index2 = i - count2
            """if len(r[index1]) < len(h[index2]):
                print (r[index1] + " " * (len(h[index2])-len(r[index1])),)
            else:
                print (r[index1],)"""
        else:
            count = 0
            for j in range(i):
                if list[j] == "i":
                    count += 1
            index = i - count
            # print (r[index],)
    # print ("HYP:",)
    for i in range(len(list)):
        if list[i] == "d":
            count = 0
            for j in range(i):
                if list[j] == "i":
                    count += 1
            index = i - count
            # print (" " * (len(r[index])),)
        elif list[i] == "s":
            count1 = 0
            for j in range(i):
                if list[j] == "i":
                    count1 += 1
            index1 = i - count1
            count2 = 0
            for j in range(i):
                if list[j] == "d":
                    count2 += 1
            index2 = i - count2
            """if len(r[index1]) > len(h[index2]):
                print (h[index2] + " " * (len(r[index1])-len(h[index2])),)
            else:
                print (h[index2],)"""
        else:
            count = 0
            for j in range(i):
                if list[j] == "d":
                    count += 1
            index = i - count
            # print (h[index],)
    # print ("EVA:",)
    for i in range(len(list)):
        if list[i] == "d":
            count = 0
            for j in range(i):
                if list[j] == "i":
                    count += 1
            index = i - count
            # print ("D" + " " * (len(r[index])-1),)
        elif list[i] == "i":
            count = 0
            for j in range(i):
                if list[j] == "d":
                    count += 1
            index = i - count
            # print ("I" + " " * (len(h[index])-1),)
        elif list[i] == "s":
            count1 = 0
            for j in range(i):
                if list[j] == "i":
                    count1 += 1
            index1 = i - count1
            count2 = 0
            for j in range(i):
                if list[j] == "d":
                    count2 += 1
            index2 = i - count2
            """if len(r[index1]) > len(h[index2]):
                print ("S" + " " * (len(r[index1])-1),)
            else:
                print ("S" + " " * (len(h[index2])-1),)"""
        else:
            count = 0
            for j in range(i):
                if list[j] == "i":
                    count += 1
            index = i - count
            # print (" " * (len(r[index])))
    # print ("WER: " + result)
    return result


def wer(r, h):
    """
    This is a function that calculate the word error rate in ASR.
    You can use it like this: wer("what is it".split(), "what is".split())
    """
    # build the matrix
    d = editDistance(r, h)
    # find out the manipulation steps
    list = getStepList(r, h, d)
    # print the result in aligned way
    # result = float(d[len(r)][len(h)]) / len(r) * 100
    result = float(d[len(r)][len(h)]) / len(r)
    # result = str("%.2f" % result) + "%"
    WER = alignedPrint(list, r, h, result)
    return WER


def readfile(filename):
    with open(filename, encoding="utf-8") as f:
        return parse(f.read())


def extract_dictionary(filename):
    result = list()
    for tokenlist in readfile(filename):
        for token in tokenlist:
            if len(token["form"]) > 1:
                result.append(token["form"])

    result = sorted(list(set(result)))
    return tuple(result)


def use_dictionary(filename):
    dictionary = list()
    with open(filename) as f:
        for line in f:
            dictionary.append(line.strip())

    return dictionary

#@functools.lru_cache()
def max_match(sentence, dictionary):
    if len(sentence) == 0:
        return tuple()

    best = 1
    for i in range(1, len(sentence)):
        token = sentence[:i]
        if token in dictionary:
            best = i

    return (sentence[:best],) + max_match(sentence[best:], dictionary)

def tokenlist_to_list(tokenlist):
    return [token["form"] for token in tokenlist]

def main():
    argparser = ArgumentParser()
    argparser.add_argument("--extract-dictionary", type=str, default=None)
    argparser.add_argument("--use-dictionary", type=str, default=None)
    argparser.add_argument("--maxmatch", type=str, default = None)
    args = argparser.parse_args()
    if args.extract_dictionary is not None:
        sys.stdout.write('\n'.join(extract_dictionary(args.extract_dictionary)))

    if args.use_dictionary is not None:
        dictionary = use_dictionary(args.use_dictionary)
        if args.maxmatch is not None:
            golden = list()
            real = list()
            for sentence in readfile(args.maxmatch):
                text = sentence.metadata["text"]
                now_real = max_match(text, dictionary)
                now_golden = tokenlist_to_list(sentence)
                real.append(now_real)
                golden.append(now_golden)
                sys.stdout.write(" ".join(now_real) + "\n")

            wers = list()
            for golden_sentence, real_sentence in zip(golden, real):
                reference = golden_sentence
                hypothesis = real_sentence
                now_wer = wer(reference, hypothesis)
                #sys.stdout.write("WER: {0}\n".format(now_wer))
                wers.append(now_wer)
            print("Mean WER: {:.2%}".format(numpy.mean(wers)))

            #reference = sum(golden[:100], list())
            #hypothesis = sum(real[:100], tuple())
            #wer_100 = wer(reference, hypothesis)

            #sys.stdout.write("Wer of first 100 sentences: {:.2%}\n".format(wer_100))

if __name__ == "__main__":
    main()
