## Morphological disambiguation
### Part-of-Speech Tagger comparison
I've decided to compare three part of speech taggers on the UD Bulgarian corpus. First, I've used UDPipe, as it says in the task, and achieved these results:
~~~~
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
UPOS       |     97.81 |     97.81 |     97.81 |     97.81
~~~~

### Constraint Grammar
I've tried to write down the rules to disambiguate the example sentence. The only tags I couldn't rid of were the ones that weren't POS since they have a different structure I couldn't work around of. 
Here are the rules that worked:

~~~~
DELIMITERS = "." ;

LIST DET = DET ;
LIST PUNCT = PUNCT ;
LIST NOUN = NOUN ;
LIST VERB = VERB ;
LIST PRON = PRON ;
LIST ADP = ADP ;
LIST PART = PART ;

SECTION

REMOVE DET IF (1C PUNCT) ;
REMOVE PRON IF (1 VERB OR NOUN) ;
REMOVE DET IF (-1C ADP) ;
REMOVE PART ;
~~~~

And the ones that didn't:
~~~~
LIST Gen = Gen ;
LIST Acc = Acc ;
LIST Nom = Nom ; 

REMOVE Acc IF (-1C NOUN) ;
REMOVE Nom IF (-1C ADP) ;
~~~~

In the end, I was left with this:
~~~~
"<Однако>"
	"однако" ADV Degree=Pos
"<стиль>"
	"стиль" NOUN Animacy=Inan Case=Nom Gender=Masc Number=Sing
	"стиль" NOUN Animacy=Inan Case=Acc Gender=Masc Number=Sing
"<работы>"
	"работа" NOUN Animacy=Inan Case=Gen Gender=Fem Number=Sing
	"работа" NOUN Animacy=Inan Case=Nom Gender=Fem Number=Plur
	"работа" NOUN Animacy=Inan Case=Acc Gender=Fem Number=Plur
"<Семена>"
	"Семен" PROPN Animacy=Anim Case=Gen Gender=Masc Number=Sing
	"Семен" PROPN Animacy=Anim Case=Acc Gender=Masc Number=Sing
"<Еремеевича>"
	"Еремеевич" PROPN Animacy=Anim Case=Gen Gender=Masc Number=Sing
"<заключался>"
	"заключаться" VERB Aspect=Imp Gender=Masc Mood=Ind Number=Sing Tense=Past VerbForm=Fin Voice=Mid
"<в>"
	"в" ADP
"<том>"
	"то" PRON Animacy=Inan Case=Loc Gender=Neut Number=Sing
;	"тот" DET Case=Loc Gender=Neut Number=Sing REMOVE:16
;	"тот" DET Case=Loc Gender=Masc Number=Sing REMOVE:16
"<,>"
	"," PUNCT
"<чтобы>"
	"чтобы" SCONJ Mood=Cnd
"<принимать>"
	"принимать" VERB Aspect=Imp VerbForm=Inf Voice=Act
"<всех>"
	"весь" DET Case=Gen Number=Plur
	"весь" DET Case=Loc Number=Plur
	"весь" DET Case=Acc Number=Plur
;	"все" PRON Animacy=Anim Case=Acc Number=Plur REMOVE:20
;	"все" PRON Animacy=Anim Case=Gen Number=Plur REMOVE:20
"<желающих>"
	"желать" VERB Aspect=Imp Case=Gen Number=Plur Tense=Pres VerbForm=Part Voice=Act
"<и>"
	"и" CCONJ
;	"и" PART REMOVE:26
"<лично>"
	"лично" ADV Degree=Pos
"<вникать>"
	"*вникать"
"<в>"
	"в" ADP
"<дело>"
	"дело" NOUN Animacy=Inan Case=Nom Gender=Neut Number=Sing
	"дело" NOUN Animacy=Inan Case=Acc Gender=Neut Number=Sing
"<.>"
	"." PUNCT
~~~~
### Improving perceptron tagger
Here are the orginal results of the perceptron tagger on Spanish UD:
~~~~
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
UPOS       |     94.72 |     94.72 |     94.72 |     94.72
~~~~
Here, I've managed to slighlty improve the perceptron used on *UD Spanish* by changing the parameters with suffix and pref1. 
I've changed the length of pref1 to *add('i pref1', word[0:3])* and got the following results:
~~~~
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
UPOS       |     95.58 |     95.58 |     95.58 |     95.58
~~~~
Then, I've played a bit with the suffix parameters, changing all of the suffix instances from [-3] to [-2]:
~~~~
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
UPOS       |     95.21 |     95.21 |     95.21 |     95.21
~~~~
