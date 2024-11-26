
# Ranking and transliteration report

## Frequencies and ranking

For this task algorithm getting frequencies (`freq.py`) and ranking algorithm (`rank.py`) were implemented (you can see them in the same folder with this report).

As a test data `ru_syntagrus-ud-train.conllu` was used.

Script `freq.py` usage:
```
python freq.py ru_syntagrus-ud-train.conllu
```

Output (file `freq_sort.txt`):
```
25951	в
23003	и
11383	на
10926	не
7835	что
7297	с
5042	по
4687	а
4148	как
3888	это
```

Script `rank.py` usage:
```
python rank.py freq_sort.txt
```
Output (file `rank_freq.txt`):

```
1	25951	в
2	23003	и
3	11383	на
4	10926	не
5	7835	что
6	7297	с
7	5042	по
8	4687	а
9	4148	как
10	3888	это
```

## Transliteration
For this task transliteration code (`transliterate.py`) and transliteration table (`transliteration_table.txt`) from Russian to English were created (you can see it in the same folder with this report).

As a test data an example from practical description was used.

Script usage:
```
python transliterate.py test.tsv
```

Script output:
```
1       Это     _       _       _       _       _       _       _       _
Translit=Eto
2       течение _       _       _       _       _       _       _       _
Translit=techenie
3       следует _       _       _       _       _       _       _       _
Translit=sleduet
4       на      _       _       _       _       _       _       _       _
Translit=na
5       север   _       _       _       _       _       _       _       _
Translit=sever
6       до      _       _       _       _       _       _       _       _
Translit=do
7       Японского       _       _       _       _       _       _       _
_       Translit=Yaponskogo
8       побережья       _       _       _       _       _       _       _
_       Translit=poberezh'ya
9       ,       _       _       _       _       _       _       _       _
Translit=,
10      оказывая        _       _       _       _       _       _       _
_       Translit=okazyvaya
11      заметное        _       _       _       _       _       _       _
_       Translit=zametnoe
12      влияние _       _       _       _       _       _       _       _
Translit=vliyanie
13      на      _       _       _       _       _       _       _       _
Translit=na
14      климат  _       _       _       _       _       _       _       _
Translit=klimat
15      японского       _       _       _       _       _       _       _
_       Translit=yaponskogo
16      побережья       _       _       _       _       _       _       _
_       Translit=poberezh'ya
17      .       _       _       _       _       _       _       _       _
Translit=.
```

### Questions
#### Question 1
What to do with ambiguous letters? For example, Cyrillic 'е' could be either je or e.

Answer:

We can write a rule for solving this issue. For example:
- if 'е' is at the beginning of the word, after vowels and 'ь' or 'ъ', it should be transliterated as 'je'
- in other cases 'e' should be transliterated as 'e'

#### Question 2
Can you think of a way that you could provide mappings from many characters to one character? For example sh → ш or дж → c ?

Answer:

We can write a rule checking the letter by which 's' is followed. For example:
- if this letter is 'h', then transliterate bigram 'sh' as 'ш'
- if this letter is not 'h', then transliterate гтшпкфь 's' as 'с'

#### Question 3
How might you make different mapping rules for characters at the beginning or end of the string?

Answer:

We should check whether the next or previous symbol is '\s' or '[.?]' if we consider the whole string as a sentence.

If we work with separated tokens, then we should check the first and the last characters of a token.
