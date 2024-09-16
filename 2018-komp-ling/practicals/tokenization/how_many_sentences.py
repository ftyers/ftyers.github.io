with open('ja_gsd-ud-train.conllu') as f:
    train = f.read().split()
count = 0
'''for i in train:
    if 'sent_id' in i:
        count += 1
        print (i)
        if i == 900:
            break
print (count)'''

with open('MaxMatchSentences_TEST.txt') as f:
    mm_s = f.read().split('\n')

for i in range(10):
    print (mm_s[i])