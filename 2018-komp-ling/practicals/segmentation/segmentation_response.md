# Segmentation report
##### *Anastasia Nikiforova*


* Brief description of each segmenter used
  * I used two segmenters: **Pragmatic Segmenter** and **NLTK's Puntk**. 
  I definitely enjoyed the performance of NLTK's Puntk more: it seems to be way more accurate.
  The problem with Pragmatic Segmenter is that it doesn't cover difficult cases, such as abbreviations or internal ".", "?", "!".
  Punkt solves this ambiguous cases better, but, again, not perfectly. NLTK works best with English, performance on other languages is lower.

* Quantitative evaluation: Accuracy percentage (how many sentence boundaries were detected correctly)
* Qualitative evaluation: What kind of mistakes does each segmenter make?
