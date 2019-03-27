# Report on Unigram model
### Functions
```
freq = []

with open('freq.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip('\n')
        (f, w) = line.split('\t')
        freq.append((f, w))


def is_palindrome(s):
	"""Return True if the given string is a palindrome."""
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

Output is like:

```
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

### Implementing _n_ dimensional matrices with dict

##### matrix.py

```
import sys

rus = ['бы', 'вас', 'видит', 'всего', 'вы']
eng = ['a', 'absorbed', 'all', 'and', 'another']

m = {}

for w1 in rus: 
    if w1 not in m: 
        m[w1] = {}
    for w2 in eng:
        m[w1][w2] = 0
        
print('\t' + '\t'.join(eng))
for w1 in m:
        print('%s\t' % (w1), end='')
        for w2 in m[w1]:
                print('%d\t' % (m[w1][w2]), end='')
        print('')
```
```
	a	absorbed	all	and	another
бы	0	0	0	0	0	
вас	0	0	0	0	0	
видит	0	0	0	0	0	
всего	0	0	0	0	0	
вы	0	0	0	0	0
```

> Why do we need end='' passed to the print() statement ? What would happen if we didn't have it ?

By default, ``end='\n'``, so if we did not print ``end=''``, we would have each zero written at the new line as follows:
```
    a	absorbed	all	and	another
бы	
0	
0	
0	
0	
0	

...
```
To save the matrix:
```
python matrix.py > rus-eng.tsv
```


### Passing arguments from the command line

##### args.py
```
import sys

print(sys.argv)
```
Output:
```
['args.py', 'a', 'b', 'c']
```

So, if we want to pass the matrix saved above to our python program using command line like this
```
python example.py rus-eng.tsv
```
we have to write something like this:

##### example.py

```
import sys

with open(sys.argv[1], 'r') as f:
    print(f.read())
```

### Unigram language model

I took several sentences from [here](https://github.com/UniversalDependencies/UD_Russian-SynTagRus/blob/master/ru_syntagrus-ud-dev.conllu) as a corpus.
The implementation of unigram model is ``train.py``, the corpus is ``sent.txt``, the output is ``output.conllu``
```
python train.py sent.txt > output.conllu
```

### Questions
> What might be a simple improvement to the language model for languages with orthographic case ?

First of all, putting everything to lower case would help greatly, and lemmatization is also a good idea.