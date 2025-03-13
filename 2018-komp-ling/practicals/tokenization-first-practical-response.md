# Tokenization report

The main problem I had when implementing MaxMatch is error in recursion. Fortunately, everything worked when I checked the last element of my dictionary - it was empty, that was the problem. After deleting it everything went smoothly.

I checked the results on test data using Word Error Rate calculating code (https://github.com/zszyellow/WER-in-python). I used first ~600-700 lines of the sentences I tokenized using my MaxMatch (see 1.txt) and compared them to the same sentences correctly tokenized (extracted from the data using sed expressions, see 2.txt). The result (result.txt) is 13.09% which is quite good. I believe when I check the whole data it would be even lower (I'll update my repo when my laptop finishes with full calculations).

I also provide the files I used during this task:
- dict.txt (prepared dictionary)
- sentences-to-tokenize-train.txt (full sentences from train.conlluu file)
- sentences-to-tokenize-test.txt (full sentences from test.conlluu file to check my algorithm)
- sentences-tokenized-train.txt (the result of train data after MaxMatch)
- sentences-tokenized-test.txt (the result of test data after MaxMatch)
- sentences-correct-train (the correct tokenization of train.conlluu file)
- sentences-correct-test (the correct tokenization of test.conlluu file)
