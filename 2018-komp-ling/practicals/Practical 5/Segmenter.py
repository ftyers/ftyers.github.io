#!/usr/bin/env python
# coding: utf-8

# In[15]:


def segmenter(file):
    with open(file,'r',encoding='utf-8') as text:
        text = text.read()
        text = text.split(' ')
        punct = ''
        text_cleansed = [word.strip(',.!?;":?*)("»«') for word in text]
        
    return text_cleansed
    

        
if __name__ == '__main__':
    segmenter(__name__)


# In[ ]:




