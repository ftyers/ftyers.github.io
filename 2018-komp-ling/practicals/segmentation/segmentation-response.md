# 1. Segmentation

## 1.0 Paragraph extraction   
I have extracted 50 paragraphs of Ukrainian text at random from a Wikipedia dump, using WikiExtractor and a command: 
```
sed 5000q < wiki.txt | sort -R | sed 50q > wiki1.txt
```
in Linux Terminal.  
## 1.1 Chosen Segmenters	
To compare segmenters, I have chosen a Pragmatic Segmenter (1), NLTK’s function sent_tokenize() from nltk.tokenize (3) and NLTK’s Punkt. 

1. Pragmatic Segmenter is a rule-based sentence boundary detection gem that works across many languages. It returns a copy of text, divided into sentences, 1 per line. 
 
2. A function sent_tokenize() from the module nltk.tokenize returns a tokenized copy of text, using NLTK PunktSentenceTokenizer for the specified language.
3. NLTK’s Punkt - Punkt Sentence Tokenizer - divides a text into a list of sentences, by using an unsupervised algorithm to build a model for abbreviation words, collocations, and words that start sentences. It must be trained on a large collection of plaintext in the target language before it can be used.
I have found pre-segmented Ukrainian Wikipedia corpus at http://lang.org.ua/en/corpora/ and learned the model on 100 000 sentences, using a command 
```
sed 100000q < file1 > file2
```
on Mac OS Terminal to cut the corpus file. You can see my code in Punkt.py.  

## 1.2 Evaluation

I manually segmented the 50 Ukrainian paragraphs in the file. The command on Linux Terminal

```
>>> sed -n '$=' wiki_manually_segmented.txt
117
```
shows, that there are 117 sentences in total.

### 1.2.1 Pragmatic Segmenter

To know the correct number of sentences detected by Pragmatic Segmenter, I have used the following commands:
```
>>> comm -12 <(sort wiki_manually_segmented.txt) <(sort segmented_wiki1.txt) > segmenter1results.txt
>>> sed -n '$=' segmenter1results.txt
108 segmenter1results.txt
>>> 108*100/117
92.3076923076923
```
So, 108 sentences (=92,3%) were detected correctly by the Pragmatic Segmenter.

For the qualitative evaluation I used the <diff> command. Pragmatic Segmenter didn’t see the name abbreviation:

> На 1950-ті роки припадає величезна робота з редагування та підготовки до друку творів М.
> Лисенка, яку було успішно виконано.

The correct sentence: 
> На 1950-ті роки припадає величезна робота з редагування та підготовки до друку творів М.Лисенка, яку було успішно виконано.

> Т.
>  Г.
>  Шевченко називав археологію «матір'ю історії»

The correct sentence: 
> Т.Г.Шевченко називав археологію «матір'ю історії»

It didn’t detect the abbreviation of ‘century’ ("ст".) as well:

> Одними з перших археологічних розкопок в Україні можна вважати розкопки Десятинної церкви в Києві (зруйнована татаро-монголами 1240), що були здійснені Петром Могилою в 30-х роках 17 ст.
> з метою будівництва на її місці нової церкви під тією ж назвою.

The correct sentence:
> Одними з перших археологічних розкопок в Україні можна вважати розкопки Десятинної церкви в Києві (зруйнована татаро-монголами 1240), що були здійснені Петром Могилою в 30-х роках 17 ст. з метою будівництва на її місці нової церкви під тією ж назвою.

### 1.2.2 A function sent_tokenize() 

For the quantitative evaluation of the NLTK tokenizer I have used the same <comm> command, as for the Pragmatic Segmenter. As a result, sent_tokenize() detected 107 (=91.5%) sentences correctly. 

However, when I used the <diff> command and looked into the segmented text file, I saw, that the <comm> command regards the sentences with inserted spaces, but with the same boundaries, as different sentences. (The deal is that sent_tokenize() insert additional spaces after name abbreviations).  It means, that sent_tokenize() works much better, than 91,5%. (I wonder, whether there are commands in Linux Terminal, which look only at sentence boundaries, but not inside sentences, and be grateful for the answer.)

If we look at the differences between a manually segmented text and the nltk-segmented text, we can see, that only 6 sentences were detected incorrectly. Thus, the accuracy rate is actually not 91,5%, but 94,9% (=111 correctly detected sentences), and, thus, it works better with Ukrainian texts, than Pragmatic Segmenter.   

As for qualitative evaluation, the sent_tokenize() function can deal with name abbreviation in comparison with the first parser, but still doesn’t see the ‘century’ abbreviation, as well as the Pragmatic Segmenter:

> Проза Франка початку ХХ ст.
> виявляє потужну тенденцію до пошуку новітніх художньо-естетичних засобів та форм моделювання художньої дійсності; тенденцію, що бере свій початок наприкінці попереднього століття, все більше вияскравлюючись та міцніючи.

The correct sentence: 
> Проза Франка початку ХХ ст. виявляє потужну тенденцію до пошуку новітніх художньо-естетичних засобів та форм моделювання художньої дійсності; тенденцію, що бере свій початок наприкінці попереднього століття, все більше вияскравлюючись та міцніючи.

Also the sent_tokenize() function didn’t recognize the abbreviation ‘англ.’ (English) and couldn’t parse the long composite sentence correctly, especially having trouble with ‘!’and parenthesis:

> Слухаючи доповіді Міріама (З. Пшесмицького), полемізуючи з «Молодою Музою», читаючи твори молодших письменників (В. Винниченка, В. Стефаника, Марка Черемшини, Л. Мартовича та ін.)
> і захоплюючись ними, Франко у своєму творчому єстві відчуває напругу між старим і новим у літературі (його «Хлопська комісія» стара у порівнянні зі «Злодієм» В.
> Стефаника!
> ), прагне «йти за віком», встигати за молодшими, «модернішими» письменниками, тому шукає нових способів «оброблювання» тем і сюжетів, прагне заглянути в «сутінки» людської душі, в оту «нижню свідомість», яка, виявляється, є значно глибшою, багатшою на збережені враження, ніж свідомість «верхня» (власне свідомість). 

---  all of this text must be recognized as one sentence. 

### 1.2.3 NLTK’s Punkt

NLTK's Punkt, trained on 100 000 Ukrainian sentence Wikipedia corpus, divided the paragraphs into 121 sentence. Only 95 (=81,2%) sentences were detected correctly. The errors of Punkt include the previous ones of other segmenters and some others (including unsolving anbiguity when there are no full stops between sentences etc.). 

# 2. Tokenization
### 2.1 Creating a dictionary
 I have extracted a dictionary of segmented surface forms from UD_Japanese-GSD/ja_gsd-ud-train.conllu. If order to make the dictionary contain 15,326 forms, I have implemented the following commands:
 ```
>>> sed '/^#/d' ja_gsd-ud-train.conllu > ja_gsd-ud-train.conllu-nocomments
>>> cut -f2 -d'	' ja_gsd-ud-train.conllu-nocomments > ja_gsd-ud-ctrain.conllu-dictionary
>>> wc -l *dictionary
169064 ja_gsd-ud-ctrain.conllu-dictionary
>>> uniq *dictionary > dict
>>> wc -l *dict
150072 dict
>>> sort -u *dictionary > dict
>>> wc -l dict
15327 dict
```
Then the first whitespace in dict file was deleted. 
```
>>> wc -l dict
15326 dict
```

### 2.2 Preparing the test file

First, I extracted the test sentences from test.conllu file:

```
sed -n '/^# text =/p' ja_gsd-ud-test.conllu > test-sentences.txt 	 
```
Then I saved sentences without some unwanted symbols:

```
>>> sed -e 's/^# text = //' test-sentences.txt > sentences.txt
>>> wc -l sentences.txt
557 sentences.txt
```

So I got the file with sentences, one sentence per line. 

### 2.3 Writing a MaxMatch algorithm in Python to tokenize sentences

My code can be seen in a file called maxmatch.py. It uses the dictionary.txt file and the sentences.txt file and outputs the list of strings: 1 string = 1 sentence with tokens divided by MaxMatch by spaces, sentences are separated by blank lines.

The program tells, that there are 18248 tokens in 558 sentences.  

### 2.4 Word Error Rate

I used the test set of test sentences to count the WER of my MaxMatch algorithm. 

At first I got a list of correctly detected tokens:
```
>>> sed '/^#/d' ja_gsd-ud-test.conllu | cut -f2 -d'  ' > correct-tokenization
```
And then l deleted blank lines in the file with MaxMatch-tokenized sentences:
```
>>> sed '/^$/d' tokenized_sentences.txt > tokenized_sentences-nospaces.txt
```
Then I implemented the WER algorithm from https://github.com/zszyellow/WER-in-python and ran it on first 10 sentences from the test set as follows:
```
>>> python2 WER.py wer-test-correct.txt wer-test-maxmatched1.txt
WER: 65.50%
```
I assume that such a high word error rate is a result of the incorrectly extracted dictionary (from the train.conllu file) or due to the unsuitable set of words in a dictionary. 

 
