## Vladislav Mikhailov MKL181
# Coreference

## udpipe
### installation with a pre-trained model and pushkin.conllu downloaded
```
$ git clone https://github.com/ufal/udpipe.git
$ cd udpipe/src
$ make
$ sudo cp udpipe /usr/local/bin
$ wget http://ilazki.thinkgeek.co.uk/ru_syntagrus-ud.udpipe
$ wget https://ftyers.github.io/028-komp-ling/classes/pushkin.conllu
```
### analysis
```
$ cat pushkin.conllu | udpipe ru_syntagrus-ud.udpipe --tokenize --tag --parse | sed '1,2d' > cool_pushkin.conllu
```

## xrenner
### python
```
import xrenner


cool_xrenner = xrenner.Xrenner(model = './eng')
# eng text
with open('coref.html', 'w+', encoding='utf-8') as f:
    f.write(cool_xrenner.analyze('eng.conllu', 'html'))
    f.close()

rusxrenner = xrenner.Xrenner(model = './rus')
# cool pushkin
with open('coref_pushkin.html', 'w+', encoding='utf-8') as c:
    c.write(rusxrenner.analyze('pushkin.conllu', 'html'))
    c.close()
```
### set up a new language directory
/rus directory was created. I copied the default /udx settings with a few rules added. 
* config.ini – default udx settings
* coref_rules.tab – default udx settings
* pronouns.tab – added a few tokens
    * e.g. он male его male она female я 1sg
* entities.tab – default UN with the writers added

### corf_cool_pushkin.html
xrenner rus model works worse than the eng one. though many matches are coreferred correctly. for example, (Пушкин and он; Тагор and его)

I tried to modify the fisrt proposed rule **(The first rule below illustrates a very ‘safe’ strategy, searching for proper noun markables with identical text (=$1) in the previous 100 sentences, since these are almost always coreferent, and undertaking no feature propagation.)** regarding lemma
however, it didn't help to improve coreference
* coref_rules.tab

```
#first match identical proper markables
form="proper";form="proper"&lemma=$1&takefirst;100;nopropagate
```
