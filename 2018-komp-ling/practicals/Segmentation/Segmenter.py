from nltk.tokenize import sent_tokenize
# sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')


with open('fifty.txt') as f:
    text = f.read()


sent_tokenize_list = sent_tokenize(text, language='english')

print (len(sent_tokenize_list))

with open('my_sentences.txt') as f:
    my_text = f.read().split('\n')

print (len(my_text))




n = 1
for i in range(len(my_text)):
    if my_text[i][:3] != sent_tokenize_list[i][:3]:
        print (n, my_text[i], '\n -', sent_tokenize_list[i], '\n')
    n += 1