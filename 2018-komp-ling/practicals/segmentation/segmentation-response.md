Mikhailov Vladislav
MKL181

**Report on Segmentation**

**Data**
For the data, I chose the English language and downloaded enwiki-20180801-pages-articles1.xml-p10p30302.bz2 (approx. 165M, the Internet in the uni is too slow). The text was extracted with the help of WikiExtractor according to the instructions given.

To set the text for segmentation, I used the following sequence of commands:
```
$ head -n 50 wiki.txt > first_wiki.txt # to find the first 50 paragraphs and write the result into a new text file

$ sort -R first_wiki.txt >  wiki_sorted.txt # to randomise the 50 paragraphs and write the result into a new text file
```

**Segmenters**

For the text segmentation, I used the suggested segmenters (pragmatic segmenter and NLTK's Punkt). I also created a new text file 'tagged.txt', containing the 50 paragraphs segmented by myself.

## Pragmatic segmenter
**A brief description** 
Pragmatic Segmenter is a rule-based sentence boundary detection gem that works out-of-the-box across many languages.

*Segmentation:*
```
$ ruby -I . segmenter.rb < wiki_sorted.txt > ruby_segmented.txt # to segment the text and write the result into a new file
```

**Qualitative evaluation**
To perform qualitative evaluation, I used the command:
```
$ diff -u ruby_segmented.txt tagged.txt
```
`--- ruby_segmented.txt	2018-11-01 11:27:45.606089370 +0300`
`+++ tagged.txt	2018-11-01 13:52:02.478371400 +0300`

There is no output followed. I checked all the sentences once again by myself and didn't find any mistakes. 

**Quantitative evaluation**
To perform quantitative evaluation, I wrote a little program in python that counts sentences in a text file containing segmented sentences:
```
def sentence_counter(filename):
    with open(filename, 'r') as f:
        text = f.read().split('\n')
        print(len(text))
```

`sentence_counter('tagged.txt') = 198`
`sentence_counter('ruby_segmented.txt') = 198`

On having counted and checked all the sentences by myself, I didn't find any quantitative/qualitative mistakes in the texts. Pragmatic segmenter seems to perform really good on the English language data given for segmentation.

## Punkt Sentence Tokenizer
**A brief description**

This tokenizer divides a text into a list of sentences, by using an unsupervised algorithm to build a model for abbreviation words, collocations, and words that start sentences. sent_tokenize uses an instance of PunktSentenceTokenizer from the nltk. tokenize.punkt module. This instance has already been trained on and works well for many European languages. So it knows what punctuation and characters mark the end of a sentence and the beginning of a new sentence.

*Segmentation:*
To perform segmentation in the terminal, I wrote a little program in python for segmentation from standard input in a text with the help of the sent_tokenize() function.
```
import sys
from nltk import sent_tokenize


for line in sys.stdin:
	for sentence in sent_tokenize(line):
		print(sentence, sep='\n')
```
```

$ python3 nltk_segmenter.py < wiki_random.txt > nltk_segmented.txt #to segment the text and write the result into a new file
```

**Qualitative evaluation**
To perform qualitative evaluation, I used the command:
```
$ diff -u nltk_segmented.txt tagged.txt
```
`--- nltk_segmented.txt	2018-11-01 13:23:12.350287220 +0300`
`+++ tagged.txt	2018-11-01 13:52:02.478371400 +0300`

The output:
@@ -1,11 +1,9 @@
-The French Pierre-Joseph Proudhon is regarded as the first self-proclaimed anarchist, a label he adopted in his groundbreaking work "What is Property?
-", published in 1840.
+The French Pierre-Joseph Proudhon is regarded as the first self-proclaimed anarchist, a label he adopted in his groundbreaking work "What is Property?", published in 1840.
-In "What is Property?
-", Proudhon answers with the famous accusation "Property is theft".
+In "What is Property?", Proudhon answers with the famous accusation "Property is theft".

*Punkt perceived the question mark in the title of the work as a sentence boundary marker and segmented one sentence into two.*

@@ -19,8 +17,7 @@
-Zhuangzi wrote: "A petty thief is put in jail.
-A great becomes a ruler of a Nation".
+Zhuangzi wrote: "A petty thief is put in jail. A great becomes a ruler of a Nation".

@@ -64,8 +55,7 @@
-Illegalism as a practice emerged and within it "he acts of the anarchist bombers and assassins ("propaganda by the deed") and the anarchist burglars ("individual reappropriation") expressed their desperation and their personal, violent rejection of an intolerable society.
-Moreover, they were clearly meant to be exemplary invitations to revolt".
+Illegalism as a practice emerged and within it "he acts of the anarchist bombers and assassins ("propaganda by the deed") and the anarchist burglars ("individual reappropriation") expressed their desperation and their personal, violent rejection of an intolerable society. Moreover, they were clearly meant to be exemplary invitations to revolt".

@@ -105,8 +95,7 @@
-However, Most himself once boasted that "the existing system will be quickest and most radically overthrown by the annihilation of its exponents.
-Therefore, massacres of the enemies of the people must be set in motion".
+However, Most himself once boasted that "the existing system will be quickest and most radically overthrown by the annihilation of its exponents. Therefore, massacres of the enemies of the people must be set in motion".

*In the three sentences with quotations, Punkt perceived the period marker '.' within the quotation as a sentence boundary marker and segmented one sentence (the quotation) into two separate ones.*

@@ -30,11 +27,7 @@
-According to Noam Chomsky, "the communists were mainly responsible for the destruction of the Spanish anarchists.
-Not just in Catalonia—the communist armies mainly destroyed the collectives elsewhere.
-The communists basically acted as the police force of the security system of the Republic and were very much opposed to the anarchists, partially because Stalin still hoped at that time to have some kind of pact with Western countries against Adolf Hitler.
-That failed and Stalin withdrew the support to the Republic.
-They even withdrew the Spanish gold reserves".
+According to Noam Chomsky, "the communists were mainly responsible for the destruction of the Spanish anarchists. Not just in Catalonia—the communist armies mainly destroyed the collectives elsewhere. The communists basically acted as the police force of the security system of the Republic and were very much opposed to the anarchists, partially because Stalin still hoped at that time to have some kind of pact with Western countries against Adolf Hitler. That failed and Stalin withdrew the support to the Republic. They even withdrew the Spanish gold reserves".

*In the sentence with a quotation, Punkt perceived the period marker '.' within the quotation as a sentence boundary marker and segmented one sentence (the quotation) into five separate ones.*

@@ -54,9 +47,7 @@
-In Latin America in particular, "anarchists quickly became active in organising craft and industrial workers throughout South and Central America, and until the early 1920s most of the trade unions in Mexico, Brazil, Peru, Chile, and Argentina were anarcho-syndicalist in general outlook; the prestige of the Spanish C.N.T.
-as a revolutionary organisation was undoubtedly to a great extent responsible for this situation.
-The largest and most militant of these organisations was the Federación Obrera Regional Argentina [...] it grew quickly to a membership of nearly a quarter of a million, which dwarfed the rival socialdemocratic unions".
+In Latin America in particular, "anarchists quickly became active in organising craft and industrial workers throughout South and Central America, and until the early 1920s most of the trade unions in Mexico, Brazil, Peru, Chile, and Argentina were anarcho-syndicalist in general outlook; the prestige of the Spanish C.N.T. as a revolutionary organisation was undoubtedly to a great extent responsible for this situation. The largest and most militant of these organisations was the Federación Obrera Regional Argentina [...] it grew quickly to a membership of nearly a quarter of a million, which dwarfed the rival socialdemocratic unions".

*In the sentence with a quotation and an abbreviation with the period marker '.', Punkt perceived the period marker '.' as the sentence boundary marker ('C.N.T.'), having segmented the sentence within a quotation into two. In the same manner, Punkt segmented the sentence within a quotation into two separate ones ('The largest and most...').*

@@ -117,10 +106,7 @@
-Anarchist historian George Woodcock reports: "The annual Congress of the International had not taken place in 1870 owing to the outbreak of the Paris Commune, and in 1871 the General Council called only a special conference in London.
-One delegate was able to attend from Spain and none from Italy, while a technical excuse – that they had split away from the Fédération Romande – was used to avoid inviting Bakunin's Swiss supporters.
-Thus only a tiny minority of anarchists was present, and the General Council's resolutions passed almost unanimously.
-Most of them were clearly directed against Bakunin and his followers".
+Anarchist historian George Woodcock reports: "The annual Congress of the International had not taken place in 1870 owing to the outbreak of the Paris Commune, and in 1871 the General Council called only a special conference in London. One delegate was able to attend from Spain and none from Italy, while a technical excuse – that they had split away from the Fédération Romande – was used to avoid inviting Bakunin's Swiss supporters. Thus only a tiny minority of anarchists was present, and the General Council's resolutions passed almost unanimously. Most of them were clearly directed against Bakunin and his followers".

*In the sentence with a quotation, Punkt perceived the period marker '.' within the quotation as a sentence boundary marker and segmented one sentence (the quotation) into four separate ones.*

@@ -206,12 +192,7 @@
-The word "" is composed from the word "anarchy" and the suffix -ism, themselves derived respectively from the Greek , i.e.
-"anarchy" (from , "anarchos", meaning "one without rulers"; from the privative prefix ἀν- ("an-", i.e.
-"without") and , "archos", i.e.
-"leader", "ruler"; (cf.
-"archon" or , "arkhē", i.e.
-"authority", "sovereignty", "realm", "magistracy")) and the suffix or ("-ismos", "-isma", from the verbal infinitive suffix , "-izein").
+The word "" is composed from the word "anarchy" and the suffix -ism, themselves derived respectively from the Greek , i.e. "anarchy" (from , "anarchos", meaning "one without rulers"; from the privative prefix ἀν- ("an-", i.e. "without") and , "archos", i.e. "leader", "ruler"; (cf. "archon" or , "arkhē", i.e. "authority", "sovereignty", "realm", "magistracy")) and the suffix or ("-ismos", "-isma", from the verbal infinitive suffix , "-izein").

*In the sentence with plenty of abbreviations with the period marker '.', Punkt perceived the period marker '.' at the end of each abbreviation as the sentence boundary marker, having segmented one sentence into five separate ones.*

All in all, there are 19 incorrectly segmented sentences.
Let's check the result on the quantitative evaluation.

**Quantitative evaluation**
I performed the  quantitative evaluation with the sentence_counter() function (the above mentioned one).

'sentence_counter('tagged.txt') = 198'
'sentence_counter('nltk_segmented.txt') = 217'

217 - 198 = 19 sentences (mistakes in the nltk_segmented.txt file)
19 (qual) = 19 (quan).

Thus, the results of counting the mistakes by myself and with the help of the written function are of the same. The common mistakes occur in the following context: sentences within a quotation, abbreviations with the period marker '.'.

