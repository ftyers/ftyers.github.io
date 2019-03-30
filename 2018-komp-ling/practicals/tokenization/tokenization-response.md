Mikhailov Vladislav
MKL181

**Report on Tokenization**

**Maxmatch implementation**
I started learning programming when entered the university, so I did my best to implement the maxmatch algorithm. Unfortunately, I do not know what I can modify so that to get better results.

Below is my maxmatch implementation (the separate maxmatch.py file is also pushed):

```
import sys


with open(sys.argv[1]) as f:
    dictionary = sorted([line.strip() for line in f], key=len, reverse=True)


def tokenize(sentence):
    tokens = []
    word_length = 0
    while word_length < len(sentence):
        word = longest_word(sentence[word_length:])
        tokens.append(word)
        word_length += len(word)
    return tokens


def longest_word(sentence):
    sen_length = len(sentence)
    while sen_length > 1:
        remain = sentence[:sen_length]
        if remain in dictionary:
            return remain
        sen_length -= 1
    return sentence[0]


for sentence in sys.stdin:
    for word in tokenize(sentence):
        word = word.strip('\n')
        print(word)
```
**The instruction on how to use the maxmatch**
The algorithm of using maxmatch is the same as of the one given in the practial.

```
$ python3 maxmatch.py dict < sentences > maxmatch_tokens
```

The dictionary of segmented surface forms was extracted from *UD_Japanese-GSD/ja_gsd-ud-train.conllu* with the help of the following commands:

```
# to delete comments in the text file and save changes into a new file
$ sed '/^#/d' ja_gsd-ud-train.conllu > ja_gsd-ud-train.conllu-nocomments

# to delete all the columns except of the second one
$ cut -f2 -d'   ' ja_gsd-ud-train.conllu-nocomments > ja_gsd-ud-train.conllu-dictionary

# to sort the dictionary
$ uniq *dictionary > dict
$ sort -u *dictionary > dict

# a whitespace in the first line was deleted with the help of vim
$ vim dict
:d
:x

# to check the size of the dictionary
$ wc -l dict
15326 dict
```

ja_gsd-ud-test.conllu file processing:

```
# to find test sentences
$ sed -n '/^# text = /p' ja_gsd-ud-test.conllu

# to delete '# text = ' segment so that it is not tokenized
# to save changes into a new file
$ sed -n '/^# text = /p' ja_gsd-ud-test.conllu | sed 's/^# text =//' > sentences

# to make a file with correctly tokenized words:
$ sed '/^#/d' ja_gsd-ud-test.conllu | cut -f2 -d'       ' > correct_tokenization

# to delete whitespaces in the 'sentences' file
$ sed 's/^ //g' sentences > sentences
```

*Tokenization process*
```
# to tokenize the processed dataset and save the results into a new file
$ python3 maxmatch.py dict < sentences > maxmatch_tokens

# to compare the total amounts of tokens
$ wc -l correct_tokenization 
13172 correct_tokenization

$ wc -l maxmatch_tokens 
18805 maxmatch_tokens
```

**Description of the maxmatch performance**
Unfortunately, the results are not that good. 
To perform the evaluation, I used apertium-eval-translator. The input files are:
1) 100 correctly tokenized sentences
2) 100 maxmatch tokenized sentences


Statistics about input files
-------------------------------------------------------
Number of words in reference: 2117
Number of words in test: 3025
Number of unknown words (marked with a star) in test: 
Percentage of unknown words: 0.00 %

Results when removing unknown-word marks (stars)
-------------------------------------------------------
Edit distance: 1528
Word error rate (WER): 72.18 %
Number of position-independent correct words: 1512
Position-independent word error rate (PER): 71.47 %

Results when unknown-word marks (stars) are not removed
-------------------------------------------------------
Edit distance: 1528
Word Error Rate (WER): 72.18 %
Number of position-independent correct words: 1512
Position-independent word error rate (PER): 71.47 %

Statistics about the translation of unknown words
-------------------------------------------------------
Number of unknown words which were free rides: 0
Percentage of unknown words that were free rides: 0%


Attached is the example of the first two sentences tokenized, compared with diff command:

```
$ diff -u correct_tokenization.txt maxmatch_tokens.txt | head -100
--- correct_tokenization.txt	2018-11-02 14:01:47.100646007 +0300
+++ maxmatch_tokens.txt	2018-11-02 17:30:05.290189861 +0300
@@ -1,18 +1,23 @@
-これ
+こ
+れ
 に
-不快感
+不快
+感
 を
-示す
+示
+す
 住民
 は
 い
-まし
+ま
+し
 た
 が
 ,
 現在
 ,
-表立っ
+表
+立っ
 て
 反対
 や
@@ -22,36 +27,53 @@
 を
 挙げ
 て
-いる
+い
+る
 住民
 は
 い
-ない
-よう
-です
+な
+い
+よ
+う
+で
+す
 。
 
 幸福
 の
 科学
 側
-から
+か
+ら
 は
 ,
 特に
-どうして
-ほしい
-という
+ど
+う
+し
+て
+ほ
+し
+い
+と
+い
+う
 要望
 は
-いただい
+い
+た
+だ
+い
 て
 い
-ませ
+ま
+せ
 ん
 。
 
-星取り
+星
+取り
 参加
 は
 当然
```

