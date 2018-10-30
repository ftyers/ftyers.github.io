Report #0. Sentence segmentation. Sorokin Semen


First of all, I extracted 50 paragraphs from wiki texts using WikiExtractor and this command:  “sed 's/\n/\n/g' < wiki.txt | sed 200q | sort -R | sed 50q > 50par.txt”.  (I used regexp to find paragraphs, took 200 random cases, sorted them, finally extracted 50 and wrote to the file) 


Qualitative analysis: 
On the next step I used Pragmatic segmenter to split this document into sentences.  The result was not absolutely correct. I observed some negative examples of splitting, for example: 
    • “Более 3 тыс.
озёр (1,5 % территории):”
    • “Территория современной Литвы была заселена людьми с конца X—IX тысячелетия до н.
э.”

Then, I’ve used nltk_parser.py, script was written on python using nltk library and PunktSentenceTokenizer. However, this script also had some errors, like this: 
    • “Более 3 тыс.
озёр (1,5 % территории):”
    • “В конце неолита (III-II тыс.
до н.
э.)
на территорию современной Литвы проникли индоевропейские племена.”
Here we can see that mis-splitting (in all sentences) is caused by some specific Russian abbreviations. However all this cases can be easily avoided on the segmentation step: it was necessary to check the capital letter of the next word after abbreviation full stop.


Quantitate analysis:
Manual segmentation lets me know that this mini-corpus contain 93 sentences. Nltk script split it to the 97 fragments, and ruby script – 95.  In terms of accuracy percentage I have 93/97= 0.96 for NLTK and 93/95 = 0.98 for Pragmatic segmenter.
