
# coding: utf-8

# In[ ]:


import sys

text = open(sys.argv[1], 'r')

word_tag = {}
freq_tag = {}
tokens = 0

for l in text:
    if l.startswith('#') or l.startswith('\n'):
        continue
    
    word = l.split('\t')[1].lower()
    tag = l.split('\t')[3]
    
    if word not in word_tag:
        word_tag[word] = {}
    if tag not in word_tag[word]:
        word_tag[word][tag] = 1
    else: 
        word_tag[word][tag] += 1
        
    if tag not in freq_tag:
        freq_tag[tag] = 1
    else:
        freq_tag[tag] += 1
        
for word in word_tag:
    w_total = sum(word_tag[word].values())
    tokens += w_total
        
with open(sys.argv[2], 'a') as result:
    result.write('# P\tcount\ttag\tform\n')
    for tag in freq_tag:
        result.write('{}\t{}\t{}\t-\n'.format(round(freq_tag[tag]/tokens, 2), freq_tag[tag], tag))
    for word in word_tag:
        for tag in word_tag[word]:
            result.write('{}\t{}\t{}\t{}\n'.format(round(word_tag[word][tag]/sum(word_tag[word].values()), 2), word_tag[word][tag], tag, word))

