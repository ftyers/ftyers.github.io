# 1

a) Such formalisms are closer to being universal as they represent the properties of a language. They allow you to set the relationship between your data and your output explicitly and to debug it in case you find that your system behaves unexpectedly.

b) You are more likely to find an annotated corpus then a whole formalism for your task; even if you have to annotate a corpus yourself, it does not require as much professional expertise as writing a formalism does; the output of the system is based upon mathematical reasoning rather then linguistical intuition. 

I feel that there are no universal solutions in NLP, so if I have like a grammar or overall if I'm in the mood for writing grammars I could stick to the first one. But overall training and HMM seems much more reasonable.

#2

We could, say, use a constraint grammar to excluse wildly incorrect tagging options and then fall back to the HMM to reason which of the equally reasonable tagging possibilities seems more plausible.

# 3

My favorite example is the following phrase:

```
Time flies like an arrow.
```

Beside from the obvious interpretation, it can also be interpreted as a statement about insects called "time flies" who feel sympathy towards an arrow. The disambiguation comes down to figuring out whether "flies" is a noun or a verb.
A disambiguator would probably take the probability of the verb "fly" to apper after the noun "time", and then compare it with the same probability for the noun "fly". 
I, however, cut off the alternate interpretation because of my feeling of pragmatics as I cannot imagine an act of communitation where this would be uttered in the sence of insects.

# 4

The evaluation of POS tagging treats it as a multi-class classification problem.In a binary classification, there are two possible outcomes both for expected and real responce, which leaves us with 2x2=4 options: True Positives, True Negatives, False Positives and False Negatives.
In a multi-class classification with n classes, we treat the problem as n binary classifications (e. g. classification NOUN / ADJ / VERB = binary classification of nouns vs. everything else + binary classification of adjs vs. everything else + binary classification of verbs vs. everything else).
We can then compute precision, recall and f1, either by calculating them for each class and taking the mean of it (which leads to ignoring the size of classes) or by putting all the TP, FN and FP together for all classes.
Since Precision is just a normalized version of FN (that is also backwards, larger = better) and the same applies to Recall and FP, I can just discuss Precision and Recall without mentioning FN and FP.
Higher precision means that we are less prone to mistaking a word of another class for the target class (e. g. misclassifying NOUN as VERB if we are looking for verbs), while higher recall means that we are less prone to missing a word of the target class (e. g. misclassifying NOUN as VERB if we are looking for nouns).
I think it doesn't make much sense to take the sum of all TP, FP and FN because mistaking NOUN for VERB is a FP for one class and FN for another. However if we take the mean it starts making sence. Higher precision means we don't take labels of rare classes where we shouldn't, while higher recall means we dare use rare labels even when in doubt.
