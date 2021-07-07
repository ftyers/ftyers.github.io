# Quiz 3

##### 1. In the reading, it is claimed that to implement a morphological disambiguator for an unseen language, it takes roughly the same amount of time whether annotating a corpus to train on versus writing constraint grammar rules.

###### a) Give an argument for why constraint grammar rules are more valuable

It can be built without corpus/dataset, just from scratch, starting as a couple of rules.	

###### b) Give an argument for why corpus annotation and HMM training is more valuable

Dataset could be annotated by people who have language background in terms of school program and don't aware on computer techniques. If we got corpus like this we can easily make a tagger. So it depends, whether it is possible for us to collect annotated corpus of proper size, which could be a challenge.

###### Which would you prefer?

Perhaps, HMM, but with some preprocessing/postprocessing on CG.

##### 2. Can the two systems be used together? Explain.

They could be used if «the taggers have complementary errors».

##### 3. Give a sentence with morphosyntactic ambiguity. What would you expect a disambiguator to do in this situation? What can _you_ do?

>Женщина пригласила к себе в гости мужчину. Наготовила ему, накрыла на стол. Он пришел, поел, выпил. Она к нему подсаживается и говорит:
>— А теперь, ты мой...  
>— Ну уж нет, мой сама!


I guess, disambiguator would rather deal with things like this.
In rules we rather have a rule "pronoun + imperative", than "pronoun + possessive pronoun", and imperative on the beginning of the clause for second line. HMM on n-grams would deal like this if it would be trained on non-specific corpus. However, every tagger would fail if we have homonyms in the same conditions, e.g. if we rewrite this dialog to:

>— Tы мой!  
>— Ты мой сама!

I am not sure that pronoun-particle _sam(a)_ would be put in CG and be presented in random corpus, so this construction would be captured by HMM tagger.

##### 4. Choose several (>2) quantities that evaluate the quality of a morphological disambiguator, and describe how to compute them. Describe what it would mean to have disambiguators which differ in quality based on which quantity is used.

##### Suggested quantities: false positive, false negative, precision, recall.

**True positive** is an item correctly labeled as belonging to some  class.  
**False positive** is an item non-correctly labeled as belonging to some  class.
**True negative** is an item labeled correctly as non-belonging to some class.
**False negative** is an item labeled non-correctly as non-belonging to some class.
**Precision** is a quantity  of true positives. True positives to all positives.  
**Recall** is a quantity of true positives (classified by our system) divided by the total amount of items of this class from our dataset. True positives to true positives and false negatives.

E.g., if we have corpus with 100 verbs to 1000 tokens, 60 of them were annotated as verbs (TP), 20 tokens were tagged as verbs, being non-verbs (FP). So it means 40 of them are FN.
Thus, precision 60/60+20 = 0.75 and recall is 60/60+40 = 0.6.


##### 5. Give an example where an n-gram HMM performs better than a unigram HMM tagger.

>_My love is as a fever_ (Shakespeare).   

Probability of noun after adjective is higher that for a verb, however, according to stats, _love_ as verb is rather more frequent than one as a noun, so unigram tagger would classify it as a a verb. But an n-gram tagger pays attention to sequences of tags.
