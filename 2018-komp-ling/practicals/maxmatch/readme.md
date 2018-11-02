This is an implementation of maxmatch tokenization algorithm.
# Usage
I recommend using it like this:
```
python maxmatch.py --extract-dictionary ja_gsd-ud-train.conllu > dictionary.txt
python maxmatch --use-dictionary dictionary.txt --maxmatch ja_gsd-ud-test.conllu | tee output.txt
```
# Requirements
This library requiers library ```connlu``` that parses .conllu-formatted files. I'm sorry to include a dependency into a homework, but connlu itself has no dependencies and is installed via ```pip install connlu``` on any version of Python.
