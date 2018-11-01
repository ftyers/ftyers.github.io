# Report 1
## Sentence segmentation

In the beginning, I've extracted 50 paragraphs from wiki texts using WikiExtractor and the linux termianal command: *“sed 's/\n/\n/g' < wiki.txt | sed 300q | sort -R | sed 50q > text.txt”.* Firstly, I used regular expressions to find paragraphs, then I took 300 of them, randomly sorted and wrote 50 sorted ones to *text.txt*.
Then I used ruby and python scripts to compare two different segmenters. 

1. Qualitative analysis:

To start with, I used ruby's Pragmatic segmenter to split text.txt into sentences. Even though the script performed quite well, there were some issues with segmentation, as can be seen below:
* В 1980 г.
* В V веке н.
* э.

Then, I’ve used segmenter.py. This script was written on python using nltk and its module PunktSentenceTokenizer. However, nltk hasn't performed greatly either, having some trouble splitting sentences:
* Данный институт впервые в российской практике введён Конституцией Российской Федерации 1993 года (пунктом «е» ч.
* 1 ст.
* 103), которая устанавливает, что Уполномоченный по правам человека назначается Государственной думой и действует в соответствии с федеральным конституционным законом.

The main issue when splitting sentences in Russian is abbreviation, as can be seen above. This problem is not inescapable, however, and can be corrected with a condition of a space and capital letter following the needed punctuation mark.

2. Quantitate analysis:

Manually, I counted 131 sentences in text.txt. After that, with a script I counted the length of the list that python has as an output, which resulted in 135 sentences. And then with a script I counted the paragraphs in the output of ruby, which was 140 sentences.
131/135 > 131/140, therefore python script performed slightly better than the ruby segmenter.
