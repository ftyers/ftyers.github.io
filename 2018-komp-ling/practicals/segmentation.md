## Segmentation

##### Pragmatic Segmenter
Pragmatic Segmenter is a rule-based sentence boundary detection gem that works out-of-the-box across many languages. Default language is English, other languages should be specified but no training data is required.
Supports Ruby 2.1.5 and above. Full description could be found [here](https://github.com/diasks2/pragmatic_segmenter/blob/master/README.md)

##### NLTK's Punkt
This tokenizer uses an unsupervised algorithm to build a model for abbreviation words, collocations, and words that start sentences. It has already been trained on and works well for many European languages. So it knows what punctuation and characters mark the end of a sentence and the beginning of a new sentence. 

##### Quantitative evaluation: Accuracy percentage (how many sentence boundaries were detected correctly)
 My dataset is made of 50 random paragraphs from a Wikipedia dump of Russian language. This data has some pecularities:
> - Some features have link to their own wiki page but this page doesn't exists. In the dump this causes deletion of the feature and appearance of ungrammatical sentence 
> *— младший и любимый сын Дегина Содо Заби, военачальник Зиона, друг и бывший одноклассник по академии Чара Азнабля (хотя сам Чар о нём невысокого мнения).*
> - Some paragraphs, which maybe headings, looks like "Some string:". Colon usualy is not sentences separation mark. 
> *Чемпионат Шотландии по футболу 1992/1993:*

So it could be hard to distinguish segmenter's mistakes and data distortions. The easiest way to evaluate accuracy is to look through the source document and count the number of sentences N. Then count the number of sentences which were found by segmentators - S for Pragmatic Segmenter and P for Punkt and count accurancy for number of sentences. Such a calculation does not take into account the quality of segmented sentences.
N = 122
S = 128
P = 134
Accuracy for Pragmatic Segmanter = -5%
Accuracy for Punkt Segmanter = - 10%
##### Qualitative evaluation: What kind of mistakes does each segmenter make?
###### Pragmatic segmenter
> - Dot in the beginning of the sentence. 
> *. Руководство страны высоко оценило труды сотрудников завода — в соответствии с указами Президиума Верховного Совета СССР от 5 июня 1942 года и от 20 января 1943 года за образцовое выполнение заданий правительства завод № 76 НКТП СССР был награждён орденами Ленина и Трудового Красного Знамени.*

> - Dot in abbreviated name is interpreted like sentences separator 
> 1.*Комиссия Государственного комитета обороны под председательством Маршала Советского Союза К. Е.* 2. *␣Ворошилова подтвердила, что дивизия стала сплочённым боевым коллективом, готовым к боям.* 
> (But if name doesn't have abbreviated patronym it is interpreted correctly: *Рецензент DVDTalk.com Д. Уоллис пишет, что отрицательные персонажи — герцогство Зион — не классические хихикающие злодеи, они лишь отказались склониться перед правительством, которое не признают, однако, постепенно Зион отходит от своей культуры и превращается в фашистскую нацию.*)
###### Punkt
> - Dot is interpreted like a separate sentence 
> 1. *.* 
> 2. *Руководство страны высоко оценило труды сотрудников завода — в соответствии с указами Президиума Верховного Совета СССР от 5 июня 1942 года и от 20 января 1943 года за образцовое выполнение заданий правительства завод № 76 НКТП СССР был награждён орденами Ленина и Трудового Красного Знамени.*
> - Wrongly interpreted dot before quotes 
> 1. *Улица Казарцева (укр.* 
> 2. *"Вулиця Казарцева")— улица на Микрорайоне Мелитополя, соединяет улицу Гризодубовой и бульвар 30-летия Победы.*





