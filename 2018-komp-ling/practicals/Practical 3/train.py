import sys


def unigram_model(file):
    res = []
    counter = 0
    words = []
    tags = []
    for line in file.readlines():
        if '\t' in line:
            line = line.split('\t')
            words.append((line[1], line[3]))
            tags.append(line[3])
            counter += 1

    t = {}    # handling tags
    for tag in tags:
        if tag not in t:
            t[tag] = 1
        else:
            t[tag] += 1

    for tag, freq in t.items():
        prob_t = round(freq / counter, 2)
        res.append((str(prob_t), str(freq), tag, '_'))

    m = {}    # handling words
    for pair in words:
        if pair[0] not in m:
            m[pair[0]] = {}
            for tag in tags:
                m[pair[0]][tag] = 0
        m[pair[0]][pair[1]] += 1

    for word, tags in m.items():
        total = sum(tags.values())
        for tag, freq in tags.items():
            if freq:
                prob_w = round(freq / total, 2)
                res.append((str(prob_w), str(freq), tag, word))

    return res


def main():
    with open(sys.argv[1], 'r', encoding='utf-8') as f:
        print('#P' + '\t' + 'count' + '\t' + 'tag' + '\t' + 'form')
        for item in unigram_model(f):
            print('\t'.join(item))


if __name__ == '__main__':
    main()