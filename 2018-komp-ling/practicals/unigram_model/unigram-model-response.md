
# Unigram model report

## Implementing n dimensional matrices with dict

Script `matrix.py` usage:
```
python matrix.py 
```
Output:
```
{'бы': {'a': 0, 'absorbed': 0, 'all': 0, 'and': 0, 'another': 0}, 'вас': {'a': 0
, 'absorbed': 0, 'all': 0, 'and': 0, 'another': 0}, 'видит': {'a': 0, 'absorbed'
: 0, 'all': 0, 'and': 0, 'another': 0}, 'всего': {'a': 0, 'absorbed': 0, 'all':
0, 'and': 0, 'another': 0}, 'вы': {'a': 0, 'absorbed': 0, 'all': 0, 'and': 0, 'a
nother': 0}}
        a       absorbed        all     and     another
бы      0       0       0       0       0
вас     0       0       0       0       0
видит   0       0       0       0       0
всего   0       0       0       0       0
вы      0       0       0       0       0

```
### Question

Why do we need end='' passed to the print() statement ? What would happen if we didn't have it?

Answer:

We use end='' in order to control the print and keep on the same line: without it the print would begin from a new line.


## Passing arguments from the command line

Script `args.py` usage:
```
python args.py a b c 
```

Output :
```
['args.py', 'a', 'b', 'c']

```


## Unigram language model
For this task unigram model `train.py` was implemented (you can see it in the same folder with this report).

As a test data 10 sentences from SynTagRus (`test.conllu`) were used.

Script usage:
```
python train.py test.conllu > test_output.conllu
```

First 10 output lines as an example (see `test_output.conllu` for the full output):
```
#P	count	tag	form
0.24	47	NOUN	_
0.16	31	PUNCT	_
0.07	13	ADJ	_
0.04	8	PROPN	_
0.02	3	AUX	_
0.13	25	VERB	_
0.13	25	ADP	_
0.07	14	ADV	_
0.04	8	CCONJ	_
0.02	4	PART	_
```

### Question

What might be a simple improvement to the language model for languages with orthographic case?

Answer:

We can use lowercasing for improving the model.
