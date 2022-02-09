#!/usr/bin/env python
# coding: utf-8

# In[1]:


import textract
import difflib
import nltk
import re

text = textract.process('ethanfrome11.pdf', method = 'tesseract')
book1 = text.decode()

text = textract.process('ethanfrome22.pdf', method = 'tesseract')
book2 = text.decode()

from nltk.tokenize import sent_tokenize, word_tokenize
from IPython.core.display import HTML

words1 = nltk.word_tokenize(book1)
words2 = nltk.word_tokenize(book2)

htmldiff = difflib.HtmlDiff()
tbl = htmldiff.make_table(words1, words2, context = True, numlines = 1)

HTML(tbl) 


# In[1]:


import textract
import difflib
import nltk
import re

text = textract.process('ethanfrome11.pdf', method = 'tesseract')
book1 = text.decode()

text = textract.process('ethanfrome22.pdf', method = 'tesseract')
book2 = text.decode()

from nltk.tokenize import sent_tokenize, word_tokenize
from IPython.core.display import HTML

words1 = nltk.word_tokenize(book1)
words2 = nltk.word_tokenize(book2)

htmldiff = difflib.HtmlDiff()
tbl = htmldiff.make_table(words1, words2, context = True, numlines = 5)

HTML(tbl) 


# In[ ]:




