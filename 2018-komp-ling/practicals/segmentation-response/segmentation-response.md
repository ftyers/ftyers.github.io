<html>
<body>
<head><meta charset="utf-8"></head>
<h2>Segmentation</h2>

<p>Comparison of Pragmatic Segmenter and NLTK's Punkt.</p>

<h3>Data</h3>

<p>Extracting the text: <xmp>$ python3 WikiExctractor.py --infn data.bz2 >wiki.txt</xmp></p>
<p>Shuffle: <xmp>$ sort -R <wiki.txt >randomwiki.txt</xmp></p>
<p>Get 50 paragraphs: <xmp>$ head -n 50 <randomwiki.txt >random50.txt</xmp></p>

<h3>Pragmatic Segmenter</h3>

<p>A rule-based Ruby package for sentence segmentation, works out-of-the-box across many languages.</p>
<p>Segmentation of wiki paragraphs using pragmatic segmenter (the value of the argument "lang" was changed to 'ru'):<br> 
	<xmp>$ ruby -I . segmenter.rb <random50.txt >pragmsegm_results.txt</xmp></p>
<p>Results are in <i>'pragmsegm_results.txt'</i> file.</p>

<h3>NLTK's Punkt</h3>

<p>Machine learning sentence and word tokenizer for Python.</p>
<p>I used pre-trained model for Russian from <a href='https://github.com/Mottl/ru_punkt'>https://github.com/Mottl/ru_punkt</a>.</p>
<p>Python code for tokenizing sentences from stdin is in <i>'sent_tokenize.py'</i> file, the results for Punkt<br>
	are in <i>'nltk_results.txt'</i>.</p>
<p>Bash command: <xmp>$ python sent_tokenize.py <random50.txt >nltk_results.txt</xmp></p>

<h3>Evaluation</h3>
<p>Amount of sentences segmented by hand is 101.</p>
<p>Accuracy<br>
	- for Pragmatic Segmenter: 0.99;<br>
	- for NLTK's Punkt: 0.98.</p>
<p>Well, the data was not really interesting and both segmenters dealed with it equally good.</p>
<p>However, the mistakes were different. For Pragmatic Segmenter it was basic abbreviation in <b>"Церковь Св. Иоанна Крестителя"</b>,<br>
the point was incorrectly recognized as the end of a sentence. Punkt processed this sentence correctly, but made mistakes
when segmenting sentences <b>"Провёл испытания самолётов «С» (лето .) и СПБ (18.02.1940 г.). <br>
Испытывал серийные ТБ-3 (1936 — 1938 гг.), СБ (1936 — 1941 гг.), Ар-2 (.), Пе-2 (.) и их модификации."</b><br>
Punkt made 5 sentences out of 2:<br>
<b>Провёл испытания самолётов «С» (лето .)<br>
и СПБ (18.02.1940 г.).<br>
Испытывал серийные ТБ-3 (1936 — 1938 гг.), СБ (1936 — 1941 гг.), Ар-2 (.<br>
), Пе-2 (.)<br>
и их модификации.</b></p>
<p>Although this is quite a difficult case, Pragmatic Segmenter processed it right.</p>

<h2>Tokenization</h2>

<p>1.Extract a dictionary of segmented surface forms from UD_Japanese-GSD/ja_gsd-ud-train.conllu. The dictionary is in "dictionary.txt" file and contain 22,313 forms.<br>
Code used to extract a dictionary is in "extract_dictionary.py" file.</p>
<p>2.From test.conllu we should extract sentences for further tokenization using maxmatch and golden standart - already tokenized sentences for further evaluation.<br>
Code for this is in "extract_sentences.py" file. Test sentences are in "sentences.txt" and tokenized sentences are in "reference_sentences.txt".</p>
<p>3.Implement maxmatch algorithm and tokenize test data. The implemented algorithm is in "maxmatch.py" file, you should use python3 and give<br>
the names of the dictionary file and the file with sentences to process as an arguments.<br>
python3 maxmatch.py dictionary.txt sentences.txt<br>
The results are in "maxmatch_results.txt" file.</p>
<p>4.Calculate WER. WER for all sentences is 0.435620160428. Well the results could've been better but I guess it's okay.</p>
<p>Let's look, for example, at the third sentence using Comparison plagin in Notepad++.<br>
<img src="./tokenization/comparison.png" width="500" height="40"><br>
Maxmatch didn't recognize 星取り as a whole token, but that's okay because there is no such token in dictionary,<br>
such as there is no token 白眼視 wich was recognized as 3 forms, although I can guess that these tokens may be some forms of words<br>
in the dictionary, but I don't know Japanese, so...<br>
Also, I discovered that there are many sentences with two whitespaces in the end in results file, it possibly have caused WER to be higher that expected<br>
but I tried to write a function that deletes it and counted WER again and result was the same.</p>

</body>
</html>