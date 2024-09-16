
##### 1. In the reading, it is claimed that to implement a morphological disambiguator for an unseen language, it takes roughly the same amount of time whether annotating a corpus to train on versus writing constraint grammar rules.

a) Give an argument for why constraint grammar rules are more valuable
- their can take into account a lot of small exceptions, which algorithms might undervalue 


b) Give an argument for why corpus annotation and HMM training is more valuable
- Corpus annotating requires a lot of effort, but can be done by less qualified people like students. Writing rules requires a professional and time of its accomplishment is hard to evaluate, as writing rules is a creative job and requires research. Also human brain capacity is quite limited and it’s hard to take into account all possible cases. Rules require hierarchy, which is also hard to figure out. 


##### 2. Can the two systems be used together? Explain.

I guess they could. If we know the patterns if HMM mistakes, we could correct them with rule-based approach. 

##### 3. Give a sentence with morphosyntactic ambiguity. What would you expect a disambiguator to do in this situation? What can you do?

> I made her duck

I guess if the disambiguator is good, it's quite possible that it will recognize 'duck' as a verb, however if it's a unigram model, it will see 'duck' as a NOUN.
What can I do? Use a good disambiguator. I don't know if in the sense 'I made a duck toy and gave it to her' requires an article before the word 'duck'. If the article isn't obligatory, then it's impossible to disambiguate the sentence. 

##### 4. Choose several (>2) quantities that evaluate the quality of a morphological disambiguator, and describe how to compute them. Describe what it would mean to have disambiguators which differ in quality based on which quantity is used.
##### Suggested quantities: false positive, false negative, precision, recall.

false positive, false negative and recall are good for binary classification. In out task we have more than 2 classes, so we might measure:

precision (it is a weak evaluation, but we can still use it. It’s a number of correct answers decided by all results - both right and wrong)
macroaveraging - we compute the performance for each class, and then average over classes
microaveraging - we collect the decisions for all classes into a single contingency table, and then compute precision and recall from that table 


##### 5. Give an example where an n-gram HMM performs better than a unigram HMM tagger.

```
A bear likes honey 

DET NOUN VERB NOUN (Bigram)

DET VERB NOUN ADJ (Unigram)
```

Here’s an example of how trigram model is better than a bigram model:

```
The still smoking remains of the campfire 

Intended: 
> DT RB VBG NNS IN DT NN 

Bigram: 
DT JJ NN VBZ ...

Unigram: 
DT ADV … 
```