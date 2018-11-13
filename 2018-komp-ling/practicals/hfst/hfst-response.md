1. A simple lexical transducer
"Now, go back to your chv.lexc file and add some more stems, for example ����� "���, garden", ���� "�����, city" and ����� "�����, council". 
Then recompile and rerun the other steps up to visualisation."
&
2. Continuation classes
"And now run it through hfst-fst2txt to visualise the resulting transducer."

> see "chv.lexc.png"

3. Phonological rules
"Now try out the other arrows with your rule, recompile and look at the output."

1) output for =>
�����<n><ins>:�������
�����<n><ins>:�������
�����<n><pl><ins>:����������
�����<n><ins>:�������
�����<n><ins>:�������
�����<n><pl><ins>:����������
����<n><ins>:������
����<n><ins>:������
����<n><pl><ins>:���������
����<n><ins>:������
����<n><ins>:������
����<n><pl><ins>:���������

In this case we have no (2) constrain, so in the context of the rule %{A%} correspond to either a or e.

2) output for <=
�����<n><ins>:�������
�����<n><pl><ins>:����������
�����<n><pl><ins>:����������
�����<n><ins>:�������
�����<n><pl><ins>:����������
�����<n><pl><ins>:����������
����<n><ins>:������
����<n><pl><ins>:���������
����<n><pl><ins>:���������
����<n><ins>:������
����<n><pl><ins>:���������
����<n><pl><ins>:���������

In this case we have no (1) constrain, so %{A%} correspond to either a or e out of context.

3) output for /<=
�����<n><ins>:�������
�����<n><pl><ins>:����������
�����<n><pl><ins>:����������
�����<n><ins>:�������
�����<n><pl><ins>:����������
�����<n><pl><ins>:����������
����<n><ins>:������
����<n><pl><ins>:���������
����<n><pl><ins>:���������
����<n><ins>:������
����<n><pl><ins>:���������
����<n><pl><ins>:���������

As said in the interpretation of the rule type, %{A%} never correspond to a in the context
and correspond to either a or e out of context.

4. Rule interactions

Added rules for %{�%} and %{A%}:0 after vowel in .twol:

"Non surface {A} after vowel"
%{A%}:0 <=> [ BackVow: | FrontVow: ] %>: _ ;

"Non surface {�} in plural genitive" 
%{�%}:0 <=> _ %>: %{A%}: � ;

Transducer is on the picture "chv.gen.png", minimazed by command:
$ hfst-minimise chv.gen.hfst  | hfst-fst2txt| python3 att2dot.py  | dot -Tpng -o chv.gen.png.

"What does minimisation do?" It makes a transducer which is equivalent to original one, but with minimum number of states.

5. More on morphotactics
"What difference do you note?" At first the values of the flags are transferred to the next states and only then the prefixes themselves.

6. Productive derivation
Command to get .mor file:  hfst-invert chv.gen.hfst -o chv.mor.hfst

7. Lexicon construction
Fisrt 10 most frequient words from wiki texts:
 33356 �������
  30359 �e���
  30343 ���
  29671 ���
  27039 ��
  26485 �������e
  25745 ��cc��
  25276 �������
  22810 �����e��
It seems there were a lot of texts about rivers..........

8. Evaluation
Coverage: also 0.12% :(

$ python3 evaluate-morph.py test.txt ref.txt

P = 3/4 = 0.75
R = 3/(4+2) = 0.6
F 1 = 2 P R P + R = 2 0.75 � 0.6 0.75 + 0.6 = 0.66

9. Weighting
$ echo "�������" | hfst-lookup -qp chv.surweights.hfst
�������	�������	11,377200

$ echo "����c" | hfst-lookup -qp chv.surweights.hfst
����?	����?	10,050300

