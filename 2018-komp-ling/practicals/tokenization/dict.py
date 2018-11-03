#!/usr/bin/python
import re
with open("ja_gsd-ud-train.conllu", 'r', encoding = "UTF-8") as f,\
        open('dict.txt', 'w', encoding='utf-8') as fileDict,\
        open('sentences.txt', 'w', encoding='utf-8') as fileSent,\
        open('train.txt', 'w', encoding='utf-8') as fileSeg:
    dict = []
    sentTokens = []
    for x in f.readlines():
        match = re.search('\d+\t.*?\t(.*?)\t.[A-Z].*', x)
        if match:
            word = match.group(1)
            if word:
                dict.append(word)
                sentTokens.append(word)
        else:
            sentMatch = re.search('#\stext\s=\s(.*)', x)
            if sentMatch:
                if sentTokens:
                    fileSeg.write("%s\n" % " ".join(sentTokens))
                    sentTokens = []
                sent = sentMatch.group(1)
                fileSent.write("%s\n" % sent)
    for item in set(dict): fileDict.write("%s\n" % item)