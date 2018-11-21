# Practical #2 - HFST
#### *Anastasia Nikiforova*

## Changes to *chv.lexc*:

There were added the following lines and sections:

* Multichar_Symbols [Added]
	* ```%<ins%>, %<gen%>, %<der_лӑх%>, %<guess%>``` - new cases
	* ```%{м%}, %{ъ%}, %{э%}, %{л%}, %{с%}, %{а%}``` - new multichar characters

* Lexicon Roots [Added]
	* ```Guesser``` - for morphological predictions

* LEXICON Guesser [New]
	* This lexicon allows us to analyse word morphology (if it's in our dictionary)

* LEXICON N/сть [New]
	* This section was added to see the difference between *сть* and *ҫ* usages (how frequent each is). The results are below in 	*Weighing. Surface forms* section of this report.

* LEXICON CASES [Added]
	* ```%<nom%>:%> # ;``` - added to display ```%<der_лӑх%>``` correctly
	* ```%<gen%>:%>%{Ă%}н # ;``` - added to see genitive forms

* LEXICON DER-N [New]
	* Added to display ```%<der_лӑх%>``` forms

* LEXICON N [Added]
	* ```%<n%>: SUBST``` and ```%<n%>: DER-N``` added for the corresponding forms

* LEXICON NUM-DIGIT, LAST-DIGIT, LOOP, DIGITLEX [New]
	* added to analyse morphology of compound digits and their forms

## Changes to *chv.lexc.twol*:

The following changes were made:

*  Alphabet [Added]

%{A%}:а %{A%}:е %{Ă%}:ӑ %{Ă%}:ӗ %{Ă%}:0 %{м%}:м %{м%}:0
 %{э%}:0 %{л%}:0 %{с%}:0 %{а%}:0 %{ъ%}

* Sets [Added]

	* New Set is added: ```Vowels``` (*FrontVow* + *BackVow*).

NB! **е** was originally missing in *FrontVow* (if an alrtness quest, it was quite a tricky and unexpected one), so it had to be added later.

* Rules [Added]
	* Three more rules were added (see chv.lexc.twol).
	* I combined two rules into one ```"%{Ă%}:0 if there is previous %{м%}: or a vowel and, optionally, a following н"```
	* Two exceptions had to be added to the %{Ă%}: vowel harmony rule
	* A rule is added to handle ablative. I specified only %{Т%} assomilaton, as vowel harmony has been added previously

## Changes to *Makefile*:

* Added one line: **hfst-invert chv.gen.hfst -o chv.mor.hfst** to create a *.mor.hfst file

## Lexicon construction

I noticed that one letter of Chuvash alphabet is missing in the HFST tutorial: **ӳӲ** (*luckily I am a native Chuvash language speaker :)* ). I added then to the command, so that the words containing this letter would not be omitted:

```
$ cat chv.crp.txt  | sed 's/[^а-яӑӗăĕҫçӳА-ЯӐӖĂĔҪÇӲ]\+/ /g' | tr ' ' '\n' | sort -f | uniq -c | sort -gr
```

*I counted differences that this modification made with ```wc -l``` , but it didn't make any difference. I expected that the amount of words will be increased. For some reasons, it didn't.*

**NB!** As a corpus (to count word frequencies) I used Chuvash wikipedia damp (lang code: **cv**). To extract texts, WikiExtractor was used.

Overall corpus size (word tokens): **2,458,544**
Word types (unique tokens): **172,336**

The results were written to *freq.txt* file

```
[Command above] > freq.txt
```


## Coverage Results
```
$ calc "(($total-$unknown)/$total)*100"
	~0.13394403330576701513
```
=> It surns out that my current analyzer has a coverage of over 13%, which is just a bit higher than in our HFST tutorial.


## Weighing. Surface forms

I am including this results to this reports because they differ (slightly) from the HFST tutorial results:

```
$ echo "область" | hfst-lookup -qp chv.surweights.hfst
область	область	11,413600

$ echo "облаç" | hfst-lookup -qp chv.surweights.hfst
облаç	облаç	10,017400
```

This difference is absolutely normal, because in the tutorial they used a different corpus.

Anyway, it's interesting that despite the corpora are different (mine is a Wikipedia dump and over 2M, another one is news and about 300K), the results are similar.

## HFST in Python

I have used the script that was mentioned in the tutorial, but I added two modifications:
* Encoding. Without mentioning the encoding, the script wouldn't work.
* ```sys.stdin```, so that we don't have to modify the ```.py``` file all the time.

