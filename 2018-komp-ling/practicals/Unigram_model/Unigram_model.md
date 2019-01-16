**Unigram model**


    print('\t' + '\t'.join(eng))
    for w1 in m:
        print('%s\t' % (w1), end='')
        for w2 in m[w1]:
                print('%d\t' % (m[w1][w2]), end='')
        print('')
        
* *Why do we need end='' passed to the print() statement ? What would happen if we didn't have it ?*

В Python у функции print() есть параметр ‘end’, который по умолчанию имеет значение ‘\n’, т.е. каждое выражение print() выводится в новой строке (после объекта функции печатается новая строка). Таким образом, если не задавать значение параметра end как ‘’, то значения m[w1][w2] = 0 будут выводиться под соответствующим w1 в столбик, а не в строку в соответствии с каждым w2, как подразумевалось.

        a	absorbed	all	and	another
    бы	
    0	
    0	
    0	
    0	
    0	

    вас	
    0	
    0	
    0	
    0	
    0	

    видит	
    0	
    0	
    0	
    0	
    0	

* *Save this code to a file called args.py and try running it on the command line as follows:*

       $ python3 args.py a b c 
    
   *What output do you get ?*

Sys.argv — список, в котором содержатся аргументы командной строки, переданные в скрипт. То есть в соответствии с кодом args.py выводятся аргументы командной строки: [‘args.py’, ‘a’, ‘b’, ‘c’]. Если же мы хотим, чтобы печатались только буквы, без названия скрипта ([‘a’, ‘b’, ‘c’]), тогда следует внести изменения в args.py таким образом: 
    
    print(sys.argv[1:len(sys.argv)])

Команда вводится следующим образом:

    python3 train.py en_gum-ud-test.conllu u_model_res.txt 

* *Unigram language model*

Скрипт train.py принимает на вход файл en_gum-ud-test.conllu и записывает результат в файл u_model_res.txt. 

    # P	count	tag	form
    0.08	1100	DET	-
    0.2	2729	NOUN	-
    0.11	1401	ADP	-
    0.07	949	ADJ	-
    0.08	1075	PROPN	-
    0.12	1655	PUNCT	-
    0.03	426	ADV	-
    0.04	475	CCONJ	-
    0.04	576	AUX	-
    0.02	287	NUM	-
    0.1	1351	VERB	-
    0.06	758	PRON	-
    0.0	18	SYM	-
    0.02	277	PART	-
    0.02	215	SCONJ	-
    0.0	32	X	-
    0.0	2	INTJ	-
    1.0	679	DET	the
    1.0	3	NOUN	prevalence
    0.99	369	ADP	of
    0.01	3	SCONJ	of
    0.01	2	NOUN	of
    1.0	18	NOUN	discrimination
    1.0	9	ADP	across

Я привела все слова-токены к нижнему регистру, чтобы слово, употребленное в начале предложение, не считалось другим токеном по сравнению с тем же самым словом, но употребленным в середине или конце предложения (и, таким образом, адекватно подсчитывалась частотность). Если нужно сохранить информацию об именах собственных, можно не использовать метод lower() — правда, в данном случае имена собственные и так имеют теги ‘PROPN’ (адекватность зависит от POS-теггера). 