Mikhailov Vladislav
MKL181

# Report on Transliteration

**Data**
The data to be processed is ru_syntagrus-ud-train.conllu file from  https://github.com/UniversalDependencies/UD_Russian-SynTagRus

**The dict datastructure**
The data has been processed with the python algorithm provided:
```
import sys


vocab = {}

for line in sys.stdin.readlines(): 
    if '\t' not in line:
        continue
    row = line.split('\t')
    if len(row) != 10:
        continue
    form = row[1]
    if form not in vocab:
    vocab[form] = 0
    vocab[form] = vocab[form] + 1

for w in vocab:
    print('%d\t%s' % (vocab[w], w))
```

*Which Unix command might you use to sort the output in frequency order?*

We can sort the output in frequency order and save changes into a new file with the help of sort command and -nr argument:
```
$ sort freqList -nr > freqListSorted

#to check whether everything works fine:
$ head freqListSorted
70048	,
45571	.
22727	в
21243	и
16177	"
12898	-
10531	на
10434	не
7464	что
6833	с
```

**I guess the difference in the outputs is because of the recent train.conllu file update (as of November 4).**

*What do you think we would get if we set the argument reverse to False?*

If we set the argument reverse to False, as here:
```
import sys


vocab = {}
freq = []

for line in sys.stdin.readlines():
    if '\t' not in line:
        continue
    row = line.split('\t')
    if len(row) != 10:
        continue
    form = row[1]
    if form not in vocab:
        vocab[form] = 0
    vocab[form] = vocab[form] + 1

for w in vocab:
    freq.append((vocab[w], w))
freq.sort(reverse=False)
print(*freq[0:4])
```
we get the frequency list sorted in numeric order (not reversed), starting with the '+' sign, and then with the '-' sign attached to the numeric:
```
$ python3 dictFreq.py < ru_syntagrus-ud-train.conllu
(1, '+7-2=2') (1, '+7°C') (1, '+8-6') (1, '-2,45')
```

The provided python code segments have been modified so that to implement a python script that allows to get a frequency list from a .conllu file, taking a command line argument and outputing a sorted frequency list to a text file (dictFreq.py file is in the practical folder):
```
import sys


vocab = {}
freq = []


def get_frequency():
    for line in sys.stdin.readlines():
        if '\t' not in line:
            continue
        row = line.split('\t')
        if len(row) != 10:
            continue
        form = row[1]
        if form not in vocab:
            vocab[form] = 0
        vocab[form] = vocab[form] + 1
    for w in vocab:
        freq.append((vocab[w], w))
    return freq.sort(reverse=True)


def results():
    with open('freq.txt', 'w+', encoding='utf-8') as f:
        for w in freq:
            f.write('%d\t%s\n' % (w[0], w[1]))
        f.close()


def main():
    get_frequency()
    results()


if __name__ == '__main__':
    main()
```

How to use:
```
$ python3 dictFreq.py < ru_syntagrus-ud-train.conllu
```

**File input/output**
*Now create a script called rank.py which takes a command line argument and reads in a frequency list from a file and outputs a ranked frequency list (either to a file or to standard output).*

The provided python code segments have been modified so that to implement the frequency ranking algorithm (rank.py file is in the practical folder):


```
import sys


freq = []
ranks = []


def frequency():
    with open(sys.argv[1], 'r') as file:
        for line in file.readlines():
            line = line.strip('\n')
            (f, w) = line.split('\t')
            freq.append((int(f), w))
    return freq


def ranking(freq):
    rank = 1
    min = freq[0][0]
    for i in range(0, len(freq)): 
        if freq[i][0] < min: 
            rank = rank + 1
            min = freq[i][0]
        ranks.append((rank, freq[i][0], freq[i][1]))
    return ranks


def output():
    for w in ranks:
        print('%d\t%d\t%s' % (w[0], w[1], w[2]))


def main():
    frequency()
    ranking(freq)
    output()


if __name__ == '__main__':
    main()
```
How to use:
```
$ python3 rank.py freq.txt
```

*Do you notice anything interesting in the data?*
There are plenty of words at the same rank. Further possible script implementation is grouping the words by the same rank and dividing them, for example, by words / non-words or (and) by lexical classes for particular needs.

*Do you think you could make the code more efficient?*
---------------

**Transliterator**

For the Cyrillic transliteration table I took the scientific transliteration table. You can find the table in translit_table file, in the practical folder.

Here is my transliterator implementation:
```
import sys
import re


v = {} # to create an empty dictionary


# to create a dictionary from a table given as the first command line argument 
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        line = line.strip('\n')
        items = line.split('\t')
        key, v[key] = items[0], items[1]


# to read in a conllu file as the second command line argument
with open(sys.argv[2], 'r') as c:
    for line in c.readlines():
        if '\t' not in line:
            continue
        row = line.split('\t')
        if len(row) != 10:
            continue
        tokens = row[1]
        # to transliterate tokens in the second column
        transliterated = ''
        for letter in tokens:
            if letter in v:
                transliterated += v[letter]
            else:
                transliterated += letter

        ```
        to provide mappings on ambigous cyrillic letter 'e' - 'e'|'je':
        the transliteration table is implemented so that 'e' is transliterated to 'je'.
        We need to save the results when 'je' is the beginning of a token or preceeded by a vowel,
        "'" and "''". Thus, we only need to implement 'je' -> 'e' mapping in the transliterated
        tokens when 'je' is preceeded by a consonant:
        ```

        transliterated = re.sub('([^aoeiuyAOEIU′″])je', r'\1e', transliterated)

        # to store the transliterated tokens in the 10th column
        row[9] = 'Translit=' + transliterated

        # to output the conllu file with the transliterated tokens to std output
        print('\t'.join(row[0:10]))
```
How to use:
```
$ python3 transliterate.py translit_table ru_syntagrus-ud-train.conllu 
```
I saved the transliterated .conllu file into a new text file with the help of the terminal (first 7000 lines):
```
$ python3 transliterate.py translit_table ru_syntagrus-ud-train.conllu | head -7000 > syntagrus_transliterated.conllu 
```

#Questions
* What to do with ambiguous letters ? For example, Cyrillic `е' could be either je or e.
	* To provide mappings on ambigous Cyrillic letter 'e' - 'e'|'je': 
	'e' is transliterated to 'je' when in the beginning of a token or when preceeded by a vowel, "'" and "''". 
	Thus, we only need to implement 'je' -> 'e' mapping in the transliterated tokens when 'je' is preceeded by a consonant:
```
transliterated = re.sub('([^aoeiuyAOEIU′″])je', r'\1e', transliterated)
```

* Can you think of a way that you could provide mappings from many characters to one character ? (For example sh → ш or дж → c ? )
	* Firstly, I guess we do not need to store the letters 's' and 'h' in our transliteration table. We implement the transliteration of all the letters in the tokens except for 's' and 'h'.
	* Secondly, we use re.sub to provide mappings from the consonant cluster 'sh' →  ш
```
transliterated = re.sub('sh', 'ш', transliterated)
```

	* Thirdly, we use re.sub to map 's' to 'с' and 'h' to 'х':

```
transliterated = re.sub('s', 'с', transliterated)
transliterated = re.sub('h', 'х', transliterated)
```

* How might you make different mapping rules for characters at the beginning or end of the string ? 
	* (Almost the same as of Question 1) One way to do it is to implement the transliteration table so that to meet our needs (as I did). There is a key-value pair 'е : je' in the dictionary. Thus, we provide correct mapping rules for Cyrillic 'e' in the beginning of a token (e.g. 'ему' -> 'jemu'). Then, we only need to implement substitution of 'je' to 'e' in the certain context (after a consonant):

	распоряжение -> rasporjažjenije -> rasporjaženije

	* Another way to do that (when there is a key-value pair 'е : e' in the dictionary) is to implement substitution of 'e' to 'je' in the transliterated tokens:
	1) When in the beginning of the token:
```
transliterated = re.sub('^е', 'je', transliterated)
```


	единственное -> edinstvennoe -> jedinstvennoe

	2) When preceeded by a vowel, "'" and "''":


```
transliterated = re.sub('(a|o|e|i|u|y|′|″)e', r'\1je', transliterated)
```


	jedinstvennoe -> jedinstvennoje

	Thus we get a sequence of changes:
	единственное -> edinstvennoe -> jedinstvennoe -> jedinstvennoje

All in all, the main idea is to implement a transliteration table so that to meet the application needs and to perform some changes in the results. To do the latter, we need to find out the context for the letter substitution and write rules with the help of regular expressions.

Attached are the files: dictFreq.py, rank.py, freq.txt, translit_table, transliterate.py, syntagrus_transliteraded.conllu.




