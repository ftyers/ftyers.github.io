# Practical 1
##### Tsvetkova Victoria 

### Segmentation
For this task I chose a wiki file in Hungarian. First I tried both suggested segmenters, and after searched on the Internet for some segmenters written for Hungarian. I found a [page](https://github.com/oroszgy/awesome-hungarian-nlp) with two presented. It took me a long time to try either, and they both didn't work: the first one was too outdated, and the second one required more memory than I have on my ubuntu.
So, now I am going to compare the ones being suggested in the practical:

##### 1. NLTK's Punkt
Used exactly as was said in practical 1. 
Evaluation: 3 wrong out of 116 (~98% accuracy).
In general, the segmenter did great: there were only two difficult cases it couldn't segment correctly:

1) Hungarian abbreviations: "kb." standing for "körülbelül", "about" (compare with Russian "прим." for "примерно", about), and "stb." standing for "és a többi", "etc". 
2) A bit more cunning example:

>'Közepes mélysége kb.\n',
 '2 m; legnagyobb mélysége 10 m, de területének 60 %-án csak max.\n',
 '2 m.\n',

When met two abbreviations and a digital at once ("max.", "m."), the segmenter failed to realise it as the same sentence. That that was also the sentence with "kb." mistake.

##### 2. Pragmatic_segmenter
Also, used as suggested on the practical page.
Evaluation: 4 wrong out of 116 (~98% accuracy).
The first three mistakes are the same as for NLTK's punct: "kb.", "stb." and "max.".
The forth one is quite interesting:
>Újságíróként írt többek között a magyar Kitekintő.\n',
 'hu, Index.hu, Új Szó, illetve a szlovák .\n',
The segmenter failed to recognize a web address Kitekintő.hu, though the next one, Index.hu, wasn't segmented.
