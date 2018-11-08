<!--
SPDX-License-Identifier: (CC-BY-SA-4.0 OR GFDL-1.3-or-later)
Copyright 2018 Nick Howell,
-->

# Practical 1: Segmentation/Tokenization

<div style="column-width: 30em">

## Comparison of segmenters

I chose to compare segmenters `nltk` and `pragmatic_segmenter`.

### `pragmatic_segmenter`

Create the segmenting program recommended in the practical.

### `nltk`

Here's a sample python program that mimics the behavior of `segmenter.rb` from the
``pragmatic_segmenter`` example; save as `segmenter.py` in the same directory as
`segmenter.rb`

```python
import sys
from nltk.tokenize import sent_tokenize

for line in sys.stdin:
	for sent in sent_tokenize(line)
		print(sent)

```

### Comparison

You can run each segmenter (remember that the command you enter starts with `$` and the response has no prefix).

```bash
$ echo "This is a test.This is a test. This is a test" | python segmenter.py
This is a test.This is a test.
This is a test.
```
```bash
$ echo "This is a test.This is a test. This is a test" | ruby -I. segmenter.rb
This is a test.
This is a test.
This is a test.
```

Here we see qualitatively that `pragmatic_segmenter` handles full-stops better
than the `nltk` segmenter.

For quantitative comparison, a first step is to compare segmentation results:
using the corpus of paragraphs, which I assume is called `wiki.txt`, you can run each
segmenter and compare them using the tool `diff`:

```bash
python segmenter.py < wiki.txt > segmented-nltk
ruby -I. segmenter.rb < wiki.txt > segmented-pragmatic

diff -U0 segmented-nltk segmented-pragmatic
```

Lines starting with `+` appear only in the second file (`segmented-pragmatic`)
and with `-` appear only in the first (`segmented-nltk`). Thus with our test we
would see:

```patch
--- segmented-nltk	2018-11-02 18:53:08.930294409 +0300
+++ segmented-pragmatic	2018-11-02 18:53:18.380294413 +0300
@@ -1 +1,2 @@
-This is a test.This is a test.
+This is a test.
+This is a test.
```

This shows us that `pragmatic_segmenter` split 'This is a test.This is a test.'
(which `nltk` thought was unsplittable) into 'This is a test.' and 'This is a
test.'

You can write a program which loops over the paragraphs in `wiki.txt` and runs
the two segmenters on each of them, and compares the output of the two
segmenters, then run statistics: does `pragmatic_segmenter` produce more or
fewer sentences on average than `nltk`? Are there cases where it's the other
way around? Is there a paragraph where they completely disagree on sentence
boundaries (i.e., there is no place to split sentences where they agree)?

## Tokenization with maxmatch

My maxmatch implementation reads sentences from standard input and writes words
to standard output. To extract sentences from a `.conllu` file, you can search for the comments starting with ""`# text = `"", then strip off that prefix.

```bash
$ grep '^# text = ' ja-test.conllu | sed 's/^# text = //g' > test-sentences
```

To extract the correct segmentation, we filter only the columnar data and choose the second column using `cut`. (The same technique works to create the dictionary file, but remember to discard duplicates using `sort -u` before saving.)

```bash
$ grep '^[0-9]' ja-test.conllu | cut -d'	' -f2 > test-segmented-correct
```

Our segmentation we create using our program; I assume you've called it
`maxmatch.py`:

```bash
$ python maxmatch.py dict < test-sentences > test-segmented-maxmatch
```

You can then apply exactly the same analysis techniques as for analyzing the
sentence segmenters, using `diff` or writing a per-sentence program.

</div>
