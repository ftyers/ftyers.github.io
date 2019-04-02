### Install udpipe and train a parsing model
```
$ cat pushkin.txt | udpipe ru_syntagrus-ud.udpipe --tokenize --tag --parse > pushkin.conllu  
# text = Однажды Пушкин написал письмо Рабиндранату Тагору.
1	Однажды	однажды	ADV	_	Degree=Pos	3	advmod	_	_
2	Пушкин	Пушкин	PROPN	_	Animacy=Anim|Case=Nom|Gender=Masc|Number=Sing	3	nsubj	_	_
3	написал	писать	VERB	_	Aspect=Perf|Gender=Masc|Mood=Ind|Number=Sing|Tense=Past|VerbForm=Fin|Voice=Act	0	root	_	_
4	письмо	письмо	NOUN	_	Animacy=Inan|Case=Acc|Gender=Neut|Number=Sing	3	obj	_	_
5	Рабиндранату	Рабиндранат	PROPN	_	Animacy=Anim|Case=Dat|Gender=Masc|Number=Sing	4	appos	_	_
6	Тагору	Тагор	PROPN	_	Animacy=Anim|Case=Dat|Gender=Masc|Number=Sing	5	flat:name	_	SpaceAfter=No
7	.	.	PUNCT	_	_	6	punct	_	SpacesAfter=\n
```