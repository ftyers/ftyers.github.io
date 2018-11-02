# Сегментация

- Для данного задания были использованы два сегментатора: pragmatic segmenter и NLTK's Punkt. Разбор проводился на текстах Википедии на немецком языке.
Pragmatic segmenter написан с помощью правил и использует язык Ruby. В документации представлено некоторое количество golden rules для каждого языка. Чтобы использовать правила для особенностей немецкого языка, я в предложенном коде поправила язык в поле lang:
```sh
require 'pragmatic_segmenter'

lang = "de"
if ARGV[0]
    lang=ARGV[0]
end

STDIN.each_with_index do |line, idx|
    ps = PragmaticSegmenter::Segmenter.new(text: line, language: lang)
    ps.segment
    for i in ps.segment
        print(i,"\n")
    end
end
```
NLTK's Punkt является библиотекой для языка Python. Для 17 европейских языков (немецкий - в их числе) существуют предварительно созданные модели, которые используются для сегментации. В своем коде я использовала модель немецкого языка, написав:
``` sh
tokenizer = nltk.data.load("tokenizers/punkt/german.pickle")
```

- Точность разбиения 50 случайных параграфов из Википедии:
-- pragmatic segmenter 97,5 %
-- nltk 94,3 %

- Какие ошибки были допущены каждым сегментатором:

Pragmatic segmenter не смог распознать сокращения Nr. (Nummer) и Jh. (Jahrhundert) и разделил предложения по точке в этих сокращениях.
> Auf der Liste der verurteilten Muslimbrüder, die auf der Website der Muslimbruderschaft veröffentlicht wurde, ist er die Nr. 4.
Im Innern der Kirche ist eine altkroatische Grabinschrift in glagolitischer Schrift aus dem 15. Jh. erhalten geblieben.

У NLTK есть некоторые проблемы с распознаванием порядковых числительных, которые в немецком языке пишутся с точкой (например, 6. - шестой).
> 1959 wurde Klingner erstmals Europameister mit dem Kleinkalibergewehr und nahm im Jahr darauf an den Olympischen Sommerspielen in Rom 1960 teil, wo er den 19. Platz belegen konnte. 
Die erstklassige "1. Division" und die zweitklassige "2. Division" waren in dieser Saison durch einen Playoff-Modus miteinander verschmolzen. 
1986 gab sie ihr Debüt als 1. Blumenmädchen in Richard Wagners "Parsifal" am Royal Opera House Covent Garden und war dort auch in Brittens "Peter Grimes" und Verdis "Falstaff" zu erleben.

Некоторые сокращения (Jh., engl.) также не были распознаны.
> Im Innern der Kirche ist eine altkroatische Grabinschrift in glagolitischer Schrift aus dem 15. Jh. erhalten geblieben.
Auch der „Great belted Plaid“ (engl. „große, gegürtete Decke“) ist eine Erfindung der späten Renaissance, sowie der Kilt der Neuzeit.

Таким образом, pragmatic segmenter, основанный на правилах, лучше справляется с распознаванием порядковых числительных в немецком языке. Однако, у обоих сегментаторов есть некоторые проблемы с сокращениями.