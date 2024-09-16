## Quiz 3

### Vladislav Mikhailov MKL181

1. In the reading, it is claimed that to implement a morphological disambiguator for an unseen language, it takes roughly the same amount of time whether annotating a corpus to train on versus writing constraint grammar rules.

a) Give an argument for why constraint grammar rules are more valuable

The CG approach is a language-independent formalism for surface-oriented, morphology-based parsing of unrestricted text, allowing for facilitating rules interpretability and grammatical adaptability to different language inputs / readings. The constraints discard as many alternatives as possible and cover more advanced levels of analysis, providing high robustness, accuracy and satisfactory tagging performance. 

b) Give an argument for why corpus annotation and HMM training is more valuable

HMM considers the best combination of tags for word order, while other tagging methods greedily tag one word at a time, regardless of the optimal combination. Comparing to the CG approach, the output of the model is based on the frequency and probability that word occurs with a particular tag in the training set.


Which would you prefer?

I think that the choice depends on the particular task we deal with and the linguistic resources available:
* if we have an open-free CG rules resources, we can use and expand / change them with our own CG so that to meet our needs.
* if we have a large tagged corpus, we can use it for training our model. We can also expand the corpus by tagging unseen texts with a robust morphological analyser so that to achieve the better results.

2. Can the two systems be used together? Explain.

The CG system can be specifically designed to complement the HMM system so that to achieve the better tagging accuracy. There seem to be the following options of combining the systems, so that to resolve remaining ambiguity cases: 

* HMM and CG systems can be used in parallel
* HMM system with CG post-usage

The combination of the systems can be really proficient for low-resourced languages. Thus, we do not need to annotate the texts, since we can use the approach on a small quantity of texts as of high-quality annotation.


3. Give a sentence with morphosyntactic ambiguity. What would you expect a disambiguator to do in this situation? What can you do?

The word *book* is ambiguous:
* (a) a verb
    * to *book* a flight
* (b) a noun
    * lend me the *book* by Pushkin

Here are the lexical likelihoods:
```
* P(book|VB)
* P(book|NN)
```

To calculate the tag sequence probabilities for our HMM disambiguator:
```
* P(VB|A)P(DET|VB)P(book|VB)
* P(NN|BY)P(PRP|NN)P(book|NN)
```

CG rules:
```
* remove NN if (-1 TO(inf))
* remove VB if (-1 DET)
```

4. Choose several (>2) quantities that evaluate the quality of a morphological disambiguator, and describe how to compute them. Describe what it would mean to have disambiguators which differ in quality based on which quantity is used.

We can summarize our tag prediction model using a 2x2 matrix depicting all four possible outcomes:
```
________________________________________________
|  True Positive (TP)   |  False Positive (FP) |
|-----------------------+----------------------|
| False negative (FN)   |  True Negative (TN)  |
------------------------------------------------
```

* Precision = TP/(TP+FP), measures the percentage of TAG word types tagged as TAG that were correctly tagged
* Recall = TP/(TP+FN), measures the percentage of actual TAG word types that were correctly tagged

Improving precision typically reduces recall and vice versa:
* false positives decrease, but false negatives increase => precision increases, while recall decreases
* false positives increase, and false negatives decrease => precision decreases, recall increases

5. Give an example where an n-gram HMM performs better than a unigram HMM tagger.

N-gram HMM performs better on tagging *casa* as a NOUN when followed by ADJ and preceeded by DET:
```
Vino     a       una      casa     grande      .
VERB    ADP      DET      NOUN       ADJ     PUNCT
```
