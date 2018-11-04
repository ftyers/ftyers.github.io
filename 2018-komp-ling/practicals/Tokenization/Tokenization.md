**Tokenization**   

Как известно, даже путь в тысячи строк начинается с первой строки, а точнее даже с постановки первой задачи — куда вообще нужно идти. Чтобы иметь возможность разбить японский текст на токены, нам нужно следующее: создать словарь уникальных слов, подготовить тестовый файл с предложениями, написать алгоритм MaxMatch, оценить результат работы нашего алгоритма с помощью метрики WER.  

Словарь мы создаем на основе файла ja_gsd-ud-train.conllu, используя регулярные выражения, чтобы избавиться от ‘шума’:  

    $ sed ‘/^#/d’ ja_gsd-ud-train.conllu > ja_gsd-ud-train.conllu-clean
    $ cut -f2 -d’	‘ ja_gsd-ud-train.conllu-clean > ja_gsd-ud-train.conllu-dict
    $ sort -u ja_gsd-ud-train.conllu-dict > ja_gsd-ud-train.conllu-dict_uniq
    
Открываем файл в редакторе vim, чтобы оценить его вид. Получившийся словарь я преобразовала в dictionary.txt и удалила первую и последнюю пустые строки. Получилось 15326 уникальных слов:  

    $ wc -l dictionary.txt
    15325 dictionary.txt
    
Чтобы извлечь предложения из файла ja_gsd-ud-test.conllu (именно их мы и будем токенизировать) нам также потребуются регулярные выражения:  

    $ sed -n ‘/^# text =/p’ ja_gsd-ud-test.conllu > jp-sentences.txt
    $ sed -e 's/^# text = //' jp-sentences.txt > sentences.txt

Получилось 558 предложений (команда $ wc -l  выдает 557, но $ wc -l — это подсчет перевода строки, поэтому нужно прибавить еще последнее предложение).   

С получившимися файлами dictionary.txt и sentences.txt можно работать дальше.  

Алгоритм MaxMatch, который я применила (конечно, его можно сделать и в более общем виде, чтобы аргументы можно было вводить из командной строки):  

    # открываем файл со словарем 
    with open('dictionary.txt', 'r') as d:
        lines_dict = d.readlines()
        lines_dict = [line.strip() for line in lines_dict] 

    # открываем файл с текстом, в котором хотим выделить токены
    with open('sentences.txt', 'r') as s:
        lines_sent = s.readlines()
        lines_sent = [line.strip() for line in lines_sent]

    # сортируем словарь по длине слов так, чтобы сначала шли длинные слова
    def sortbylength(word):
        return len(word)
    def new_sorted(dictionary):
        dict_sorted = sorted(dictionary, key=sortbylength, reverse=True)
        return dict_sorted

    dictionary = lines_dict
    new_dictionary = new_sorted(dictionary)

    ‘’’ применяем MaxMatch
    проверяем, совпадают ли первые символы строки со словом из словаря; 
    если да — отделяем слово и начинаем по-новой с оставшимися символами строки, 
    если нет — неизвестный символ назначается словом, отделяется и мы повторяем алгоритм с оставшимися символами;
    если длина строки — ноль, то и токенов, соответственно, нет
    ‘’’
    def maxmatch(line):
        if len(line) == 0:
            return '\n'
        try:
            word = next(w for w in new_dictionary if line.startswith(w))
        except StopIteration:
            word = line[0]
        return (word+ ' ' + maxmatch(line[len(word):]))

    list = lines_sent

    for line in list:
        sentences_tokenized = maxmatch(line)
        print(sentences_tokenized)
            
В итоге мы получаем файл с предложениями, разбитыми на токены. 
            
Чтобы иметь возможность вводить предложения из командной строки, в программу нужно импортировать sys, а также добавить следующее:   

    for line in sys.stdin:
        for word in maxmatch(line):
            print(word)

С помощью команды 

    $ grep '^[0-9]' ja_gsd-ud-test.conllu | cut -d $'\t'  -f2 > correct_sentences_tokenized.txt
    
получаем файл с токенами, которые правильно и последовательно выделены из наших тестовых предложений. 



