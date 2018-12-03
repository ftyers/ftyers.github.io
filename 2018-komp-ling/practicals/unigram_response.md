# 1. Palindrome

You can find it in the file palindrome.py

# 2.  Matrices

see the file matrix.py

Why do we need end='' passed to the print() statement ? What would happen if we didn't have it?
- Because otherwise we would start with a new line every time.

# 3. Passing argument 

I get the list of 4 arguments: ['args.py', 'a', 'b', 'c']

# 4. Unigram language model

Actually I created 3 arguments: you have to specify both input and output files in terminal like this:
```bash
$ python3 train.py text.txt results.txt 
```

The result looks kind of like this:

```bash
0.186	89	PUNCT	-
0.021	10	SCONJ	-
0.23	110	NOUN	-
0.081	39	ADJ	-
0.04	19	ADV	-
0.125	60	ADP	-
0.081	39	PROPN	-
0.102	49	VERB	-
0.048	23	PRON	-
0.01	5	PART	-
0.025	12	DET	-
0.019	9	CCONJ	-
0.015	7	NUM	-
0.01	5	X	-
0.004	2	AUX	-
0.002	1	SYM	-
1.0	8	PUNCT	«
1.0	1	SCONJ	если
1.0	1	NOUN	передача
1.0	1	ADJ	цифровых
1.0	1	NOUN	технологий
1.0	2	ADV	сегодня
1.0	22	ADP	в
1.0	3	PROPN	сша
1.0	1	VERB	происходит
1.0	1	ADV	впервые
1.0	37	PUNCT	,
0.33	3	SCONJ	то
1.0	3	ADP	о
```
I didn't quite understand about 'orthographic case'. If you mean upper and lower case, I lowercased everything in train.py.
If you mean cases of Russian nouns, then you have to lemmatize the text.

 