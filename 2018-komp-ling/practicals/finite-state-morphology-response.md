# chv
Files in the directory *chv* correspond to the units "A simple lexical transducer" and "Morphotactics". It follows the practical pretty straightforwardly, allowing you to generate forms and restrict them with vowel harmony:
```
$ hfst-fst2strings chv.gen.hfst | grep gen
канаш<n><gen>:канашӑн
канаш<n><pl><gen>:канашсен
пакча<n><gen>:пакчан
пакча<n><pl><gen>:пакчасен
урам<n><gen>:урамӑн
урам<n><pl><gen>:урамсен
хула<n><gen>:хулан
хула<n><pl><gen>:хуласен
```
The only original part was to modify the rule so that {A} disappears after a vowel. So I added a group called Vow and modified the rule:
```
%{Ă%}:0 <=> [%{м%}: | Vows ] %>: _ н ;
```
I also modified the exception of the vowel harmony rule to avoid conflicts:
```
%{Ă%}:ӑ <=> BackVow: [ ArchiCns: | Cns: | %>: ]+ _ ;
        except:
                                   [%{м%}: | Vows] %>:  _ н ;
```
# ava
This part is devoted to morphological, rather then phonological, restrictions. We can compare the output with or without morphological restraints:
```
$ hfst-fst2strings ava.lexc.hfst 
бицине<v><tv><aor><pl>:риц>уна
бицине<v><tv><aor><nt>:риц>уна
бицине<v><tv><aor><f>:риц>уна
бицине<v><tv><aor>%<m%>:риц>уна
бицине<v><tv><aor><pl>:биц>уна
бицине<v><tv><aor><nt>:биц>уна
бицине<v><tv><aor><f>:биц>уна
бицине<v><tv><aor>%<m%>:биц>уна
бицине<v><tv><aor><pl>:йиц>уна
бицине<v><tv><aor><nt>:йиц>уна
бицине<v><tv><aor><f>:йиц>уна
бицине<v><tv><aor>%<m%>:йиц>уна
бицине<v><tv><aor><pl>:виц>уна
бицине<v><tv><aor><nt>:виц>уна
бицине<v><tv><aor><f>:виц>уна
бицине<v><tv><aor>%<m%>:виц>уна

$ hfst-fst2strings -X obey-flags ava.lexc.hfst
бицине<v><tv><aor><pl>:риц>уна
бицине<v><tv><aor><nt>:биц>уна
бицине<v><tv><aor><f>:йиц>уна
бицине<v><tv><aor>%<m%>:виц>уна
```

# fin
This is devoted to working with cyclic transducers. It will help later when we work with (obviously infinite) numerals.
```
$ hfst-fst2strings -r 5 fin.lex
c.hfst
kala<n><gen>:kala>n
kissa<n><gen>:kissa>n
kissa<n><nom>:kissa
koira<n><nom>:koira
korva<n><nom>:korva
```

# chv2
This part is devoted to derivation and weights of various ways of interpreting words; those weights are defined in the lexicon:
```
$ echo патшалӑх | hfst-lookup -qp chv.mor.hfst 
патшалӑх	патшалӑх<n><nom>	0,000000
патшалӑх	патша<n><der_лӑх><nom>	1,000000

$ echo патшалӑх | hfst-lookup -qp -b 0 chv.mor.hfst 
патшалӑх	патшалӑх<n><nom>	0,000000

$ echo "тӗслӗх" | hfst-lookup -qp -b 0 chv.mor.hfst 
тӗслӗх	тӗс<n><der_лӑх><nom>	1,000000
```
We then construct a frequency dictionary chv.frc.txt with a corpus chv.crp.txt.

Then, we take care of the morphotactics with loan words:
```
$ hfst-fst2strings -r 1000 chv.gen.hfst |grep gen | grep специалист
специалист<n><gen>:специалистсӑ
специалист<n><pl><gen>:специалистсемсӗ
специалист<n><der_лӑх><gen>:специалистлӑхсӗ
специалист<n><der_лӑх><pl><gen>:специалистлӑхсемсӗ
```
(We take a thousand random words because this transducer is cyclic due to the numerals stored in the same directory.)

Taking care of numerals required a bit of manual work.
I added DIGITLEX to Root:

```
LEXICON Root

Nouns ;
DIGITLEX ;
```

And I had to define these rules:
```
"Consonant assimilation for {Т}"
%{Т%}:т <=> [Sons | %{л%}:] %- %>: _ ;

"Vowel harmony for {A} in numerals"
%{А%}:е <=> %{э%}: [%{л%}: | %{с%}: ]* %- %>: [%{Т%}:р | %{Т%}:т] _ ;
```

# chv2/unittests
I have written a python program that takes in a tsv-file and performs the tests. It's a bit raw as I had weird problems with the Python binding, but it must be either ready or few small steps from that.

# chv2
The coverage of our analizer upon our corpus is around 0.21%:
```
$ calc "(($total-$unknown)/$total)*100"
	~0.21300064660910577764

```
The part about generating paradigms is really following the manual, I didn't add anything.
The part about weighting can be found in the relevant files.
The part about guessers took me some struggling that I have not yet fully overcome. I expect that the code is alright, but I couldn't reproduce the correct behaviour as I have discussed with Fran.
As for the Python bindings, I have used them to implement the unit tests.
