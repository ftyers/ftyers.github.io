import sys

text = open(sys.argv[1], 'r').readlines()

d = {}
tag_count = {}
tokens = 0

for i in text:
    k = i.split('\t')
    if len (k) > 1:
        tokens += 1
        k1 = k[1].lower()
        k3 = k[3]
        if k3 not in tag_count:
            tag_count[k3] = 1
        else:
            tag_count[k3] += 1
        if k1 not in d:
            d[k1] = {}
        if k3 not in d[k1]:
            d[k1][k3] = 1
        else:
            d[k1][k3] += 1

output_file = sys.argv[2]
print (output_file)
stat = open(output_file, 'w')
stat.write('# P\tcount\ttag\tform\n')
stat = open(output_file, 'w')
for i in tag_count:
    s ='{}\t{}\t{}\t{}\n'.format(round(tag_count[i]/tokens, 3), tag_count[i], i, '-')
    stat.write(s)
for i in d:
    all_usage = 0
    for v in d[i]:
        all_usage += d[i][v]
    max_key = max(d[i], key=lambda k: d[i][k])
    max_value = d[i][max_key]
    s ='{}\t{}\t{}\t{}\n'.format(round(max_value/all_usage, 2), all_usage, max_key, i)
    stat.write(s)

stat.close()