# Practical 2 - HFST for Chuvash 

### Overview of the files
__chv.lexc__ file is Chuvash lexicon file which consists of the following sections (the ones in __bold__ I wrote fully by myself):
-  Multichar_Symbols : the symbols used for defining cases, archiphonemes and helper symbols for the phonological rules
```
%<n%>                ! Имя существительное
%<pl%>               ! Множественное число
%<nom%>              ! Именительный падеж
%{A%}                ! Творительный падеж
%<gen%>              ! Родительный падеж
%<abl%>              ! Аблатив для числительных
%<der_лӑх%>          ! Суффикс деривации

%{А%}                ! Архифонема [а] или [е]
%{Т%}                ! Архифонема [т] или [р]
%{Ă%}                ! Архифонема [ӑ]
%{м%}                ! Архифонема [м]
%{ъ%}                ! force back harmony in loan words

%{э%}                ! front vowel in numerals
%{а%}                ! back vowel in numerals
%{л%}                ! -н, -л, or -р at the end in numerals
%{с%}                ! other consonants at the end in numerals

%>                   ! Граница морфемы
```
-  LEXICON Root: the lexicons used in the file (we have nouns and numbers)
```
Nouns ;
DIGITLEX ;
```
- LEXICON CASES: forms of cases which we have for our nouns: Nominative, Instrumental, Genitive
```
%<nom%>:%> # ;
%<ins%>:%>п%{А%} # ;
%<gen%>:%>%{Ă%}н # ;
```
- LEXICON PLURAL: how we form plural forms of nouns (we can form plural forms of the above mentioned cases)
```
                 CASES ;
%<pl%>:%>се%{м%} CASES ;
```
- LEXICON SUBST: we form nouns with abstract meaning
```
PLURAL ;

LEXICON DER-N

%<der_лӑх%>:%>л%{Ă%}х SUBST "weight: 1.0" ; 

LEXICON N 

%<n%>: PLURAL ;
%<n%>: SUBST ;
%<n%>: DER-N ;
```
- LEXICON Nouns: the list of stems used in our lexicon
```
урам:урам N ;     ! "улица"
пакча:пакча N ;   ! "сад"
хула:хула N ;     ! "город"
канаш:канаш N ;   ! "совет"
тӗс:тӗс N ;       ! "вид"
патша:патша N ;   ! "царь"
куҫ:куҫ N ;       ! "глаз"
патшалӑх:патшалӑх N ; ! "государство"
специалист:специалист%{ъ%} N ; ! "специалист"
```
- __LEXICON ABLATIVE : Ablative case used for numerals__
```
%<abl%>:%>%{Т%}%{А%}н # ;
```
- __LEXICON NUM-DIGIT: the pattern how we form ablative form of numeral__
```
%<num%>:%- ABLATIVE ;
```
- LEXICON LAST-DIGIT: the lexicon for the last digit in numerals (using helping symbols for future rules)
```
1:1%{э%}%{л%}    NUM-DIGIT ; ! "пӗр" 
2:2%{с%}%{э%}    NUM-DIGIT ; ! "иккӗ" 
3:3%{с%}%{э%}    NUM-DIGIT ; ! "виҫҫӗ" 
4:4%{с%}%{а%}    NUM-DIGIT ; ! "тӑваттӑ" 
5:5%{э%}%{с%}    NUM-DIGIT ; ! "пиллӗк" 
6:6%{с%}%{а%}    NUM-DIGIT ; ! "улттӑ" 
7:7%{с%}%{э%}    NUM-DIGIT ; ! "ҫиччӗ" 
8:8%{э%}%{л%}    NUM-DIGIT ; ! "саккӑр" 
9:9%{э%}%{л%}    NUM-DIGIT ; ! "тӑххӑр" 
```
- LEXICON LOOP: how we generate random numbers
```
                 LAST-DIGIT ; 
                 DIGITLEX ; 

LEXICON DIGITLEX

%0:%0 LOOP ;
1:1   LOOP ;
2:2   LOOP ;
3:3   LOOP ;
4:4   LOOP ;
5:5   LOOP ;
6:6   LOOP ;
7:7   LOOP ;
8:8   LOOP ;
9:9   LOOP ;
```

__chv.twol__ file is Chuvash rules file which consists of the following sections (the ones in __bold__ I wrote by myself):
- Alphabet: used to define characters and achiphonems in the rules
```
Alphabet
  а ӑ е ё ӗ и о у ӳ ы э ю я б в г д ж з к л м н п р с ҫ т ф х ц ч ш щ й ь ъ
  А Ӑ Е Ё Ӗ И О У Ӳ Ы Э Ю Я Б В Г Д Ж З К Л М Н П Р С Ҫ Т Ф Х Ц Ч Ш Щ Й Ь Ъ 
  1 2 3 4 5 6 7 8 9
 %{А%}:а %{А%}:е
 %{Ă%}:ӑ %{Ă%}:ӗ %{Ă%}:0
 %{м%}:м %{м%}:0
 %{ъ%}:0
 %{э%}:0 %{л%}:0 %{с%}:0 %{а%}:0
 %{Т%}:р %{Т%}:т
 %-
;
```
- Sets: used to combine characters into groups which are used in the rules
```
BackVow = ӑ а ы о у я ё ю %{ъ%};

FrontVow = ӗ э и ӳ; 

Cns = б в г д ж з к л м н п р с ҫ т ф х ц ч ш щ й ь ъ ; 

Vow = а ӑ е ё ӗ и о у ӳ ы э ю я ;

ArchiCns = %{м%} ;
```
- Rules: the section where the rules are defined.
```
"Remove morpheme boundary"
%>:0 <=> _ ;

"Back vowel harmony for archiphoneme {A}"
%{А%}:а <=> BackVow: [ Cns: | %>: ]+ _ ; 

"Back vowel harmony for archiphoneme {Ă}"
%{Ă%}:ӑ <=> BackVow: [ ArchiCns: | Cns: | %>: ]+ _ ;
		except
									%{м%}: %>:  _ н ; 
                                    Vow: %>:  _ н ;
                                     
"Non surface {Ă} in plural and singular genitive"
%{Ă%}:0 <=> [ Vow: | %{м%}: ] %>: _ н ;
```
Rules I wrote by myself (more on that below):
```
"Deleting м in plural genitive"
%{м%}:0 <=> _ %>: %{Ă%}: н ;

"Ablative surface consonant т" 
%{Т%}:т <=> %{л%}: %- %>: _ ; 

"Ablative vowel harmony"
%{А%}:а <=> %{э%}: [%{л%}: | %{с%}: ]* %- %>: [%{Т%}:р | %{Т%}:т] _ ;
```

### The things I've done 
I followed the tutorial straightforwardly. I've modified the rule for {Ă} which shouldn't be in surface form when it goes after a vowel. So I've added a set called "Vow" where I put all the vowels from the alphabet, I've added an exceptiong in the back vowel harmony rule and written an additional rule for deleting {Ă} after vowels and archiphoneme {м}.
```
"Back vowel harmony for archiphoneme {Ă}"
%{Ă%}:ӑ <=> BackVow: [ ArchiCns: | Cns: | %>: ]+ _ ;
		except
									%{м%}: %>:  _ н ; 
                                    Vow: %>:  _ н ;
                                     
"Non surface {Ă} in plural and singular genitive"
%{Ă%}:0 <=> [ Vow: | %{м%}: ] %>: _ н ;
```
After that I should have got the following: 
```
канаш<n><pl><gen>:канашсен
урам<n><pl><gen>:урамсен
```
My forms of plural genetive were "канашсемн" and "урамсемн". So I've added one more rule which deletes "м" from surface form of plural suffix.
```
"Deleting м in plural genitive"
%{м%}:0 <=> _ %>: %{Ă%}: н ;
```
The next big part was the ablative case of numerals. I've constructed the loop which generates random numerals (LEXICON DIGITLEX mentioned above) and the following ablative case:
```
%<abl%>:%>%{Т%}%{А%}н # ;
```
The last digit in numeral defines the form of the ablative suffix, it was described the following way:
```
LEXICON LAST-DIGIT

1:1%{э%}%{л%}    NUM-DIGIT ; ! "пӗр" 
2:2%{с%}%{э%}    NUM-DIGIT ; ! "иккӗ" 
3:3%{с%}%{э%}    NUM-DIGIT ; ! "виҫҫӗ" 
4:4%{с%}%{а%}    NUM-DIGIT ; ! "тӑваттӑ" 
5:5%{э%}%{с%}    NUM-DIGIT ; ! "пиллӗк" 
6:6%{с%}%{а%}    NUM-DIGIT ; ! "улттӑ" 
7:7%{с%}%{э%}    NUM-DIGIT ; ! "ҫиччӗ" 
8:8%{э%}%{л%}    NUM-DIGIT ; ! "саккӑр" 
9:9%{э%}%{л%}    NUM-DIGIT ; ! "тӑххӑр" 
```
My task was to write the rules which transform ablative suffix %{Т%}%{А%}н into "тан"/"ран" or "тен"/"рен". The following rule transform archiphoneme {T} into "т" when in follows {л} archiphoneme (which replace -н, -л, or -р), in other cases {T} transforms into "р".
```
"Ablative surface consonant т" 
%{Т%}:т <=> %{л%}: %- %>: _ ; 
```
I had a very long battle with transformation of archiphoneme {A} in this suffix. We even thought that it was a bug in twolc, I've updated the version from 3.9.0 to 3.15.0. After a week of battling with it, I have tried to check whether all {А} were written in cyrillic (though I have done it earlier multiple times). After compiling the rule I've written finally worked! :) It looks like that:
```
"Ablative vowel harmony"
%{А%}:а <=> %{э%}: [%{л%}: | %{с%}: ]* %- %>: [%{Т%}:р | %{Т%}:т] _ ;
```
It replaces {A} with "а" in ablative suffix when it goes after front vowel (archiphoneme {э}).

#### Evaluation

I've created a Chuvach corpus using a Wikipedia database backup dump, and then made a frequency list (see chv.freq.txt). I've calculated naïve coverage (the percentage of tokens in our corpus that receive at least one analysis from our morphological analyser) - the result is only ~0.01763585486867166741. To increase this number more stems and cases should be added to our lexc file.

### THE LONG BATTLE WITH (PROBABLY NON-EXISTING) BUG
The rule mentioned above didn't transform {A} in ablative suffix, it remained {A} on surface for a veeeery long time. I have tried to run a separate file to check whether the rule transforms it or not. It contains the following:
```
Alphabet
  а е %>
 %{A%}:а %{A%}:е
 ;

Sets 


Rules 

"Remove morpheme boundary"
%>:0 <=> _ ;

"Ablative vowel harmony"
%{A%}:е <=> _ ;
```
So we have a rule that forbids {А} to be "a" in any context. However, after compiling this twol file, I got the following output:
```
hfst-fst2strings chv_test.twol.hfst -r 50 | grep {A}
{A}{A}:аа
{A}{A}:ае
{A}е:ае
{A}:е
{A}{A}{A}:еаа
{A}{A}:ее
{A}а@#@:еа
{A}е:ее
а{A}:ае
```
__I have a question - is it a real bug or just an error in writing rules?__