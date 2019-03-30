1. A simple lexical transducer
"Now, go back to your chv.lexc file and add some more stems, for example пахча "сад, garden", хула "город, city" and канаш "совет, council". 
Then recompile and rerun the other steps up to visualisation."
&
2. Continuation classes
"And now run it through hfst-fst2txt to visualise the resulting transducer."

> see "chv.lexc.png"

3. Phonological rules
"Now try out the other arrows with your rule, recompile and look at the output."

1) output for =>
канаш<n><ins>:канашпа
канаш<n><ins>:канашпе
канаш<n><pl><ins>:канашсемпе
пакча<n><ins>:пакчапа
пакча<n><ins>:пакчапе
пакча<n><pl><ins>:пакчасемпе
урам<n><ins>:урампа
урам<n><ins>:урампе
урам<n><pl><ins>:урамсемпе
хула<n><ins>:хулапа
хула<n><ins>:хулапе
хула<n><pl><ins>:хуласемпе

In this case we have no (2) constrain, so in the context of the rule %{A%} correspond to either a or e.

2) output for <=
канаш<n><ins>:канашпа
канаш<n><pl><ins>:канашсемпа
канаш<n><pl><ins>:канашсемпе
пакча<n><ins>:пакчапа
пакча<n><pl><ins>:пакчасемпа
пакча<n><pl><ins>:пакчасемпе
урам<n><ins>:урампа
урам<n><pl><ins>:урамсемпа
урам<n><pl><ins>:урамсемпе
хула<n><ins>:хулапа
хула<n><pl><ins>:хуласемпа
хула<n><pl><ins>:хуласемпе

In this case we have no (1) constrain, so %{A%} correspond to either a or e out of context.

3) output for /<=
канаш<n><ins>:канашпе
канаш<n><pl><ins>:канашсемпа
канаш<n><pl><ins>:канашсемпе
пакча<n><ins>:пакчапе
пакча<n><pl><ins>:пакчасемпа
пакча<n><pl><ins>:пакчасемпе
урам<n><ins>:урампе
урам<n><pl><ins>:урамсемпа
урам<n><pl><ins>:урамсемпе
хула<n><ins>:хулапе
хула<n><pl><ins>:хуласемпа
хула<n><pl><ins>:хуласемпе

As said in the interpretation of the rule type, %{A%} never correspond to a in the context
and correspond to either a or e out of context.

4. Rule interactions

Added rules for %{м%} and %{A%}:0 after vowel in .twol:

"Non surface {A} after vowel"
%{A%}:0 <=> [ BackVow: | FrontVow: ] %>: _ ;

"Non surface {м} in plural genitive" 
%{м%}:0 <=> _ %>: %{A%}: н ;

Transducer is on the picture "chv.gen.png", minimazed by command:
$ hfst-minimise chv.gen.hfst  | hfst-fst2txt| python3 att2dot.py  | dot -Tpng -o chv.gen.png.

"What does minimisation do?" It makes a transducer which is equivalent to original one, but with minimum number of states.

5. More on morphotactics
"What difference do you note?" At first the values of the flags are transferred to the next states and only then the prefixes themselves.

6. Productive derivation
Command to get .mor file:  hfst-invert chv.gen.hfst -o chv.mor.hfst

7. Lexicon construction
Fisrt 10 most frequient words from wiki texts:
 33356 Юханшыв
  30359 кeрет
  30343 шыв
  29671 Шыв
  27039 км
  26485 бассейнe
  25745 Раccей
  25276 юханшыв
  22810 хыпарeпе
It seems there were a lot of texts about rivers..........

8. Evaluation
Coverage: also 0.12% :(

9. Weighting
$ echo "область" | hfst-lookup -qp chv.surweights.hfst
область	область	11,377200

$ echo "облаc" | hfst-lookup -qp chv.surweights.hfst
обла?	обла?	10,050300

All the files I've got doing this practical are in this folder. As I understood there should be a description of changes I've done
in the files so I'll comment some parts of chv.lexc and chv.twol.

I. chv.lexc

# ADDED SOME NECESSERY MULTICHAR SYMBOLS
Multichar_Symbols

%<n%>                ! Имя существительное
%<pl%>               ! Множественное число
%<nom%>              ! Именительный падеж
%<ins%>              ! Творительный падеж
%<gen%>              ! Родительный падеж

%<num%>              ! Число

%{A%}                ! Архифонема [а] или [е]
%{Ă%}                ! Архифонема [ӑ] или [ӗ] или 0
%{м%}                ! Архифонема [м] или 0
%{с%}                ! Несонорные согласные
%{л%}                ! -н, -л, или -р
%{э%}                ! Передние гласные
%{а%}                ! Задние гласные

%{ъ%}                ! Для заимствованных слов

%<der_лӑх%>          ! Суффикс -лӐх

%>                   ! Граница морфемы

# ADDED LEXICON GUESSER TO THE ROOT
LEXICON Root

Nouns ; 
Guesser ;

# ADDED GENETIVE AND NOMINATIVE TO THE CASES LEXICON
LEXICON CASES 

%<nom%>:%> # ;
%<ins%>:%>п%{A%} # ;
%<gen%>:%>%{Ă%}н # ;

# EDITES PLURAL RULE TO WORK WITH GENITIVE PLURAL
LEXICON PLURAL

             CASES ; 
%<pl%>:%>се%{м%} CASES ;

# ADDED LEXICONS SUBST AND DER-N TO WORK WITH PRODUCTIVE DERIVATION
LEXICON SUBST 

PLURAL ;

LEXICON DER-N

%<der_лӑх%>:%>л%{Ă%}х SUBST "weight: 1.0" ;

# ADDED THEM INTO LEXICON N
LEXICON N

%<n%>: PLURAL ;
%<n%>: SUBST ;
%<n%>: DER-N ;

# *ADDED THE PART TO HANDLE WITH NUMERAL EXPRESSIONS*

# ADDED LEXICON N/СТЬ TO WORK WITH WEIGHTING OF DIFFERENT SURFACE FORMS
LEXICON N/сть

%<n%>:ҫ SUBST "weight: 0.5" ;
%<n%>%<nom%>:сть # "weight: 1.0" ;

# ADDED SOME WORDS TO NOUNS
LEXICON Nouns

урам:урам N ;     ! "улица"
пакча:пакча N ;   ! "сад"
хула:хула N ;     ! "город"
канаш:канаш N ;   ! "совет"
тӗс:тӗс N ;       ! "вид"
патша:патша N ;   ! "царь"
куҫ:куҫ N ;       ! "глаз"
патшалӑх:патшалӑх N ; ! "государство"
специалист:специалист%{ъ%} N ; ! "специалист"

II. chv.twol

# ADDED ALL POSSIBLE OUTPUTS FOR NEW ARCHIFONEMES
Alphabet
  а ӑ е ё ӗ и о у ӳ ы э ю я б в г д ж з к л м н п р с ҫ т ф х ц ч ш щ й ь ъ
  А Ӑ Е Ё Ӗ И О У Ӳ Ы Э Ю Я Б В Г Д Ж З К Л М Н П Р С Ҫ Т Ф Х Ц Ч Ш Щ Й Ь Ъ 
 %{A%}:а %{A%}:е
 %{Ă%}:ӑ %{Ă%}:ӗ %{Ă%}:0
 %{м%}:м %{м%}:0
 %{ъ%}:0
 %{э%}:0 %{л%}:0 %{с%}:0 %{а%}:0
;

# ADDED SOME SPECIAL ARCHIFONEMES TO SETS
Sets 

BackVow = ӑ а ы о у я ё ю %{ъ%} %{а%} ;
FrontVow = ӗ э и ӳ %{э%} ; 
Cns = б в г д ж з к л м н п р с ҫ т ф х ц ч ш щ й ь ъ %{л%} %{с%};
ArchiCns = %{м%} ;

# ADDED SOME RULES (SEE ABOVE)
Rules 

"Remove morpheme boundary"
%>:0 <=> _ ;

"Back vowel harmony for archiphoneme {A}"
%{A%}:а <=> BackVow: [ Cns: | %>: ]+ _ ;

"Non surface {Ă} after vowel"
%{Ă%}:0 <=> [ BackVow: | FrontVow: ] %>: _ ;

"Non surface {Ă} in plural genitive"
%{Ă%}:0 <=> %{м%}: %>: _ н ;

"Non surface {м} in plural genitive" 
%{м%}:0 <=> _ %>: %{Ă%}: н ;

"Back vowel harmony for archiphoneme {Ă}"
%{Ă%}:ӑ <=> BackVow: [ ArchiCns: | Cns: | %>: ]+ _ ;
        except
                                     %{м%}: %>:  _ н ;
									 BackVow: %>: _ ;
