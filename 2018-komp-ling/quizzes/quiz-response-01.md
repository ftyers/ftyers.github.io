# Quiz 1

1. Which problems does maxmatch suffer from? (Choose all that
   apply.)

      a) requires comprehensive dictionary
           
      d) constructs non-grammatical sentences

2. Write a perl/sed substitution with regular expressions that
   adds whitespace for segmentation around "/" in "either/or"
   expressions but not around fractions "1/2":

        "either/or" -> "either / or"
        "1/2"       -> "1/2"

    ```bash
    perl -pe 's/(?<!\d)(\/)(?!\d)/ $1 /'
    ```

3. the text mentions several times that machine learning
   techniques produce better segmentation than rule-based
   systems; what are some downsides of machine learning
   techniques compared to rule-based?
   
   - much harder (or even impossible) to debug
   
   - they are trained for specific dataset, so they could work differently on other data
   

4. write a sentence (in English or in Russian) which maxmatch
   segments incorrectly.
   
   `Медведьлюбитмедведьмедсладкий.`
   
   ← We will get here two "медведь" with maxmatch.

5. what are problems for sentence segmentation? provide one
   example in English or Russian for each that applies.

      a) ambiguous abbreviations with punctuation

      If abbreviation is ended up with dot and next token is started from number or capital letter, it's a problem: end of the sentence with abbreviations or just an abbreviations in the middle of sentence.
      
      ```You could find description of the process at p. 38 or in the article of B. H. Johnson.```
 

      b) sentences containing symbols '!' and '?'
      
      Not really  frequent problem, but it may be with brands/slogans like *Yahoo!*, or when quotations are presented without quotations marks.
      
      ```Yahoo! is a web services provider headquartered in Sunnyvale, California and owned by Verizon Communications through Oath Inc.```
      
      c) sentences lacking separating punctuation
      
      In computer-mediated communication
      
      ```Yeap I like starbucks maybe I go there tomorrow what about u```
      
      d) sentences not separated by whitespace
      
      If they are glued together with no space, it's tokenization problem, if they have another separator, like new line character, it's not a problem.

