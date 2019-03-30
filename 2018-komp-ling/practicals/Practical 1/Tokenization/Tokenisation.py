from maxmatch import  maxmatch

# create a dictionary for maxmatch algo


def create_dict(filename):
    f = open(filename, 'r', encoding='UTF-8')
    text = f.read()
    dictionary = text.split('\n')
    return dictionary


def sentences_to_tokenize(filename):
    f = open(filename, 'r', encoding='UTF-8')
    text = f.read()
    sentences = text.split('\n')
    return sentences


def main():
    dict = create_dict('dict.txt')
    sentences = [sentence.strip() for sentence in sentences_to_tokenize('japanese_texts.txt')]

    # all tokens are separated with commas
    tokenized_sentences = [', '.join(filter(lambda token: token != ',', maxmatch(sentence, dict))) for sentence in sentences]

    results = open('tokenization_result.txt', 'w', encoding='UTF-8')
    results.write('\n'.join(tokenized_sentences))
    results.close()

    return tokenized_sentences


if __name__ == '__main__':
    main()


