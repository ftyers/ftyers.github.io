Practical 3. Response.

In this practical I implement a unigram language model which can be trained on any given coprora in conllu format. 

To train model use:

python3 train.py {some_corpus}.conllu 

Output of model:

semen@semen-Aspire-V3-571:~/Files/Git/ftyers.github.io/2018-komp-ling/practicals/Practical3$ head -n 15 model.result 
# P      Count      tag     form
0.09365970902334461	10989	ADJ	-
0.09815135218062031	11516	ADP	-
0.049834226832240966	5847	ADV	-
0.007576984377263933	889	AUX	-
0.03542176273555558	4156	CCONJ	-
0.023480980831678443	2755	DET	-
9.375346248583044e-05	11	INTJ	-
0.24419367760741165	28651	NOUN	-
0.022935506140851793	2691	NUM	-
0.029617571103478253	3475	PART	-
0.04280271714580368	5022	PRON	-
0.040518541877967086	4754	PROPN	-
0.18227377715654272	21386	PUNCT	-
0.017455190106452793	2048	SCONJ	-


Train corpus was download from universal dependacies site, using this simple command:

wget https://raw.githubusercontent.com/UniversalDependencies/UD_Russian-SynTagRus/master/ru_syntagrus-ud-test.conllu

What might be a simple improvement to the language model for languages with orthographic case?

Russian,like many languages with with orthographic case, has a nice property which can help to improve this unigram model. We can use stemming and the quality will be increased. Simple stemming in this case is to delete some final characters(1 or 2)


.    
