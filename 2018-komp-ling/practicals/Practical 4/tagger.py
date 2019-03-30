import sys

tags = []
tokens = []

with open('./tagger_base.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        res = line.split('\t')
        [p, count, tag, form] = res

        if form == '_' and tag != '_':
            tags.append(res)
        else:
            tokens.append(res)



def find_most_frequent_tag(tags):
    sorted_tags = sorted(tags, key=lambda token: token[0], reverse=True)
    return sorted_tags[0][2]

def define_PoS(word):
    matched_tokens = list(filter(lambda token: word == token[3], tokens))

    if (len(matched_tokens) != 0):
        sorted_tokens = sorted(matched_tokens, key=lambda token: token[0], reverse=True)
        return sorted_tokens[0][2]

    return None


def main():
    most_frequent_tag = find_most_frequent_tag(tags)

    words = []

    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip('\n')
            res = line.split('\t')
            words.append(res[1])

    tagged_words = [[str(index), word, define_PoS(word) or most_frequent_tag] for index, word in enumerate(words, start=1)]

    with open(sys.argv[2], 'w+', encoding='utf-8') as new_text:
        text = '\n'.join(['\t'.join(line) for line in tagged_words])
        new_text.write(text)
        new_text.close()

    return tagged_words

if __name__ == '__main__':
    main()