Files description:
1. ru_syntagrus-ud-test.conllu - train corpus for unigram language model
2. test_text.txt - test corpus to evaluate language model
3. unigram_model.conllu  - language model results
4. train.py - script to train LM
5. segmenter.py - sentences parser
6. tokenazer.py - word parser
7. tagger.py - PoS tagge
8. result.txt - output after models applying 
9. true_tagged_sent.conllu - true tagged sentences from ud corpus
10. eval.py - extractor for true tagged sentences from ud corpus 

I use a command:
$cat test_text.txt | python3 segmenter.py | python3 tokenizer.py | python3 tagger.py unigram_model.conllu > result.conllu

After using of scripts I tried to compare the results with 'diff' and the output was like this:

(command: $diff -y -W 120 result.conllu true_tagged_sent.conllu )


0	В	-	PROPN	-	-	-	   |	1	В	-	ADP	-	-	-
1	Ереванской	-	PROPN	-	-	   |	2	Ереванской	-	PROPN	-	-
2	губернии	-	NOUN	-	-	   |	3	губернии	-	NOUN	-	-
3	росло	-	VERB	-	-	-	   |	4	росло	-	VERB	-	-	-
4	число	-	NOUN	-	-	-	   |	5	число	-	NOUN	-	-	-
5	жителей	-	NOUN	-	-	-	   |	6	жителей	-	NOUN	-	-	-
6	и	-	PART	-	-	-	   |	7	и	-	CCONJ	-	-	-
7	по	-	ADP	-	-	-	   |	8	по	-	ADP	-	-	-
8	данным	-	NOUN	-	-	-	   |	9	данным	-	NOUN	-	-	-
9	переписи	-	NOUN	-	-	   |	10	переписи	-	NOUN	-	-
10	1897	-	NUM	-	-	-	   |	11	1897	-	NUM	-	-	-
11	года	-	NOUN	-	-	-	   |	12	года	-	NOUN	-	-	-
12	здесь	-	ADV	-	-	-	   |	13	здесь	-	ADV	-	-	-
13	проживало	-	VERB	-	-	   |	14	проживало	-	VERB	-	-
14	830	-	NUM	-	-	-	   |	15	830	-	NUM	-	-	-
15	тысяч	-	NOUN	-	-	-	   |	16	тысяч	-	NOUN	-	-	-
16	человек	-	NOUN	-	-	-	   |	17	человек	-	NOUN	-	-	-
17	.	-	PUNCT	-	-	-	   |	18	.	-	PUNCT	-	-	

So we can see that model works good with sentences on which it was trained :) 
But often it tagged prepositions (like 'B' in this case) like 'PROPN'.
