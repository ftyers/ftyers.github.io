#!/usr/bin/python
import io
from textblob import TextBlob
from nltk.tokenize import sent_tokenize

def write2file(filename, the_list):
    with io.open(filename+".txt", 'w', encoding='utf-8') as f:
        for line in the_list:
            # print(line)
            f.write(str(line)+"\n\n")
        f.close()
    return

with io.open("sample.txt",'r', encoding='utf-8') as fo:
    text = fo.read()

    sent_tokenize_list = sent_tokenize(text)
    he = len(sent_tokenize_list)
    write2file("nltk", sent_tokenize_list)
    print(he)

    blob = TextBlob(text)
    he2 = len(blob.sentences)
    write2file("textblob", blob.sentences)
    print(he2)

    import spacy
    nlp = spacy.load('en')
    doc = nlp(text)
    splen = len(list(doc.sents))
    write2file("spacy", list(doc.sents))
    print(splen)
