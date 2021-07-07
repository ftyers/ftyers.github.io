#### 1.
<br />
a) contraint grammar rules give you a more predictable result which is easier to manipulate
<br />
b) the constraint rules are based on the context of ambiguous words, in other words on sequence of information -
that is what HMM is suitable for, it deals with recognising patterns in sequence of fearute, it is hard for a 
person to predict all the exeptions, but when you have a big data and a language model that has a better memory 
for this kind of task it seems to be more realizable 
<br />
I would probably choose HMM training as I always seem to miss some cases when it comes to predicting what might go
wrong + you can always use a little crowdsourcing :)
#### 2.
<br />
a) We can apply both models and compare them and then analyse the difference to expand the rules 
<br />
b) We can use HMM in cases when our rules don't provide the disambiguation of the word
#### 3.
<br />
Это шило остро.
```
"<Это>"
        "это" PRON Animacy=Inan Case=Nom Gender=Neut Number=Sing
        "этот" DET Case=Nom Gender=Neut Number=Sing
        "это" PRON Animacy=Inan Case=Acc Gender=Neut Number=Sing
        "это" PART
        "этот" DET Case=Acc Gender=Neut Number=Sing
"<шило>"
        "шить" VERB Aspect=Imp Gender=Neut Mood=Ind Number=Sing Tense=Past VerbForm=Fin Voice=Act
	"шило" NOUN Animacy=Inan Case=Nom Gender=Neut Number=Sing
	"шило" NOUN Animacy=Inan Case=Acc Gender=Neut Number=Sing
"<остро>"
        "остро" ADV Degree=Pos
	"острый" ADJ Case=Nom Degree=Neut Gender=Neut Number=Sing
"<.>"
        "." PUNCT
```
<br />
HMM model is likely to make a mistake here because adverb is more common than the short form of the adjective even 
if it is in the same context with the noun "шило" (wich is also to be identified as noun). So I believe that the rule
which, for example, excludes transitive verbs after neutral pronouns and determiners could help us identify "шило"
as a noun, and a rule which leaves determiner to the left of the noun where there could be pronouns would help us
identify "это" as a determiner. And finally there should be no adverb after a noun (unless it's case is instrumental)
in a sentence without a verb.
#### 4.
<br />
The problem is that this is the case of classification on n classes which is evaluated as n binary classifications,
so we take all tags and for each calculate: 
<br />
- TP (the answer equals to the target)
<br />
- FN (the target is the TAG, the answer is not)
<br />
- FP (the answer is the TAG, the target is not)
<br />
- TN (both the target and the answer are not the TAG)
<br />
Accuracy sometimes gives confusing results: suppose we have 100 Nouns and 10 Non-Nouns, if our algorithm
defines everything as Nouns we get accuracy of 91 which is rather high for such output. So there are Precision 
TP/(TP+FP) and Recall TP/(TP+FN) that tell you how you model pehaves, but I really like the Fβ score as you can conciously give a greater weight to one of the metrics.  
#### 5.

```
"<Он>"
        "он" PRON Case=Nom Gender=Masc Number=Sing Person=3
"<любил>"
        "любить" VERB Aspect=Imp Gender=Masc Mood=Ind Number=Sing Tense=Past VerbForm=Fin Voice=Act
"<свою>"
        "свой" DET Case=Acc Gender=Fem Number=Sing
"<мать>"
        "мать" NOUN Animacy=Anim Case=Nom Gender=Fem Number=Sing
        "мать" NOUN Animacy=Anim Case=Acc Gender=Fem Number=Sing
"<.>"
        "." PUNCT
```
Assuming that probability of "мать" being of Nom case is higher we will get the wrong analyses while with a bigram we
can take into account the analyses of "свою" and their coucurrance give us a higher probability of "мать" being 
of Acc case.
