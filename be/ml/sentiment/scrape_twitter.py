# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 15:39:16 2020

@author: Bosec
"""

from googlesearch import search 
from sumy.parsers.html import HtmlParser
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words
import os
import pickle
from tqdm import tqdm
LANGUAGE = "english"
SENTENCES_COUNT = 10


def summarize_url(url):
    try:
        parser = HtmlParser.from_url(url, Tokenizer(LANGUAGE))
    except:
        return ["" * SENTENCES_COUNT]
    stemmer = Stemmer(LANGUAGE)
    summarizer = Summarizer(stemmer)
    summarizer.stop_words = get_stop_words(LANGUAGE)
    outs = []
    for sentence in summarizer(parser.document, SENTENCES_COUNT):
        outs.append(str(sentence))
    return outs

events = [x[:-4] for x in os.listdir("../../../data/gifs_")]
print(events)

outs = {}
for query in tqdm(events):
    findings_ = []
    outs[query] = []
    #query = "MV Wakashio oil spill"
    for j in search(query, tld="com", num=10, stop=20, pause=2): 
        findings_=findings_+summarize_url(j)
        outs[query] = [] +  [" ".join(list(set(findings_)))]
    print(outs[query])     

with open("text_data.pkl", "wb") as f:
    pickle.dump(outs, f)
