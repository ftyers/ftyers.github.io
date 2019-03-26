# Transliteration
## Frequency and ranking
### Data
[SynTagRus](https://github.com/UniversalDependencies/UD_Russian-SynTagRus), train dataset
Script `freq.py` takes lines from standard input, counts frequency of each token and puts the result into `freq_sort.txt`. It has two columns: frequency and token and 107867 rows.
Three the most frequent tokens are:
Frequency| Word
--------|------
70048   |   ,
45571   |   .
22727   |   в
So two the most frequent tokens are punctuation marks and the third one is preposition. I want to look at words only, so the next version of script ignores the punctuation.
New file has 107852 rows, and the most frequent tokens are:
Frequency| Word
--------|-------------
22727   |	в
21243   |	и
10531	|   на
All of them are prepositions. Data has a long tail of single words such as proper nouns, numbers and abbreviations.
I also modified `freq.py` script to investigate the role of case. If I normalize each token to lower case, then the final list contains 99239 tokens instead of 107852. But this way leads to the loss of information proper nouns and abbreviations.
Script `rank.py` takes takes a command line argument and reads in a frequency list from a file and outputs a ranked frequency list `rank_freq.txt`
I used *pylab* module to look through the data and see that frequences are distributed according to the Zipf's law: the frequency of the word is inversely proportional to its rank in the frequency table. It is shown at [the picture](https://github.com/DorkEMK/ftyers.github.io/blob/master/2018-komp-ling/practicals/freq-rank/freq_rank.png)

## Transliteration
I looked through several systems for romanizing Russian Cyrillic ([Wikipedia]() and [A Reference Grammar of Russian](https://books.google.ru/books?id=-VFNWqXxRoMC&printsec=frontcover&hl=ru#v=onepage&q&f=false) and I didn't identify which one has been used in the example. All of this systems have lots in common, but differs in some aspects. This allows one to choose the right system based on ones goals: to make text more readable or easy to pronounce or to provide unambiguous reconstruction of Cyrillic text.
I've chosen the system of the Uppsala Corpus for some reasons:
- it has no diacritics
- it is unambiguous
- it has out-of-the-box equivalent for 'щ' - 'w'

A script `transliterate.py` takes two command line arguments: first is connlu file and second - tsv with transcription table. It changes 10-th column (MISC) to Translit='transliteration of the word'. The non-dictionary symbols are printed as is. Script also saves capitalized letters (e.g. at the beginning os the sentence).
  
This is how the source data looks like
```
# text = Начальник областного управления связи Семен Еремеевич был человек простой, приходил на работу всегда вовремя, здоровался с секретаршей за руку и иногда даже писал в стенгазету заметки под псевдонимом "Муха".
1	Начальник	начальник	NOUN	_	Animacy=Anim|Case=Nom|Gender=Masc|Number=Sing	8	nsubj	8:nsubj	_
2	областного	областной	ADJ	_	Case=Gen|Degree=Pos|Gender=Neut|Number=Sing	3	amod	3:amod	_
3	управления	управление	NOUN	_	Animacy=Inan|Case=Gen|Gender=Neut|Number=Sing	1	nmod	1:nmod	_
```
The script's output  will be
```
# text = Начальник областного управления связи Семен Еремеевич был человек простой, приходил на работу всегда вовремя, здоровался с секретаршей за руку и иногда даже писал в стенгазету заметки под псевдонимом "Муха".
1	Начальник	начальник	NOUN	_	Animacy=Anim|Case=Nom|Gender=Masc|Number=Sing	8	nsubj	8:nsubj	Translit=Nachalqnik
2	областного	областной	ADJ	_	Case=Gen|Degree=Pos|Gender=Neut|Number=Sing	3	amod	3:amod	Translit=oblastnogo
3	управления	управление	NOUN	_	Animacy=Inan|Case=Gen|Gender=Neut|Number=Sing	1	nmod	1:nmod	Translit=upravlenija
```
### Questions
Some rules can be added to improve transliteration.
1. For ambiguous letters like *e* and *je* we can look at the previous sign. After consonant we will put *e* and after vowel or at the beginning of the word - *je*. An additional list or other structure for storing consonants is required. E.g. *пение* turns into *penije*.
2. In case of *sh → ш*  if  we meet *s*  we should check the next  symbol  before transliteration. If it is *h* - we print *ш*, if it is not *h* - print *с* and go to the next symbol. Using this approach we should avoid an disambiguity *sh → ш*  or  *sh → сх* . We may know about the target language that it doesn't have *сх* or we shouldn't transliterate both *s → с* and *s → х* or we should add some additional rules.
3. If we work with full sentence as string, we should check whether the previous or the next symbols are spaces or punctuation. If we work with tokens separately - we should check the first and the last characters.
