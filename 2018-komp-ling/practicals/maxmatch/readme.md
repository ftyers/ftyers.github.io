This is an implementation of maxmatch tokenization algorithm.
# Usage
I recommend using it like this:
```
python maxmatch.py --extract-dictionary ja_gsd-ud-train.conllu > dictionary.txt
python maxmatch.py --use-dictionary dictionary.txt --maxmatch ja_gsd-ud-test.conllu | tee output.txt
```
# Requirements
This library requiers library ```connlu``` that parses .conllu-formatted files. I'm sorry to include a dependency into a homework, but connlu itself has no dependencies and is installed via ```pip install connlu``` on any version of Python.

# Analysis

It was too computationally hard to evaluate WER upon the whole corpus because this metric is computed recursively.
Instead, I evaluated mean WER upon all couples "output sentence -- target sentence".
The mean WER was 25.87%.
It's hard for me to analyze the result as I'm comletely unfamiliar with the Japanese language; however, I spotted some interesting occasions with non-hieroglypic elements in the Japanese language.
For instance, "JavaScript" was tokenized as "Java S c r i p t" because Java was in the dictionary and Script wasn't. It also split 1466 into 14 6 6.
MaxMatch fails with words in latin chars and digits, just as the textbook said.
