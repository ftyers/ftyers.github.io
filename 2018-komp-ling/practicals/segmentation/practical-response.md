#### Practical 1
##### Segmentation
<br /> I compared nltk and pragmatic_segmenter segmenters <br />
<br /> my nltk segmenter looked like this: <br />
```import nltk
from nltk.tokenize import sent_tokenize
import sys

my_file = open("/home/marina/WikiExtractor/segmented.txt", "w")
for line in sys.stdin:
    for sentence in sent_tokenize(line):
        # for word in nltk.tokenize.WordPunctTokenizer().tokenize(sent):
        my_file.write(sentence)
        print(sentence)```
**Comparison**
<br />After executing<br />
```$ diff -U0 segmented-nltk segmented-pragmatic | sed -n '/^@@ /p'```
<br />We get the following results<br />
@@ -1,2 +0,0 @@
@@ -9 +7,2 @@
@@ -19 +18,2 @@
@@ -21,2 +21 @@
@@ -37 +36,2 @@
@@ -41 +41,3 @@
@@ -66,2 +68 @@
@@ -79,2 +80,4 @@
<br />So overall nltk makes more linebreaks than pragmatic segmenter. Let's look at the errors<br />
