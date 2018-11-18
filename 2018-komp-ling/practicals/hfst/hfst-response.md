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

All the files I've got doing this practical are in this folder.
