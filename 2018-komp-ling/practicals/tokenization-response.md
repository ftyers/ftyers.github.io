# Sentence tokenization

## Preprocessing

`dict.py` processes `ja_gsd-ud-train.conllu` and produces 3 files:
-`dict.txt` – file with dictionary (list of standalone tokens)
-`sentences.txt` – file with list of the sentences where tokens are not split (7 164 items)
-`train.txt`– file with list of the sentences every of each consists of standalone tokens, according to `ja_gsd-ud-train.conllu`

## MaxMatch script

`maxmatch.py` – takes dictionary files as first argument and sentences to split as second argument or from standard input

## Testing

To test tokenizer one needs to take unsplit sentences from `ja_gsd-ud-test.conllu`. Actually, they seems to be the same as were extracted from `ja_gsd-ud-train.conllu`

### diff
After running `maxmatch.py dict.txt sentences.txt > test.txt` we got file `test.txt`
```bash
diff -U  0 train.txt out.txt | grep -c ^@
815
```
I guess, it's not bad result regarding to sentences, but as to token-to-token mapping accuracy is not so good.

### WER

As to [WER](https://github.com/zszyellow/WER-in-python), unfortunately, on the machine with Python 2.7 (Debian 8, KVM, 1 GB RAM) it crashes with this error:
```python
Traceback (most recent call last):
  File "wer.py", line 204, in <module>
    wer(r, h)
  File "wer.py", line 189, in wer
    d = editDistance(r, h)
  File "wer.py", line 17, in editDistance
    d = numpy.zeros((len(r)+1)*(len(h)+1), dtype=numpy.uint8).reshape((len(r)+1, len(h)+1))
MemoryError
```
## Performance
On an i3 of the year 2011 the code took less than 8 min to complete the job:

```bash
real    7m44,939s
user    0m0,000s
sys     0m0,031s
```
On the 20 sentences sample in above mentioned KVM environment it worked 1 sec, so ≈ 0.05 per sentence. It's not super slow, but rather not ready for production.