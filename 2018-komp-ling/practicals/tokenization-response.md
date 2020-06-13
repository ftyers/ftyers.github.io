# Report for Japanese tokenization task


1. Downloaded train and test sets from Universal Dependencies (UD_Japanese-GSD)

>ja_gsd-ud-train.conllu
>ja_gsd-ud-test.conllu
2. Wrote MaxMatch in file 'max_match.py'

>max_match.py


3. Create a dictionary using the train set (should contain 15,326 forms), but I get 22K and I'm sure it's correct.
- The dictionary in the file 'word_forms_train.txt' was created by the command 
```sh 
$ grep '\^[0-9]' ja_gsd-ud-train.conllu | cut -d $'\t'  -f2 | sort -u
```

4. Test MaxMatch on test set (and train set just for myself):
- extract test sentences with the command
```sh
grep '^# text = ' ja_gsd-ud-test.conllu | sed 's/^# text = //g' > test-sentences.txt
```
- Install conllu module for this, the parsing code is in the file 'conllu_parser.py'
>conllu_parser.py

- had a difficulty importing conllu directly into my python file, because Python doesn't search in the right directory for some reason, and I don't know how to add another path, so I just used this method in python to import the module directly into my fyle:
```sh
sys.path.append() 
```
- extract correctly tokenized tokens into file 'correct_tokenized_test.txt'

> correct_tokenized_test.txt


5. Apply MaxMatch to test set
- Applied MaxMatch to test set in file 'Test_maxmatch.py'
> Test_maxmatch.py
- MaxMatch tokenized sentences into file 'MaxMatchSentences_TEST.txt'
>MaxMatchSentences_TEST.txt

6. Use WER to test the results in the file 'check_wer_test.py'
>check_wer_test.py
- same problem with importing numpy: used sys.path.append to import numpy

Results
>The result for the whole set of 557 sentences is 142%
- I am not sure how to interpret the result, but I guess maxmatch created on average more words than expected. I am willing to investigate the work of WER and the results further

7. Other results:
- Need to learn terminal commands and regex for terminal, right now I can't use them with confidence
- Except for that I've learnt a lot about the steps to be performed for tokenization and its evaluation. However the practical has produced more questions than answers, which is definitely good.

