import nltk.data
tokenizer = nltk.data.load("tokenizers/punkt/italian.pickle")
with open("wikifiltered.txt", "r", encoding="utf-8") as f:
    l = f.read()
    token_list = tokenizer.tokenize(l)
    print(len(token_list))
with open("wikisegmented_nltk.txt", "w+", encoding="utf-8") as s:
    for x in token_list:	
        s.write(x + "\n")

