# Practical 1
##### Tsvetkova Victoria 

### Tokenization

My maxmatch takes three arguments: a dictionary file, sentences and tokens (which = 0 and implemented in the script). First it prepare the sentences deleting all Japanese punctuation. Then it tokenizes them line by line and write them in a file. The tokenize proccess is the following:
First we iterate over the given sentence from the end to the beginning. When we find a word matching a word from the dictionary, we add the word to the list of tokens and then cut the last len(word) symbols from the sentence. Then, the process starts again.

To evaluate its performance I had to delete the Japanese punctuation also from the reference file. I used [this WER code](https://github.com/imalic3/python-word-error-rate) and got 58%. The difference result can be seen in diff.html file with different colour markers:
* red colour means missing words in the hypothesis file. There are quite many of such words: it seems that the maxmatch couldn't find them in the dictionary, that's why it skipped them during the tokenization process. "歳" is a good example of a word missing in our train data.
* yellow colour implicates substitution words, which means basically "wrong split", This mistake multiplies itself as one wrong split means that the next word will be split wrong, too: いま (い ) し (まし ) = hypothesis (reference).
* green colour stands for inserting words. In our case that also means wrong split: 産業 構造 (産業構造 ) = hypothesis (reference).
