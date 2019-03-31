
# Tokenisation report
For the current task maxmatch algorithm was implemented (you can see it in the same folder with this report).

As a prerequirement a list of unique words should be prepared.

There are 2 inputs for the algorithm:
- a sentence for tokenisation
- a list of unique words.

### Examples
Original sentence:
> これに不快感を示す住民はいましたが,現在,表立って反対や抗議の声を挙げている住民はいないようです。

Original tokenisation:
> 'これ', 'に', '不快感', 'を', '示す', '住民', 'は', 'い', 'まし', 'た', 'が', ',', '現在', ',', '表立っ', 'て', '反対', 'や', '抗議', 'の', '声', 'を', '挙げ', 'て', 'いる', '住民', 'は', 'い', 'ない', 'よう', 'です', '。'

Maxmatch tokenisation:
> 'これ', 'に', '不快', '感', 'を', '示す', '住民', 'は', 'いま', 'し', 'たが', ',', '現在', ',', '表', '立っ', 'て', '反対', 'や', '抗議', 'の', '声', 'を', '挙げて', 'いる', '住民', 'は', 'い', 'ない', 'ようで', 'す', '。'

These are tokenisation errors for this sentence:
- '不快' and '感' instead of '不快感' (*oversegmentation*)
- 'いま' and 'し' instead of 'い' and 'まし'
- 'たが' instead of 'た' and 'が'
- '表', '立っ'and 'て' instead of '表立っ'
- '挙げて' instead of '挙げ' and 'て'
- 'ようで' and 'す' instead of 'よう' and 'です'

### Evaluation

As an evaluation metric WER (Word Error Rate) was used.
WER for first 100 sentences of the test dataset was about 23%.
