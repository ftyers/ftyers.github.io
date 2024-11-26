
# Quiz 3

1.  In the reading, it is claimed that to implement a morphological disambiguator for an unseen language, it takes roughly the same amount of time whether annotating a corpus to train on versus writing constraint grammar rules.
    
    *a) Give an argument for why constraint grammar rules are more valuable*
    
    With them it is possible to include multiple exceptions and small cases which a trained model will not be able to distinguish normally.
    
    *b) Give an argument for why corpus annotation and HMM training is more valuable*
    
    Corpus annotation does not need as much skill because in a lot of cases the annotation is done by students. Also, it allows to have a large corpus (unlike the rule-based tagging) as it's almost impossible to write all of the possible rules for a large amount of textual information.
    
    *Which would you prefer?*
	
I would prefer working with the annotated corpus and HMM training as it's more convinient.    
    
2.  Can the two systems be used together? Explain.

Yes, because where the training failed to work the rules would be applicable to resolve various small issues.    

3.  Give a sentence with morphosyntactic ambiguity. What would you expect a disambiguator to do in this situation? What can  _you_  do?

~~~~
Time flies like an arrow.
~~~~

In such a case, the context is absolutely necessary to disambiguate the sentence, since like here can be a noun, a verb and a preposition without any context. In such a case, it might be necessary to look at the context and see if like is used with articles - then it is most likely a noun.
    
4.  Choose several (>2) quantities that evaluate the quality of a morphological disambiguator, and describe how to compute them. Describe what it would mean to have disambiguators which differ in quality based on which quantity is used.
    
    Suggested quantities: false positive, false negative, precision, recall.

False positives are the amount of pos tags that the disambiguator left incorrectly, even though the other tag should've been chosen, false negatives are the pos tags that should've been left as is but have been changed for the other possible tag.
Each of these quanities are essentially important for the disambiguator, but the most important one would be their correlation, which is f-score, as it connects all of the metrics together to better show the results.
    
5.  Give an example where an n-gram HMM performs better than a unigram HMM tagger.

Time flies like an arrow.
~~~~
Unigram
NOUN NOUN VERB ART NOUN
N-gram
NOUN VERB PREP ART NOUN
~~~~
