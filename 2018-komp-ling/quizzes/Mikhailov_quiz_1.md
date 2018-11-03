Quiz 1

1. a) requires comprehensive dictionary
   d) constructs non-grammatical sentences

2. ```echo "either/neither", "1/2" | sed 's/\([^0-9]\+\)\/\([^0-9]\+\)/\1 \/ \2/g'```

3. Large data and time requirements
Building machine learning  algorithms requires for a huge amount of collected tagged data. Though there are many corpora available to use, there is no such data for some specific languages. Collecting and tagging specific language data needs plenty of time and other resources. 

Debugging
The output of a certain machine learning algorithm is harder to debug and interpret.

Lack of specific training data
Some output errors may occur due to the lack of specific training data for the machine learning algorithm to make a solid prediction. 

4. In my code, I set the CMU dictionary from nltk corpus as a dictionary for the English language

The sentence: The town was fairly large with a dozen or so business buildings on each side of the street

The input: 'Thetownwasfairlylargewithadozenorsobusinessbuildingsoneachsideofthestreet'

The output: ['T', 'he', 'town', 'was', 'fairly', 'large', 'with', 'ado', 'zenor', 'sob', 'usines', 's', 'buildings', 'one', 'ac', 'h', 'side', 'oft', 'he', 'street']

5. a) ambiguous abbrevations with punctuation

The input: The principal market is on Mon. but there are inferior ones for butter on Wed. Fri. and Sat.


The output: ['The principal market is on Mon.', 'but there are inferior ones for butter on Wed. Fri. and Sat.']

The problem: In this case, the problem appears when segmenting a sentence with relatively disambigous abbreviations with the period character '.'; it is a complex sentence for the sentence segmentation (nltk sentence tokenizer). The problem is that the abbreviation 'Mon.' is perceived as a marker for the end of the sentence (the sentence boundary marker).

b) sentences containing symbols '!' and '?'

Input 1: '"I got the concert tickets!" he exclaimed.'

Output 1: ['"I got the concert tickets!"', 'he exclaimed.']

Input 2: '"Ugh! Why are you yelling at me?" his friend cried.'

Output 2: ['"Ugh!', 'Why are you yelling at me?"', 'his friend cried.']

The problem: In this case, the problem appears when segmenting a sentence with the direct speech. The problem is that the nltk sentence tokenizer takes the question mark '?' and the exclamation mark '!' as the sentence boundary markers. One more problem is whether we consider the utterance as a sentence with the quotation marks as the sentence boundary markers or not.

c) sentences lacking separating punctuation

The input: 'Arrays are really hashtables They grow as needed They take strings (and numbers) as keys'

The output: ['Arrays are really hashtables They grow as needed They take strings (and numbers) as keys']

The problem: When copypasting a text segment from pdf docs or from some sites we can face lacking separating punctuation. The problem is that the three sentences are not tokenized. The nltk sentence tokenizer perceives the input as one sentence, since there are no sentence boundary markers.

d) sentences not separated by whitespace

The input: 'Extract 50 paragraphs of text at random from a Wikipedia dump of a language of your choice and compare two sentence segmenters.You can choose any two segmenters you like.'

The output: ['Extract 50 paragraphs of text at random from a Wikipedia dump of a language of your choice and compare two sentence segmenters.You can choose any two segmenters you like.']

The problem: In the data to be processed, the sentences might not be separated by whitespaces. It causes the following problem: the nltk sentence tokenizer takes these two sentences as one, since there is no whitespace after the sentence boundary marker.




