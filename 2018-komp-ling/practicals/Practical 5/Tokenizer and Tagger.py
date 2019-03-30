#!/usr/bin/env python
# coding: utf-8

# In[19]:


from pymystem3 import Mystem

def segmenter(file):
    with open(file,'r',encoding='utf-8') as text:
        text = text.read()
        text = text.split(' ')
        punct = ''
        text_cleansed = [word.strip(',.!?;":?*)("»«') for word in text]
        
    return text_cleansed


def analyzer(segments):
    m = Mystem()
    analized = [m.analyze(word) for word in segments]
    
    return analized


def get_results(analized_info):
    tagged = {}
    for item in analized_info:
        try:
            word = item[0]['text']
            grammar = item[0]['analysis'][0]['gr']
            ini = 0
            pos = ''
            while pos == '':
                if grammar[ini] == '=' or grammar[ini] == ',':
                    pos = grammar[:ini]
                else: 
                    ini += 1
            tagged[word] = pos
        except:
            pass
    
    return tagged



if __name__ == '__main__':
    seg = segmenter(r'Архиерейский собор РПЦ принял решение о канонизации доктора Евгения Боткина.txt')
    ana = analyzer(seg)
    tag = get_results(ana)
    for i in tag:
        print(i,' : ',tag[i])


# In[ ]:




