# Unigram tagger (engineering)

Files are presented in subdirectory `tagger`.  

#### matplotlib

File `makeranks.sh`  uses file of model from previous practical, transforms it to make it fit for plot drawing code (file `ranks.txt`). Plot drawing is done with `ranks.py`. Result is `ranks.png`.

#### scikit learn

**What kind of accuracy do you get ?** 

Classifier is `pronunciation.py`, on the whole dataset we got accuracy 0.9955177050649933 (output is in `pronunciation_output.txt`). After train/test splitting the resulted accuracy is practically the same  (output is in `pronunciation_output_split.txt`).

What kind of  errors does the classifier make ? 

Words which have Ve letter before vowels “spoil” the dataset, so we got "вь" at the end of the words as [v] instead of [f]

How do you think you might be able to improve on the accuracy ?

We have to deal with “technical” characters of Russian orthography like Ь and Ъ - either or strip them on data preprocessing step, or consider context when building vectors.

### screenscraping

Wiktionary content was retrieved with `getwiktionary.sh`: files `tree.html` and `fear.html.` Required content was extracted via `wiktionary.py`. 

### unigram tagger

File `tagger.py` . I use example data as `test.tsv` and result is in `result.tsv`.

-  **How accurate is the tagger?**

  - It is not really accurate, because I use my language model, which has not too much words in it. Also, by design it fallbacks to the most frequent part of speech, which in my case is noun – it is not really fine-tuned heuristics.

-  **How could you improve performance without incorporating context ...**

- -  **using Python string functions ?** 
    - chunk words like stemmer does?
  -  **using regular expressions ?** 
    - write rules for paradigms and parse tokens?
  -  **using screen scraping ?** 
    - scrape external dictionaries?

-  Could you store other single-word features in your unigram model ? Which features might you like to store ? 

  - We could, the format allows it. It would be reasonable to store paradigm classes, if possible, or word structure (like root and affixes). Right/left context may be of use.