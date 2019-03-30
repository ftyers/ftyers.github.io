- "Which Unix command might you use to sort the output in frequency order?"
> sort -nr

- "What do you think we would get if we set the argument reverse to False?"
> same list but from the least frequent words to the most frequent

1. At first I created freq.py that takes data from SynTagRus and creates txt file 
with words from corpus and their frequency.<br>
$ head freq.txt<br>
70048   ,<br>
45571   .<br>
22727   в<br>
21243   и<br>
16177   "<br>
12898   -<br>
10531   на<br>
10434   не<br>
7464    что<br>
6833    с<br>

2. The I've created rank.py that reads the sorted file and gives each token a rank
in addition to its frequency, the checked if the lens are equal.<br>
$ python3 rank.py<br>
107867<br>
$ wc -l freq.txt<br>
107867 freq.txt<br>

Also I added part that outputs a ranked frequency list:<br>
$ python3 rank.py | head -20<br>
1       70048   ,<br>
2       45571   .<br>
3       22727   в<br>
4       21243   и<br>
5       16177   "<br>
6       12898   -<br>
7       10531   на<br>
8       10434   не<br>
9       7464    что<br>
10      6833    с<br>
11      4306    по<br>
12      3590    :<br>
13      3490    к<br>
14      3439    как<br>
15      3258    а<br>
16      3224    В<br>
17      3058    из<br>
18      2979    это<br>
19      2691    для<br>
20      2554    )<br>

3. Transliteration table is in table.txt (got from https://ru.wikipedia.org/wiki/Транслит),
the code with comments is in trasliterate.py, results are in 'results.conllu'.

***Questions***
- What to do with ambiguous letters? For example, Cyrillic 'е' could be either je or e.<br>
It seems that the simplest way is to add simple if-statements to the code,
which would consider the context that affects the spelling of such letters.
Also it is possible to write a FST with special phonological rules for such cases.

- Can you think of a way that you could provide mappings from many characters to one character ?
	For example sh → ш or дж → c ? <br>
Maybe making some list of all possible examples and first check if there is key from this list in the word,
I can't come up with a more clever solution ¯\_(ツ)_/¯.

- How might you make different mapping rules for characters at the beginning or end of the string?<br>
At first it is needed to check if the letter is ambiguos, the if it's in the beggining or in the end
of the string and write some rules to decide what is the right spelling of this letter depending on the context.
We can use the same algorithms as in the first answer.

