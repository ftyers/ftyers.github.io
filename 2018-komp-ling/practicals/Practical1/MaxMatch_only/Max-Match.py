import sys

parsed_sent=[]
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

def main():
    with open(sys.argv[1]) as f:
        used_dict = [l.strip('\n') for l in f]

    global parsed_sent
    res = []

    for sent in sys.stdin:
        maxmatch(sent, used_dict)
        res.append(parsed_sent)
        print(' '.join(parsed_sent))
        parsed_sent=[]


main()