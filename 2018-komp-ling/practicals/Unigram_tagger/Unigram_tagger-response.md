## Regular expressions  

Input:  

    import re

    s = 'Привет мир!'

    print(re.search(r'м[а-я]+', s))

    m = re.search(r'м[а-я]+', s)
    
    print(m.group())
    print(m.span())

    print(re.sub('[а-я]', 'x', s))

What we get:  

    <re.Match object; span=(7, 10), match='мир'>
    мир
    (7, 10)
    Пxxxxx xxx!
    
## Libraries and modules in Python  

    %matplotlib inline

    import sys
    import matplotlib.pyplot as plt

    x = []
    y = []

    fd = open('/Users/dariabakshandaeva/Desktop/ranks.txt', 'r')
    for line in fd.readlines():
        line = line.strip()
        if line == '':
                continue
	
        row = line.split('\t')
        x.append(int(row[0]))
        y.append(int(row[1]))

    plt.plot(x, y, 'ro')
    plt.show()
    
![](https://i.imgur.com/T35PFKW.png)

## ElementTree  

    import xml.etree.ElementTree as ET

    tree = ET.parse('isl-ex.xml')
    root = tree.getroot()

    print(root.tag)
    >> xigt-corpus

    for tier in root.findall('.//tier'):
        if tier.attrib['id'] == 'n':
                for item in tier.findall('.//item'):
                        print(item.text)
                        
Output:  

    (Þau) Jón og María eru vinir.
    they.NEUT Jón og María are friends
    Jón and María are friends.
    
How would you get just the Icelandic line and the gloss line ?  

    for tier in root.findall('.//tier'):
        if tier.attrib['id'] == 'n':
                for item in tier.findall('.//item'):
                    if item.attrib['tag'] != "T":
                        print(item.text)
                        
Output:  

    (Þau) Jón og María eru vinir.
    they.NEUT Jón og María are friends
    
## scikit learn  

With the help of `train_test_split` in `pronunciation.py` we can split the data in two randomly and train on one half and test on the other half:  

    words_train, words_test, data_train, data_test, labels_train, labels_test = train_test_split(words, data, labels, test_size=0.5)

What kind of accuracy do you get ?  

`0.9946236559139785`

What kind of errors does the classifier make ? How do you think you might be able to improve on the accuracy ?  

    - 0 ('#морковь#', '[mɐrˈkofʲ]', 1)
    - 0 ('#явь#', '[jæfʲ]', 1)
    - 0 ('#хоругвь#', '[xɐˈrukfʲ]', 1) 
    - 0 ('#нелюбовь#', '[nʲɪlʲʊˈbofʲ]', 1)
    - 0 ('#кровь#', '[krofʲ]', 1)

All these words have 'ь' after 'в' and have in fact label '/f/', but their feature vector is just like the vector for these words:  

    #бивень#	[ˈbʲivʲɪnʲ]	1,0,0,0,0,0,0,0
    #щавель#	[ɕːɪˈvʲelʲ]	1,0,0,0,0,0,0,0
    #благословение#	[bləɡəslɐˈvʲenʲɪje]	1,0,0,0,0,0,0,0
(btw, it's rather strange, because in aforementioned words the next character after 'в' is vowel, not consonant)
And we want words like 'морковь', 'явь' to have a feature vector that is similar to the vector of  

    #анклав# [ɐnˈklaf]	1,0,0,0,0,0,0,1
    
Actually we can omit the fact that there is a character 'ь' after 'в' - and change the last component of the feature vector to '1' (#), because 'ь' only has an impact on the softness of sound, but does't affect its type (in this case, voiceless sound at the end of the word).  

## Screenscraping  

I leave the second problem (dealing with the окончание) as an exercise for the reader.  

In `wiktionary.py`:  

    if text.count('Корень:') > 0:
        stem = text.split(':')[1].split(';')[0]
    if text.count('тип склонения') > 0:
        zkod = text.split('тип склонения')[1].split(' ')[1]    
    if text.count('МФА') > 0:
        ipa = text.split('&#91;')[1].split('&#93')[0]
        
Output:  

    -дерев-	 1a^	ˈdʲerʲɪvə
    -страх-.  3a	strax
    
## Unigram tagger  

`tagger.py` is the script that takes unigram language model, conllu file without tags and the name of the output file - and returns this output file with tags.  

`en_gum_w_tags.conllu`

    # newdoc id = GUM_academic_discrimination
    # sent_id = GUM_academic_discrimination-1
    # text = The prevalence of discrimination across         racial groups in contemporary America:
    # s_type=frag
    1	The	the	DET	_	_	_	_	_	_
    2	prevalence	prevalence	NOUN	_	_	_	_	    _	_
    3	of	of	ADP	_	_	_	_	_	_
    4	discrimination	discrimination	NOUN	_	_	    _	_	_	_
    5	across	across	ADP	_	_	_	_	_	_
    6	racial	racial	ADJ	_	_	_	_	_	_
    7	groups	group	NOUN	_	_	_	_	_	_
    8	in	in	ADP	_	_	_	_	_	_
    9	contemporary	contemporary	ADJ	_	_	_	    _	_	_
    10	America	America	PROPN	_	_	_	_	_	        SpaceAfter=No
    11	:	:	PUNCT	_	_	_	_	_	_
    
    
How accurate is the tagger ?  

With the help of `eval.py` we can find out that its accuracy is `0.9392165691130122`  

How could you improve performance without incorporating context  

Well, it's hard to say how can we define the POS of, for instance, word 'much' correctrly without the context: it's better to know al least the POS of the next word. Maybe in some contexts it would be useful to use stemming/lemmatization.  

Could you store other single-word features in your unigram model ? Which features might you like to store ?  

Stem, zkod, pronunciation (ipa) and so on.   

