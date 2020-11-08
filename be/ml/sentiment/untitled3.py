# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 16:34:45 2020

@author: Bosec
"""
titles = []
datas = []
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
    
def extract_money(mapped):
    mon = list()
    for m in mapped:
        print(type(m))
        if "MONEY" in m:
            tmp = m["MONEY"]
            mon = mon + list(set(tmp))
    return mon


tags = list()
prsns = list()

with open('data.csv',encoding="utf-8") as f:
    f = f.readlines()
    mapped = []
    for line in f:
        dics = {}
        parsed = line.split("|")
        titles.append(parsed[0][1:-1])
        datas.append(parsed[1][1:-1])
        doc = nlp(" ".join([parsed[0][1:-1],parsed[1][1:-1]]))
        for X in doc.ents:
            dics[X.label_] = dics.get(X.label_, []) + [X.text]
            #if not X.label_ == "CARDINAL" and not X.label_ == "ORDINAL":
            tags = tags + [(X.text, X.label_) for X in doc.ents ]
            if X.label_ == "ORG" or X.label_ ==  "NORG": prsns.append(X.text)            
        mapped.append(dics)
        print(dics.keys())
prsns=list(set(prsns))
print(prsns)

extract_money(mapped)
print([x["QUANTITY"] for x in mapped  if "MONEY" in x])
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
