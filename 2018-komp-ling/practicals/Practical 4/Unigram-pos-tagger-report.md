# Unigram tagger
I prepared training [data](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%204/model.tsv) from [universal dependencies corpus for Russian](https://github.com/UniversalDependencies/UD_Russian-GSD/blob/master/ru_gsd-ud-train.conllu) using some bash commands delete all comments:

>sed '/^#/d' ru_gsd-ud-train.conllu > corpus.txt

and to delete all blank lines

>sed '/^\s*$/d' corpus.txt > tagger_base.txt

Then I wrote [python code](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%204/tagger.py) to count the most frequent tag per word and most frequent tag in general and then to predict the pos-tag for each word. It runs with:

> $ python3 tagger.py [text to be tagged] [output file]



