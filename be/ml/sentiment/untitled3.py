# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:34:45 2020

@author: Bosec
"""
import itertools
import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm
nlp = en_core_web_sm.load()
import pickle
import os
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pandas as pd
import seaborn as sns
from graphviz import Digraph, Graph
import networkx as nx
from nltk.tokenize import sent_tokenize

def build_graph(from_list, to_list):
    dot = Graph(strict=True)
    dot.format = 'svg'
    for e in from_list:
            for p in to_list:
                if e == p:
                    continue
                if not '\t'+e in dot.body:
                    dot.node(e)
                if not '\t'+p in dot.body:
                    dot.node(p)
                dot.edge(e,p)
    print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
    dot.render()          


def sent_graph(data, name):
    sentences = sent_tokenize(data)
    dot = Graph(strict=True, name=name)
    for sent in sentences:
        doc = nlp(sent)
        persons = [X.text for X in doc.ents if X.label_ == "PERSON"]
        if len(persons) > 1:
            pairs = list(itertools.combinations(persons[:min(len(persons),10)], 2))
            for pair in pairs:
                f, t = pair
                if not '\t'+f in dot.body:
                    dot.node(f)
                if not '\t'+t in dot.body:
                    dot.node(t)
                dot.edge(f,t)
    print(dot.source)
    dot.render()          

def extract_term(mapped, term="MONEY"):
    df = pd.DataFrame(mapped)
    l_temp = df[term].tolist()
    l_out = []
    for t in l_temp:
        if type(t) == type(list()):
            l_out = l_out + t
    return l_out

def rank_terms(terms, top_n = 5):
    counts = Counter(terms)    
    di = counts.most_common(top_n)
    outs = [ x for x,y in di]
    return outs

def export(mapped):
    prepare_export = {}
    for term in ["MONEY", "ORG", "PERSON"]:
        if not term in mapped[0]:
            prepare_export[term] = []
            continue
        raw_terms = extract_term(mapped, term)
        ranked_terms = rank_terms(raw_terms)
        print(term, ranked_terms)
        prepare_export[term] = ranked_terms
    return prepare_export

import pickle
def imports():
    with open("text_data.pkl","rb") as f:
        text_data = pickle.load(f)
    return text_data

        
tags = list()
prsns = list()

texts = []
outs = {}
text_data = imports()
for text in text_data:
    mapped = []
    continue
    dics = {}
    texted = " ".join(text_data[text])
    doc = nlp(texted)
    texts.append(texted)
    for X in doc.ents:
        dics[X.label_] = dics.get(X.label_, []) + [X.text]
    mapped.append(dics)
    #texts = " ".join(texts)
    #sent_graph(texted, text)
    outs[text] = export(mapped)


with open("analysis_data.pkl","wb") as f:
    pickle.dump(outs,f)
    
exit(0) 
with open('data.csv',encoding="utf-8") as f:
    f = f.readlines()
    mapped = []
    for line in f:
        dics = {}
        parsed = line.split("|")
        title = parsed[0][1:-1]
        abstract = parsed[1][1:-1]
        text = " ".join([title, abstract])
        doc = nlp(text)
        texts.append(text)
        for X in doc.ents:
            dics[X.label_] = dics.get(X.label_, []) + [X.text]
            tags = tags + [(X.text, X.label_) for X in doc.ents ]
            if X.label_ == "ORG" or X.label_ ==  "NORG": prsns.append(X.text)            
        mapped.append(dics)
        print(dics.keys())
texts = " ".join(texts)
sent_graph(texts)

prsns=list(set(prsns))

export(mapped)
exit(0)


counts = Counter(tags)    
di = counts.most_common(50)
df = pd.DataFrame(di, columns=["tag", "value"])
df = df.sort_values('value', ascending=False)
plot = df.plot(xticks=df.index, kind='bar', rot=45)
plot.set_xticklabels(df.tag)   
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
print(df)
plt.show()
print(mapped[0].keys)

build_graph(mapped[0]["PERSON"], mapped[0]["GPE"])

#build_graph(prsns, prsns)
exit(0)
dot = Graph(strict=True)
dot.format = 'svg'

print(prsns)

for e in prsns:
        for p in prsns:
            if e == p:
                continue
            if not '\t'+e in dot.body:
                dot.node(e)
            if not '\t'+p in dot.body:
                dot.node(p)
            dot.edge(e,p)

print(dot.source)  # doctest: +NORMALIZE_WHITESPACE
        
dot.render()  
