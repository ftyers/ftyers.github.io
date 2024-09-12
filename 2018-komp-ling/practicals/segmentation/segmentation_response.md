# Segmentation report
##### *Anastasia Nikiforova*

**UPDATE** - Pragmatic Segmenter lang is set to "ru". Correcting the report below...

* Brief description of each segmenter used
  * I used two segmenters: **Pragmatic Segmenter** and **NLTK's Puntk**. 
  
  I definitely enjoyed the performance of NLTK's Puntk more, but in some cases Pragmatic Segmenter works better (see the table below).
  The noticeable problem with Pragmatic Segmenter is that it segments names when it shouldn't (like: A. C. Пушкин).
  Punkt solves this case better. NLTK works best with English, performance on other languages is lower.
  The advantage of Pragmatic Segmenter is that is really easy to add new exceptions to segmentation rules (just add them to the library in the *Languages* folder). I'm sure it is possible to add rules to Punkt as well, but it seems to me it requires a bit more of a hustle :)

* Quantitative evaluation

  * First 1000 paragraphs - Punkt: 2531 sentences; Pragmatic Segmenter: 2869 sentences.
  * On average, Pragmatic Segmenter's result contains 12% more sentences than Punkt's.
  * Accuracy rate for Punkt: 0.86;
  * Accuracy rate for Pragmatic Segmenter: 0.89;  
  

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

It is noticeable that both Pragmatic Segmenter and Puntk are not aware of some abbreviations, and unconventional punktuation combination.

NLTK Punkt works perfectly with contracted names. 

**Interesting:** I noticed that Pragmatic Segmenter does one very interesting thing. It treats one quotation as an inseparable segment. How cool is that!
Punkt doen't split names or most abbreviations, however there are some abbr. that are very popular, but Punkt still splits them.
