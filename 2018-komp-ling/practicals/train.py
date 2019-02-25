import sys

def conllu_open(file=sys.argv[1]):
    lines = []
    with open(file) as f:
        for line in f.readlines():
            if line[0].isdigit():
                line = line.split('\t'); lines.append(line)
    return lines


def data_count_table(lines=conllu_open()):
    uni_tags = ['ADJ', 'ADP', 'ADV', 'AUX', 'CCONJ', 'DET', 'INTJ', 'NOUN', 'NUM', 'PART', 'PRON',\
            'PROPN', 'PUNCT', 'SCONJ', 'SYM', 'VERB', 'X']
    result = {}
    for i in lines:
            if i[2] not in result:
                result[i[2]] = {}
                for tag in uni_tags:
                    result[i[2]][tag] = 0
                for tag in result[i[2]]:
                    if i[3] == tag:
                        result[i[2]][tag] += 1
            else:
                for tag in result[i[2]]:
                    if i[3] == tag:
                        result[i[2]][tag] += 1
    return result


def data_freq_table(data=data_count_table()):
    for key, value in data.items():
        count = 0
        for tags in value:
            count += value[tags]
        try:
            for tags in value:
                value[tags] /= count
        except ZeroDivisionError:
            continue
    return data


def count_tag(data=data_count_table()):
    tags = {}
    for values in data.values():
        for tag in values:
            if tag not in tags:
                tags[tag] = values[tag]
            else:
                tags[tag] += values[tag]
    return tags


def freq_tag(tags=count_tag()):
    for keys in tags:
        tags[keys] /= len(conllu_open())
        tags[keys] = round(tags[keys], 4)
    return tags


def nice_lists(freq=freq_tag(), count=count_tag(), data_count=data_count_table(), data_p=data_freq_table()):
    result = []
    for key, value in freq.items():
        list = []
        list.append(value)
        if key in count:
            list.append(count[key])
        list.append(key)
        list.append("__")
        result.append(list)

    for key, value in data_p.items():
        for v in value:
            list = []
            if value[v] > 0:
                list.append(value[v])
                list.append(data_count[key][v])
                list.append(v)
                list.append(key)
                result.append(list)
    for i in result:
        i[0] = round(i[0], 3)
    return result


print('# P', ' '*6, 'count', ' '*4, 'tag', ' '*6, 'form', ' '*5)
for i in nice_lists():
    for s in i:
        x = str(s)
        print(s, ' '*(10-len(x)), end='')
    print('\n')
