I ran the suggested segmentors, the "Practical Segmentor" by diasks2, a multi-language out-of-the-box segmentor on Ruby and the NLTK's Punkt.

I first used a part of the wikinews in English as a corpus. I manually split the articles into sentences by "\n" and automatically created the input by concatenacing the lines. Then, I evaluated the accuracy of both segmentors by aligning the expected and real output char-by-char and counting unnecessary or dismissed sentence boundaries as mistakes and divining them into the number of expected boundaries. 

The accuracy of the two segmentors differed drastically as NLTK Punkt performed with the accuracy of 399 / 401 = 99.5% and Ruby with the accuracy of 29/401 = 7,5%.

I am not certain what made the practical segmentor ignore a large amount of sentence boundaries; I would think I ran it wrong if not for the fact that my classmates had a similar experience.

It is thus hard to analyze its mistakes but one obvious occation is when he mistakingly interpreted occasions like: 

```He said: "I haven't submitted the proposal yet." I sighed.```

as:

```
He said: "I haven't submitted the proposal yet.
" I sighed.
```

This counted as a dismissed sentence boundary. 

As for NLTK Punkt, its both mistakes were in the following example:

```
Foreign ministry spokesman Mark Regev has apologized for the incident, saying: "If Egyptians were hit then we regret it.
This was not our intention.
We want good co-operative relations with Egypt ... and if Egyptians were hurt then our thoughts go out to them and their families and the Egyptian people."
```

Here, NLTK interpreted periods inside of reported speech as sentence boundaries which I didn't when I created the corpus.
