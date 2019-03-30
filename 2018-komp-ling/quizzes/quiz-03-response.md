# Quiz 3

## Question 1

In the reading, it is claimed that to implement a morphological disambiguator for an unseen language, it takes roughly the same amount of time whether annotating a corpus to train on versus writing constraint grammar rules.

a) Give an argument for why constraint grammar rules are more valuable

b) Give an argument for why corpus annotation and HMM training is more valuable

Which would you prefer?

Answer:

a) There is no need in annotated corpora for writing rules.

b) Annotating a corpora does not require a strong linguistic background, so crowdsourcing can be done.

Personally I'd prefer rules because they are easier for debugging.

## Question 2

Can the two systems be used together? Explain.

Answer:

Yes, both system can be combined in a one model: HMM takes into account a window of defined width, while rules can work with bigger contexts and improve the disambiguation.

## Question 3

Give a sentence with morphosyntactic ambiguity. What would you expect a disambiguator to do in this situation? What can you do?

Answer:

There is a classic example: *Time flies like an arrow*.

I would expect a disambiguator to give me analyses which would be the combinations of the following tags:

- *time* as NOUN, as VERB and as ADJ
- *flies* as NOUN and as VERB
- *like* as NOUN, as VERB and as CONJ
- *an* as DET
- *arrow* as NOUN and as CONJ

The most probable analysis is expected to be this one: *Tine-NOUN flies-VERB like-CONJ an-DET arrow-NOUN*.

I'd write some rules, for example:

- VERB should not be preceeded by VERB in the beginning of the sentence 
- DET cannot be followed by CONJ
- etc.

## Question 4

Choose several (>2) quantities that evaluate the quality of a morphological disambiguator, and describe how to compute them. Describe what it would mean to have disambiguators which differ in quality based on which quantity is used.

Suggested quantities: false positive, false negative, precision, recall.

Answer:

The quantities are:
- FP (false positive): predicted positive, but negative in fact
- FN (false negative): predicted negative, but positive in fact
- precision = TP/(TP+FP) - how much of the identified tags are positive in fact (according to the gold standart)
- recall = TP/(TP+FN) - how much of the tags that should be identified were identified by the model in fact

There is an inverse proportion in some way between precision and recall:
- if the model identifies almost everything, it will have high recall and low precision
- if the model identifies almost nothing, it will have high precision and low recall

I suppose that for the disambiguation task precision is more important than recall: first of all, we want to know the number of the positive tags.
Frankly speaking, it seems a bit difficult to understand what is recall itself in the disambiguation task.

## Question 5

Give an example where an n-gram HMM performs better than a unigram HMM tagger.

Answer:

Example from the Question 3 is fine for this: for example, bigrams like (*time-NOUN, flies-VERB*) are more likely to occur than bigrams like (*time-ADJ, flies-VERB*).
