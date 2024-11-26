# Tokenization

To apply a maxMatch algo, you need a dictionary. So, I made one.
Firstly, I downloaded japanese_trainings conllu file. Then I parsed them using bash commands. 
1. delete all comments
> sed '/^#/d' ja_gsd-ud-train.conllu > japanese_dict.txt
2. delete all blank lines
> sed '/^\s*$/d' japanese_dict.txt > japanese_dict_no_empty_lines.txt

Also you need a data to test on. Here is mine.
I downloaded japanese_test conllu file and extracted a text from it with this bash commands:
1. extract texts
> sed -n '/^# text =/p' ja_gsd-ud-test.conllu > japanese_test_texts.txt
2. delete '# text = ' tags
> sed 's/^# text =//' japanese_test_texts.txt > japanese_texts.txt


Then I wrote [Python code](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%201/Tokenization/Tokenisation.py) to tokenize text using [maxMatch](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%201/Tokenization/maxmatch.py) algorithm (suggested in Jurafsky & Martin's book).  
[Here](https://github.com/Veranchos/ftyers.github.io/blob/master/2018-komp-ling/practicals/Practical%201/Tokenization/tokenization_result.txt) is the result. All the tokens are separated with commas.

