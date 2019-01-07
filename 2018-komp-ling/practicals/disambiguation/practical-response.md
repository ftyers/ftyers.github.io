### Tager comparison
<br />
I tested the speech taggers for Japanese

```
$ git clone https://github.com/UniversalDependencies/UD_Japanese-GSD
$ cat ja_gsd-ud-train.conllu | udpipe --tokenizer=none --parser=none --train ja.udpipe
$ cat ja_gsd-ud-test.conllu | udpipe --tag ja.udpipe > ja_gsd-ud-test_output.conllu
$ python3 conll17_ud_eval.py --verbose ja_gsd-ud-test.conllu ja_gsd-ud-test_output.conllu

Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     96.88 |     96.88 |     96.88 |     96.88
XPOS       |     96.36 |     96.36 |     96.36 |     96.36
Feats      |     99.98 |     99.98 |     99.98 |     99.98
AllTags    |     96.33 |     96.33 |     96.33 |     96.33
Lemmas     |     99.01 |     99.01 |     99.01 |     99.01
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
```

<br />
### Constraint Grammar
<br />
I ran the following rules:

```
DELIMITERS = "." ;

LIST DET = DET ;
LIST PUNCT = PUNCT ;
LIST PART = PART ;
LIST VERB = VERB ;

SECTION

REMOVE DET IF (1C PUNCT) ;
REMOVE PART IF (-1C VERB) ;
```

And that's what I've got:


```
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
;       "тот" DET Case=Loc Gender=Neut Number=Sing REMOVE:10
;       "тот" DET Case=Loc Gender=Masc Number=Sing REMOVE:10
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
        "все" PRON Animacy=Anim Case=Acc Number=Plur
        "все" PRON Animacy=Anim Case=Gen Number=Plur
"<желающих>"
        "желать" VERB Aspect=Imp Case=Gen Number=Plur Tense=Pres VerbForm=Part Voice=Act
"<и>"
        "и" CCONJ
;       "и" PART REMOVE:11
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
```

I also wanted to remove a tag Case=Nom when it follows an ADP and remove tags Number=Plur when they follow a NOUN 
but I coudn't figure out how to implemment these rules with this kind of tags :(
 
### Perceptron tagger
Everything went well on these steps

```
$ cat ../UD_Japanese-GSD/ja_gsd-ud-train.conllu | python3 tagger.py -t ja-ud.dat
$ cat ../UD_Japanese-GSD/ja_gsd-ud-test.conllu | python3 tagger.py -t ja-ud.dat > jp-ud-test.out
```

but this line

```
$ python3 ../evaluation_script/conll17_ud_eval.py --verbose ../UD_Japanese-GSD/ja_gsd-ud-test.conllu jp-ud-test.out
```

gave me the following:

```
Metrics    | Precision |    Recall |  F1 Score | AligndAcc
-----------+-----------+-----------+-----------+-----------
Tokens     |    100.00 |    100.00 |    100.00 |
Sentences  |    100.00 |    100.00 |    100.00 |
Words      |    100.00 |    100.00 |    100.00 |
UPOS       |     95.62 |     95.62 |     95.62 |     95.62
XPOS       |    100.00 |    100.00 |    100.00 |    100.00
Feats      |    100.00 |    100.00 |    100.00 |    100.00
AllTags    |     95.62 |     95.62 |     95.62 |     95.62
Lemmas     |    100.00 |    100.00 |    100.00 |    100.00
UAS        |    100.00 |    100.00 |    100.00 |    100.00
LAS        |    100.00 |    100.00 |    100.00 |    100.00
```

