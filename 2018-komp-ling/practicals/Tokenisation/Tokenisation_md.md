
# Tokenisation

1) Downloaded train and test set of UD_Japanese-GSD

2) Got forms and sentences files for both sets using recommended commands in bash


cat ja_gsd-ud-train.conllu  | grep '^[0-9]' | cut -f2 | sort -f | uniq -c | sort -gr > forms.txt


$ cat ~/source/UniversalDependencies/UD_Japanese-GSD/ja_gsd-ud-train.conllu | grep '# text = ' | cut -f2 -d'=' | sed 's/^ *//g'> sentences.txt. 

Located files to my repo file

3) Created dictionatry of the forms and check all existing lengths of extracted words


```python
import numpy as np
```


```python
forms = "C://mcl2018_hw1_babakov//practicals//Tokenisation//forms.txt"
dictionary = {}
lines = 0
with open(forms,'r',encoding = 'utf-8') as f: 
    for line in f:
        lines += 1
        if (line not in dictionary):
            dictionary[line[:-1]] = 1
    print('dictionary_length = ', len(dictionary), 'total_lines = ', lines)
```

    dictionary_length =  22313 total_lines =  161900
    


```python
collected_length = []
for name in dictionary:
    length = len(name)
    if (length not in collected_length):
        print (name,length)
        collected_length.append(length)
```

    info 4
    425001-435001-435501-425501 27
    22380 5
    20257/8 7
    2008-2009 9
    1447-1 6
    972 3
    673-0405 8
    99 2
    9 1
    ユーゴスラビア連邦軍 10
    福岡ソフトバンクホークス 12
    マイクロソフト株式会社 11
    voodoowedding 13
    VLCMediaPlayer 14
    UnitedMusicPublishersLtd 24
    TheMagazineofFantasy 20
    TheEmotionMachine 17
    TheCorporationoftheCityofSarnia 31
    theCHEMISTRYjointalbum 22
    TechnicalDesignReport 21
    TARGETfrontierJV 16
    TakamiyClassics 15
    PaulKantner'sWoodenship 23
    MozillaThunderbird 18
    http://en.wikipedia.org/wiki/Acute_intermittent_porphyria 57
    EnterpriseJavaBeans 19
    EconomicCommunitiyofWestAfricanStates 37
    Daisenguchistationmonument 26
    アニメポケットモンスターオリジナルサウンドトラックベスト 28
    

4) Implement MaxMatch using recursion  and apply it to train set


```python
def MaxMatch(line):
    parsed_line = []
    parsed_rest_line = []
    line = line.replace(" ", "")
    found_dict_symb = False
    
    for char_index in range(len(line)-1,0,-1):
        phrase_under_review = ''
        phrase_under_review = line[:char_index]
        if (phrase_under_review in dictionary):
            parsed_line.append(phrase_under_review)
            if(len(line[char_index:]) >= 2):
                parsed_rest_line = MaxMatch(line[char_index:])
                parsed_line += parsed_rest_line
                found_dict_symb = True
            else:#if the next is empty
                return parsed_line
            
            return parsed_line 
    if (found_dict_symb == False):
        parsed_line += line[0]
        if(len(line) >= 2):
            parsed_rest_line = MaxMatch(line[1:])
        else:
            return parsed_line 
        
        parsed_line += parsed_rest_line
        return parsed_line 

text = "C://mcl2018_hw1_babakov//practicals//Tokenisation//sentences.txt"
parsed_sentences = []
with open(text,'r',encoding = 'utf-8') as t:
    print_count = 0 
    for line in t:
        parsed = MaxMatch(line)
        if(print_count < 10):
            print("============")
            print(line)
            print(parsed,'\n')
        parsed_sentences.append(parsed)
        print_count += 1
```

    ============
     ホッケーにはデンジャラスプレーの反則があるので、膝より上にボールを浮かすことは基本的に反則になるが、その例外の一つがこのスクープである。
    
    ['ホッケー', 'に', 'は', 'デンジャラスプレー', 'の', '反則', 'が', 'ある', 'ので', '、', '膝', 'より', '上', 'に', 'ボール', 'を', '浮かす', 'こと', 'は', '基本的', 'に', '反則', 'に', 'なる', 'が、', 'その', '例外', 'の', '一', 'つ', 'が', 'この', 'スクープ', 'である', '。'] 
    
    ============
     また行きたい、そんな気持ちにさせてくれるお店です。
    
    ['また', '行き', 'たい', '、', 'そんな', '気持ち', 'に', 'させ', 'て', 'くれる', 'お', '店', 'です', '。'] 
    
    ============
     手に持った特殊な刃物を使ったアクロバティックな体術や、揚羽と薄羽同様にクナイや忍具を使って攻撃してくる。
    
    ['手', 'に', '持っ', 'た', '特殊', 'な', '刃物', 'を', '使っ', 'た', 'アクロバティック', 'な', '体', '術', 'や', '、', '揚羽', 'と', '薄羽', '同様', 'に', 'クナイ', 'や', '忍具', 'を', '使っ', 'て', '攻撃', 'し', 'て', 'くる', '。'] 
    
    ============
     3年次にはトータルオフェンスで2,892ヤードを獲得し、これは大学記録となった。
    
    ['3', '年次', 'に', 'は', 'トータルオフェンス', 'で', '2,892', 'ヤード', 'を', '獲得', 'し', '、', 'これ', 'は', '大学', '記録', 'と', 'なっ', 'た', '。'] 
    
    ============
     葬儀の最中ですよ!
    
    ['葬儀', 'の', '最中', 'です', 'よ', '!'] 
    
    ============
     1998年度に着手し、道の駅遠山郷北側からかぐら大橋南詰現道交点までの1.060 kmのみ開通済み。
    
    ['1998', '年度', 'に', '着手', 'し', '、', '道', 'の', '駅', '遠山郷', '北', '側', 'から', 'かぐら', '大橋', '南', '詰', '現道', '交点', 'まで', 'の', '1.060', 'km', 'のみ', '開通', '済み', '。'] 
    
    ============
     そして、第40話でそのカオルと百子をも失い、完全に孤児になってゲンとともに美山家に身を寄せ、またゲンに連れ添って円盤生物を調査するパートナーとなる。
    
    ['そして', '、', '第', '40', '話', 'で', 'その', 'カオル', 'と', '百子', 'を', 'も', '失い', '、', '完全', 'に', '孤児', 'に', 'なっ', 'て', 'ゲン', 'とともに', '美', '山家', 'に', '身', 'を', '寄せ', '、', 'また', 'ゲン', 'に', '連れ添っ', 'て', '円盤', '生物', 'を', '調査', 'する', 'パートナー', 'と', 'なる', '。'] 
    
    ============
     一般的な層流翼型と比べ負圧中心が前進し、圧力勾配はなだらかである。
    
    ['一般的', 'な', '層流', '翼', '型', 'と', '比べ', '負', '圧', '中心', 'が', '前進', 'し', '、', '圧力', '勾配', 'は', 'なだらか', 'である', '。'] 
    
    ============
     一直線に伸びる電撃を放ち、電撃ダメージを与える。
    
    ['一', '直線', 'に', '伸びる', '電撃', 'を', '放ち', '、', '電撃', 'ダメージ', 'を', '与える', '。'] 
    
    ============
     配属されて最初の1カ月こそ「親切な先輩に恵まれてラッキーだな」と思ったものの、その後すぐに「ちょっとおせっかいかな」と感じるようになり、半年後には「少し邪魔かも」と思い、1年後には「生産性の阻害要因だ」と確信するに至りました。
    
    ['配属', 'さ', 'れ', 'て', '最初', 'の', '1', 'カ月', 'こそ', '「', '親切', 'な', '先輩', 'に', '恵まれ', 'て', 'ラッキー', 'だ', 'な', '」', 'と', '思っ', 'たも', 'の', 'の', '、', 'その後', 'すぐ', 'に', '「', 'ちょっと', 'おせっかい', 'かな', '」', 'と', '感じる', 'ように', 'なり', '、', '半年', '後', 'に', 'は', '「', '少し', '邪魔', 'か', 'も', '」', 'と', '思い', '、', '1', '年', '後', 'に', 'は', '「', '生産性', 'の', '阻害', '要因', 'だ', '」', 'と', '確信', 'する', 'に', '至り', 'まし', 'た', '。'] 
    
    

5) Apply to test set


```python
text = "C://mcl2018_hw1_babakov//practicals//Tokenisation//sentence_test.txt"
parsed_sentences_test = []
with open(text,'r',encoding = 'utf-8') as t:
    print_count = 0 
    for line in t:
        parsed = MaxMatch(line)
        if(print_count < 10):
            print("============")
            print(line)
            print(parsed,'\n')
        parsed_sentences_test.append(parsed)
        print_count += 1
```

    ============
    ﻿これに不快感を示す住民はいましたが,現在,表立って反対や抗議の声を挙げている住民はいないようです。
    
    ['\ufeff', 'これ', 'に', '不快', '感', 'を', '示す', '住民', 'は', 'いま', 'し', 'たが', ',', '現在', ',', '表', '立っ', 'て', '反対', 'や', '抗議', 'の', '声', 'を', '挙げて', 'いる', '住民', 'は', 'い', 'ない', 'ようで', 'す', '。'] 
    
    ============
    幸福の科学側からは,特にどうしてほしいという要望はいただいていません。
    
    ['幸福', 'の', '科学', '側', 'から', 'は', ',', '特に', 'どうして', 'ほしい', 'という', '要望', 'は', 'いただい', 'て', 'いま', 'せ', 'ん', '。'] 
    
    ============
    星取り参加は当然とされ,不参加は白眼視される。
    
    ['星', '取り', '参加', 'は', '当然', 'と', 'さ', 'れ', ',', '不', '参加', 'は', '白', '眼', '視', 'さ', 'れる', '。'] 
    
    ============
    室長の対応には終始誠実さが感じられた。
    
    ['室長', 'の', '対応', 'に', 'は', '終始', '誠実', 'さ', 'が', '感じ', 'られ', 'た', '。'] 
    
    ============
    多くの女性が生理のことで悩んでいます。
    
    ['多く', 'の', '女性', 'が', '生', '理', 'の', 'こと', 'で', '悩ん', 'で', 'いま', 'す', '。'] 
    
    ============
    先生の理想は限りなく高い。
    
    ['先生', 'の', '理想', 'は', '限り', 'なく', '高い', '。'] 
    
    ============
    それは兎も角,私も明日の社説を楽しみにしております。
    
    ['それ', 'は', '兎', 'も', '角', ',', '私', 'も', '明日', 'の', '社', '説', 'を', '楽しみ', 'に', 'し', 'て', 'おり', 'ます', '。'] 
    
    ============
    そうだったらいいなあとは思いますが,日本学術会議の会長談話について“当会では,標記の件について,以下のように考えます。”
    
    ['そうだっ', 'たら', 'いい', 'なあ', 'と', 'は', '思い', 'ます', 'が', ',', '日本学術会議', 'の', '会長', '談', '話', 'について', '“', '当', '会', 'では', ',', '標記', 'の', '件', 'について', ',', '以下', 'のよ', 'う', 'に', '考え', 'ます', '。', '”'] 
    
    ============
    教団にとっては存続が厳しくなると思う。
    
    ['教団', 'にとって', 'は', '存続', 'が', '厳しく', 'なる', 'と', '思う', '。'] 
    
    ============
    しかし強制していなくても問題です
    
    ['しかし', '強制', 'し', 'て', 'い', 'なく', 'て', 'も', '問題', 'です'] 
    
    

6) Write results to txt


```python
with open("C://mcl2018_hw1_babakov//practicals//Tokenisation//sentence_test_parsed.txt", 'w',encoding = 'utf-8') as f:
    for t in parsed_sentences_test:
        f.write(' '.join(str(s) for s in t) + '\n')
```

7) Extract correctly tokenized test text for further evaluation


```python
test_conllu = "C://mcl2018_hw1_babakov//practicals//Tokenisation//ja_gsd-ud-test.conllu"
parsed_file = []
print_count = 0
with open(test_conllu, "r", encoding = 'utf-8') as data:
    parsed_sentence = [] 
    for line in data:
        row = line.split('\t')
        if('# text =' in row[0] and print_count < 10):
            print('found text', row[0][8:-1])
        if(str(row[0]).isdigit()):
            parsed_sentence.append(row[1])
        else:
            if parsed_sentence:
                parsed_file.append(parsed_sentence)
                if (print_count < 10):
                    print(parsed_sentence)
                    print_count += 1
            parsed_sentence = []
            
```

    found text  これに不快感を示す住民はいましたが,現在,表立って反対や抗議の声を挙げている住民はいないようです。
    ['これ', 'に', '不快感', 'を', '示す', '住民', 'は', 'い', 'まし', 'た', 'が', ',', '現在', ',', '表立っ', 'て', '反対', 'や', '抗議', 'の', '声', 'を', '挙げ', 'て', 'いる', '住民', 'は', 'い', 'ない', 'よう', 'です', '。']
    found text  幸福の科学側からは,特にどうしてほしいという要望はいただいていません。
    ['幸福', 'の', '科学', '側', 'から', 'は', ',', '特に', 'どうして', 'ほしい', 'という', '要望', 'は', 'いただい', 'て', 'い', 'ませ', 'ん', '。']
    found text  星取り参加は当然とされ,不参加は白眼視される。
    ['星取り', '参加', 'は', '当然', 'と', 'さ', 'れ', ',', '不', '参加', 'は', '白眼視', 'さ', 'れる', '。']
    found text  室長の対応には終始誠実さが感じられた。
    ['室長', 'の', '対応', 'に', 'は', '終始', '誠実', 'さ', 'が', '感じ', 'られ', 'た', '。']
    found text  多くの女性が生理のことで悩んでいます。
    ['多く', 'の', '女性', 'が', '生理', 'の', 'こと', 'で', '悩ん', 'で', 'い', 'ます', '。']
    found text  先生の理想は限りなく高い。
    ['先生', 'の', '理想', 'は', '限りなく', '高い', '。']
    found text  それは兎も角,私も明日の社説を楽しみにしております。
    ['それ', 'は', '兎', 'も', '角', ',', '私', 'も', '明日', 'の', '社説', 'を', '楽しみ', 'に', 'し', 'て', 'おり', 'ます', '。']
    found text  そうだったらいいなあとは思いますが,日本学術会議の会長談話について“当会では,標記の件について,以下のように考えます。”
    ['そう', 'だっ', 'たら', 'いい', 'なあ', 'と', 'は', '思い', 'ます', 'が', ',', '日本学術会議', 'の', '会長', '談話', 'について', '“', '当', '会', 'で', 'は', ',', '標記', 'の', '件', 'について', ',', '以下', 'の', 'ように', '考え', 'ます', '。', '”']
    found text  教団にとっては存続が厳しくなると思う。
    ['教団', 'にとって', 'は', '存続', 'が', '厳しく', 'なる', 'と', '思う', '。']
    found text  しかし強制していなくても問題です
    ['しかし', '強制', 'し', 'て', 'い', 'なく', 'て', 'も', '問題', 'です']
    

8) Write results to sentences_test_correctly_parsed.txt


```python
with open("C://mcl2018_hw1_babakov//practicals//Tokenisation//sentences_test_correctly_parsed.txt", 'w',encoding = 'utf-8') as f:
    for t in parsed_file:
        f.write(' '.join(str(s) for s in t) + '\n')
```

9) Evaluate maxmatch results


```python
import numpy


def editDistance(r, h):

    '''

    This function is to calculate the edit distance of reference sentence and the hypothesis sentence.

    Main algorithm used is dynamic programming.

    Attributes: 

        r -> the list of words produced by splitting reference sentence.

        h -> the list of words produced by splitting hypothesis sentence.

    '''

    d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8).reshape((len(r)+1, len(h)+1))

    for i in range(len(r)+1):

        for j in range(len(h)+1):

            if i == 0: 

                d[0][j] = j

            elif j == 0: 

                d[i][0] = i

    for i in range(1, len(r)+1):

        for j in range(1, len(h)+1):

            if r[i-1] == h[j-1]:

                d[i][j] = d[i-1][j-1]

            else:

                substitute = d[i-1][j-1] + 1

                insert = d[i][j-1] + 1

                delete = d[i-1][j] + 1

                d[i][j] = min(substitute, insert, delete)

    return d



def getStepList(r, h, d):

    '''

    This function is to get the list of steps in the process of dynamic programming.

    Attributes: 

        r -> the list of words produced by splitting reference sentence.

        h -> the list of words produced by splitting hypothesis sentence.

        d -> the matrix built when calulating the editting distance of h and r.

    '''

    x = len(r)

    y = len(h)

    list = []

    while True:

        if x == 0 and y == 0: 

            break

        elif x >= 1 and y >= 1 and d[x][y] == d[x-1][y-1] and r[x-1] == h[y-1]: 

            list.append("e")

            x = x - 1

            y = y - 1

        elif y >= 1 and d[x][y] == d[x][y-1]+1:

            list.append("i")

            x = x

            y = y - 1

        elif x >= 1 and y >= 1 and d[x][y] == d[x-1][y-1]+1:

            list.append("s")

            x = x - 1

            y = y - 1

        else:

            list.append("d")

            x = x - 1

            y = y

    return list[::-1]



def alignedPrint(list, r, h, result):

    '''

    This funcition is to print the result of comparing reference and hypothesis sentences in an aligned way.

    

    Attributes:

        list   -> the list of steps.

        r      -> the list of words produced by splitting reference sentence.

        h      -> the list of words produced by splitting hypothesis sentence.

        result -> the rate calculated based on edit distance.

    '''

   # print ("REF:",)

    for i in range(len(list)):

        if list[i] == "i":

            count = 0

            for j in range(i):

                if list[j] == "d":

                    count += 1

            index = i - count

            #print (" "*(len(h[index])),)

        elif list[i] == "s":

            count1 = 0

            for j in range(i):

                if list[j] == "i":

                    count1 += 1

            index1 = i - count1

            count2 = 0

            for j in range(i):

                if list[j] == "d":

                    count2 += 1

            index2 = i - count2

            """if len(r[index1]) < len(h[index2]):

                print (r[index1] + " " * (len(h[index2])-len(r[index1])),)

            else:

                print (r[index1],)"""

        else:

            count = 0

            for j in range(i):

                if list[j] == "i":

                    count += 1

            index = i - count

            #print (r[index],)

    #print ("HYP:",)

    for i in range(len(list)):

        if list[i] == "d":

            count = 0

            for j in range(i):

                if list[j] == "i":

                    count += 1

            index = i - count

            #print (" " * (len(r[index])),)

        elif list[i] == "s":

            count1 = 0

            for j in range(i):

                if list[j] == "i":

                    count1 += 1

            index1 = i - count1

            count2 = 0

            for j in range(i):

                if list[j] == "d":

                    count2 += 1

            index2 = i - count2

            """if len(r[index1]) > len(h[index2]):

                print (h[index2] + " " * (len(r[index1])-len(h[index2])),)

            else:

                print (h[index2],)"""

        else:

            count = 0

            for j in range(i):

                if list[j] == "d":

                    count += 1

            index = i - count

            #print (h[index],)

    #print ("EVA:",)

    for i in range(len(list)):

        if list[i] == "d":

            count = 0

            for j in range(i):

                if list[j] == "i":

                    count += 1

            index = i - count

            #print ("D" + " " * (len(r[index])-1),)

        elif list[i] == "i":

            count = 0

            for j in range(i):

                if list[j] == "d":

                    count += 1

            index = i - count

            #print ("I" + " " * (len(h[index])-1),)

        elif list[i] == "s":

            count1 = 0

            for j in range(i):

                if list[j] == "i":

                    count1 += 1

            index1 = i - count1

            count2 = 0

            for j in range(i):

                if list[j] == "d":

                    count2 += 1

            index2 = i - count2

            """if len(r[index1]) > len(h[index2]):

                print ("S" + " " * (len(r[index1])-1),)

            else:

                print ("S" + " " * (len(h[index2])-1),)"""

        else:

            count = 0

            for j in range(i):

                if list[j] == "i":

                    count += 1

            index = i - count

            #print (" " * (len(r[index])))



    #print ("WER: " + result)

    return result



def wer(r, h):

    """

    This is a function that calculate the word error rate in ASR.

    You can use it like this: wer("what is it".split(), "what is".split()) 

    """

    # build the matrix

    d = editDistance(r, h)



    # find out the manipulation steps

    list = getStepList(r, h, d)



    # print the result in aligned way

    #result = float(d[len(r)][len(h)]) / len(r) * 100

    result = float(d[len(r)][len(h)]) / len(r)

    #result = str("%.2f" % result) + "%"

    WER = alignedPrint(list, r, h, result)

    return WER
```


```python
#It turned out that some sentences have whitespace in the beginning. that is why I decided to implement this function
def delete_first_whitespace(line):
    ind = 0 
    while (line[ind] == ' '):
        ind += 1
    return line [ind:]
    
delete_first_whitespace('   test')
```




    'test'




```python
sentences_parsed = "C://github//ftyers.github.io//2018-komp-ling//practicals//Tokenisation//sentence_test_parsed.txt"
coorect_parsed = "C://github//ftyers.github.io//2018-komp-ling//practicals//Tokenisation//sentences_test_correctly_parsed.txt"
```


```python
import statistics
```


```python
with open(coorect_parsed, "r", encoding = 'utf-8') as reference, open(sentences_parsed, "r", encoding = 'utf-8') as hypo: 
    wer_overall = []
    print_count = 0 
    for r, h in zip(reference, hypo):
        #get rid of whitespaces in front
        r = delete_first_whitespace(r)
        h = delete_first_whitespace(h)
        #get list of tokenized words
        r = r.split()
        h = h.split()
        wer_ind = wer(r,h)
        wer_overall.append(wer_ind)

    overall_wer_median = statistics.median(wer_overall)
    print(overall_wer_median)      
```

    0.23076923076923078
    
