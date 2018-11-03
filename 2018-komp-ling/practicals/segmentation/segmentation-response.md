# Sentence segmentation

## Data source

As a data source Wikipedia was used, in my case it was Belarusian part of it (175 Mb in archive). Texts were extracted via
```bash
python WikiExtractor.py --infn bewiki-20181001-pages-articles.xml.bz2
```
It seems that it was not a good idea to take texts from Wikipedia dump, because there are a load of pseudosentences (like image captions, titles, technical texts etc.) which don't have normal sentence-alike punctuation (they end with colon, have artifacts of punctuation mark combinations in place of removed HTML markup, whitespaces before marks etc.) or even without any marks, some of them consist of couple of words and so on. So, better way to deal with is not to take sample amount, but iterate over them and get only well-formed and standalone text fragments.

However, I've got 1069927 lines of extracted dump, then I took a sample of 100 items (`randomLines.py`) and then hand-picked only well-formed ones, it was 46 excerpts.

All excerpts were joined into one big text, which was segmented via NLTK, TextBlob, and  Spacy (`sent.py`). None of the segmentators was  trained or customized to deal with the dataset (models or abbreviations dictionary). Then I run the code
Results are like this: NLTK – 122 sentences, TextBlob – 122, Spacy – 165.

## Discussion

As it is stated on the home page of TextBlob, «TextBlob stands on the giant shoulders of NLTK and pattern». So, I guess, it shares code base with NLTK, that's why results are same for both frameworks.  Diff for textblob.txt and nltk.txt  produces empty output. **Nltk** produced mostly reasonable results. It mostly had not cases when sentences remained joint, only one is complex one:
 *Даследуе дзейнасць польскага антысавецкага падполля на Беларусі ў 1940-я г. Флаўэрз узяў узнагароды ад часопіса «NME» як «Найлепш апрануты» і «Самы прывабны».*
First sentence was ended up with abbreviation "г." (year) and second one was started with proper noun.  However, it's systemic issue that it's stumbled in was one of abbreviations with dot it was not aware about (like "тыс.", "т.б.", "стст.", "літ."), so they were treated as normal words and dot as end-of-a-sentence marker. 
 If one provides abbreviation dictionary, the much better results are expected.
 **Spacy** completely mishandled «» and produced some odd splittings, however, it's good that it managed to correctly segment at least some cases (about 10 sentences from the sample). It works on some language-independent pretrained model (with code xx), so it would be miracle if it produced results closer to ideal.
 
 