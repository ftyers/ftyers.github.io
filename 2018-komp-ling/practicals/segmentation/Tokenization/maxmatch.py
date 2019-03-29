
# coding: utf-8

# In[1]:


import sys
with open(sys.argv[1]) as f:
    m = f.read()
    dictionary = m.split()

sentences = []
with open(sys.argv[2]) as d:
    sentences = d.readlines()

punct = ["「", "」", "。", "、", "!", "?", "“", "\n"] 

for i in range(len(sentences)):
    for elem in punct:
        sentences[i] = sentences[i].replace(elem, "")

for sentence in sentences:
    sentence = sentence.strip()

print(sentences)

#tokens = []

def tokenize(text, dictionary, tokens):
    for i in range(len(text), -1, -1):
        word = text[:i]
        if word in dictionary:
            tokens.append(word)
            text = text[len(word):]
            tokenize(text, dictionary, tokens)
            return tokens
    return tokens

with open("max.txt", "w", encoding = "utf-8") as final:
    for sentence in sentences:
        tokens = []
        tokenize(sentence, dictionary, tokens)
        final.write("\n".join(tokens))
        final.write("\n")
        
final.close()
    

