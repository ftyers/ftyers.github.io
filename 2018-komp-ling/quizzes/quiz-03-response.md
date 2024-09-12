# Quiz 3
#### *Anastasia Nikiforova*


1. *In the reading, it is claimed that to implement a morphological disambiguator for an unseen language, 
it takes roughly the same amount of time whether annotating a corpus to train on versus writing constraint grammar rules.*

**a) Give an argument for why constraint grammar rules are more valuable**

Constraint grammar rules are more valuable, because they show actual morphological and syntactical rules of the language. 
Due to that, it is possible to take into account every little exception a language grammar has.

**b) Give an argument for why corpus annotation and HMM training is more valuable**

In rule-based approach it is very time- and even money-consuming to tag a corpus (sometimes people tagging the corpus need to be paid).
The taggers have to be skilled, as every little mistake can ruin everything.
On the contrary, corpus annotation and HMM training allow us to work with larger corpora without a need for a skilled professional who would write rules for us.

**Which would you prefer?**

Personally, I prefer the latter. Even if, logically thinking, constraint grammar rules are far more precise, 
it would be too difficult to write down every rule of the language. Also, if we mess up with some rules,it would be much more difficult to find and correct the mistake.

2. **Can the two systems be used together? Explain.**

Absolutely. Rules can cover cases that automatic tagging cannot cover. Like, some exceptions from general rules.

3. **Give a sentence with morphosyntactic ambiguity. 
What would you expect a disambiguator to do in this situation? What can you do?**

*Example:* ```He fed her cat food.```

Here, in order to resolve ambiguity, we need to build a syntactic tree of the sentence. 
It could be ```He fed her [cat food].``` or ```He fed [her cat] food.``` 
Then we could see, which collocation is more probable in this context, 
and choose the syntactic tree which is more frequent in some corpus that we use as a reference.

4. **Choose several (>2) quantities that evaluate the quality of a morphological disambiguator, and describe how to compute them. 
Describe what it would mean to have disambiguators which differ in quality based on which quantity is used.**

*Suggested quantities: false positive, false negative, precision, recall.*

**False positive:** a disambiguator classified a sentence as ambiguous even if in fact it isn't.

**False negative:** a disambiguator wrongly classified sentence as non-ambiguous.

**Presision/Positive predictive value**: an amount of correctly disamiguated sentences among all disambiguated sentences.

Precision=TP/(TP+FP)

**Recall/True positive rate**: an amount of correctly disamiguated sentences among all sentences that needed to be disambiguated at first place

Recall= TP/(TP+FN)

5. **Give an example where an n-gram HMM performs better than a unigram HMM tagger.**

I saw a cat.
```
HMM: [PRON NOUN DET NOUN]
n-gram HMM: [PRON VERB DET NOUN]
```
