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
