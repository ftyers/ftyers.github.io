# Tagger comparison

Udpipe trained upon the Finnish corpus performed as follows:

```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
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

```
We have trained a bigram tagger that falls back to simpler taggers in case of emergency.
It has performed with the accuracy of 0.9360702420503085
```

As I understand from reading the evaluation script doc strings, the alignacc is just accuracy in case the words are aligned, so it's comparable with the accuracy from nltk.
So the result of 94.64% and 93.61% are quite compatible.

# Constraint grammar

I managed to reproduce the output successfully, although the part with REMOVE:6 somehow had REMOVE:8 instead:

```
$ echo "Однако стиль работы Семена Еремеевича заключался в том, чтобы принимать всех желающих и лично вникать в дело." |  python3 ud-scripts/conllu-analyser.py ru-analyser.tsv | vislcg3 -t -g rus.cg3 | grep REMOVE

;	"тот" DET Case=Loc Gender=Neut Number=Sing REMOVE:8
;	"тот" DET Case=Loc Gender=Masc Number=Sing REMOVE:8

```

# Improve perceptron tagger

Using UD_Portugese.git didn't work (it doesn't seem to be an actual address), so I used UD_Portugese-BSD.git instead.

The result with the standard features was as follows:

```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     96.35 |     96.35 |     96.35 |     96.35
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     96.35 |     96.35 |     96.35 |     96.35
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
```

I tried adding several features such as prefix of the context +2 word, properties of the string (numeric, register...) and length. Here is the full list of the added features:
```
add('i prefix', word[:3])
add("i-1 pref1", context[i-1][-3:])
add("i-1 prefix", context[i-1][:3])
add("i+1 pref1", context[i+1][-3:])
add("i+1 prefix", context[i +1][:3])
add("i-2 pref1", context[i-2][-3:])
add("i+1 prefix", context[i+2][:3])
add("i+2 suffix", context[i+2][-3:])
add("i+2 pref1", context[i+2][0])
add("i+2 prefix", context[i+2][:3])

add('upper register', str(int(word.isupper())))
add('lower register', str(int(word.islower())))
add('capitalized', str(int(word[0].isupper())))
add('numeric', str(int(word.isnumeric())))
add('alpha', str(int(word.isalpha())))

add("length", str(len(word)))
```

They didn't seem to have any effect on the performance. It seems like pretty much everything useful for disambiguation is already used.
