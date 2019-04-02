## Unigram part-of-speech tagger

##### Dict question
```
print('\t' + '\t'.join(eng))
for w1 in m:
        print('%s\t' % (w1), end='')
        for w2 in m[w1]:
                print('%d\t' % (m[w1][w2]), end='')
        print('')
```
We need ```end=''``` passed to the ```print()``` statement because by default ```end = '\n'``` and the result of using this meaning will look like
```
	a	absorbed	all	and	another
бы	
0	
0	
0	
0	
0	
```
##### sys.argv question
['args.py', 'a', 'b', 'c']
##### Unigram Language Model
```
[$ python3 train.py ohenry_sobolya.conllu table
```
Script ```train.py``` takes file in conllu format and writes the result in file the name of which is specified on the command line (*table* in the example).
The head of the result (Markdown makes something strange with intervals, all columns are tab separated):
```
# P	count	tag	form
0.04	107	PROPN	-
0.20	524	NOUN	-
0.21	558	PUNCT	-
0.02	51	SCONJ	-
0.08	218	ADJ	-
0.13	353	VERB	-
0.08	218	ADP	-
0.01	35	NUM	-
0.09	233	PRON	-
0.01	15	AUX	-
0.03	85	CCONJ	-
0.03	67	DET	-
0.04	109	ADV	-
0.03	72	PART	-
0.00	4	INTJ	-
0.50	1	PROPN	Русские
0.50	1	ADJ	Русские
1.00	9	NOUN	соболя
1.00	157	PUNCT	.
```

If we save case and sort the result by the number of word, the first rows will be
```
1.00	241	PUNCT	,
1.00	157	PUNCT	.
1.00	108	PUNCT	—
0.95	56	CCONJ	и
1.00	39	ADP	в
1.00	37	ADP	с
1.00	31	PART	не
1.00	30	ADP	на
0.97	28	PROPN	Молли
1.00	27	PROPN	Малыш
1.00	19	PUNCT	!
1.00	19	PRON	он
1.00	18	ADP	к
1.00	16	PUNCT	?
1.00	16	PRON	Я
1.00	16	PRON	я
1.00	15	VERB	сказал
1.00	15	SCONJ	как
1.00	14	ADP	за 
0.78	14	SCONJ	что
```
If we use lowercased tokens, the result will change, especially for pronoun *Я*:
```
1.00	241	PUNCT	,
1.00	157	PUNCT	.
1.00	108	PUNCT	—
0.95	57	CCONJ	и
1.00	39	ADP	в
1.00	38	ADP	с
1.00	35	ADP	на
1.00	34	PART	не
1.00	32	PRON	я
0.97	28	PROPN	молли
1.00	27	PROPN	малыш
1.00	22	PRON	он
1.00	20	ADP	к
1.00	19	PUNCT	!
1.00	18	PRON	ты
1.00	16	PUNCT	?
1.00	16	PRON	это
1.00	15	VERB	сказал
1.00	15	SCONJ	как
1.00	15	ADP	за
```
Using one case allows to calculate high frequency tokens, but if the pos-tagger didn't catch proper nouns separately, this aproach may lead to loosing information about them.
