import nltk
from nltk import *
import nltk.tokenize.punkt 

with open('/Users/anyway/compling/segmentation/wiki_corpus_test.txt', 'r') as f:
    traindata = f.read()
trainer = nltk.tokenize.punkt.PunktTrainer(traindata) 
trainer.INCLUDE_ALL_COLLOCS = True 
trainer.INCLUDE_ABBREV_COLLOCS = True
params = trainer.get_params()
trainer.train(traindata)

sbd = PunktSentenceTokenizer(params)
with open('/Users/anyway/compling/segmentation/wiki1.txt', 'r') as f:
    f = f.read()
    
sents = []
with open('/Users/anyway/compling/segmentation/segmented_wiki3.txt', 'w') as wf:
    for sentence in sbd.sentences_from_text(f, realign_boundaries=True):
        sents.append(sentence)