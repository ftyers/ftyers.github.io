import sys

with  open(sys.argv[1]) as f:
    ja_dict = sorted([l.strip() for l in f], key=len, reverse=True)  
    # key tells how to sort the list. Here we sort by length 
    # (longest to shortest)

def tokenize(sent):
    if len(sent) == 0:
        return []
    try:
        word = next(w for w in ja_dict if sent.startswith(w))
        # find the fist entry
        # as the dict is sorted, the next entry will be the longest matching one
    except StopIteration:
        word = sent[0]
    return [word] + tokenize(sent[len(word):])


for sentence in sys.stdin:
    for token in tokenize(sentence):
        print(token)




