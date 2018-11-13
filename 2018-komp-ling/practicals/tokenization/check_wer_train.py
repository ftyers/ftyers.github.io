from WER import *
import sys
import os


with open('correct_tokenized_test.txt', 'r') as f:
    test = f.read().split('\n')

with open('MaxMatchSentences_TEST.txt', 'r') as f:
    test_maxmatch = f.read().split('\n')
counter = 0
percentage = 0
for i in range(len(test)):
    wer_result = wer(test[i].split(), test_maxmatch[i].split())
    counter += 1
    percentage += (float(wer_result[:-1]))

print ('END')
print ("The result for the whole set of {} sentences is {} %".format(counter, int(percentage/counter)))