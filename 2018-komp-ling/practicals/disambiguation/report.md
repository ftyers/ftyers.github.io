# Tagger comparison

Udpipe trained upon the Finnish corpus performed as follows:

```Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     94.64 |     94.64 |     94.64 |     94.64
XPOS       |     95.81 |     95.81 |     95.81 |     95.81
Feats      |     90.77 |     90.77 |     90.77 |     90.77
AllTags    |     89.75 |     89.75 |     89.75 |     89.75
Lemmas     |     84.52 |     84.52 |     84.52 |     84.52
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
```

I wrote a small program that fits an nltk tagger (a binary tagger that falls back to a unigram tagger that falls back to marking everything with the most popular tag). The program is named train_nltk_tagger.py and is located in the disambiguation folder. It has performed as follows:

```We have trained a bigram tagger that falls back to simpler taggers in case of emerbency.
It has performed with the accuracy of 0.9360702420503085
```

As I understand from reading the evaluation script doc strings, the alignacc is just accuracy in case the words are aligned, so it's comparable with the accuracy from nltk.
So the result of 94.64% and 93.61% are quite compatible.


