# Report for segmentation task

I did the following steps:

1. Downloaded the file -pages-articles.xml.bz2 from https://dumps.wikimedia.org (for the English language)
2. Installed WikiExtractor 
3. Installed nltk with:
```sh
$ sudo apt-get install python3-nltk
```
4. In the python file 'Segmenter.py' imported sentence tokenizer:
```sh
from nltk.tokenize import sent_tokenize
```
- Applied it to my fifty paragraphs in the file 'fifty.txt' to the file 'my_sentences.txt'
5. Did the segmentation myself in the file 'my_sentences.txt - копия' and compared the results.

#The results:

- The segmentor and I made the same number of mistakes: two.
- I was just not attentive enough, and NLTK confused a few things, for example, it apparently confused the dot in etc. with the end of the sentence:
> The first two lines of the "Iliad" read: In geometry, capital A, B, C etc. \n
>are used to denote segments, lines, rays, etc. \n

- The same way it confused the dot in i.e. with the end of the sentence:
> *kVn- "Co-wife" Semitic, Berber, Chadic randomization-based analysis assumes only the homogeneity of the Adobe walls are load bearing, i.e. \n 
they carry their own weight into the foundation rather than by another structure, hence the adobe must have sufficient compressive strength. \n


Apart from that I didn't notice any terrible mistakes.

Unfortunately I didn't have time to test another segmentor. I'll try to do it as soon as I can.

