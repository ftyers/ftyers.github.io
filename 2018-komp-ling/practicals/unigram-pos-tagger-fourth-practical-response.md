# Regular expressions
I'm familiar with regular expressions and use them quite often.

# Matplotlib
I implemented some modifications for the code as I had only file with Chuvash word frequencies without indexing. After running I got the following plot: see plot.png

# ElementTree
```python
print(root.tag)
# xigt-corpus
```
After running gloss.py file I got the following output:
```
(Þau) Jón og María eru vinir.
they.NEUT Jón og María are friends
Jón and María are friends.
```

To get just the Icelandic line and the gloss line the code should be the following:
```python
import xml.etree.ElementTree as ET
tree = ET.parse('isl-ex.xml')
root = tree.getroot()

for tier in root.findall('.//tier'):
        if tier.attrib['id'] == 'n':
                for item in tier.findall('.//item')[:2]:
                        print(item.text)
```

# Scikit learn
After running the code I got the following accuracy: 0.9955177050649933, which is really high.

For splitting the data into test and train I use function "train_test_split" from sklearn.model_selection. After splitting and training my perceptron (see file perceptron.py) I get 0.9973118279569892 accuracy which is higher than I had before.
The perceptron got mistakes in the following examples:
```
- 0 ('#церковь#', '[ˈt͡sɛrkəfʲ]', 1)
- 0 ('#бровь#', '[brofʲ]', 1)
- 0 ('#нелюбовь#', '[nʲɪlʲʊˈbofʲ]', 1)
```
There are only 3 mistakes, though when we trained on the whole data, there were 10 mistakes, that's why accuracy is higher with splitting.
It is to mention that the mistakes are the same: the words which end with "вь" are wrongly classified. I think to improve the perceptrom we should add one more feature in the training data: whether the sound is palatalized or not (because in Russian palatalization is crucial for undestanding, for example пыл [pyl] (
eagerness) and пыль [pyl'] (dust) ).

# Screenscraping
After running the code to parse html-page for страх, I got the following output:
```
 -страх-	3a	strax
```
When I ran the same code to parse page for дерево, I got something different:
```
 -дерев-; окончание	1a^	ˈdʲerʲɪvə
```
I modified the code a little bit to remove окончание part and ^ for Zaliznyak code, you can see the code in file wiktionary.py. After modification I got the right output:
```
 -дерев-	1a	ˈdʲerʲɪvə
```

# Unigram tagger

I prepared model.tsv using training_data.conllu (syn_tag rus corpus) and the code from the third practical (train.py). I chose 3 sentences to test my tagger, and I excluded them from training data. I also prepared the test data deleting all the pos tags.
I wrote the tagger in file tagger.py. To run it in Terminal you should write:
```
python3 tagger.py input.conllu model.tsv > output.conllu
```
I put all the files in the folder.

How accurate is the tagger?
I tested it on 3 sentences, there were 50 words (punctuation included) total.
There were 9 mistakes. Calculating accuracy we get 0.82 which is quite good. I counted as mistakes the cases when the tagger got "NOUN" instead of "PROPN" though I believe it is not really crucial - there were 3 such cases out of 9 mistakes. Also 1 word got missing from the output - it might be caused by fact that this word (помещении) was missing in the model. The most crucial mistakes were in defining verb as nouns: открыта, распространялась, оплачена, выпущенную - these are verb forms (short passive forms, participle) - 4 out of 9 mistakes.

How could you improve performance without incorporating context ...
- using Python string functions ?
I used one in my tagger - I lowered my words in the model. It would help to define words which are in the beginning of the sentence and start with capital letter.
- using regular expressions?
Strip some endings which can differentiate similar forms, for example: открыт and открыта - ending "a" gives another form which may not be in the model dictionary.
- using screen scraping ?
In the screenscraping part of this practical I parsed wiktionary - the forms and roots parsed from there can be useful for language model.

Could you store other single-word features in your unigram model ? Which features might you like to store ?
For Russian language besides POS tags the following word features are common: case (for nouns, pronouns and adjectives), singular/plural form (nouns, adjs, verbs, pronouns), tense (for verbs), grammatical gender (for nouns, adj, pronouns, verbs).