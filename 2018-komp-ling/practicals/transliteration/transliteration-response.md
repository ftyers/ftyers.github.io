- "Which Unix command might you use to sort the output in frequency order?"
> sort -nr

- "What do you think we would get if we set the argument reverse to False?"
> same list but from the least frequent words to the most frequent

1. At first I created freq.py that takes data from SynTagRus and creates txt file 
with words from corpus and their frequency.
$ head freq.txt
70048   ,
45571   .
22727   в
21243   и
16177   "
12898   -
10531   на
10434   не
7464    что
6833    с

2. The I've created rank.py that reads the sorted file and gives each token a rank
in addition to its frequency, the checked if the lens are equal.
$ python3 rank.py
107867
$ wc -l freq.txt
107867 freq.txt

Also I added part that outputs a ranked frequency list:
$ python3 rank.py | head -20
1       70048   ,
2       45571   .
3       22727   в
4       21243   и
5       16177   "
6       12898   -
7       10531   на
8       10434   не
9       7464    что
10      6833    с
11      4306    по
12      3590    :
13      3490    к
14      3439    как
15      3258    а
16      3224    В
17      3058    из
18      2979    это
19      2691    для
20      2554    )

3. Transliteration table is in table.txt (got from https://ru.wikipedia.org/wiki/Транслит),
the code with comments is in trasliterate.py, results are in 'results.conllu'.

***Questions***
- What to do with ambiguous letters? For example, Cyrillic 'е' could be either je or e.
It seems that the simplest way is to add simple if-statements to the code,
which would consider the context that affects the spelling of such letters.
Also it is possible to write a FST with special phonological rules for such cases.

- Can you think of a way that you could provide mappings from many characters to one character ?
	For example sh → ш or дж → c ?
Maybe making some list of all possible examples and first check if there is key from this list in the word,
I can't come up with a more clever solution ¯\_(ツ)_/¯.

- How might you make different mapping rules for characters at the beginning or end of the string?
At first it is needed to check if the letter is ambiguos, the if it's in the beggining or in the end
of the string and write some rules to decide what is the right spelling of this letter depending on the context.
We can use the same algorithms as in the first answer.

