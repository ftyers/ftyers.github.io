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

