# Test 1
### Tsvetkova Victoria

###### Question 1:
*Which problems does maxmatch suffer from? (Choose all that apply.)*
a) and d)

###### Question 2:
*Write a perl/sed substitution with regular expressions that adds whitespace for segmentation around "/" in "either/or" expressions but not around fractions "1/2":*

```sh
$ sed -i 's/\([[:alpha:]][[:alpha:]]*\)\/\([[:alpha:]][[:alpha:]]*\)/\1\ \/ \2/g' test.txt
```
###### Question 3:
*the text mentions several times that machine learning techniques produce better segmentation than rule-based systems; what are some downsides of machine learning techniques compared to rule-based?*

1) We need lots of preprocessed data which have to be marked up to build a ML model. It takes some considerable time (though sometiemes rule-based system can take some time too, of course);
2) ML models can skip some cunning and complicated examples as there might be not enough data (meanwhile if we use a rule-based system we can add this as a rule);
3) An ML model is often a black box while rule-based systems are easy to be interpreted;
4) Probably training an ML model takes a lot of time, but I am not sure, I haven't built one yet.

###### Question 4:
*write a sentence (in English or in Russian) which maxmatch segments incorrectly.*

> He hid his wealth under that tree. ->
> Hehidhiswealthunderthattree. ->
> he hid his weal thunder that tree.

###### Question 5:
*what are problems for sentence segmentation? provide one example in English or Russian for each that applies.*

Basically all the answers can become a problem for sentence segmentation. 

a) ambiguous abbrevations with punctuation
One of the segmenters I used (nltk) didn't manage to recognise *m. (= meters)* as an abbrevation and split the sentence. But even if we write a segmenter which will deal with such abbrevations, it can still make mistakes as abbrevations sometimes are cunning. For example, [the dictionary](https://en.oxforddictionaries.com/punctuation/punctuation-in-abbreviations) says that we should put a period if we use only the first part of a word:
> Sun. (for Sunday). 

You can't list all such examples for the rule-based system, so it will keep making mistakes. 
Probably, if we make POS-tagging and provide a dictionary for the system, it will segment sentences correctly. However, it might not help with the example "Sun. for Sunday".

b) sentences containing symbols '!' and '?'
When we try to segment a sentence with direct speech, we can often do it wrong:

> 'Can I come?' he said. > ['Can I come?'], [he said.]
> 'No!' she cried. > ['No!'], [she cried.]

Or probably the last ' mark will go to the second sentence.

c) sentences lacking separating punctuation
When our data is downloaded from the internet, we can get sentences without seperating punctuation. Or it might be a list of something (for example, titles or events). This problem might be solved by adding /n or /t as a segmentation mark.

>  -Type some Markdown on the left
>  -See HTML in the right
>  -Magic

d) sentences not separated by whitespace
Same as for c). 

> Some people might not use whitespace after punctuation marks.It's really strange!But people are strange.