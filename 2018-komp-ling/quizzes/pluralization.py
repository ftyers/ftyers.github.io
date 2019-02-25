import sys
import re

word = sys.argv[1]
plur = {'s<PL>': 'ses', 'sh<PL>': 'shes', 'ch<PL>': 'ches', 'tz<PL>': 'tzes', 'x<PL>': 'xes'}

for key, value in plur:
    if word.endswith(key):
        word = word.replace(key, value)
    word = re.sub('<PL>', 's', word)

print(word)


