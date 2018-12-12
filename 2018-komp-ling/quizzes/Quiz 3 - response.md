# Quiz 3

1. In the reading, it is claimed that to implement a morphological disambiguator for an unseen language, it takes roughly the same amount of time whether annotating a corpus to train on versus writing constraint grammar rules.

a) Give an argument for why constraint grammar rules are more valuable.
It is based on large data-base of hand-written disambiguation rules - it's full (mostly) description of the language in terms of constraints. It's easy to debug and these rules probably can be re-used for other closely-related languages. The rules tend to be universal, so they can be also used for some topological research. It is the best way for the languages without large annotated corpus.

b) Give an argument for why corpus annotation and HMM training is more valuable.
It is the best way for the languages with rich annotated corpus - if there is one, HMM training takes much less time than writing rules. Besides, writing rules is a job for qualified linguists, and annotating a corpus can be done via crowdsoursing. 

Which would you prefer?
For the language with large annotated corpora available I'd prefer using HMM, for some low-resourse language - writing rules.

2. Can the two systems be used together? Explain.
Yes, the two systems are used together in transformation-based tagging (aka Brill tagging). It is approach to machine learning: it's based on the rules which are autimatically induced from the data (pre-tagged training corpus).
Firsly, the most basic rule (for the most cases) is implemented to tag the sentence. Then more specific and rare rules are chosen and they transform the incorrect tags. This transformations can be infinite, so there are special templates to follow (which list all the steps possible).

3. Give a sentence with morphosyntactic ambiguity. What would you expect a disambiguator to do in this situation? What can you do?
The are two widely-known examples from Russian:
- Он увидел их __семью__ (NOUN or CARDINAL NUMBER) своими глазами. (He saw their _family (NOUN)_ with his eyes. vs. He saw them with his _seven (CARDINAL)_ eyes.)
- Эти типы __стали__ (NOUN or VERB) есть в цехе. (These types of _steel (NOUN)_ are in the factory shop. vs. These fellows _started (VERB)_ to eat in the factory shop.)

I believe a HMM disambiguator would count the probabilities of both variants for these sentences and would choose the one with the highest probability (though I have doubts regarding the second example, I assume that the VERB case is more common). The rules would have the same problem with the second example, if there is no very rare rule with the word "типы" ("types") - the correct chain for this word is NOUN NOUN.

4. Choose several (>2) quantities that evaluate the quality of a morphological disambiguator, and describe how to compute them. Describe what it would mean to have disambiguators which differ in quality based on which quantity is used.

Suggested quantities: false positive, false negative, precision, recall.

- False positive: when you get a positive result for a test, when in fact you should have got a negative result. 
- False negative: when you get a negative test result, but you should have got a positive test result.
- Precision: the percentage of the items that the system detected (i.e., the system labeled as positive) that are in fact positive (i.e., are positive according to the human gold labels). We should devide the correct results that our system gave us by the correct results of golden standart (some of these results are not detected by our system, so they're false positives).
```
precision = true positives / (true positives + false positives)
```
- Recall: the percentage of items actually present in the input that were correctly identified by the system.
```
recall = true positives / (true positives + false negatives)
```
The difference between precision and recall is the following: precision tells how many of the selected objects were correct, and recall tells how many of the objects that should have been selected were actually selected.
However, if we use only one of them, the real quality of the algorithm can be estimated incorrectly. For example, if I select almost everything with my algorithm, I'll get very high recall, but precision will be very low. If I select almost nothing, precision will be very high, and recall will be low. These both are balanced in F-score, which is the harmonic mean of precision and recall, so that if either precision or recall is too low, F-1 score is too low. The goal of maximizing the F-1 score ensures that we get a reasonably high precision and recall.

5. Give an example where an n-gram HMM performs better than a unigram HMM tagger.
Unigram tagger is quive primitive, it assigns the  tag  that  is  most  likely  for  that  word.  For example, it will assign the tag JJ to any occurrence of the word "frequent", since "frequent" is usually used as an adjective (e.g. a frequent word). The following example would be tagged incorrectly: I frequent this cafe. This won't happen if we use at least bigram tagger - the probability of the chain NOUN ADJ will be lower than NOUN VERB, and the sentence will be tagged correctly.
