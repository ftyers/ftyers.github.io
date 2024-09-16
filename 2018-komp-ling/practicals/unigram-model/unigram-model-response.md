### Vladislav Mikhailov, MKL181

# Report on Unigram Model

## Functions

**palindrome.py**
```
import sys


freq = []


with open(sys.argv[1], 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        (f, w) = line.split('\t')
        freq.append((int(f), w))


def is_palindrome(s):
    rev = ''
    if len(s) == 1:
        return False
    for j in range(1, len(s) + 1):
        rev = rev + s[-j]
    if s == rev:
        return True
    return False

for i in freq:
    if is_palindrome(i[1]):
        print('%d\t%s' % (i[0], i[1]))
```

For the frequency llist to find palindromes in, the freq.txt on practical-2 is given:
```
$ python3 palindrome.py freq.txt | head

3439    как
1669    или
1254    еще
1085    ее
283    тут
279    тот
190    оно
90    XX
80    11
71    XIX
```
## Implementing n dimensional matrices with dict

**matrix.py**
```
import sys


rus = ['бы', 'вас', 'видит', 'всего', 'вы']
eng = ['a', 'absorbed', 'all', 'and', 'another']

m = {}

for wl in rus:
    if wl not in m:
        m[wl] = {}
    for w2 in eng:
        m[wl][w2] = 0
print('\t' + '\t'.join(eng))
for wl in m:
    print('%s\t' % (wl), end='')
    for w2 in m[wl]:
        print('%d\t' % (m[wl][w2]), end='')
    print('')
```

**Output**
```
$ python3 matrix.py

    a    absorbed    all    and    another
бы    0    0    0    0    0    
вас    0    0    0    0    0    
видит    0    0    0    0    0    
всего    0    0    0    0    0    
вы    0    0    0    0    0
```

### Why do we need end='' passed to the print() statement ? What would happen if we didn't have it?

The default value of the end parameter is '\n'. If we didn't have the parameter end='' in the print() function, the output would be implemented so that our values '0' + '\t' are appended each on a new line instead of being appended as a 'cell' value in the matrix. 

Thus, we would get the following output:
```
$ python3 matrix.py

	a	absorbed	all	and	another
бы	
0	
0	
0	
0	
0	

вас	
0	
0	
0	
0	
0	
...	
```

To save the output to a .tsv file:
```
$ python3 matrix.py > rus-eng.tsv
```

## Passing arguments from the command line 

### How do you get from that command line to having the filename as a variable you can use in your program?

```
$ python3 train.py rus-eng.tsv
```
Our python code train.py reads in rus-eng.tsv file as the first command line argument with the sys module imported:
```
import sys


with open(sys.argv[1], 'r') as f:
    <some code>
```
If we have something like:
```
import sys


for line in sys.stdin:
    <some code>
```
We will need to do the following:
```
$ python3 train.py < rus-eng.tsv
```
### What output do you get?

```
$ python3 args.py a b c
```

**Output**

If we use print(sys.argv) in our code, we get a list of all the variables given as command line arguments.

```
['args.py', 'a', 'b', 'c']
```
 
## Unigram language model

* For the tagged corpus of sentences I took the first 10 sentences from syntagrus_transliterated.conllu file on practical-2 (syntagrus_10.conllu);
* For the test sentence I took the one given as an example ("Это течение...", test.conllu);
* The implementation of the Unigram LM is train.py, with comments provided. I also submitted another version of the code, implemented without using functions (train_plain.py). Both of them seem to works fine, but the train.py works slower, than the train_plain.py

When testing the program, I get a little bit different output from the one given as an example. The order of the values printed is not the same, though all the values are correct:
```
$ python3 train.py test.conllu

# P    count    tag    form
0.06     1    DET    _
0.35     6    NOUN    _
0.12     2    VERB    _
0.18     3    ADP    _
0.18     3    ADJ    _
0.12     2    PUNCT    _
1.0     1    DET    Это
1.0     1    NOUN    течение
1.0     1    VERB    следует
1.0     2    ADP    на
1.0     1    NOUN    север
1.0     1    ADP    до
1.0     1    ADJ    Японского
1.0     2    NOUN    побережья
1.0     1    PUNCT    ,
1.0     1    VERB    оказывая
1.0     1    ADJ    заметное
1.0     1    NOUN    влияние
1.0     1    NOUN    климат
1.0     1    ADJ    японского
1.0     1    PUNCT    .
```
To save the output on syntagrus_10.conllu to a new .conllu file:
```
$ python3 train.py syntagrus_10.conllu > output.conllu
```
**Output example**
```
$ python3 train.py syntagrus_10.conllu | head -20
# P    count    tag    form
0.23     52    NOUN    _
0.16     36    PUNCT    _
0.07     15    ADJ    _
0.04     10    PROPN    _
0.01     3    AUX    _
0.14     31    VERB    _
0.12     27    ADP    _
0.08     18    ADV    _
0.04     9    CCONJ    _
0.02     5    PART    _
0.04     9    PRON    _
0.01     3    DET    _
0.03     7    SCONJ    _
0.01     2    NUM    _
1.0     1    NOUN    Анкета
1.0     11    PUNCT    .
1.0     1    NOUN    Начальник
1.0     1    ADJ    областного
1.0     1    NOUN    управления
```

## Questions

* What might be a simple improvement to the language model for languages with orthographic case?
    * We need to normalize our words with lowering the case, so that to merge the frequency results for both upper and lower cases. On dealing with proper nouns we can use some dictionaries if needed.
