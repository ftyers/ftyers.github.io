## Tokenization

I have written maxmatch algorithm based on pseudocode in Juraffsky's book.
Programm maxmatch.py takes 3 arguments: file with sentences, dictionary file and output file.
File with sentences has one sentence per line.
Dictionary file has one unique token per line. In program the list of tokens is created.
Output file has one tokenized sentence per line.
This is not optimal algorithm because it looks through all dictionary each time when it searches a token.

For Japanise it shows WER = 1.26% (by [WER in python](https://github.com/zszyellow/WER-in-python)
And [apertium-eval-translator](http://svn.code.sf.net/p/apertium/svn/trunk/apertium-eval-translator/) shows WER = 24.11 %
It looks strange and requires more investigations.

Japanese dictionary contains 22312 tokens, punctuation included.
Japanese train set contains 557 sentences.

Maxmatch didn't correctly find tokens, which are not presented in dictionary (for example 不快感).
So the sentence
これに不快感.......
was tokenized like
これ に 不快 感.....
instead of
これ に 不快感.....
