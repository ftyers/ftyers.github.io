# Maxmatch Algorithm Instructions
##### *Anastasia Nikiforova*
---
The algorithm is presented in ```maxmatch.py```.

First, the conllu files need to be parsed. I used the following terminal commands to:
1. Extract sentences
    ```
    $ grep '^# text = ' ja_gsd-ud-train.conllu | sed 's/^# text = //g' > train-sentences
    ```
    Here we match all lines starting with specified regex and then delete the beginning of the line leaving just a plain sentence.

2. Extract correctly segmented tokens (second column)
    ```
    $ grep '^[0-9]' ja_gsd-ud-test.conllu | cut -f2 > test-segmented-correct
    ```
    All lines containing tokens begin with a number (1,2,3 etc.). Here we extract this tokens by finding lines starting with a number and cutting the second "field" from the line
3. Collect dictionaries (unique correctly segmented tokens)
    ```
    $ grep '^[0-9]' ja_gsd-ud-test.conllu | cut -f2 | sort -u  > train-dictionary
    ```
    Unique of what's in (2)

4. Run maxmatch from ```maxmatch.py```
    ```
    python3 maxmatch.py train-dictionary < test-sentences > maxmatch-results
    ```
    We need to use the dictionary as an argument, and then feed the sentences to the maxmatch algorithm. Tokenized sentences are written to ```maxmatch-results.txt```
    
### Performance

The maxmatch algorithm I have written have found 19362 tokens instead of 12635 correct ones.

The results of the WER on 1000 sentences 14%
