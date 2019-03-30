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
    global parsed_sent
    print('Insert name of dict:')
    n_dict=str(input())
    used_dict = open(n_dict, 'r', encoding='utf-8').read().splitlines()

    print('Sentence to parce:')
    n_test_sent=str(input())
    sentences = open(n_test_sent, 'r', encoding='utf-8').read().splitlines()

    print('Save to:')
    s_file = str(input())


    res = []
    for sent in sentences:
        maxmatch(sent, used_dict)
        res.append(parsed_sent)
        parsed_sent=[]

    save = open(s_file, 'w', encoding='utf-8')
    for i in res:
        save.write(' '.join(i)+'\n')
    save.close()

main()