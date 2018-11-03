# Segmentation report
##### *Anastasia Nikiforova*


* Brief description of each segmenter used
  * I used two segmenters: **Pragmatic Segmenter** and **NLTK's Puntk**. 
  
  I definitely enjoyed the performance of NLTK's Puntk more: it seems to be way more accurate.
  The problem with Pragmatic Segmenter is that it doesn't cover difficult cases, such as abbreviations or internal ".", "?", "!".
  Punkt solves this ambiguous cases better, but, again, not perfectly. NLTK works best with English, performance on other languages is lower.

* Quantitative evaluation

  * First 1000 paragraphs - Punkt: 2531 sentences; Pragmatic Segmenter: 2869 sentences.
  * On average, Pragmatic Segmenter's result contains 12% more sentences than Punkt's.
  * Accuracy rate for Punkt: 0.86;
  * Accuracy rate for Pragmatic Segmenter: 0.79;
    ** (Tested on a mini corpus of 56 sentences, where Punkt founв 65 segments, and Pragmatic Segmenter found 71 sentences)
  
  

* Qualitative evaluation: Comparing performance on ambiguous cases.

### Main differences: Pragmatic Segmenter VS NLTK's Punkt

|Split?|Example| PRAGM|PUNKT|
|---:|:---:|:---:|:---:|
|Names|*F. M. Last*|split :(| -- |
|Abbr.,|*6 тыс., и...*|split :(| -- |
|.)|*1825 г.) и ...*| -- |split :(|
|.\. (almost ellipsis)|*Day is warm.\.*<EOS> *Night is cold*|split| -- :(
|Quotation|*"Newton. Said. This."*| -- :) |split :\||
|Numbered list|*1. First claim.*| -- |split after **(/d/.)** :(|
|Abbrev. at the EOS|*до XX в.*<EOS>|split| -- :(|
|Abbrev.--|*Кошки, собаки и др. -- любят спать*| -- :(|split|
|Spesific ones:| *тыс. руб.*|split :( | split :(|
||*н. э.*| -- |split :( |
||*г.*| split :( | -- |
||*тыс. человек*| -- |split :(|
||*др.*| -- | split :(|

It is noticeable that Pragmatic Segmenter is not aware of some abbreviations, names and unconventional punktuation combination. However, its adnavtage is that it can treat one quotation as an inseparable segment.
Punkt doen't split names or most abbreviations, however there are some abbr. that are very popular, but Punkt still splits them.
