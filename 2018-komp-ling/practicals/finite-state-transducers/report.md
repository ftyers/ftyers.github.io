## Lexicon construction

I noticed that one letter of Chuvash alphabet is missing in the HFST tutorial: **ӳӲ** (*luckily I am a native Chuvash language speaker :)* ). I added then to the command, so that the words containing this letter would not be omitted:

```
$ cat chv.crp.txt  | sed 's/[^а-яӑӗăĕҫçӳА-ЯӐӖĂĔҪÇӲ]\+/ /g' | tr ' ' '\n' | sort -f | uniq -c | sort -gr
```

*I counted differences that this modification made with ```wc -l``` , but it didn't make any difference. I expected that the amount of words will be increased. For some reasons, it didn't.*

**NB!** As a corpus (to count word frequencies) I used Chuvash wikipedia damp (lang code: **cv**). To extract texts, WikiExtractor was used.

Overall corpus size (word tokens): **2,458,544**
Word types (unique tokens): **172,336**

The results were written to *freq.txt* file:

```
$ cat chv.crp.txt  | sed 's/[^а-яӑӗăĕҫçӳА-ЯӐӖĂĔҪÇӲ]\+/ /g' | tr ' ' '\n' | sort -f | uniq -c | sort -gr > freq.txt
```


## Coverage Results
```
$ calc "(($total-$unknown)/$total)*100"
	~0.13394403330576701513
```
=> So it surns out that my current analyzer has a coverage of oevr 13%, which is just a bit higher than in our HFST tutorial.



## Weighing. Surface forms

I am including this results to this reports because they differ (slightly) from the HFST tutorial results:

```
$ echo "область" | hfst-lookup -qp chv.surweights.hfst
область	область	11,413600

$ echo "облаç" | hfst-lookup -qp chv.surweights.hfst
облаç	облаç	10,017400
```

This difference is absolutely normal, because in the tutorial they used a different corpus.

Anyway, it's interesting that despite the corpora are different (mine is a Wikipedia dump and over 2M, another one is news and about 300K), the results are similar.

