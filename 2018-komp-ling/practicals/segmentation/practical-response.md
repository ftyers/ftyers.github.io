#### Practical 1
##### Segmentation
<br /> I compared nltk and pragmatic_segmenter segmenters on the German language <br />
<br /> my nltk segmenter looked like this: <br />

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
<br /> And pragmatic_segmenter segmenters was also for German <br />
``` require 'pragmatic_segmenter'

lang = "en"
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
<br />To be continued<br />
