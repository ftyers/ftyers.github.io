import sys

# read in an input file
input_file = [line.strip().split('\t') for line in sys.stdin.readlines()]

# create a wordform-tag dictionary
my_cool_freq_dict = {}

for line in open(sys.argv[1], encoding='utf-8').readlines():
    if line.startswith('#'):
        continue
    p, stat, tag, word = line.strip().split('\t')
    if word not in my_cool_freq_dict.keys():
        my_cool_freq_dict[word] = [(float(p), tag)]
    else:
        my_cool_freq_dict[word].append((float(p), tag))

# getting pos of maximum frequency
for token in input_file:
    for cool_key in my_cool_freq_dict.keys():
        cool_value = my_cool_freq_dict[cool_key]
        max_freq = max([i[0] for i in cool_value])
        cool_tag = ''.join([i[1] for i in cool_value if i[0] == max_freq])
        if cool_key == token[1].lower():
            token[3] = cool_tag
            token == '\t'.join(token)
# output
    print('\t'.join(token))
