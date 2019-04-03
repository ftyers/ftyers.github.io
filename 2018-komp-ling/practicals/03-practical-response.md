# Unigram model (engineering)

Files are presnted in subdirectory `unigram`.  
File `unigram.py` which takes two command line arguments – source and destination. Source file must be in [CoNLL-U format](http://universaldependencies.org/format.html) (Universal Dependencies), output is tab-separated.  
File `model.txt` is a result of running the script against [Taiga train set](https://raw.githubusercontent.com/UniversalDependencies/UD_Russian-Taiga/master/ru_taiga-ud-train.conllu).


##### What might be a simple improvement to the language model for languages with orthographic case?

In the example of the tutorial, Russian words which differ in letter case are presented as different forms. It would be worthwhile to merge them into one form (technically it is simpler to use lowercase one). Proper noun should receive their specific annotation.