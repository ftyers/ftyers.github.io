```
def maxmatch(sents, dictionary):
    if not sents:
        return []
    for i in range(len(sents)-1, -1, -1):
        word = sents[:i+1]
        remains = sents[i+1:]
        if word in dictionary:
            return [word] + maxmatch(remains, dictionary)            
        else:
            word = sents[0]
            remains = sents[1:]
            return [word] + maxmatch(remains, dictionary)
```