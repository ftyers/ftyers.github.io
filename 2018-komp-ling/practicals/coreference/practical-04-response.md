# Coreference

## installing udpipe 
```
$ git clone https://github.com/ufal/udpipe.git
$ cd udpipe/src
$ make
$ sudo cp udpipe /usr/local/bin
```
### + downloading ru_syntagrus-ud.udpipe and pushkin.conllu from https://ftyers.github.io/028-komp-ling/classes/11.html
```
### analysing
```
$ cat pushkin.conllu | udpipe ru_syntagrus-ud.udpipe --tokenize --tag --parse | sed '1,2d' > new_pushkin.conllu
```

## installing xrenner
```
$ git clone https://github.com/amir-zeldes/xrenner.git
$ cd xrenner
$ git checkout develop
$ python3 setup.py install [--prefix=PREFIX]
$ cd xrenner/models
$ cp eng.xrm eng/
$ cd eng/
$ unzip -n eng.xrm
$ cd ../../
$ python3 xrenner.py -t 
```
### python
```
import xrenner


eng_xrenner = xrenner.Xrenner(model = './eng')
# eng text
with open('coreference_english.html', 'w+', encoding='utf-8') as f:
    f.write(eng_xrenner.analyze('eng.conllu', 'html'))
    f.close()

rus_xrenner = xrenner.Xrenner(model = './rus')
# cool pushkin
with open('coreference_russian.html', 'w+', encoding='utf-8') as f:
    f.write(rus_xrenner.analyze('pushkin.conllu', 'html'))
    f.close()
```
### setting up a new language directory and writing rules

I implemented the "Co-refer mentions that exactly match" rule but it didn't seen to improve coreference maybe
because it is simple enough to solve these cases without an additional rule

