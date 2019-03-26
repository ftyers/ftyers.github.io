Regular expressions
I have tried them as explained in the taks.

matplotlib




ElementTree
https://github.com/bbkjunior/HSE_learning/blob/2efde9407ed3c80673721be7a95292f7781a793d/Autotutor/Polysemantic%20words%20detection.ipynb
I have used ElementTree library in Autotutor task.
I had lxml sence-dictionary so my task was to detect the words which have two or more sences. I used the library and finally received dictionary namded mult_sence which contains the keys = words and values = number of sences for the corresponding word.  



scikit learn
I followed the instrutions from the assignment first and then split the data upo to train and test using train_test_split() function.
Then I trained preceptron with this trainset and get accuracy 0.995 with text set.
The code is inside sklearn.py


Screenscraping
I have done much screensraping when performed interview task for Sberbank.
My aim was to collect food-orieneted dialogues which will be used for implementing seq2seq model. 
The link for the repo is here https://github.com/bbkjunior/chatbot_dataset_collection

I have decided to get the dialogues from subtitles and from forums.

DOwnloading the subtitles was rather diffiult for me so I split this up to three notebooks
https://github.com/bbkjunior/chatbot_dataset_collection/blob/master/download_subtitles_report.ipynb
Here I collected a list of links to be used for downloading each definite suntitle fil
https://github.com/bbkjunior/chatbot_dataset_collection/blob/master/process_and_write_subtitles_report.ipynb
Then I preprocessed them and saved them as csv
https://github.com/bbkjunior/chatbot_dataset_collection/blob/master/extart_food_from_subs_report.ipynb
The final step was extracting food-related dialogues from the preprocessed subs

The next taks performed which turned out to be more effective was scraping food-related forums. 
Moreover this was more about screensraping
The workflow is decribed here https://github.com/bbkjunior/chatbot_dataset_collection/blob/master/parse_forums_report.ipynb
What I have done is as follows
1. I implemented the function extract_dialogue() which takes web page url and parses all quote-response phrases from it. It literally meets the requirement for dialogues to be collected. 
2. Then I collected links for pages with recepies - get_recipies_links
3. Then I went over all collected links and collected necessary dialogues from them using get_dialogues_from_links_list()
4. FInally I saved the dialogues with save_dialogues()


Unigram tagger