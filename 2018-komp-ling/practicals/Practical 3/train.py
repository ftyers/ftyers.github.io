import sys

input = []
tokens = {}
tags = {}
number_of_tokens = 0
token_tags = []

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        res = line.split('\t')
        input.append([res[1], res[3]])

number_of_tokens = len(input)

for line in input:
    [token, tag] = line

    if token in tokens:
        if tag in tokens[token]:
            tokens[token][tag] += 1
        else:
            tokens[token][tag] = 1
    else:
        tokens[token] = { tag: 1 }

    if tag in tags:
        tags[tag] += 1
    else:
        tags[tag] = 1

res = [['# P', 'count', 'tag', 'form']]

for tag in tags:
    tag_number = tags[tag]
    res.append([str(tag_number / number_of_tokens), str(tag_number), tag, '_'])

for token in tokens:
    token_info = tokens[token]
    token_number = sum(token_info.values())

    for tag in token_info:
        token_tag_number = token_info[tag]
        res.append([str(token_tag_number / token_number), str(token_tag_number), tag, token])

with open(sys.argv[2], 'w+', encoding='utf-8') as new_text:
    text = '\n'.join(['\t'.join(line) for line in res])
    new_text.write(text)
    new_text.close()gi