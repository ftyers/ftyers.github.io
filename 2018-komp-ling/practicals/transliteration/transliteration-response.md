# Transliteration

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
