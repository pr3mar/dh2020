# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 20:10:22 2020

@author: Bosec
"""

import text2emotion as te
import numpy as np
import pandas as pd
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer as Summarizer
from sumy.nlp.stemmers import Stemmer
from sumy.utils import get_stop_words




def summarize_news(news):
    """
    

    Parameters
    ----------
    news : LIST(str)
        List of news data to be summarized.

    Returns
    -------
    sentence : str
        Most important sentence in the given articles.

    """
    LANGUAGE = "english"
    SENTENCES_COUNT = 1
    parsed = []
    for data in news:
        parser = PlaintextParser.from_string(data, Tokenizer(LANGUAGE))
        stemmer = Stemmer(LANGUAGE)
        summarizer = Summarizer(stemmer)
        summarizer.stop_words = get_stop_words(LANGUAGE)
        for sentence in summarizer(parser.document, SENTENCES_COUNT):
            parsed.append(sentence)
    return parsed

def get_emotions(tweets):
    emotions = [ te.get_emotion(tweet) for tweet in tweets]
    df = pd.DataFrame(emotions)
    return df.mean(axis = 0).to_dict()


def test_env():
    texts = [ "Brazil, victim of a criminal oil spill.", 
             "The criminal Venezuela government, promoted this terrorist act against Brazil.",
             " Petrobras has analyzed 23 times the oil spilled on our northeast coast, and proved to be Venezuelan oil.",
             "Silence of international press...support the act"]
    print(get_emotions(read_tweets()))
    print(summarize_news([" ".join(texts)]))

def read_tweets(f_path = "tweets_mauritus.txt"):
    with open(f_path, "r") as f:
        f = f.readlines()
        cleaned = [line.strip() for line in f]
        return cleaned
import os
files = [x for x in os.listdir("../../../data/tweets_reacts")]
outs = {}
for x in files:
    name = x[:-4]
    with open("../../../data/tweets_reacts/"+x,'r', encoding='utf-8') as f:
        f = f.readlines()
        twts = [z.strip() for z in f]
        outs[name] = get_emotions(twts)
        print(outs[name])
import pickle
with open("../../../data/sentiments.pkl","wb") as f:
    pickle.dump(outs,f)
print(test_env())



