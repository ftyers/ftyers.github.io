with open('dict.txt', 'r') as f: #make the dictionary
    f = f.read().split()
    dictionary = sorted(f, key = len, reverse=True) #create the dictionary, where the longest words come first

def MaxMatch(sent):
    if len(sent) == 0:
        return []
    try:    #checks if first symbols of the sentence are in the dictionary, and if yes, the same goes for other symbols till the end of the sentence
        token = next(word for word in dictionary if sent.startswith(word)) 
    except StopIteration:   #if the there is no such a word in the dictionary, which starts from the first symbol, 
                            #it detects the symbol as the first word of the sentence and then repeats the operation for other symbols in the sentence
        token = sent[0]
    return [token] + MaxMatch(sent[len(token):])

with open('sentences.txt', 'r') as f: 
    f = f.read().split('\n')
    number_of_tokens = 0
    for sent in f:
        sent = MaxMatch(sent)
        for word in sent:
            print(word, end=' ')
        number_of_tokens += len(sent)  
        print('\n') #the output is strings of tokens separated with spaces, strings separated by blank lines
print(len(f))
print(number_of_tokens) 