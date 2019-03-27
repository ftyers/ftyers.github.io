$cat test.txt | python3 segmenter.py | python3 tokenizer.py | python3 tagger.py uni_model.conllu > result.conllu

1. How accurate is the tagger?

The tagger works almost perfectly. Looking at the result, it is possible to notice some places that might need improvement - for example, the tagger determend the conjunction "и" as a participle or could not determine "-". But these are considerably small issues.

2. How could you improve performance without incorporating context ...

	a) using Python string functions?
	
	From the Python string methods "split" and "join" were used, also it could've been useful to check the "isupper" for the first letter of the word to determine it as a proper noun.  
	
	b) using regular expressions?
	
	The only thing that comes to my mind right now is that regular expression are usually used to find a pattern - so for Russian it could be as simple as trying to identify a two-letter word and a multiple letter word after it as preposition and noun. 
	
	c) using screen scraping?
	
	It would be useful to work with word information (as in the example with HTML scrapping) from various sources, for example, we could use to find all of the word forms for one word and merge them into one dictionary for the language model to recognize it better. 
