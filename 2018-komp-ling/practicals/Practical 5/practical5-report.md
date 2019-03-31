# Udpipe

I installed udpipe using bash commands described in the tutoral:

>$ git clone https://github.com/ufal/udpipe.git
>$ cd udpipe/src
>$ make
>$ sudo cp udpipe /usr/local/bin/

and downloaded pre-trained model (don't want to grow old while it is training):

> $ wget http://ilazki.thinkgeek.co.uk/ru_syntagrus-ud.udpipe

and the example text

> $ wget https://ftyers.github.io/028-komp-ling/classes/pushkin.conllu

Then I segmented the text into sentences and tokens and tag/dependency parsed it using this pipeline:

> $ cat pushkin.txt | udpipe ru_syntagrus-ud.udpipe --tokenize --tag --parse |  > result.conllu

[Here](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%205/result.conllu) is what I got.
