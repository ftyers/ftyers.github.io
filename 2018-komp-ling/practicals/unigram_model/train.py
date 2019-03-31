import sys


def unigram_model(file):
    words, tags, pairs = [], [], []
    counter = 0
    for line in file.readlines():
        if '\t' not in line:
            continue
        line = line.split('\t')
        words.append((line[1], line[3]))
        tags.append(line[3])
        counter += 1

    tag_dict = {}
    for tag in tags:
        if tag not in tag_dict:
            tag_dict[tag] = 1
        else:
            tag_dict[tag] += 1

    for tag, freq in tag_dict.items():
        prob_tag = round(freq / counter, 2)
        pairs.append((str(prob_tag), str(freq), tag, '_'))

    words_dict = {}
    for elem in words:
        if elem[0] not in words_dict:
            words_dict[elem[0]] = {}
            for tag in tags:
                words_dict[elem[0]][tag] = 0
        words_dict[elem[0]][elem[1]] += 1

    for word, tags in words_dict.items():
        total = sum(tags.values())
        for tag, freq in tags.items():
            if freq:
                prob_word = round(freq / total, 2)
                pairs.append((str(prob_word), str(freq), tag, word))

    return pairs


def main():
    with open(sys.argv[1], 'r', encoding='utf8') as infile:
        print('#P' + '\t' + 'count' + '\t' + 'tag' + '\t' + 'form')
        for elem in unigram_model(infile):
            print('\t'.join(elem))


if __name__ == '__main__':
    main()