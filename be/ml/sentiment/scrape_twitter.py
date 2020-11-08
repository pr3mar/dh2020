# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:39:16 2020

@author: Bosec
"""

    
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words


LANGUAGE = "english"
SENTENCES_COUNT = 10


def summarize_url(url):
    parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        print(sentence)
        break
    
    
from googlesearch import search 

# to search 
query = "MV Wakashio oil spill"
for j in search(query, tld="com", num=50, stop=20, pause=2): 
    print(j)
    summarize_url(j)     
