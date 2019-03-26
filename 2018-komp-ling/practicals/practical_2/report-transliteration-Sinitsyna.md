# Report 3
## Transliteration

I wrote a simple transliterator, which takes Russian UD corpus, extracts words from the second column and converts each symbol in it to its Latin counterpart. To do that, firstly, I've created a dictionary file with transliterations of Russian Cyrillic symbols in Latin. Its name is *dictionary.txt*.

Then, I've downloaded Russian UD test corpus. The first function in the program takes the UD corpus (in .txt format), looks at the second column with words of the sentence and deletes all the rest of the columns (since we do not use them here, and they are pointless).
My next step was to prepare the dictionary file so I could work with it later. There I just took each line in the file, looked at it and created a dictionary out of it by splitting each line into key and value.

The next function is the most important one, since it's the one transliterating each word. It takes the dictionary and the parsed UD file, takes each symbol from the sentence and transliterates it to the one set in the dictionary. Then, it writes each transliterated word in the end of the line with the original one. There I've had to add the condition for the Russian letter "Е", as it needs to be treated differently at the beginning of the word than the rest of it (in that case, *e* should become *ye*).

The main function takes the Russian UD txt, the dictionary and applies the transliteration function to the test file. In the terminal, I do the output to the result.txt (which is in the practicals folder as well).

As for the questions in the task:
1) The ambiguous letters need special attention in that they either require a list of variations as a value in the dictionary or a condition for a change (as I've done with the letter "E")
2) The context of the symbol should be taken into consideration when applying the transliteration function. For example, if there is an h following s, then the transliterated symbol for both should be ш.
3) Mapping should be written in the conditions when applying the transliteration function also (as with letter "Е").
