gold = []
test = []
with open('goldstandard.tsv', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if '#' in line or line == '\n':
            continue
        word, tag = line.split('\t')[1].lower(), line.split('\t')[3]
        gold.append((word,tag))


with open('output.tsv', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if '#' in line or line == '\n':
            continue
        print(line.split('\t'))
        word, tag = line.split('\t')[1].lower(), line.split('\t')[2]
        test.append((word,tag))

total = 0
correct = 0
for g,t in zip(gold, test):
    if g == t:
        correct += 1
    total += 1
print(correct/total)
