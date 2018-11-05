#### Practical 1
##### Segmentation
<br /> Comaparison of nltk and pragmatic_segmenter segmenters for the German language <br />
<br /> nltk segmenter: <br />

```import nltk
from nltk.tokenize import sent_tokenize
import sys

my_file = open("/home/marina/WikiExtractor/segmented.txt", "w")
for line in sys.stdin:
    for sentence in sent_tokenize(line, language='german'):
        # for word in nltk.tokenize.WordPunctTokenizer().tokenize(sent):
        my_file.write(sentence)
        print(sentence)
```        
<br /> pragmatic_segmenter for German <br />
``` require 'pragmatic_segmenter'

lang = "de"
if ARGV[0]
    lang=ARGV[0]
end

STDIN.each_with_index do |line, idx|
    ps = PragmaticSegmenter::Segmenter.new(text: line, language: lang)
    ps.segment
    for i in ps.segment
        print(i,"\n")
    end
end
```

**Comparison**
<br />After executing<br />
```$ diff -U0 segmented-nltk segmented-pragmatic | sed -n '/^@@ /p'```
<br />We get the following results:<br />
```
@@ -9 +7,2 @@
@@ -19 +18,2 @@
@@ -21,2 +21 @@
@@ -37 +36,2 @@
@@ -41 +41,3 @@
@@ -66,2 +68 @@
@@ -79,2 +80,4 @@
```
<br />So overall pragmatic segmenter makes more linebreaks than nltk. Let's look at the errors:<br />
```
-Am 9. November 1141 findet Rollshausen seine erste Erwähnung.
+Am 9.
+November 1141 findet Rollshausen seine erste Erwähnung.

-Apfel stand auf der ersten Ausbürgerungsliste des Deutschen Reichs vom 23. August 1933.
+Apfel stand auf der ersten Ausbürgerungsliste des Deutschen Reichs vom 23.
+August 1933.

-Augustus (63 v. Chr.–14 n. Chr.), der Großneffe und Erbe Gaius Iulius Caesars, war von 31 v. Chr. an Alleinherrscher des Römischen Reiches.
+Augustus (63 v. Chr.–14 n. Chr.), der Großneffe und Erbe Gaius Iulius Caesars, war von 31 v.
+ Chr.
```
<br />Consequently, pragmatic segmenter doesn't seem to solve the dates issues and some abbreviations in which case nltk segmenter turned put to be more useful.<br />

##### Tokenisation
<br />At first we create a dictionary<br />
```cd UD_Japanese-GSD
   cat ja_gsd-ud-train.conllu  | grep '^[0-9]' | cut -f2 | sort -f | sort -u | uniq -c | sort -gr > sortedforms.txt
```
<br />It contains 22313 sortedforms<br />   
<br />Than we get the sentences from the dataset and correct tokenisation in order to be able to evaluate the results of the algorithm later<br /> 
```sed -n '/^# text =/p' ja_gsd-ud-test.conllu | sed 's/^# text =//'g > sentences
cat sentences
sed '/^#/d' ja_gsd-ud-test.conllu | cut -f2 -d' ' > correct-tokenization
```
<br />Implementing the algorithm (the python code is in ...segmentation/maxmatch.py)<br />

```
python3 maxmatch.py sortedforms <sentences > maxmatch-tokenization
```
<br />We get 13172 correct-tokenization and 23511 of maxmatch-tokenization which already indicates that it's not good<br />
The calculation of WER was made with the gelp of the following (but slightly changed for python 3) code:
https://github.com/zszyellow/WER-in-python <br />
<br /> The WER turned out to be 50%. After an observation it turned out that maxmatch fails on digits and some English words, probably because they were not in the dictionary. In other cases it was impossible to interprete the results but these particular situations can be improved with additional lines to maxmatch like checking if a character can be an integer.
<br /> 
