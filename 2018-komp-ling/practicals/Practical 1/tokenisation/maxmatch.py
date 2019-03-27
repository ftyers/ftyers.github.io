tokens = []
def tokenize(sentence, dictionary):
    """
    maxmatch algorithm
    :param sentence: string
    :param dictionary: list
    :return: list of tokens
    """
    global tokens
    for counter in range(len(sentence), -1, -1):
        first_word = sentence[:counter]
        remainder = sentence[counter:]
        if first_word in dictionary:
            tokens.append(first_word)
            return tokenize(remainder, dictionary)
        if counter == 1:
            first_word = sentence[0]
            remainder = sentence[1:]
            tokens.append(first_word)
            tokens.append(remainder)
    return tokens


def main():
    print('Insert path to dictionary')
    n_dict = str(input())
    f = open(n_dict)
    dictionary = []
    for line in f.readlines():
        if '\n' in line:
            line = line.strip('\n')
        dictionary.append(line)

    print('Insert sentence: ')
    sentence = str(input())

    print(tokenize(sentence, dictionary))

if __name__ == '__main__':
    main()
