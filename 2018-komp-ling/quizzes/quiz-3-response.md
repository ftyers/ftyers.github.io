
# Quiz 3

1.  In the reading, it is claimed that to implement a morphological disambiguator for an unseen language, it takes roughly the same amount of time whether annotating a corpus to train on versus writing constraint grammar rules.
    
    *a) Give an argument for why constraint grammar rules are more valuable*
    
    Because they allow for including various exceptions and small cases that a trained model wouldn't be able to distinguish properly.
    
    *b) Give an argument for why corpus annotation and HMM training is more valuable*
    
    Corpus annotation doesn't require as much skill as in a lot of cases students are the ones doing it. Also, it allows for a large corpus unlike the rule-based tagging as it's almost impossible to write rules for a large amount of textual information.
    
    *Which would you prefer?*
I would chose working with the annotated corpus and HMM training as it's more convinient.    
    
2.  Can the two systems be used together? Explain.

Of course, the rules can  be written to work on such cases that the training didn't include.    

3.  Give a sentence with morphosyntactic ambiguity. What would you expect a disambiguator to do in this situation? What can  _you_  do?

~~~~
We saw her duck
~~~~

In such a case, the context is absolutely necessary to disambiguate the sentence, since duck here can be both a noun and a verb without any context. In such a case, it might be necessary to look at the context and see if duck as used with articles - then no doubt it's a noun.
    
4.  Choose several (>2) quantities that evaluate the quality of a morphological disambiguator, and describe how to compute them. Describe what it would mean to have disambiguators which differ in quality based on which quantity is used.
    
    Suggested quantities: false positive, false negative, precision, recall.

False positives are the amount of pos tags that the disambiguator left incorrectly, even though the other tag should've been chosen, false negatives are the pos tags that should've been left as is but have been changed for the other possible tag.
Each of these quanities are essentially important for the disambiguator, but the most important one would be their correlation, which is f-score, as it connects all of the metrics together to better show the results.
    
5.  Give an example where an n-gram HMM performs better than a unigram HMM tagger.

I saw her tiny duck.
~~~~
Unigram
PRON VERB PRON ADJ VERB
N-gram
PRON VERB PRON ADJ NOUN
~~~~
