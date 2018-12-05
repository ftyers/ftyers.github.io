# Frequency and ranking
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

