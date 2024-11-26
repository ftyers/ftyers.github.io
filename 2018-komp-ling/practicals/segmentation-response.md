Report #0. Sentence segmentation. Sorokin Semen


First of all, I extracted 50 paragraphs from wiki texts using WikiExtractor and this command:  “sed 's/\n/\n/g' < wiki.txt | sed 200q | sort -R | sed 50q > 50par.txt”.  (I used regexp to find paragraphs, took 200 random cases, sorted them, finally extracted 50 and wrote to the file) 


Qualitative analysis: 


On the next step I used Pragmatic segmenter to split this document into sentences.  The result was not absolutely correct. I observed some negative examples of splitting, for example: 


“Более 3 тыс.


озёр (1,5 % территории):”


“Территория современной Литвы была заселена людьми с конца X—IX тысячелетия до н.


э.”

Then, I’ve used nltk_parser.py, script was written on python using nltk library and PunktSentenceTokenizer. However, this script also had some errors, like this: 


“Более 3 тыс.


озёр (1,5 % территории):”


“В конце неолита (III-II тыс.


до н.


э.)


на территорию современной Литвы проникли индоевропейские племена.”


Here we can see that mis-splitting (in all sentences) is caused by some specific Russian abbreviations. However all this cases can be easily avoided on the segmentation step: it was necessary to check the capital letter of the next word after abbreviation full stop.


Quantitate analysis:


Manual segmentation lets me know that this mini-corpus contain 93 sentences. Nltk script split it to the 97 fragments, and ruby script – 95.  In terms of accuracy percentage I have 93/97= 0.96 for NLTK and 93/95 = 0.98 for Pragmatic segmenter.


Report #1.

In this part of practical I implement MaxMatch algorithm according to Jurafsky pseudo-cod.


To use only MaxMatch script, you can run it with python3 (requirements: pip install conllu).


Example: sed これに不快感を示す住民はいましたが,現在,表立って反対や抗議の声を挙げている住民はいないようです。| python3 Max-Match.py sort_d.txt


Also I implement the utility to parse sentences in any languages presented as a tree and saved in conllu format. It also provides evaluation of this parsing. 


How evaluation works?


Evaluation script looks at the symbols, punctuation and spaces to determine where maxmatch was mistaken and where it was correct. If both sentences have a space in the same place, the algorithm split sentences correctly (true positive), if both sentences have a text symbol or a punctuation mark in the same place, the algorithm correctly didn't split the sentences (true negative). If the parsed sentence has a space where it shouldn't, it's false positive, and if it doesn't have a space where it should, it's false negative. Finnaly,  it counts accuracy and precision to see how well the algorithm did.


To use it, run main.py (from 'parser for conllu' directory) and insert direcroties or file names with train and test corpus.


Example: python3 main.py


Insert file name of train corpus
data/ja_gsd-ud-train.conllu


Insert file name of test corpus
data/ja_gsd-ud-test.conllu


Using this utility I counted Accuracy (it was 0.94) and Precision (it was 0.9) and these results are pretty good. 
